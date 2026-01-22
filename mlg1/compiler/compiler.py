"""
An mlg1 compiler implementation made with ANTLR.

By Miles Burkart
https://github.com/7Limes
"""

import sys
import os
import argparse
from collections import deque
import importlib.metadata
from antlr4 import Lexer, ParserRuleContext, ParseTreeWalker, FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from g1asm.data import parse_entry
from mlg1.parser.mlg1Lexer import mlg1Lexer
from mlg1.parser.mlg1Listener import mlg1Listener
from mlg1.parser.mlg1Parser import mlg1Parser
from mlg1.compiler.constants import \
    RESERVED_NAMES, ENTRYPOINT_FUNCTIONS, BUILTIN_FUNCTIONS, \
    ARITHMETIC_REGISTER_ADDRESS, CALL_STACK_POINTER_ADDRESS, CALL_STACK_DATA_ADDRESS, RETURN_REGISTER_ADDRESS, \
    DEFAULT_INDENT_SIZE, get_return_routine
from mlg1.compiler.util import error, generic_error, get_error_string, CodeWriter
from mlg1.compiler.expression import FunctionCallHandler, ExpressionHandler, ExpressionException, evaluate_constant_expression
from mlg1.compiler.data import CodegenPassData, ContextOverride, InitialPassData, MemoryPassData, CompilerFlags, FunctionToken

from pathlib import Path
STDLIB_PATH = Path(__file__).parents[1] / 'stdlib'


class Mlg1CompilerError(Exception):
    """
    Exception class for compiler errors.
    """
    


class CustomErrorListener(ErrorListener):
    def __init__(self, source_lines: list[str]):
        super(CustomErrorListener, self).__init__()
        
        self.errors = []
        self.source_lines = source_lines

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_type = 'LEXING' if isinstance(recognizer, Lexer) else 'PARSING'
        message = f'{error_type} ERROR: {msg}'
        error_string = get_error_string((line, column), self.source_lines[line-1], message)
        self.errors.append(error_string)


def ctx_error(ctx: ParserRuleContext, message: str, source_lines: list[str]):
    line = ctx.start.line-1
    error((line, ctx.start.column), source_lines[line], message)


class BaseListener(mlg1Listener):
    def __init__(self, source_lines: list[str]):
        super().__init__()
        self.source_lines = source_lines
    
    def error(self, ctx: ParserRuleContext, message: str):
        ctx_error(ctx, message, self.source_lines)


class InitialListener(BaseListener):
    def __init__(self, initial_pass_data: InitialPassData, source_lines: list[str], source_file: str):
        super().__init__(source_lines)
        self.data = initial_pass_data
        self.source_file = source_file
        self.current_function_token: FunctionToken | None = None
        self.ctx_override = ContextOverride(self.source_file, self.source_lines)
        
    
    def enterFunction(self, ctx: mlg1Parser.FunctionContext):
        function_name: str = ctx.NAME().getText()
        if function_name in RESERVED_NAMES or function_name in BUILTIN_FUNCTIONS:
            self.error(ctx, f'Function "{function_name}" is reserved.')
        if function_name in self.data.function_tokens:
            self.error(ctx, f'Function "{function_name}" declared twice.')
        
        function_token = FunctionToken(ctx, function_name, self.source_file, self.source_lines, called_functions=set())
        self.current_function_token = function_token
        self.data.function_tokens[function_name] = function_token
    
    def exitFunction(self, _ctx):
        self.current_function_token = None
    
    def enterFunctionCall(self, ctx: mlg1Parser.FunctionCallContext):
        called_function_name: str = ctx.NAME().getText()
        if called_function_name not in BUILTIN_FUNCTIONS and self.current_function_token:
            self.current_function_token.called_functions.add(called_function_name)

    def enterIncludeFile(self, ctx: mlg1Parser.IncludeFileContext):
        include_path: str = ctx.STRING().getText()[1:-1]
        file_path = include_path + '.mlg1'
        if file_path not in self.data.included_files:
            self.data.included_files.add(file_path)

            # Try to include normally
            try:
                initial_pass(self.data, file_path)
                return
            except Mlg1CompilerError as e:
                original_error = e

            # Try to include from stdlib
            try:
                stdlib_file_path = str(STDLIB_PATH / include_path) + '.mlg1'
                initial_pass(self.data, stdlib_file_path)
            except Mlg1CompilerError as e:
                # Failed to include
                self.error(ctx, str(original_error))

    def enterMetaVariable(self, ctx: mlg1Parser.MetaVariableContext):
        name = ctx.META_VARIABLE_NAME().getText()
        value = int(ctx.INTEGER().getText())
        self.data.meta_variables[name] = value

        # Add meta var to the constant namespace to allow constant propagation
        self.data.constant_namespace[name.upper()] = value
    
    def enterLoadFile(self, ctx: mlg1Parser.LoadFileContext):
        name = ctx.NAME().getText()
        path = ctx.STRING().getText()[1:-1]
        operation = ctx.FILE_OPERATION().getText()

        parse_entry_result = parse_entry('file', operation, path)
        if isinstance(parse_entry_result, str):
            self.error(ctx, parse_entry_result)

        if name in self.data.data_entries:
            self.error(ctx, f'Data identifier "{name}" declared twice.')
        
        self.data.data_entries[name] = {
            'data_type': 'file',
            'operation': operation,
            'data': path
        }
    
    def enterConstantDefinition(self, ctx: mlg1Parser.ConstantDefinitionContext):
        constant_name = ctx.NAME().getText()
        value = evaluate_constant_expression(self.data.constant_namespace, ctx.expression())
        self.data.constant_namespace[constant_name] = value
    
    def enterGlobalVarDeclaration(self, ctx: mlg1Parser.GlobalVarDeclarationContext):
        self.data.global_var_tokens.append((ctx, self.ctx_override))
    
    def enterGlobalArrayDeclaration(self, ctx: mlg1Parser.GlobalArrayDeclarationContext):
        self.data.global_array_tokens.append((ctx, self.ctx_override))


class MemoryListener(BaseListener):
    def __init__(self, memory_pass_data: MemoryPassData, function_token: FunctionToken):
        super().__init__(function_token.source_lines)
        self.data = memory_pass_data
        
        self.current_function_name: str = None
    
    def check_variable(self, ctx: ParserRuleContext, name: str):
        # Error checking
        if name in RESERVED_NAMES:
            self.error(ctx, f'Variable name "{name}" is reserved.')
        
        current_locals = self.data.local_namespaces[self.current_function_name]['locals']
        if name in current_locals or name in self.data.global_namespace or name in self.data.constant_namespace:
            self.error(ctx, f'Variable "{name}" declared twice.')
        
        if self.current_function_name is None:
            self.error(ctx, 'Current function is None.')
    
    def add_namespace_entry(self, name: str, is_global: bool):
        if is_global:
            self.data.global_namespace[name] = self.data.current_address
        else:
            current_locals = self.data.local_namespaces[self.current_function_name]['locals']
            current_locals[name] = self.data.current_address
    
    def declare_variable(
            self,
            ctx: mlg1Parser.LocalVarDeclarationContext | mlg1Parser.GlobalVarDeclarationContext,
            is_global: bool
        ):
        """
        Reserves space for a new variable and adds it to the namespace.
        Also adds string data entries if the variable is a string.
        """
        for declared_var_token in ctx.declaredVariablesList().declaredVariable():
            name = declared_var_token.NAME().getText()
            string_token = declared_var_token.STRING()
            self.check_variable(ctx, name)

            # Set namespace value
            self.add_namespace_entry(name, is_global)
            
            # Add string data entry if necessary
            if string_token is not None:
                if name in self.data.data_entries:
                    self.error(declared_var_token, f'Variable name "{name}" declared twice.')
                
                string_data: str = string_token.getText()[1:-1]
                
                self.data.data_entries[name] = {
                    'data_type': 'string',
                    'operation': 'raw',
                    'data': string_data,
                    'var_address': self.data.current_address
                }

            self.data.current_address += 1
    
    def declare_array(self, ctx: ParserRuleContext, is_global: bool):
        """
        Reserves space for a new array.
        """
        size_expression_token = ctx.expression()
        initializer_list_token: mlg1Parser.ExpressionListContext = ctx.expressionList()

        if initializer_list_token is None:
            array_value_tokens = []
        else:
            array_value_tokens = list(initializer_list_token.getChildren(lambda c: isinstance(c, mlg1Parser.ExpressionContext)))
        
        if size_expression_token is None:
            array_size = len(array_value_tokens)
        else:
            array_size = evaluate_constant_expression(self.data.constant_namespace, size_expression_token)
        if array_size <= 0:
            self.error(ctx, 'Array size must be greater than zero.')
        
        if len(array_value_tokens) > array_size:
            self.error(initializer_list_token, 'Array initializer length exceeds array size.')
        
        name = ctx.NAME().getText()
        self.check_variable(ctx, name)

        # Set namespace value
        self.add_namespace_entry(name, is_global)

        # Add `array_size` here to allocate space for the array,
        # Plus 1 for the variable that stores the pointer to the array
        self.data.current_address += array_size + 1
    
    
    def enterFunction(self, ctx: mlg1Parser.FunctionContext):
        function_name: str = ctx.NAME().getText()
        parameter_list_token = ctx.parameterList()
        if function_name in ENTRYPOINT_FUNCTIONS and parameter_list_token is not None:
            self.error(parameter_list_token, f'{function_name} function cannot have parameters.')
        
        parameter_count = 0
        function_namespace = {'locals': {}}

        # Get set of all global names to check for variable name shadowing
        all_global_names: set[str] = set()
        for t, _ in self.data.global_var_tokens:
            for declared_var_token in t.declaredVariablesList().declaredVariable():
                all_global_names.add(declared_var_token.NAME().getText())
        for t, _ in self.data.global_array_tokens:
            all_global_names.add(t.NAME().getText())

        if parameter_list_token:
            seen_parameter_names = set()
            for parameter_name_token in parameter_list_token.children:
                parameter_name = parameter_name_token.getText()
                if parameter_name == ',':  # stupid solution
                    continue
                if parameter_name in seen_parameter_names:
                    self.error(parameter_list_token, f'Parameter "{parameter_name}" declared twice.')
                if parameter_name in all_global_names:
                    self.error(parameter_list_token, f'Parameter "{parameter_name}" shadows existing global name.')
                seen_parameter_names.add(parameter_name)
                parameter_count += 1
                function_namespace['locals'][parameter_name] = self.data.current_address
                self.data.current_address += 1
        
        function_namespace['parameter_count'] = parameter_count
        self.data.local_namespaces[function_name] = function_namespace
        self.current_function_name = function_name

        if function_name == 'start':
            for global_var_ctx, _ in self.data.global_var_tokens:
                self.declare_variable(global_var_ctx, True)
            for global_array_ctx, _ in self.data.global_array_tokens:
                self.declare_array(global_array_ctx, True)
    
    def exitFunction(self, _ctx: mlg1Parser.FunctionContext):
        self.current_function_name = None
    
    def enterFunctionCall(self, ctx: mlg1Parser.FunctionCallContext):
        function_name: str = ctx.NAME().getText()
        if function_name not in BUILTIN_FUNCTIONS:
            if function_name not in self.data.function_tokens:
                self.error(ctx, f'Tried to call unrecognized function "{function_name}".')
            self.data.include_return_subroutine = True  # Include return subroutine if a custom function is called [note 1]
    
    def enterLocalVarDeclaration(self, ctx: mlg1Parser.LocalVarDeclarationContext):
        self.declare_variable(ctx, False)
    
    def enterAssignment(self, ctx):
        name: str = ctx.NAME().getText()
        if name in RESERVED_NAMES:
            self.error(ctx, f'Variable name "{name}" is reserved.')
        
    def enterLocalArrayDeclaration(self, ctx):
        self.declare_array(ctx, False)


class CodegenListener(BaseListener):
    def __init__(self, codegen_pass_data: CodegenPassData, code_writer: CodeWriter, function_token: FunctionToken) -> None:
        super().__init__(function_token.source_lines)

        self.data = codegen_pass_data
        self.code_writer = code_writer

        self.function_token: FunctionToken = function_token

        self.block_end_stack: deque[str] = deque()
        self.break_label_stack: deque[str] = deque()
        self.continue_label_stack: deque[str] = deque()
        self.for_loop_end_stack: deque[tuple[str, mlg1Parser.AssignmentContext]] = []
    
    def get_var_address(self, ctx: ParserRuleContext, var_name: str, is_global: bool) -> int:
        if is_global:
            return self.data.global_namespace[var_name]
        
        namespace = self.data.get_current_local_namespace()
        if var_name not in namespace['locals']:
            self.error(ctx, f'Tried to reference undefined variable "{var_name}".')
        
        return namespace['locals'][var_name]

    def add_conditional_inversion(self):
        inversion_instruction = f'not {ARITHMETIC_REGISTER_ADDRESS} ${ARITHMETIC_REGISTER_ADDRESS}'
        if self.code_writer.last_line == inversion_instruction:  # [note 3]
            self.code_writer.lines.pop()
        else:
            self.code_writer.add_line(inversion_instruction)
    
    def add_var_declaration(
            self,
            ctx: mlg1Parser.LocalVarDeclarationContext | mlg1Parser.GlobalVarDeclarationContext,
            is_global: bool,
            add_comment: bool,
            context_override: ContextOverride | None=None
        ):

        if add_comment:
            self.add_source_code_comment(ctx, context_override)
        
        for declared_var_token in ctx.declaredVariablesList().declaredVariable():
            
            var_name = declared_var_token.NAME().getText()
            var_address = self.get_var_address(ctx, var_name, is_global)
            if declared_var_token.STRING():
                string_address = self.data.string_vars[var_address]
                self.code_writer.add_line(f'mov {var_address} {string_address}')
            elif declared_var_token.expression():
                expression_token = declared_var_token.expression()
                try:
                    expression = ExpressionHandler(self.data.get_namespaces(), expression_token)
                    expression_code = expression.generate_code(var_address, self.function_token.name, self.data.function_base_registers)
                except ExpressionException as e:
                    self.error(e.token, str(e))
                
                self.code_writer.add_lines(expression_code)
    
    def add_array_declaration(
            self,
            ctx: mlg1Parser.LocalArrayDeclarationContext | mlg1Parser.GlobalArrayDeclarationContext,
            is_global: bool,
            context_override: ContextOverride | None=None
        ):
        self.add_source_code_comment(ctx, context_override)

        var_name = ctx.NAME().getText()
        array_address = self.get_var_address(ctx, var_name, is_global)
        self.code_writer.add_line(f'mov {array_address} {array_address+1}')

        initializer_list_token: mlg1Parser.ArrayInitializerListContext = ctx.expressionList()
        if initializer_list_token is not None:
            array_value_tokens = initializer_list_token.getChildren(lambda c: isinstance(c, mlg1Parser.ExpressionContext))
            for i, array_value_token in enumerate(array_value_tokens):
                try:
                    expression = ExpressionHandler(self.data.get_namespaces(), array_value_token)
                except ExpressionException as e:
                    self.error(e.token, str(e))
                expression_code = expression.generate_code(array_address+i+1, self.function_token.name, self.data.function_base_registers)
                self.code_writer.add_lines(expression_code)
    
    def add_source_code_comment(self, ctx, context_override: ContextOverride | None=None):
        """
        Adds a comment containing the source line that corresponds to a block of generated code.
        """
        if not self.data.compiler_flags.include_source:
            return
        
        if context_override:
            source_file = context_override.source_file
            line = context_override.source_lines[ctx.start.line-1].strip()
        else:
            source_file = self.function_token.source_file
            line = self.source_lines[ctx.start.line-1].strip()
        
        self.code_writer.add_lines([
            '',  # Extra line for padding
            f'; {source_file}@{ctx.start.line}:{ctx.start.column} {line}'
        ])


    def enterFunction(self, ctx: mlg1Parser.FunctionContext):
        self.code_writer.add_line('')
        self.add_source_code_comment(ctx)

        function_name = ctx.NAME().getText()
        self.code_writer.add_line(f'{function_name}:')

        if function_name == 'start':
            self.code_writer.indent_level += 1

            # Initialize call stack
            if self.data.include_return_subroutine:
                if self.data.compiler_flags.include_source:
                    self.code_writer.add_line(f'; Initialize call stack')
                self.code_writer.add_line(f'mov {CALL_STACK_POINTER_ADDRESS} {CALL_STACK_DATA_ADDRESS}')

            # Inject global var assignments into start routine
            for global_var_ctx, ctx_override in self.data.global_var_tokens:
                self.add_var_declaration(global_var_ctx, True, self.data.compiler_flags.include_source, ctx_override)
            for global_array_ctx, ctx_override in self.data.global_array_tokens:
                self.add_array_declaration(global_array_ctx, True, ctx_override)
            
            self.code_writer.indent_level -= 1
    

    def exitFunction(self, ctx: mlg1Parser.FunctionContext):
        if ctx.NAME().getText() in ENTRYPOINT_FUNCTIONS:
            self.code_writer.add_line('jmp end 1')
        elif self.code_writer.last_line != 'jmp return 1':
            whitespace = " "*self.data.compiler_flags.indent_size
            self.code_writer.add_line(f'{whitespace}jmp return 1')
    
    def enterLocalVarDeclaration(self, ctx: mlg1Parser.LocalVarDeclarationContext, add_comment: bool=True):
        if isinstance(ctx.parentCtx, mlg1Parser.ForLoopContext):
            return

        self.add_var_declaration(ctx, False, add_comment)
    
    def enterAssignment(self, ctx: mlg1Parser.AssignmentContext, add_comment: bool=True):
        if isinstance(ctx.parentCtx, mlg1Parser.ForLoopContext):
            return
        
        if add_comment:
            self.add_source_code_comment(ctx)

        expression_token = ctx.expression()
        try:
            expression = ExpressionHandler(self.data.get_namespaces(), expression_token)
        except ExpressionException as e:
            self.error(e.token, str(e))
        
        var_name = ctx.NAME().getText()
        is_global = var_name in self.data.global_namespace
        destination = self.get_var_address(ctx, var_name, is_global)
        expression_code = expression.generate_code(destination, self.function_token.name, self.data.function_base_registers)
        self.code_writer.add_lines(expression_code)
    
    def enterLocalArrayDeclaration(self, ctx: mlg1Parser.LocalArrayDeclarationContext):
        self.add_array_declaration(ctx, False)
        
    def enterFunctionCall(self, ctx: mlg1Parser.FunctionCallContext):
        if isinstance(ctx.parentCtx, mlg1Parser.StatementContext):
            self.add_source_code_comment(ctx)

            try:
                function_call = FunctionCallHandler.from_token(self.data.get_namespaces(), ctx)
                function_call_code = function_call.generate_code(
                    RETURN_REGISTER_ADDRESS, ARITHMETIC_REGISTER_ADDRESS,
                    self.function_token.name, self.data.function_base_registers
                )
            except ExpressionException as e:
                self.error(e.token, str(e))
            
            self.code_writer.add_lines(function_call_code)
    
    def enterReturnStatement(self, ctx: mlg1Parser.ReturnStatementContext):
        self.add_source_code_comment(ctx)
        
        expression_token = ctx.expression()
        try:
            expression = ExpressionHandler(self.data.get_namespaces(), expression_token)
        except ExpressionException as e:
            self.error(e.token, str(e))
        
        expression_code = expression.generate_code(RETURN_REGISTER_ADDRESS, self.function_token.name, self.data.function_base_registers)
        self.code_writer.add_lines(expression_code)
        self.code_writer.add_line('jmp return 1')
    
    def enterBreakStatement(self, ctx: mlg1Parser.BreakStatementContext):
        self.add_source_code_comment(ctx)

        break_label = self.break_label_stack[-1]
        self.code_writer.add_line(f'jmp {break_label} 1')
    
    def enterContinueStatement(self, ctx: mlg1Parser.ContinueStatementContext):
        self.add_source_code_comment(ctx)

        continue_label = self.continue_label_stack[-1]
        self.code_writer.add_line(f'jmp {continue_label} 1')

    def generate_if_statement(self, ctx, parent_if_ctx: mlg1Parser.IfStatementContext):
        condition_token = ctx.expression()
        try:
            condition_expression = ExpressionHandler(self.data.get_namespaces(), condition_token)
        except ExpressionException as e:
            self.error(e.token, str(e))
        
        expression_code = condition_expression.generate_code(ARITHMETIC_REGISTER_ADDRESS, self.function_token.name, self.data.function_base_registers)
        self.code_writer.add_lines(expression_code)
        self.add_conditional_inversion()
        
        skip_label_name = f'{self.function_token.name}_skip_{ctx.start.line}_{ctx.start.column}'
        self.code_writer.add_line(f'jmp {skip_label_name} ${ARITHMETIC_REGISTER_ADDRESS}')
        
        end_label_name = f'{self.function_token.name}_end_{parent_if_ctx.start.line}_{parent_if_ctx.start.column}'
        
        if parent_if_ctx.elseIfClause() or parent_if_ctx.elseClause():
            if ctx == parent_if_ctx:
                self.block_end_stack.append(end_label_name + ':')
            
            # If this is the last else if without a final else
            if parent_if_ctx.elseClause() is None and \
                    isinstance(ctx, mlg1Parser.ElseIfClauseContext) and \
                    ctx == parent_if_ctx.elseIfClause()[-1]:
                self.block_end_stack[-1] = [end_label_name + ':', skip_label_name + ':', f'jmp {end_label_name} 1']
            else:
                self.block_end_stack.append([skip_label_name + ':', f'jmp {end_label_name} 1'])
        else:
            self.block_end_stack.append(skip_label_name + ':')

    def enterIfStatement(self, ctx: mlg1Parser.IfStatementContext):
        self.add_source_code_comment(ctx)
        
        self.generate_if_statement(ctx, ctx)
    
    def enterElseIfClause(self, ctx: mlg1Parser.ElseIfClauseContext):
        self.add_source_code_comment(ctx)

        parent: mlg1Parser.IfStatementContext = ctx.parentCtx
        self.generate_if_statement(ctx, parent)

    def enterElseClause(self, ctx: mlg1Parser.ElseClauseContext):
        self.add_source_code_comment(ctx)

    def enterWhileLoop(self, ctx: mlg1Parser.WhileLoopContext):
        self.add_source_code_comment(ctx)

        loop_label_name = f'{self.function_token.name}_loop_{ctx.start.line}_{ctx.start.column}'
        loop_end_label_name = f'{self.function_token.name}_end_{ctx.start.line}_{ctx.start.column}'
        condition_token = ctx.expression()
        try:
            condition_expression = ExpressionHandler(self.data.get_namespaces(), condition_token)
        except ExpressionException as e:
            self.error(e.token, str(e))
        
        expression_code = condition_expression.generate_code(ARITHMETIC_REGISTER_ADDRESS, self.function_token.name, self.data.function_base_registers)
        
        self.code_writer.add_line(loop_label_name + ':')
        self.code_writer.add_lines(expression_code)
        self.add_conditional_inversion()
        self.code_writer.add_line(f'jmp {loop_end_label_name} ${ARITHMETIC_REGISTER_ADDRESS}')
        self.block_end_stack.append([loop_end_label_name + ':', f'jmp {loop_label_name} 1'])

        self.break_label_stack.append(loop_end_label_name)
        self.continue_label_stack.append(loop_label_name)
    
    def enterForLoop(self, ctx: mlg1Parser.ForLoopContext):
        self.add_source_code_comment(ctx)

        var_declaration: mlg1Parser.VariableDeclarationContext = ctx.localVarDeclaration()
        assignment: list[mlg1Parser.AssignmentContext] = ctx.assignment()

        if var_declaration is not None: 
            parent = var_declaration.parentCtx
            var_declaration.parentCtx = None
            self.enterLocalVarDeclaration(var_declaration, add_comment=False)
            var_declaration.parentCtx = parent
            increment_token = assignment[0]
        elif len(assignment) == 2:
            initial_assignment_token = assignment[0]
            parent = initial_assignment_token.parentCtx
            initial_assignment_token.parentCtx = None
            self.enterAssignment(initial_assignment_token, add_comment=False)
            initial_assignment_token.parentCtx = parent
            increment_token = assignment[1]
        else:
            increment_token = assignment[0]

        condition_token = ctx.expression()
        try:
            condition_expression = ExpressionHandler(self.data.get_namespaces(), condition_token)
        except ExpressionException as e:
            self.error(e.token, str(e))
        
        expression_code = condition_expression.generate_code(ARITHMETIC_REGISTER_ADDRESS, self.function_token.name, self.data.function_base_registers)
        loop_label_name = f'{self.function_token.name}_loop_{ctx.start.line}_{ctx.start.column}'
        loop_continue_label_name = f'{self.function_token.name}_continue_{ctx.start.line}_{ctx.start.column}'
        loop_end_label_name = f'{self.function_token.name}_end_{ctx.start.line}_{ctx.start.column}'
        
        self.code_writer.add_line(loop_label_name + ':')
        self.code_writer.add_lines(expression_code)
        self.add_conditional_inversion()
        self.code_writer.add_line(f'jmp {loop_end_label_name} ${ARITHMETIC_REGISTER_ADDRESS}')
        self.block_end_stack.append([loop_end_label_name + ':', f'jmp {loop_label_name} 1'])
        self.for_loop_end_stack.append((loop_continue_label_name + ':', increment_token))

        self.break_label_stack.append(loop_end_label_name)
        self.continue_label_stack.append(loop_continue_label_name)
    
    def enterBlock(self, ctx: mlg1Parser.BlockContext):
        self.code_writer.indent_level += 1
    
    def exitBlock(self, ctx: mlg1Parser.BlockContext):
        if isinstance(ctx.parentCtx, mlg1Parser.ForLoopContext):
            loop_continue_label, increment_token = self.for_loop_end_stack.pop()
            self.code_writer.add_line(loop_continue_label)
            increment_token.parentCtx = None
            self.enterAssignment(increment_token, add_comment=False)
        
        if isinstance(ctx.parentCtx, (mlg1Parser.WhileLoopContext, mlg1Parser.ForLoopContext)):
            self.break_label_stack.pop()
            self.continue_label_stack.pop()
        
        self.code_writer.indent_level -= 1

        if isinstance(ctx.parentCtx, (mlg1Parser.IfStatementContext, mlg1Parser.ElseClauseContext, 
                                      mlg1Parser.ElseIfClauseContext, mlg1Parser.WhileLoopContext, 
                                      mlg1Parser.ForLoopContext)):
            popped = self.block_end_stack.pop()
            if isinstance(popped, list):
                self.code_writer.add_lines(list(reversed(popped)))
            else:
                self.code_writer.add_line(popped)


def initial_pass(initial_pass_data: InitialPassData, file_path: str):
    """
    Records functions, constants, globals, meta vars, and loads files.
    """
    if not os.path.isfile(file_path):
        raise Mlg1CompilerError(f'Path "{file_path}" does not exist or is not a file.')
    
    token_stream = FileStream(file_path)
    with open(file_path, 'r') as f:
        source_lines = f.read().split('\n')

    # Lexing
    error_listener = CustomErrorListener(source_lines)
    lexer = mlg1Lexer(token_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    token_stream = CommonTokenStream(lexer)

    # Parsing
    parser = mlg1Parser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    program_token = parser.program()

    if error_listener.errors:
        generic_error(f'Preprocessing errors found in {file_path}:')
        for error_string in error_listener.errors:
            print(error_string)
        raise Mlg1CompilerError('Preprocessing error.')
    
    walker = ParseTreeWalker()
    source_file = os.path.splitext(os.path.basename(file_path))[0]
    listener = InitialListener(initial_pass_data, source_lines, source_file)
    walker.walk(listener, program_token)


def after_initial_pass(initial_pass_data: InitialPassData) -> MemoryPassData:
    # Walk through function call tree starting at entrypoints to determine which functions will actually be used
    functions_to_walk: deque[str] = deque(ENTRYPOINT_FUNCTIONS)
    seen_functions: set[str] = set()
    while functions_to_walk:
        function_name = functions_to_walk.pop()
        function_token = initial_pass_data.function_tokens.get(function_name)
        if function_token is not None:
            for called_function in function_token.called_functions:
                if called_function not in seen_functions:
                    functions_to_walk.append(called_function)
        # If function_token is None, then it's a call to an unrecognized 
        # function and we'll catch this error in the memory pass
        seen_functions.add(function_name)
    
    used_function_tokens = {t.name: t for t in initial_pass_data.function_tokens.values() if t.name in seen_functions}
    return MemoryPassData(
        initial_pass_data.meta_variables,
        initial_pass_data.constant_namespace,
        initial_pass_data.data_entries,
        used_function_tokens,
        initial_pass_data.global_var_tokens,
        initial_pass_data.global_array_tokens
    )


def memory_pass(memory_pass_data: MemoryPassData, compiler_flags: CompilerFlags) -> CodegenPassData:
    """
    Determines the memory layout of everything in the program.
    """
    # Walk through function tokens
    walker = ParseTreeWalker()
    for function_token in memory_pass_data.function_tokens.values():
        listener = MemoryListener(memory_pass_data, function_token)
        walker.walk(listener, function_token.token)
    
    # Create data entry lines
    data_entry_lines = []
    for var_name, data_entry in memory_pass_data.data_entries.items():
        data_type = data_entry['data_type']
        operation = data_entry['operation']
        data = data_entry['data']

        parse_entry_result = parse_entry(data_type, operation, data)
        if isinstance(parse_entry_result, str):
            raise Mlg1CompilerError(parse_entry_result)
        entry_size = len(parse_entry_result)

        data_entry_lines.append(f'@{memory_pass_data.current_address} {data_type} {operation} "{data}"')

        if data_type == 'file':
            # Add addresses of loaded files to the constant namespace
            memory_pass_data.constant_namespace[var_name] = memory_pass_data.current_address
        elif data_type == 'string':
            memory_pass_data.string_vars[data_entry['var_address']] = memory_pass_data.current_address
        
        memory_pass_data.current_address += entry_size
    
    memory_pass_data.meta_variables['memory'] += memory_pass_data.current_address  # offset requested memory by the stack memory size [note 2]
    
    return CodegenPassData(
        compiler_flags,
        memory_pass_data.function_tokens,
        memory_pass_data.meta_variables,
        data_entry_lines,
        memory_pass_data.constant_namespace,
        memory_pass_data.global_namespace,
        memory_pass_data.global_var_tokens,
        memory_pass_data.global_array_tokens,
        memory_pass_data.local_namespaces,
        memory_pass_data.string_vars,
        memory_pass_data.include_return_subroutine
    )


def codegen_pass(codegen_pass_data: CodegenPassData, code_writer: CodeWriter):
    """
    Generates assembly code.
    """
    # Write meta variable lines
    for meta_var_name, meta_var_value in codegen_pass_data.meta_variables.items():
        code_writer.add_line(f'#{meta_var_name} {meta_var_value}')
    code_writer.add_line('')  # Padding line

    # Write data entry lines
    if codegen_pass_data.data_entry_lines:
        code_writer.add_lines(codegen_pass_data.data_entry_lines)
        code_writer.add_line('')  # Padding line
    
    # Write return subroutine
    if codegen_pass_data.include_return_subroutine:
        code_writer.add_lines(get_return_routine(codegen_pass_data.compiler_flags.indent_size))
        
    # Walk through each function with the codegen listener
    walker = ParseTreeWalker()
    for function_token in codegen_pass_data.function_tokens.values():
        codegen_pass_data.current_function_token = function_token
        listener = CodegenListener(codegen_pass_data, code_writer, function_token)
        walker.walk(listener, function_token.token)
    
    code_writer.add_line('end:')


def main() -> int:
    try:
        arg_parser = argparse.ArgumentParser('mlg1', description='Compile mlg1 programs')
        arg_parser.add_argument('--version', '-v', action='version', version=f'mlg1 compiler v{importlib.metadata.version('mlg1')}')
        arg_parser.add_argument('input_file', help='Path to the input mlg1 program')
        arg_parser.add_argument('output_file', help='Path to the output g1 program')
        arg_parser.add_argument('--include_source', '-s', action='store_true', help='Add source code comments to the output program')
        arg_parser.add_argument('--indent_size', '-i', type=int, default=DEFAULT_INDENT_SIZE, help='Set the indent size to be used')
        parsed_args = arg_parser.parse_args()
    except Exception as e:
        print(e)
        return 1

    compiler_flags = CompilerFlags(parsed_args.include_source, parsed_args.indent_size)
    
    # Initial pass
    try:
        initial_pass_data = InitialPassData()
        initial_pass(initial_pass_data, parsed_args.input_file)
    except Mlg1CompilerError as e:
        print(e)
        return 2
    
    # After initial pass
    memory_pass_data = after_initial_pass(initial_pass_data)
    
    # Memory layout pass
    try:
        codegen_pass_data = memory_pass(memory_pass_data, compiler_flags)
    except Mlg1CompilerError as e:
        print(e)
        return 3

    # Codegen pass
    code_writer = CodeWriter(compiler_flags.indent_size)
    codegen_pass(codegen_pass_data, code_writer)
    code_writer.write_file(parsed_args.output_file)

    return 0


if __name__ == '__main__':
    sys.exit(main())
