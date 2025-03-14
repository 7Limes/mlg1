"""
An mlg1 compiler implementation made with ANTLR.

By Miles Burkart
https://github.com/7Limes
2-7-2025
"""

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from mlg1.parser.mlg1Lexer import mlg1Lexer
from mlg1.parser.mlg1Listener import mlg1Listener
from mlg1.parser.mlg1Parser import mlg1Parser
import sys
import os
from mlg1.compiler.constants import *
from mlg1.compiler.util import error, preprocess_error, COLOR_ERROR
from mlg1.compiler.expression import FunctionCallHandler, ExpressionHandler
from mlg1.compiler.data import CompilerData, CompilerFlags, CodeWriter
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
        self.current_function: str = None
        self.files_to_load: dict[str, str] = {}
        self.compiler_flags = CompilerFlags()
    
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
            self.compiler_flags.contains_return = True  # add returning code if a custom function exists [note 1]
        
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
        if name in RESERVED_NAMES:
            self.error(ctx, f'Variable name "{name}" is reserved.')
        current_locals = self.function_namespaces[self.current_function]['locals']
        if name in current_locals or name in self.global_namespace or name in self.constant_namespace:
            self.error(ctx, f'Variable "{name}" declared twice.')
        if self.current_function is None:
            self.error(ctx, 'Current function is None.')
        
        if keyword == 'let':  # local var
            self.function_namespaces[self.current_function]['locals'][name] = self.current_address
        else:  # global var
            self.global_namespace[name] = self.current_address
        self.current_address += 1
    
    def enterConstantDefinition(self, ctx: mlg1Parser.ConstantDefinitionContext):
        name = ctx.NAME().getText()
        value = int(ctx.INTEGER().getText())
        self.constant_namespace[name] = value
    
    def enterLoadFile(self, ctx):
        name = ctx.NAME().getText()
        path = ctx.STRING().getText()
        self.files_to_load[name] = path[1:-1]
    

    def after_walk(self) -> list[str]:
        """
        Called after this listener has finished walking the parse tree.
        Adds addresses of loaded files to the global namespace and sets the HEAP address variable
        """
        data_file_rules = []
        for var_name, file_path in self.files_to_load.items():
            data_file_rules.append(f'{self.current_address} f {file_path}')
            self.constant_namespace[var_name] = self.current_address
            with open(file_path, 'rb') as f:
                file_bytes = f.read()
            file_extension = os.path.splitext(file_path)[1]
            self.current_address += get_parsed_file_size(file_bytes, file_extension)
        
        self.constant_namespace[HEAP_VARIABLE_NAME] = self.current_address

        return data_file_rules

class MainListener(BaseListener):
    def __init__(self, compiler_data: CompilerData) -> None:
        super().__init__(compiler_data.source_lines)
        self.compiler_data = compiler_data

        self.current_function = None

        self.block_end_stack: list[str] = []

        # Add meta variable lines
        for meta_var_name, meta_var_value in self.compiler_data.meta_variables.items():
            self.compiler_data.code_writer.add_line(f'#{meta_var_name} {meta_var_value}')
        
        if self.compiler_data.compiler_flags.contains_return:
            self.compiler_data.code_writer.add_lines(RETURN_CODE)
    
    def _get_var_address(self, var_name: str, is_global: bool) -> int:
        if is_global:
            return self.compiler_data.global_namespace[var_name]
        return self.compiler_data.function_namespaces[self.current_function]['locals'][var_name]


    def _add_conditional_inversion(self):
        inversion_instruction = f'not {ARITHMETIC_REGISTER_ADDRESS} ${ARITHMETIC_REGISTER_ADDRESS}'
        if self.compiler_data.code_writer.last_line == inversion_instruction:  # [note 3]
            self.compiler_data.code_writer.lines.pop()
        else:
            self.compiler_data.code_writer.add_line(inversion_instruction)


    def enterFunction(self, ctx: mlg1Parser.FunctionContext):
        function_name = ctx.NAME().getText()
        self.compiler_data.code_writer.add_lines(['', f'{function_name}:'])
        if function_name == 'start' and self.compiler_data.compiler_flags.contains_return:
            self.compiler_data.code_writer.add_line(f'{" "*INDENT_SIZE}mov {CALL_STACK_POINTER_ADDRESS} {CALL_STACK_DATA_ADDRESS}')
        self.current_function = function_name
    
    def exitFunction(self, ctx: mlg1Parser.FunctionContext):
        self.current_function = None
        if ctx.NAME().getText() in {'start', 'tick'}:
            self.compiler_data.code_writer.add_line('jmp end 1')
        elif self.compiler_data.code_writer.last_line != 'jmp return 1':
            self.compiler_data.code_writer.add_line(f'{" "*INDENT_SIZE}jmp return 1')
    
    def enterVariableDeclaration(self, ctx: mlg1Parser.VariableDeclarationContext):
        expression_token = ctx.expression()
        expression = ExpressionHandler(self.compiler_data, expression_token, self.current_function)
        var_name = ctx.NAME().getText()
        is_global = ctx.VARIABLE_KEYWORD().getText() == 'global'
        expression_code = expression.generate_code(self._get_var_address(var_name, is_global))
        self.compiler_data.code_writer.add_lines(expression_code)
    
    def enterAssignment(self, ctx: mlg1Parser.AssignmentContext):
        expression_token = ctx.expression()
        expression = ExpressionHandler(self.compiler_data, expression_token, self.current_function)
        var_name = ctx.NAME().getText()
        is_global = var_name in self.compiler_data.global_namespace
        expression_code = expression.generate_code(self._get_var_address(var_name, is_global))
        self.compiler_data.code_writer.add_lines(expression_code)
    
    def enterFunctionCall(self, ctx: mlg1Parser.FunctionCallContext):
        if isinstance(ctx.parentCtx, mlg1Parser.StatementContext):
            function_call = FunctionCallHandler.from_token(self.compiler_data, ctx)
            function_call_code = function_call.generate_code(self.current_function, RETURN_REGISTER_ADDRESS)
            self.compiler_data.code_writer.add_lines(function_call_code)
    
    def enterReturnStatement(self, ctx: mlg1Parser.ReturnStatementContext):
        expression_token = ctx.expression()
        expression = ExpressionHandler(self.compiler_data, expression_token, self.current_function)
        expression_code = expression.generate_code(RETURN_REGISTER_ADDRESS)
        self.compiler_data.code_writer.add_lines(expression_code)
        self.compiler_data.code_writer.add_line('jmp return 1')
    
    def enterIfStatement(self, ctx: mlg1Parser.IfStatementContext):
        condition_expression_token = ctx.expression()
        condition_expression = ExpressionHandler(self.compiler_data, condition_expression_token, self.current_function)
        expression_code = condition_expression.generate_code(ARITHMETIC_REGISTER_ADDRESS)
        self.compiler_data.code_writer.add_lines(expression_code)
        self._add_conditional_inversion()

        else_token = ctx.elseStatement()
        if else_token is None:
            skip_label_name = f'{self.current_function}_skip_{ctx.start.line}_{ctx.start.column}'
            self.compiler_data.code_writer.add_line(f'jmp {skip_label_name} ${ARITHMETIC_REGISTER_ADDRESS}')
            self.block_end_stack.append(skip_label_name + ':')
        else:
            else_label_name = f'{self.current_function}_else_{ctx.start.line}_{ctx.start.column}'
            end_label_name = f'{self.current_function}_end_{ctx.start.line}_{ctx.start.column}'
            self.compiler_data.code_writer.add_line(f'jmp {else_label_name} ${ARITHMETIC_REGISTER_ADDRESS}')
            self.block_end_stack.extend([end_label_name + ':', [else_label_name + ':', f'jmp {end_label_name} 1']])
    
    def enterWhileLoop(self, ctx: mlg1Parser.WhileLoopContext):
        loop_label_name = f'{self.current_function}_loop_{ctx.start.line}_{ctx.start.column}'
        loop_end_label_name = f'{self.current_function}_end_{ctx.start.line}_{ctx.start.column}'
        condition_expression_token = ctx.expression()
        condition_expression = ExpressionHandler(self.compiler_data, condition_expression_token, self.current_function)
        expression_code = condition_expression.generate_code(ARITHMETIC_REGISTER_ADDRESS)
        self.compiler_data.code_writer.add_line(loop_label_name + ':')
        self.compiler_data.code_writer.add_lines(expression_code)
        self._add_conditional_inversion()
        self.compiler_data.code_writer.add_line(f'jmp {loop_end_label_name} ${ARITHMETIC_REGISTER_ADDRESS}')
        self.block_end_stack.append([loop_end_label_name + ':', f'jmp {loop_label_name} 1'])
    
    def enterBlock(self, ctx: mlg1Parser.BlockContext):
        self.compiler_data.code_writer.indent_level += 1
    
    def exitBlock(self, ctx: mlg1Parser.BlockContext):
        self.compiler_data.code_writer.indent_level -= 1
        if isinstance(ctx.parentCtx, (mlg1Parser.IfStatementContext, mlg1Parser.ElseStatementContext, mlg1Parser.WhileLoopContext)):
            popped = self.block_end_stack.pop()
            if isinstance(popped, list):
                self.compiler_data.code_writer.add_lines(list(reversed(popped)))
            else:
                self.compiler_data.code_writer.add_line(popped)


def get_compiler_data(program: mlg1Parser.ProgramContext, source_lines: list[str], walker: ParseTreeWalker) -> tuple[CompilerData, list[str]]:
    listener = InitialListener(source_lines)
    walker.walk(listener, program)
    data_file_rules = listener.after_walk()
    cd = CompilerData(
        source_lines, listener.meta_variables,
        listener.function_namespaces, listener.global_namespace, listener.constant_namespace,
        listener.compiler_flags, listener.current_address, CodeWriter(), []
    )
    cd.meta_variables['memory'] += cd.heap_address  # offset requested memory by the stack memory size [note 2]
    return cd, data_file_rules


def validate_cli_args(argv: list[str]):
    if len(argv) <= 1:
        print('USAGE: mlg1 [infile] [outfile]')
        return -1
    if len(argv) == 2:
        print('Please enter an output file.')
        return -2
    if not os.path.isfile(argv[1]):
        print(f'Path "{argv[1]}" does not exist or is not a file.')
        return -3
    return 0


def main(argv) -> int:
    valid_args = validate_cli_args(argv)
    if valid_args != 0:
        return valid_args

    token_stream = FileStream(argv[1])
    with open(argv[1], 'r') as f:
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
        return -1
    
    walker = ParseTreeWalker()
    
    compiler_data, data_file_rules = get_compiler_data(program, source_lines, walker)

    main_listener = MainListener(compiler_data)
    walker.walk(main_listener, program)
    compiler_data.code_writer.add_line('end:')
    main_listener.compiler_data.code_writer.write_file(argv[2])
    if data_file_rules:
        data_file_cw = CodeWriter()
        data_file_cw.add_lines(data_file_rules)
        data_file_cw.write_file(argv[2] + 'd')

    return 0


if __name__ == '__main__':
    main(sys.argv)