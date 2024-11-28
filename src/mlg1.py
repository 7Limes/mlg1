"""
An mlg1 compiler implementation made with ANTLR.

By Miles Burkart
https://github.com/7Limes
11-27-2024
"""

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Tree import TerminalNodeImpl
from parser.mlg1Lexer import mlg1Lexer
from parser.mlg1Listener import mlg1Listener
from parser.mlg1Parser import mlg1Parser
import sys
import os
import dataclasses
import re


CALL_STACK_POINTER_ADDRESS = 14

RETURN_REGISTER_ADDRESS = 15
RETURN_ARITHMETIC_ADDRESS = 16

ARITHMETIC_REGISTER_ADDRESS = 17
AMOUNT_ARITHMETIC_REGISTERS = 15

CALL_STACK_DATA_ADDRESS = 32

LOCAL_VAR_ADDRESS = 64


INDENT_SIZE = 4

INTEGER_REGEX = re.compile('-?\d+')

RETURN_CODE = [
    'return:',
    f'{" "*INDENT_SIZE}sub {CALL_STACK_POINTER_ADDRESS} ${CALL_STACK_POINTER_ADDRESS} 1',
    f'{" "*INDENT_SIZE}movp {RETURN_ARITHMETIC_ADDRESS} ${CALL_STACK_POINTER_ADDRESS}',
    f'{" "*INDENT_SIZE}jmp ${RETURN_ARITHMETIC_ADDRESS} 1'
]


META_VAR_DEFAULTS = {'width': 100, 'height': 100, 'tickrate': 60, 'memory': 0}

GLOBAL_NAMESPACE = {
    'CONTROL1': 0,
    'CONTROL2': 1,
    'A': 2,
    'B': 3,
    'UP': 4,
    'DOWN': 5,
    'LEFT': 6,
    'RIGHT': 7,
    'MEMORY': 8,
    'WIDTH': 9,
    'HEIGHT': 10,
    'TICKRATE': 11,
    'DELTA': 12
}

RESERVED_NAMES = {'let', 'fn', 'return'}
RESERVED_NAMES.update(GLOBAL_NAMESPACE.keys())


COLOR_ERROR = '\x1b[31m'
COLOR_RESET = '\x1b[0m'


OPERATORS = {
    '+': {
        'function': lambda a, b: a+b,
        'instruction': 'add {dest} {a} {b}'
    },
    '-': {
        'function': lambda a, b: a-b,
        'instruction': 'sub {dest} {a} {b}'
    },
    '*': {
        'function': lambda a, b: a*b,
        'instruction': 'mul {dest} {a} {b}'
    },
    '/': {
        'function': lambda a, b: a//b,
        'instruction': 'div {dest} {a} {b}'
    },
    '%': {
        'function': lambda a, b: a%b,
        'instruction': 'mod {dest} {a} {b}'
    },
    '==': {
        'function': lambda a, b: int(a==b),
        'instruction': 'equal {dest} {a} {b}'
    },
    '<': {
        'function': lambda a, b: int(a<b),
        'instruction': 'less {dest} {a} {b}'
    },
    '!': {
        'function': lambda a: int(not a),
        'instruction': 'not {dest} {a}',
        'unary': True
    },
    r'\-': {  # Unary subtraction
        'function': lambda a: -a,
        'instruction': 'mul {dest} {a} -1',
        'unary': True
    }
}

BUILTIN_FUNCTIONS = {
    'color': [
        'color {a0} {a1} {a2}'
    ],
    'point': [
        'point {a0} {a1} {a2} {a3}'
    ],
    'line': [
        'line {a0} {a1} {a2} {a3}'
    ],
    'rect': [
        'rect {a0} {a1} {a2} {a3}'
    ],
    'get': [
        'add {return_register} {a0} {heap_address}',
        'movp {return_register} ${return_register}'
    ],
    'set': [
        'add {return_register} {a0} {heap_address}',
        'mov ${return_register} {a1}'
    ]
}


def list_get(l: list, index: int, default=None):
    try:
        return l[index]
    except IndexError:
        return default


def is_integer(s: str) -> bool:
    return bool(INTEGER_REGEX.match(s))


def get_ctx_pos(ctx: ParserRuleContext) -> tuple[int, int]:
    return ctx.start.line, ctx.start.column

def error(position: tuple[int, int], line_text: str, message: str):
    print(f'{COLOR_ERROR}ERROR:', message)
    print(f'{position[0]+1} | {line_text}')
    print(f'{" " * (len(str(position[0]+1))+3+position[1])}^{COLOR_RESET}')
    sys.exit(1)

def error_ctx(ctx: ParserRuleContext, source_lines: list[str], message: str):
    line, column = get_ctx_pos(ctx)
    error((line-1, column), source_lines[line-1], message)

def preprocess_error(message: str):
    print(f'    {COLOR_ERROR}{message}{COLOR_RESET}')


class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_type = "Lexical" if isinstance(recognizer, Lexer) else "Parsing"
        self.errors.append(f"{error_type} error at line {line}, column {column}: {msg}")


class CodeWriter:
    def __init__(self):
        self.lines: list[str] = []
        self.indent_level = 0
        self.last_line: str = ''

    def add_line(self, line: str, from_start: bool=False):
        wrote_line = ' '*self.indent_level*INDENT_SIZE + line
        if from_start:
            self.lines.insert(0, wrote_line)
        else:
            self.lines.append(wrote_line)
            self.last_line = line
    
    def add_lines(self, lines: list[str], from_start: bool=False):
        for line in lines:
            self.add_line(line, from_start)
        self.last_line = lines[-1]

    def write_file(self, file_path: str):
        with open(file_path, 'w') as f:
            f.write('\n'.join(self.lines))


@dataclasses.dataclass
class CompilerFlags:
    contains_return: bool=False

@dataclasses.dataclass
class CompilerData:
    source_lines: list[str]
    meta_variables: dict[str, int]
    function_namespaces: dict[str, dict[str, list[str]|dict[str, int]]]
    global_namespace: dict[str, int]
    constant_namespace: dict[str, int]
    compiler_flags: CompilerFlags
    heap_address: int
    code_writer: CodeWriter
    used_registers: list[str]


    def get_first_unused_register(self) -> str:
        for i in range(ARITHMETIC_REGISTER_ADDRESS, ARITHMETIC_REGISTER_ADDRESS+AMOUNT_ARITHMETIC_REGISTERS):
            register = f'${i}'
            if register not in self.used_registers:
                self.used_registers.append(register)
                return register
        error((-1, -1), '', 'Ran out of arithmetic registers!')
    

    def is_arithmetic_register(self, value: str) -> bool:
        is_register = value[0] == '$'
        if is_register:
            register_number = int(value[1:])
            return is_register and register_number >= ARITHMETIC_REGISTER_ADDRESS and \
                   register_number < ARITHMETIC_REGISTER_ADDRESS+AMOUNT_ARITHMETIC_REGISTERS
        return False


    def get_arithmetic_register(self, a: str, b: str) -> str:
        a_is_register = self.is_arithmetic_register(a)
        b_is_register = self.is_arithmetic_register(b)
        amount_registers = a_is_register + b_is_register
        if amount_registers == 0:  # neither are registers
            return self.get_first_unused_register()
        elif amount_registers == 1:  # only 1 is a register
            return a if a_is_register else b
        else:  # both are registers
            self.used_registers.remove(max(a, b))
            return min(a, b)


class FunctionCallHandler:
    def __init__(self, compiler_data: CompilerData, function_name: str, arguments: list[mlg1Parser.ExpressionContext], token_position: tuple[int, int]):
        self.compiler_data = compiler_data
        self.function_name = function_name
        self.arguments = arguments
        self.token_position = token_position

    @staticmethod
    def from_token(compiler_data: CompilerData, token: mlg1Parser.FunctionCallContext):
        function_name = token.NAME().getText()
        argument_list_token = token.argumentList()
        function_args = []
        if argument_list_token is not None:
            function_args = [t for t in argument_list_token.children if isinstance(t, mlg1Parser.ExpressionContext)]
        token_position = (token.start.line, token.start.column)
        return FunctionCallHandler(compiler_data, function_name, function_args, token_position)

    def generate_builtin(self, parent_function_name: str, return_register: int):
        generated_lines = []
        argument_destinations = range(ARITHMETIC_REGISTER_ADDRESS, ARITHMETIC_REGISTER_ADDRESS+4)
        builtin_arguments = {
            'return_register': return_register,
            'heap_address': self.compiler_data.heap_address
        }
        for i, expression_token, arg_destination in zip(range(len(self.arguments)), self.arguments, argument_destinations):
            expression = ExpressionHandler(self.compiler_data, expression_token, parent_function_name)
            expression_code = expression.generate_code(arg_destination)
            if expression_code[0].startswith('mov'):
                builtin_arguments[f'a{i}'] = expression_code[0].split(' ')[-1]  # very hacky but works (dont do this)
            else:
                builtin_arguments[f'a{i}'] = f'${arg_destination}'
                generated_lines.extend(expression_code)

        parsed_lines = []
        for line in BUILTIN_FUNCTIONS[self.function_name]:
            line = line.format(**builtin_arguments)
            parsed_lines.append(line)
        generated_lines.extend(parsed_lines)
        return generated_lines

    def generate_regular(self, parent_function_name: str) -> list[str]:
        generated_lines = []
        argument_destinations = self.compiler_data.function_namespaces[self.function_name]['parameters']
        for expression_token, destination in zip(self.arguments, argument_destinations):
            expression = ExpressionHandler(self.compiler_data, expression_token, parent_function_name)
            expression_code = expression.generate_code(destination)
            generated_lines.extend(expression_code)

        return_label = f'{self.function_name}_return_{self.token_position[0]}_{self.token_position[1]}'
        final_lines = [
            f'mov ${CALL_STACK_POINTER_ADDRESS} {return_label}',
            f'add {CALL_STACK_POINTER_ADDRESS} ${CALL_STACK_POINTER_ADDRESS} 1',
            f'jmp {self.function_name} 1',
            f'{return_label}:'
        ]
        generated_lines.extend(final_lines)
        return generated_lines

    def generate_code(self, parent_function_name: str, builtin_return_register: int) -> list[str]:
        if self.function_name in BUILTIN_FUNCTIONS:
            return self.generate_builtin(parent_function_name, builtin_return_register)
        return self.generate_regular(parent_function_name)


def flatten_expression(ctx: mlg1Parser.ExpressionContext) -> list:
    tokens = []
    def flatten(node):
        if isinstance(node, (mlg1Parser.PrimaryContext,
                             mlg1Parser.OperatorContext,
                             mlg1Parser.UnaryOperatorContext
                             )):
            tokens.append(node)
            return
        if isinstance(node, TerminalNodeImpl) and node.getText() in ['(', ')']:
            tokens.append(node)
            return
        if isinstance(node, (mlg1Parser.ExpressionContext,
                             mlg1Parser.UnaryExpressionContext
                             )):
            for child in node.getChildren():
                flatten(child)
    
    flatten(ctx)
    return tokens


def convert_to_rpn(tokens: list) -> list:
    output = []
    operator_stack = []
    operator_types = (mlg1Parser.OperatorContext, mlg1Parser.UnaryOperatorContext)
    
    # Helper function to get operator precedence
    def get_precedence(op: mlg1Parser.OperatorContext | mlg1Parser.UnaryOperatorContext) -> int:
        # Customize these precedence levels according to your grammar
        op_text = op.getText()
        if isinstance(op, mlg1Parser.UnaryOperatorContext):
            return 4
        if op_text in ['*', '/', '%']:
            return 3
        elif op_text in ['+', '-']:
            return 2
        return 1  # Default precedence for other operators

    # Process each token in the expression
    for token in tokens:
        # If it's a primary (number, variable) or function call, add to output
        if isinstance(token, mlg1Parser.PrimaryContext) or \
           isinstance(token, mlg1Parser.FunctionCallContext):
            output.append(token)
            
        # If it's an operator
        elif isinstance(token, operator_types):
            # While there's an operator on top of the stack with greater or equal precedence
            while (operator_stack and 
                  isinstance(operator_stack[-1], operator_types) and
                  get_precedence(operator_stack[-1]) >= get_precedence(token)):
                output.append(operator_stack.pop())
            operator_stack.append(token)
            
        # If it's a left parenthesis
        elif isinstance(token, TerminalNodeImpl) and token.getText() == '(':
            operator_stack.append(token)
            
        # If it's a right parenthesis
        elif isinstance(token, TerminalNodeImpl) and token.getText() == ')':
            # Pop operators until we find the matching left parenthesis
            while operator_stack and not (
                isinstance(operator_stack[-1], TerminalNodeImpl) and 
                operator_stack[-1].getText() == '('
            ):
                output.append(operator_stack.pop())
                
            # Pop the left parenthesis
            if operator_stack:  # Check if there was a matching left parenthesis
                operator_stack.pop()
                
            # If there's a function call on top of the stack, add it to output
            if operator_stack and isinstance(operator_stack[-1], mlg1Parser.FunctionCallContext):
                output.append(operator_stack.pop())
    
    # Pop any remaining operators from the stack
    while operator_stack:
        top = operator_stack[-1]
        # Don't add parentheses to the output
        if isinstance(top, TerminalNodeImpl) and top.getText() in ['(', ')']:
            operator_stack.pop()
            continue
        output.append(operator_stack.pop())
    return output


class ExpressionHandler:
    def __init__(self, compiler_data: CompilerData, ctx: mlg1Parser.ExpressionContext, parent_function_name: str):
        self.compiler_data = compiler_data
        flat_expression = flatten_expression(ctx)
        rpn_expression = convert_to_rpn(flat_expression)
        self.expression_values: list[FunctionCallHandler | str] = [parse_primary(compiler_data, t, parent_function_name) for t in rpn_expression]
        self.expression_values = [t for t in self.expression_values if t is not None]
        self.ctx = ctx
        self.parent_function_name = parent_function_name

        self._check()
        self._reduce()
    
    def _check(self):
        operand_count = 0
        for value in self.expression_values:
            if value in OPERATORS:
                if OPERATORS[value].get('unary') is None:
                    operand_count -= 1
                    if operand_count <= 0:
                        error_ctx(self.ctx, self.compiler_data.source_lines, 'Invalid RPN expression.')
            else:
                operand_count += 1
        if operand_count != 1:
            error_ctx(self.ctx, self.compiler_data.source_lines, 'RPN expression has leftover values.')
    
    def _reduce(self):
        stack = []

        def pop_parse() -> str:
            value = stack.pop()
            if not isinstance(value, str) or is_integer(value):
                return value
            const_value = self.compiler_data.constant_namespace.get(value)
            return str(const_value) if const_value is not None else value

        for value in self.expression_values:
            if value not in OPERATORS:
                stack.append(value)
            else:
                b = pop_parse()
                if OPERATORS[value].get('unary'):
                    if isinstance(b, str) and is_integer(b):
                        stack.append(str(OPERATORS[value]['function'](int(b))))
                    else:
                        stack.extend([b, value])
                else:
                    a = pop_parse()
                    if isinstance(a, str) and is_integer(a) and isinstance(b, str) and is_integer(b):
                        stack.append(str(OPERATORS[value]['function'](int(a), int(b))))
                    else:
                        stack.extend([a, b, value])
        self.expression_values = stack
    

    def generate_code(self, destination: int) -> list[str]:
        def value_to_string(value: FunctionCallHandler|str) -> str:
            if isinstance(value, FunctionCallHandler):  # value is a function call
                return_register = int(self.compiler_data.get_first_unused_register()[1:])
                function_call_code = value.generate_code(self.parent_function_name, return_register)
                generated_lines.extend(function_call_code)
                if value.function_name not in BUILTIN_FUNCTIONS:
                    generated_lines.append(f'mov {return_register} ${RETURN_REGISTER_ADDRESS}')
                return f'${return_register}'

            if is_integer(value):  # value is an integer
                return value
            
            if value in self.compiler_data.constant_namespace:  # value is a constant
                return str(self.compiler_data.constant_namespace[value])
            if value in self.compiler_data.global_namespace:  # value is a global variable
                return f'${self.compiler_data.global_namespace[value]}'
            return f'${self.compiler_data.function_namespaces[self.parent_function_name]["locals"][value]}'  # value is a local variable
        
        def get_register(i: int, a: str, b: str|None):
            b = 'placeholder' if b is None else b  # [note 4]
            if i == len(self.expression_values)-1:
                if self.compiler_data.used_registers:
                    self.compiler_data.used_registers.pop()  # not sure that this works 100% of the time
                return destination
            return int(self.compiler_data.get_arithmetic_register(a, b)[1:])

        generated_lines = []
        stack = []
        for i, value in enumerate(self.expression_values):
            if value not in OPERATORS:
                stack.append(value_to_string(value))
            else:
                instruction_template: str = OPERATORS[value]['instruction']
                if OPERATORS[value].get('unary'):
                    a = stack.pop()
                    register = get_register(i, a, None)
                    instruction = instruction_template.format(dest=register, a=a)
                else:
                    b = stack.pop()
                    a = stack.pop()
                    register = get_register(i, a, b)
                    instruction = instruction_template.format(dest=register, a=a, b=b)
                generated_lines.append(instruction)
                stack.append(f'${register}')
        
        if not generated_lines:
            return [f'mov {destination} {stack[0]}']
        if self.expression_values[-1] not in OPERATORS:
            generated_lines.append(f'mov {destination} {stack[0]}')
        return generated_lines


def parse_primary(compiler_data: CompilerData, token: mlg1Parser.PrimaryContext, parent_function_name: str) -> ExpressionHandler | FunctionCallHandler | str:
    first_child = None
    if isinstance(token, TerminalNode):
        return None
    if token.children:
        first_child = token.children[0]
    if isinstance(first_child, mlg1Parser.ExpressionContext):  # Expression
        return ExpressionHandler(compiler_data, first_child, parent_function_name)
    if isinstance(first_child, mlg1Parser.FunctionCallContext):  # Function call
        return FunctionCallHandler.from_token(compiler_data, first_child)
    if isinstance(token, mlg1Parser.PrimaryContext):
        name = token.NAME()
        function_locals = compiler_data.function_namespaces[parent_function_name]['locals']
        if name is not None and name.getText() not in function_locals \
            and name.getText() not in compiler_data.global_namespace \
            and name.getText() not in compiler_data.constant_namespace:
            error_ctx(token, compiler_data.source_lines, f'Tried to reference undefined variable "{name}"')
        return token.getText()
    if isinstance(token, mlg1Parser.OperatorContext):  # Operator
        return token.getText()
    if isinstance(token, mlg1Parser.UnaryOperatorContext):
        if token.getText() == '-':  # Unary subtraction operator
            return r'\-'
        return token.getText()
    return None


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


def get_compiler_data(program: mlg1Parser.ProgramContext, source_lines: list[str], walker: ParseTreeWalker) -> CompilerData:
    listener = InitialListener(source_lines)
    walker.walk(listener, program)
    cd = CompilerData(
        source_lines, listener.meta_variables,
        listener.function_namespaces, listener.global_namespace, listener.constant_namespace,
        listener.compiler_flags, listener.current_address, CodeWriter(), []
    )
    cd.meta_variables['memory'] += cd.heap_address  # offset requested memory by the stack memory size [note 2]
    return cd


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
    
    compiler_data = get_compiler_data(program, source_lines, walker)

    main_listener = MainListener(compiler_data)
    walker.walk(main_listener, program)
    compiler_data.code_writer.add_line('end:')
    main_listener.compiler_data.code_writer.write_file(argv[2])

    return 0


if __name__ == '__main__':
    main(sys.argv)