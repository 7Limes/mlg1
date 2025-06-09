"""
An mlg1 compiler implementation made with ANTLR.

By Miles Burkart
https://github.com/7Limes
"""

import sys
import os
import argparse
from result import Result, Ok, Err
from antlr4 import Lexer, ParserRuleContext, ParseTreeWalker, FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from mlg1.parser.mlg1Lexer import mlg1Lexer
from mlg1.parser.mlg1Listener import mlg1Listener
from mlg1.parser.mlg1Parser import mlg1Parser
from mlg1.compiler.constants import \
    RESERVED_NAMES, BUILTIN_FUNCTIONS, META_VAR_DEFAULTS, \
    ARITHMETIC_REGISTER_ADDRESS, CALL_STACK_POINTER_ADDRESS, CALL_STACK_DATA_ADDRESS, RETURN_REGISTER_ADDRESS, \
    DEFAULT_INDENT_SIZE, HEAP_VARIABLE_NAME, get_return_code
from mlg1.compiler.util import error, preprocess_error, COLOR_ERROR, CodeWriter
from mlg1.compiler.expression import FunctionCallHandler, ExpressionHandler
from mlg1.compiler.data import CompilerState, CompilerFlags, FunctionToken
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
        super().__init__()
        self.source_lines = source_lines
    
    def error(self, ctx: ParserRuleContext, message: str):
        line = ctx.start.line-1
        error((line, ctx.start.column), self.source_lines[line], message)


class PreprocessListener(BaseListener):
    def __init__(self, compiler_state: CompilerState, source_lines: list[str], source_file: str):
        super().__init__(source_lines)
        self.compiler_state = compiler_state
        self.source_file = source_file
        
        self.current_function: str = None
    
    def _declare_variable(self, ctx: ParserRuleContext, name: str, is_global: bool):
        """
        Declares a new variable at the current address. Does not increment `self.current_address`.
        """
        # Error checking
        if name in RESERVED_NAMES:
            self.error(ctx, f'Variable name "{name}" is reserved.')
        current_locals = self.compiler_state.function_namespaces[self.current_function]['locals']
        if name in current_locals or name in self.compiler_state.global_namespace or name in self.compiler_state.constant_namespace:
            self.error(ctx, f'Variable "{name}" declared twice.')
        if self.current_function is None:
            self.error(ctx, 'Current function is None.')
        
        # Set namespace values
        if is_global:  # global var
            self.compiler_state.global_namespace[name] = self.compiler_state.current_address
        else:  # local var
            self.compiler_state.function_namespaces[self.current_function]['locals'][name] = self.compiler_state.current_address
    
    def enterMetaVariable(self, ctx: mlg1Parser.MetaVariableContext):
        name = ctx.META_VARIABLE_NAME().getText()
        value = int(ctx.INTEGER().getText())
        self.compiler_state.meta_variables[name] = value
    
    def enterIncludeFile(self, ctx):
        file_path = ctx.STRING().getText()[1:-1] + '.mlg1'

        preprocess_result = preprocess(self.compiler_state, file_path)
        if isinstance(preprocess_result, Err):
            self.error(ctx, preprocess_result.err_value)
    
    def enterLoadFile(self, ctx):
        name = ctx.NAME().getText()
        path = ctx.STRING().getText()
        self.compiler_state.data_entries[name] = {'type': 'f', 'path': path[1:-1]}
    
    def enterConstantDefinition(self, ctx: mlg1Parser.ConstantDefinitionContext):
        name = ctx.NAME().getText()
        value = int(ctx.signedInteger().getText())
        self.compiler_state.constant_namespace[name] = value
    
    def enterFunction(self, ctx: mlg1Parser.FunctionContext):
        function_name = ctx.NAME().getText()
        if function_name in RESERVED_NAMES or function_name in BUILTIN_FUNCTIONS:
            self.error(ctx, f'Function "{function_name}" is reserved.')
        if function_name in self.compiler_state.function_namespaces:
            self.error(ctx, f'Function "{function_name}" declared twice.')
        parameter_list_token = ctx.parameterList()
        if function_name in {'start', 'tick'} and parameter_list_token is not None:
            self.error(parameter_list_token, f'{function_name} function cannot have parameters.')
        
        if function_name not in {'start', 'tick'}:
            self.compiler_state.contains_return = True  # include return subroutine if a custom function exists [note 1]
        
        self.compiler_state.function_namespaces[function_name] = {'parameters': [], 'locals': {}}
        if parameter_list_token:
            seen_parameter_names = set()
            for parameter_name_token in parameter_list_token.children:
                parameter_name = parameter_name_token.getText()
                if parameter_name == ',':  # stupid solution
                    continue
                if parameter_name in seen_parameter_names:
                    self.error(parameter_list_token, f'Parameter "{parameter_name}" declared twice.')
                seen_parameter_names.add(parameter_name)
                self.compiler_state.function_namespaces[function_name]['parameters'].append(self.compiler_state.current_address)
                self.compiler_state.function_namespaces[function_name]['locals'][parameter_name] = self.compiler_state.current_address
                self.compiler_state.current_address += 1
        self.current_function = function_name
        
        function_token = FunctionToken(ctx, self.source_file, self.source_lines)
        self.compiler_state.function_tokens.append(function_token)
    
    def exitFunction(self, _ctx: mlg1Parser.FunctionContext):
        self.current_function = None
    
    def enterVariableDeclaration(self, ctx: mlg1Parser.VariableDeclarationContext):
        name = ctx.NAME().getText()
        keyword = ctx.VARIABLE_KEYWORD().getText()  # either 'let' or 'global'
        self._declare_variable(ctx, name, keyword == 'global')

        if ctx.STRING() is not None:
            self.compiler_state.data_entries[name] = {
                'type': 's',
                'string': ctx.STRING().getText()[1:-1],
                'var_address': self.compiler_state.current_address
        }
        
        self.compiler_state.current_address += 1
    
    def enterArrayDeclaration(self, ctx: mlg1Parser.ArrayDeclarationContext):
        array_size_token: mlg1Parser.ArraySizeContext = ctx.arraySize()
        if array_size_token.NAME() is not None:  # Defined constant size
            size_constant_name = array_size_token.NAME().getText()
            if size_constant_name not in self.compiler_state.constant_namespace:
                self.error(array_size_token, f'Tried to declare array size with undefined constant "{size_constant_name}".')
            array_size = self.compiler_state.constant_namespace[size_constant_name]
        else:  # Integer literal size
            array_size = int(array_size_token.INTEGER().getText())
        
        if array_size <= 0:
            self.error(array_size_token, 'Array size must be greater than zero.')
        
        initializer_list_token: mlg1Parser.ArrayInitializerListContext = ctx.expressionList()
        if initializer_list_token is not None:
            array_value_tokens = list(initializer_list_token.getChildren(lambda c: isinstance(c, mlg1Parser.ExpressionContext)))
            if len(array_value_tokens) > array_size:
                self.error(initializer_list_token, 'Array initializer length exceeds array size.')
        
        name = ctx.NAME().getText()
        keyword = ctx.VARIABLE_KEYWORD().getText()
        self._declare_variable(ctx, name, keyword == 'global')

        # Add `array_size` here to allocate space for the array
        self.compiler_state.current_address += array_size + 1


class CodegenListener(BaseListener):
    def __init__(self, compiler_state: CompilerState, code_writer: CodeWriter, source_lines: list[str], source_file: str) -> None:
        super().__init__(source_lines)
        self.source_file = source_file

        self.compiler_state = compiler_state
        self.code_writer = code_writer

        self.current_function = None

        self.block_end_stack: list[str] = []
    
    
    def _get_var_address(self, var_name: str, is_global: bool) -> int:
        if is_global:
            return self.compiler_state.global_namespace[var_name]
        return self.compiler_state.function_namespaces[self.current_function]['locals'][var_name]


    def _add_conditional_inversion(self):
        inversion_instruction = f'not {ARITHMETIC_REGISTER_ADDRESS} ${ARITHMETIC_REGISTER_ADDRESS}'
        if self.code_writer.last_line == inversion_instruction:  # [note 3]
            self.code_writer.lines.pop()
        else:
            self.code_writer.add_line(inversion_instruction)
        
    
    def _add_source_code_comment(self, ctx):
        """
        Adds a comment containing the source line that corresponds to a block of generated code.
        """
        if not self.compiler_state.compiler_flags.include_source:
            return
        
        line_stripped = self.source_lines[ctx.start.line-1].strip()
        self.code_writer.add_lines([
            '',  # Extra line for padding
            f'; {self.source_file}@{ctx.start.line}:{ctx.start.column} {line_stripped}'
        ])


    def enterFunction(self, ctx: mlg1Parser.FunctionContext):
        self.code_writer.add_line('')
        self._add_source_code_comment(ctx)

        function_name = ctx.NAME().getText()
        self.code_writer.add_line(f'{function_name}:')
        if function_name == 'start' and self.compiler_state.contains_return:
            whitespace = " "*self.compiler_state.compiler_flags.indent_size
            self.code_writer.add_line(f'{whitespace}mov {CALL_STACK_POINTER_ADDRESS} {CALL_STACK_DATA_ADDRESS}')
        self.current_function = function_name
    
    def exitFunction(self, ctx: mlg1Parser.FunctionContext):
        self.current_function = None
        if ctx.NAME().getText() in {'start', 'tick'}:
            self.code_writer.add_line('jmp end 1')
        elif self.code_writer.last_line != 'jmp return 1':
            whitespace = " "*self.compiler_state.compiler_flags.indent_size
            self.code_writer.add_line(f'{whitespace}jmp return 1')
    
    def enterVariableDeclaration(self, ctx: mlg1Parser.VariableDeclarationContext):
        self._add_source_code_comment(ctx)

        var_name = ctx.NAME().getText()
        is_global = ctx.VARIABLE_KEYWORD().getText() == 'global'
        if ctx.STRING():
            var_address = self._get_var_address(var_name, is_global)
            string_address = self.compiler_state.string_vars[var_address]
            self.code_writer.add_line(f'mov {var_address} {string_address}')
        else:
            expression_token = ctx.expression()
            expression = ExpressionHandler(self.compiler_state, expression_token, self.current_function)
            expression_code = expression.generate_code(self._get_var_address(var_name, is_global))
            self.code_writer.add_lines(expression_code)
    
    def enterAssignment(self, ctx: mlg1Parser.AssignmentContext):
        self._add_source_code_comment(ctx)

        expression_token = ctx.expression()
        expression = ExpressionHandler(self.compiler_state, expression_token, self.current_function)
        var_name = ctx.NAME().getText()
        is_global = var_name in self.compiler_state.global_namespace
        expression_code = expression.generate_code(self._get_var_address(var_name, is_global))
        self.code_writer.add_lines(expression_code)
    
    def enterArrayDeclaration(self, ctx):
        self._add_source_code_comment(ctx)

        var_name = ctx.NAME().getText()
        is_global = ctx.VARIABLE_KEYWORD().getText() == 'global'
        array_address = self._get_var_address(var_name, is_global)
        self.code_writer.add_line(f'mov {array_address} {array_address+1}')

        initializer_list_token: mlg1Parser.ArrayInitializerListContext = ctx.expressionList()
        if initializer_list_token is not None:
            array_value_tokens = initializer_list_token.getChildren(lambda c: isinstance(c, mlg1Parser.ExpressionContext))
            for i, array_value_token in enumerate(array_value_tokens):
                expression = ExpressionHandler(self.compiler_state, array_value_token, self.current_function)
                expression_code = expression.generate_code(array_address+i+1)
                self.code_writer.add_lines(expression_code)
        
    def enterFunctionCall(self, ctx: mlg1Parser.FunctionCallContext):
        if isinstance(ctx.parentCtx, mlg1Parser.StatementContext):
            self._add_source_code_comment(ctx)

            function_call = FunctionCallHandler.from_token(self.compiler_state, ctx)
            function_call_code = function_call.generate_code(self.current_function, RETURN_REGISTER_ADDRESS)
            self.code_writer.add_lines(function_call_code)
    
    def enterReturnStatement(self, ctx: mlg1Parser.ReturnStatementContext):
        self._add_source_code_comment(ctx)
        
        expression_token = ctx.expression()
        expression = ExpressionHandler(self.compiler_state, expression_token, self.current_function)
        expression_code = expression.generate_code(RETURN_REGISTER_ADDRESS)
        self.code_writer.add_lines(expression_code)
        self.code_writer.add_line('jmp return 1')
    
    def enterIfStatement(self, ctx: mlg1Parser.IfStatementContext):
        self._add_source_code_comment(ctx)

        condition_expression_token = ctx.expression()
        condition_expression = ExpressionHandler(self.compiler_state, condition_expression_token, self.current_function)
        expression_code = condition_expression.generate_code(ARITHMETIC_REGISTER_ADDRESS)
        self.code_writer.add_lines(expression_code)
        self._add_conditional_inversion()

        else_token = ctx.elseStatement()
        if else_token is None:
            skip_label_name = f'{self.current_function}_skip_{ctx.start.line}_{ctx.start.column}'
            self.code_writer.add_line(f'jmp {skip_label_name} ${ARITHMETIC_REGISTER_ADDRESS}')
            self.block_end_stack.append(skip_label_name + ':')
        else:
            else_label_name = f'{self.current_function}_else_{ctx.start.line}_{ctx.start.column}'
            end_label_name = f'{self.current_function}_end_{ctx.start.line}_{ctx.start.column}'
            self.code_writer.add_line(f'jmp {else_label_name} ${ARITHMETIC_REGISTER_ADDRESS}')
            self.block_end_stack.extend([end_label_name + ':', [else_label_name + ':', f'jmp {end_label_name} 1']])
    
    def enterWhileLoop(self, ctx: mlg1Parser.WhileLoopContext):
        self._add_source_code_comment(ctx)

        loop_label_name = f'{self.current_function}_loop_{ctx.start.line}_{ctx.start.column}'
        loop_end_label_name = f'{self.current_function}_end_{ctx.start.line}_{ctx.start.column}'
        condition_expression_token = ctx.expression()
        condition_expression = ExpressionHandler(self.compiler_state, condition_expression_token, self.current_function)
        expression_code = condition_expression.generate_code(ARITHMETIC_REGISTER_ADDRESS)
        self.code_writer.add_line(loop_label_name + ':')
        self.code_writer.add_lines(expression_code)
        self._add_conditional_inversion()
        self.code_writer.add_line(f'jmp {loop_end_label_name} ${ARITHMETIC_REGISTER_ADDRESS}')
        self.block_end_stack.append([loop_end_label_name + ':', f'jmp {loop_label_name} 1'])
    
    def enterBlock(self, ctx: mlg1Parser.BlockContext):
        self.code_writer.indent_level += 1
    
    def exitBlock(self, ctx: mlg1Parser.BlockContext):
        self.code_writer.indent_level -= 1
        if isinstance(ctx.parentCtx, (mlg1Parser.IfStatementContext, mlg1Parser.ElseStatementContext, mlg1Parser.WhileLoopContext)):
            popped = self.block_end_stack.pop()
            if isinstance(popped, list):
                self.code_writer.add_lines(list(reversed(popped)))
            else:
                self.code_writer.add_line(popped)


def after_preprocess(compiler_state: CompilerState, data_file_path: str):
    """
    Called after preprocessing has finished.
    - Adds addresses of loaded files to the global namespace
    - Sets the HEAP address variable
    - Adds meta vars into the constant namespace
    - Generates the data file if necessary
    """
    data_file_rules = []
    for var_name, data_entry in compiler_state.data_entries.items():
        entry_type = data_entry['type']
        if entry_type == 'f':  # file
            file_path = data_entry['path']
            data_file_rules.append(f'{compiler_state.current_address} f {file_path}')
            compiler_state.constant_namespace[var_name] = compiler_state.current_address
            with open(file_path, 'rb') as f:
                file_bytes = f.read()
            file_extension = os.path.splitext(file_path)[1]
            compiler_state.current_address += get_parsed_file_size(file_bytes, file_extension)

        elif entry_type == 's':  # string
            string = data_entry['string']
            data_file_rules.append(f'{compiler_state.current_address} s {string}')
            compiler_state.string_vars[data_entry['var_address']] = compiler_state.current_address
            compiler_state.current_address += len(string) + 1  # add 1 for length prefix
    
    compiler_state.heap_address = compiler_state.current_address
    compiler_state.meta_variables['memory'] += compiler_state.heap_address  # offset requested memory by the stack memory size [note 2]
    compiler_state.constant_namespace[HEAP_VARIABLE_NAME] = compiler_state.heap_address

    # Add meta vars to the constant namespace to allow constant propagation
    for meta_var_name in META_VAR_DEFAULTS:
        compiler_state.constant_namespace[meta_var_name.upper()] = compiler_state.meta_variables[meta_var_name]
    
    # Write the data file
    if data_file_rules:
        data_file_cw = CodeWriter(compiler_state.compiler_flags.indent_size)
        data_file_cw.add_lines(data_file_rules)
        data_file_cw.write_file(data_file_path)


def preprocess(compiler_state: CompilerState, file_path: str) -> Result[None, str]:
    if not os.path.isfile(file_path):
        return Err(f'Path "{file_path}" does not exist or is not a file.')

    token_stream = FileStream(file_path)
    with open(file_path, 'r') as f:
        source_lines = f.read().split('\n')

    # Lexing
    error_listener = CustomErrorListener()
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
        print(f'{COLOR_ERROR}Preprocessing errors found in {file_path}:')
        for message in error_listener.errors:
            preprocess_error(message)
        return Err('Preprocessing error.')
    
    walker = ParseTreeWalker()
    source_file = os.path.splitext(os.path.basename(file_path))[0]
    listener = PreprocessListener(compiler_state, source_lines, source_file)
    walker.walk(listener, program_token)

    return Ok(None)


def codegen(compiler_state: CompilerState, code_writer: CodeWriter):
    # Add meta variable lines
    for meta_var_name, meta_var_value in compiler_state.meta_variables.items():
        code_writer.add_line(f'#{meta_var_name} {meta_var_value}')
    
    if compiler_state.contains_return:
        code_writer.add_lines(get_return_code(compiler_state.compiler_flags.indent_size))
    walker = ParseTreeWalker()

    # Walk through each function with the codegen listener
    for function_token in compiler_state.function_tokens:
        listener = CodegenListener(compiler_state, code_writer, function_token.source_lines, function_token.source_file)
        walker.walk(listener, function_token.token)
    
    code_writer.add_line('end:')


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
    
    compiler_flags = CompilerFlags(parsed_args.include_source, parsed_args.indent_size)
    compiler_state = CompilerState(compiler_flags)
    preprocess_result = preprocess(compiler_state, parsed_args.input_file)
    if isinstance(preprocess_result, Err):
        return 2
    
    after_preprocess(compiler_state, parsed_args.output_file + 'd')

    code_writer = CodeWriter(compiler_flags.indent_size)
    codegen(compiler_state, code_writer)
    code_writer.write_file(parsed_args.output_file)

    return 0


if __name__ == '__main__':
    sys.exit(main())