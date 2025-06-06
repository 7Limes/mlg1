"""
An mlg1 compiler implementation made with ANTLR.

By Miles Burkart
https://github.com/7Limes
"""

import sys
import os
import argparse
from antlr4 import Lexer, ParserRuleContext, ParseTreeWalker, FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from mlg1.parser.mlg1Lexer import mlg1Lexer
from mlg1.parser.mlg1Listener import mlg1Listener
from mlg1.parser.mlg1Parser import mlg1Parser
from mlg1.compiler.constants import *
from mlg1.compiler.util import error, preprocess_error, COLOR_ERROR
from mlg1.compiler.expression import FunctionCallHandler, ExpressionHandler
from mlg1.compiler.data import CompilerState, CompilerFlags, CodeWriter
from mlg1.compiler.file import get_parsed_file_size


class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_type = "Lexical" if isinstance(recognizer, Lexer) else "Parsing"
        self.errors.append(f"{error_type} error at line {line}, column {column}: {msg}")


class BaseListener(mlg1Listener):
    def __init__(self, source_lines: list[str]):
        self.source_lines = source_lines
    
    def error(self, ctx: ParserRuleContext, message: str):
        line = ctx.start.line-1
        error((line, ctx.start.column), self.source_lines[line], message)


class InitialListener(BaseListener):
    def __init__(self, source_lines: list[str]):
        super().__init__(source_lines)
        self.meta_variables: dict[str, int] = META_VAR_DEFAULTS.copy()
        self.current_address = LOCAL_VAR_ADDRESS
        self.function_namespaces: dict[str, dict[str, dict[str, int]]] = {}
        self.global_namespace: dict[str, int] = GLOBAL_NAMESPACE.copy()
        self.constant_namespace: dict[str, int] = {}
        self.string_vars: dict[int, int] = {}
        self.current_function: str = None
        self.data_entries: dict[str, dict[str, str]] = {}
        self.contains_return: bool = False
    
    def _declare_variable(self, ctx: ParserRuleContext, name: str, is_global: bool):
        """
        Declares a new variable at the current address. Does not increment `self.current_address`.
        """
        # Error checking
        if name in RESERVED_NAMES:
            self.error(ctx, f'Variable name "{name}" is reserved.')
        current_locals = self.function_namespaces[self.current_function]['locals']
        if name in current_locals or name in self.global_namespace or name in self.constant_namespace:
            self.error(ctx, f'Variable "{name}" declared twice.')
        if self.current_function is None:
            self.error(ctx, 'Current function is None.')
        
        # Set namespace values
        if is_global:  # global var
            self.global_namespace[name] = self.current_address
        else:  # local var
            self.function_namespaces[self.current_function]['locals'][name] = self.current_address

    
    def enterMetaVariable(self, ctx: mlg1Parser.MetaVariableContext):
        name = ctx.META_VARIABLE_NAME().getText()
        value = int(ctx.INTEGER().getText())
        self.meta_variables[name] = value
    
    def enterFunction(self, ctx: mlg1Parser.FunctionContext):
        function_name = ctx.NAME().getText()
        if function_name in RESERVED_NAMES or function_name in BUILTIN_FUNCTIONS:
            self.error(ctx, f'Function "{function_name}" is reserved.')
        if function_name in self.function_namespaces:
            self.error(ctx, f'Function "{function_name}" declared twice.')
        parameter_list_token = ctx.parameterList()
        if function_name in {'start', 'tick'} and parameter_list_token is not None:
            self.error(parameter_list_token, f'{function_name} function cannot have parameters.')
        
        if function_name not in {'start', 'tick'}:
            self.contains_return = True  # add returning code if a custom function exists [note 1]
        
        self.function_namespaces[function_name] = {'parameters': [], 'locals': {}}
        if parameter_list_token:
            seen_parameter_names = set()
            for parameter_name_token in parameter_list_token.children:
                parameter_name = parameter_name_token.getText()
                if parameter_name == ',':  # stupid solution
                    continue
                if parameter_name in seen_parameter_names:
                    self.error(parameter_list_token, f'Parameter "{parameter_name}" declared twice.')
                seen_parameter_names.add(parameter_name)
                self.function_namespaces[function_name]['parameters'].append(self.current_address)
                self.function_namespaces[function_name]['locals'][parameter_name] = self.current_address
                self.current_address += 1
        self.current_function = function_name
    
    def exitFunction(self, ctx: mlg1Parser.FunctionContext):
        self.current_function = None
    
    def enterVariableDeclaration(self, ctx: mlg1Parser.VariableDeclarationContext):
        name = ctx.NAME().getText()
        keyword = ctx.VARIABLE_KEYWORD().getText()  # either 'let' or 'global'
        self._declare_variable(ctx, name, keyword == 'global')

        if ctx.STRING() is not None:
            self.data_entries[name] = {
                'type': 's',
                'string': ctx.STRING().getText()[1:-1],
                'var_address': self.current_address
        }
        
        self.current_address += 1
    
    def enterArrayDeclaration(self, ctx: mlg1Parser.ArrayDeclarationContext):
        array_size_token: mlg1Parser.ArraySizeContext = ctx.arraySize()
        if array_size_token.NAME() is not None:  # Defined constant size
            size_constant_name = array_size_token.NAME().getText()
            if size_constant_name not in self.constant_namespace:
                self.error(array_size_token, f'Tried to declare array size with undefined constant "{size_constant_name}".')
            array_size = self.constant_namespace[size_constant_name]
        else:  # Integer literal size
            array_size = int(array_size_token.INTEGER().getText())
        
        if array_size <= 0:
            self.error(array_size_token, f'Array size must be greater than zero.')
        
        initializer_list_token: mlg1Parser.ArrayInitializerListContext = ctx.arrayInitializerList()
        if initializer_list_token is not None:
            array_value_tokens = list(initializer_list_token.getChildren(lambda c: isinstance(c, mlg1Parser.ExpressionContext)))
            if len(array_value_tokens) > array_size:
                self.error(initializer_list_token, f'Array initializer length exceeds array size.')
        
        name = ctx.NAME().getText()
        keyword = ctx.VARIABLE_KEYWORD().getText()
        self._declare_variable(ctx, name, keyword == 'global')

        # Add `array_size` here to allocate space for the array
        self.current_address += array_size + 1
    
    def enterConstantDefinition(self, ctx: mlg1Parser.ConstantDefinitionContext):
        name = ctx.NAME().getText()
        value = int(ctx.signedInteger().getText())
        self.constant_namespace[name] = value
    
    def enterLoadFile(self, ctx):
        name = ctx.NAME().getText()
        path = ctx.STRING().getText()
        self.data_entries[name] = {'type': 'f', 'path': path[1:-1]}


    def after_walk(self) -> list[str]:
        """
        Called after this listener has finished walking the parse tree.
        Adds addresses of loaded files to the global namespace and sets the HEAP address variable
        """
        data_file_rules = []
        for var_name, data_entry in self.data_entries.items():
            entry_type = data_entry['type']
            if entry_type == 'f':  # file
                file_path = data_entry['path']
                data_file_rules.append(f'{self.current_address} f {file_path}')
                self.constant_namespace[var_name] = self.current_address
                with open(file_path, 'rb') as f:
                    file_bytes = f.read()
                file_extension = os.path.splitext(file_path)[1]
                self.current_address += get_parsed_file_size(file_bytes, file_extension)

            elif entry_type == 's':  # string
                string = data_entry['string']
                data_file_rules.append(f'{self.current_address} s {string}')
                self.string_vars[data_entry['var_address']] = self.current_address
                self.current_address += len(string) + 1  # add 1 for length prefix
        
        self.constant_namespace[HEAP_VARIABLE_NAME] = self.current_address

        # Add meta vars to the constant namespace to allow constant propagation
        for meta_var_name in META_VAR_DEFAULTS:
            self.constant_namespace[meta_var_name.upper()] = self.meta_variables[meta_var_name]

        return data_file_rules


class MainListener(BaseListener):
    def __init__(self, compiler_state: CompilerState) -> None:
        super().__init__(compiler_state.source_lines)
        self.compiler_state = compiler_state

        self.current_function = None

        self.block_end_stack: list[str] = []

        # Add meta variable lines
        for meta_var_name, meta_var_value in self.compiler_state.meta_variables.items():
            self.compiler_state.code_writer.add_line(f'#{meta_var_name} {meta_var_value}')
        
        if self.compiler_state.contains_return:
            self.compiler_state.code_writer.add_lines(get_return_code(self.compiler_state.compiler_flags.indent_size))
    
    def _get_var_address(self, var_name: str, is_global: bool) -> int:
        if is_global:
            return self.compiler_state.global_namespace[var_name]
        return self.compiler_state.function_namespaces[self.current_function]['locals'][var_name]


    def _add_conditional_inversion(self):
        inversion_instruction = f'not {ARITHMETIC_REGISTER_ADDRESS} ${ARITHMETIC_REGISTER_ADDRESS}'
        if self.compiler_state.code_writer.last_line == inversion_instruction:  # [note 3]
            self.compiler_state.code_writer.lines.pop()
        else:
            self.compiler_state.code_writer.add_line(inversion_instruction)
        
    
    def _add_source_code_comment(self, ctx):
        """
        Adds a comment containing the source line that corresponds to a block of generated code.
        """
        if not self.compiler_state.compiler_flags.include_source:
            return
        
        line_stripped = self.source_lines[ctx.start.line-1].strip()
        self.compiler_state.code_writer.add_lines([
            '',  # Extra line for padding
            f'; SRC@{ctx.start.line}:{ctx.start.column} {line_stripped}'
        ])


    def enterFunction(self, ctx: mlg1Parser.FunctionContext):
        function_name = ctx.NAME().getText()
        self.compiler_state.code_writer.add_lines(['', f'{function_name}:'])
        if function_name == 'start' and self.compiler_state.contains_return:
            whitespace = " "*self.compiler_state.compiler_flags.indent_size
            self.compiler_state.code_writer.add_line(f'{whitespace}mov {CALL_STACK_POINTER_ADDRESS} {CALL_STACK_DATA_ADDRESS}')
        self.current_function = function_name
    
    def exitFunction(self, ctx: mlg1Parser.FunctionContext):
        self.current_function = None
        if ctx.NAME().getText() in {'start', 'tick'}:
            self.compiler_state.code_writer.add_line('jmp end 1')
        elif self.compiler_state.code_writer.last_line != 'jmp return 1':
            whitespace = " "*self.compiler_state.compiler_flags.indent_size
            self.compiler_state.code_writer.add_line(f'{whitespace}jmp return 1')
    
    def enterVariableDeclaration(self, ctx: mlg1Parser.VariableDeclarationContext):
        self._add_source_code_comment(ctx)

        var_name = ctx.NAME().getText()
        is_global = ctx.VARIABLE_KEYWORD().getText() == 'global'
        if ctx.STRING():
            var_address = self._get_var_address(var_name, is_global)
            string_address = self.compiler_state.string_vars[var_address]
            self.compiler_state.code_writer.add_line(f'mov {var_address} {string_address}')
        else:
            expression_token = ctx.expression()
            expression = ExpressionHandler(self.compiler_state, expression_token, self.current_function)
            expression_code = expression.generate_code(self._get_var_address(var_name, is_global))
            self.compiler_state.code_writer.add_lines(expression_code)
    
    def enterAssignment(self, ctx: mlg1Parser.AssignmentContext):
        self._add_source_code_comment(ctx)

        expression_token = ctx.expression()
        expression = ExpressionHandler(self.compiler_state, expression_token, self.current_function)
        var_name = ctx.NAME().getText()
        is_global = var_name in self.compiler_state.global_namespace
        expression_code = expression.generate_code(self._get_var_address(var_name, is_global))
        self.compiler_state.code_writer.add_lines(expression_code)
    
    def enterArrayDeclaration(self, ctx):
        self._add_source_code_comment(ctx)

        var_name = ctx.NAME().getText()
        is_global = ctx.VARIABLE_KEYWORD().getText() == 'global'
        array_address = self._get_var_address(var_name, is_global)
        self.compiler_state.code_writer.add_line(f'mov {array_address} {array_address+1}')

        initializer_list_token: mlg1Parser.ArrayInitializerListContext = ctx.arrayInitializerList()
        if initializer_list_token is not None:
            array_value_tokens = initializer_list_token.getChildren(lambda c: isinstance(c, mlg1Parser.ExpressionContext))
            for i, array_value_token in enumerate(array_value_tokens):
                expression = ExpressionHandler(self.compiler_state, array_value_token, self.current_function)
                expression_code = expression.generate_code(array_address+i+1)
                self.compiler_state.code_writer.add_lines(expression_code)
        
    def enterFunctionCall(self, ctx: mlg1Parser.FunctionCallContext):
        if isinstance(ctx.parentCtx, mlg1Parser.StatementContext):
            self._add_source_code_comment(ctx)

            function_call = FunctionCallHandler.from_token(self.compiler_state, ctx)
            function_call_code = function_call.generate_code(self.current_function, RETURN_REGISTER_ADDRESS)
            self.compiler_state.code_writer.add_lines(function_call_code)
    
    def enterReturnStatement(self, ctx: mlg1Parser.ReturnStatementContext):
        self._add_source_code_comment(ctx)
        
        expression_token = ctx.expression()
        expression = ExpressionHandler(self.compiler_state, expression_token, self.current_function)
        expression_code = expression.generate_code(RETURN_REGISTER_ADDRESS)
        self.compiler_state.code_writer.add_lines(expression_code)
        self.compiler_state.code_writer.add_line('jmp return 1')
    
    def enterIfStatement(self, ctx: mlg1Parser.IfStatementContext):
        self._add_source_code_comment(ctx)

        condition_expression_token = ctx.expression()
        condition_expression = ExpressionHandler(self.compiler_state, condition_expression_token, self.current_function)
        expression_code = condition_expression.generate_code(ARITHMETIC_REGISTER_ADDRESS)
        self.compiler_state.code_writer.add_lines(expression_code)
        self._add_conditional_inversion()

        else_token = ctx.elseStatement()
        if else_token is None:
            skip_label_name = f'{self.current_function}_skip_{ctx.start.line}_{ctx.start.column}'
            self.compiler_state.code_writer.add_line(f'jmp {skip_label_name} ${ARITHMETIC_REGISTER_ADDRESS}')
            self.block_end_stack.append(skip_label_name + ':')
        else:
            else_label_name = f'{self.current_function}_else_{ctx.start.line}_{ctx.start.column}'
            end_label_name = f'{self.current_function}_end_{ctx.start.line}_{ctx.start.column}'
            self.compiler_state.code_writer.add_line(f'jmp {else_label_name} ${ARITHMETIC_REGISTER_ADDRESS}')
            self.block_end_stack.extend([end_label_name + ':', [else_label_name + ':', f'jmp {end_label_name} 1']])
    
    def enterWhileLoop(self, ctx: mlg1Parser.WhileLoopContext):
        self._add_source_code_comment(ctx)

        loop_label_name = f'{self.current_function}_loop_{ctx.start.line}_{ctx.start.column}'
        loop_end_label_name = f'{self.current_function}_end_{ctx.start.line}_{ctx.start.column}'
        condition_expression_token = ctx.expression()
        condition_expression = ExpressionHandler(self.compiler_state, condition_expression_token, self.current_function)
        expression_code = condition_expression.generate_code(ARITHMETIC_REGISTER_ADDRESS)
        self.compiler_state.code_writer.add_line(loop_label_name + ':')
        self.compiler_state.code_writer.add_lines(expression_code)
        self._add_conditional_inversion()
        self.compiler_state.code_writer.add_line(f'jmp {loop_end_label_name} ${ARITHMETIC_REGISTER_ADDRESS}')
        self.block_end_stack.append([loop_end_label_name + ':', f'jmp {loop_label_name} 1'])
    
    def enterBlock(self, ctx: mlg1Parser.BlockContext):
        self.compiler_state.code_writer.indent_level += 1
    
    def exitBlock(self, ctx: mlg1Parser.BlockContext):
        self.compiler_state.code_writer.indent_level -= 1
        if isinstance(ctx.parentCtx, (mlg1Parser.IfStatementContext, mlg1Parser.ElseStatementContext, mlg1Parser.WhileLoopContext)):
            popped = self.block_end_stack.pop()
            if isinstance(popped, list):
                self.compiler_state.code_writer.add_lines(list(reversed(popped)))
            else:
                self.compiler_state.code_writer.add_line(popped)


def get_compiler_state(program: mlg1Parser.ProgramContext, source_lines: list[str], compiler_flags: CompilerFlags, walker: ParseTreeWalker) -> tuple[CompilerState, list[str]]:
    listener = InitialListener(source_lines)
    walker.walk(listener, program)
    data_file_rules = listener.after_walk()
    compiler_state = CompilerState(
        source_lines, compiler_flags, listener.meta_variables,
        listener.function_namespaces, listener.global_namespace, listener.constant_namespace, listener.string_vars,
        listener.contains_return, listener.current_address, CodeWriter(compiler_flags.indent_size), []
    )
    compiler_state.meta_variables['memory'] += compiler_state.heap_address  # offset requested memory by the stack memory size [note 2]
    return compiler_state, data_file_rules


def main() -> int:
    try:
        arg_parser = argparse.ArgumentParser(description='Compile mlg1 programs')
        arg_parser.add_argument('input_file', help='Path to the input mlg1 program')
        arg_parser.add_argument('output_file', help='Path to the output g1 program')
        arg_parser.add_argument('--include_source', '-s', action='store_true', help='Add source code comments to the output program')
        arg_parser.add_argument('--indent_size', '-i', type=int, default=DEFAULT_INDENT_SIZE, help='Set the indent size to be used')
        parsed_args = arg_parser.parse_args()
    except Exception as e:
        print(e)
        return 1
    
    if not os.path.isfile(parsed_args.input_file):
        print(f'Path "{parsed_args.input_file}" does not exist or is not a file.')
        return 2

    token_stream = FileStream(parsed_args.input_file)
    with open(parsed_args.input_file, 'r') as f:
        source_lines = f.read().split('\n')
    
    error_listener = CustomErrorListener()
    lexer = mlg1Lexer(token_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    token_stream = CommonTokenStream(lexer)

    parser = mlg1Parser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    program = parser.program()
    
    if error_listener.errors:
        print(f'{COLOR_ERROR}Preprocessing errors found:')
        for message in error_listener.errors:
            preprocess_error(message)
        return 3
    
    walker = ParseTreeWalker()
    
    compiler_flags = CompilerFlags(parsed_args.include_source, parsed_args.indent_size)
    compiler_state, data_file_rules = get_compiler_state(program, source_lines, compiler_flags, walker)

    main_listener = MainListener(compiler_state)
    walker.walk(main_listener, program)
    compiler_state.code_writer.add_line('end:')
    main_listener.compiler_state.code_writer.write_file(parsed_args.output_file)
    if data_file_rules:
        data_file_cw = CodeWriter()
        data_file_cw.add_lines(data_file_rules)
        data_file_cw.write_file(parsed_args.output_file + 'd')

    return 0


if __name__ == '__main__':
    sys.exit(main())