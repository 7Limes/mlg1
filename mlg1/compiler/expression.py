from collections import deque
from antlr4.tree.Tree import TerminalNodeImpl, TerminalNode
from mlg1.parser.mlg1Parser import mlg1Parser
from mlg1.compiler.constants import \
    BUILTIN_FUNCTIONS, BUILTIN_FUNCTION_ARGUMENT_COUNTS, \
    ARITHMETIC_REGISTER_ADDRESS, CALL_STACK_POINTER_ADDRESS, RETURN_REGISTER_ADDRESS
from mlg1.compiler.util import is_integer, error_ctx, is_arithmetic_register
from mlg1.compiler.data import CompilerState


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
    '>': {
        'function': lambda a, b: int(a>b),
        'instruction': 'less {dest} {b} {a}'
    },
    '<=': {
        'function': lambda a, b: int(a<=b),
        'instruction': 'less {dest} {b} {a}',
        'negate': True
    },
    '>=': {
        'function': lambda a, b: int(a>=b),
        'instruction': 'less {dest} {a} {b}',
        'negate': True
    },
    '!=': {
        'function': lambda a, b: int(a!=b),
        'instruction': 'equal {dest} {a} {b}',
        'negate': True
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


class FunctionCallHandler:
    def __init__(self, compiler_state: CompilerState, function_name: str, arguments: list[mlg1Parser.ExpressionContext], token: mlg1Parser.FunctionCallContext):
        self.compiler_state = compiler_state
        self.function_name = function_name
        self.arguments = arguments
        self.token = token
        self.is_builtin = function_name in BUILTIN_FUNCTIONS

    @staticmethod
    def from_token(compiler_state: CompilerState, token: mlg1Parser.FunctionCallContext):
        function_name = token.NAME().getText()
        argument_list_token = token.expressionList()
        function_args = []
        if argument_list_token is not None:
            function_args = [t for t in argument_list_token.children if isinstance(t, mlg1Parser.ExpressionContext)]
        return FunctionCallHandler(compiler_state, function_name, function_args, token)

    def generate_builtin(self, parent_function_name: str, return_register: int, current_register: int):
        generated_lines = []
        argument_destinations = range(current_register, current_register+4)
        builtin_arguments = {
            'return_register': return_register,
            'heap_address': self.compiler_state.heap_address
        }

        for i, expression_token, arg_destination in zip(range(len(self.arguments)), self.arguments, argument_destinations):
            expression = ExpressionHandler(self.compiler_state, expression_token, parent_function_name)
            expression_code = expression.generate_code(arg_destination)
            if expression_code[-1].startswith('mov'):
                builtin_arguments[f'a{i}'] = expression_code[-1].split(' ')[-1]  # very hacky but works (dont do this)
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
        argument_destinations = self.compiler_state.function_namespaces[self.function_name]['parameters']
        for expression_token, destination in zip(self.arguments, argument_destinations):
            expression = ExpressionHandler(self.compiler_state, expression_token, parent_function_name)
            expression_code = expression.generate_code(destination)
            generated_lines.extend(expression_code)

        token_position = (self.token.start.line, self.token.start.column)
        return_label = f'{self.function_name}_return_{token_position[0]}_{token_position[1]}'
        final_lines = [
            f'mov ${CALL_STACK_POINTER_ADDRESS} {return_label}',
            f'add {CALL_STACK_POINTER_ADDRESS} ${CALL_STACK_POINTER_ADDRESS} 1',
            f'jmp {self.function_name} 1',
            f'{return_label}:'
        ]
        generated_lines.extend(final_lines)
        return generated_lines

    def generate_code(self, parent_function_name: str, builtin_return_register: int, current_register: int) -> list[str]:
        name = self.function_name

        if not self.is_builtin and name not in self.compiler_state.function_namespaces:
            error_ctx(self.token, self.compiler_state.current_function_token.source_lines, f'Unrecognized function "{name}"')

        if self.is_builtin:
            amount_args = BUILTIN_FUNCTION_ARGUMENT_COUNTS[name]
        else:
            amount_args = len(self.compiler_state.function_namespaces[name]['parameters'])
        amount_passed_args = len(self.arguments)
        if amount_passed_args != amount_args:
            error_ctx(self.token, self.compiler_state.current_function_token.source_lines, f'Expected {amount_args} arguments for function "{name}" but got {amount_passed_args}.')
        
        if self.is_builtin:
            return self.generate_builtin(parent_function_name, builtin_return_register, current_register)
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
    
    def get_precedence(op: mlg1Parser.OperatorContext | mlg1Parser.UnaryOperatorContext) -> int:
        op_text = op.getText()
        if isinstance(op, mlg1Parser.UnaryOperatorContext):
            return 4
        if op_text in ['*', '/', '%']:
            return 3
        if op_text in ['+', '-']:
            return 2
        return 1  # default precedence for other operators

    
    for token in tokens:
        # primary
        if isinstance(token, (mlg1Parser.PrimaryContext, mlg1Parser.FunctionCallContext)):
            output.append(token)
            
        # operator
        elif isinstance(token, operator_types):
            while (operator_stack and 
                  isinstance(operator_stack[-1], operator_types) and
                  get_precedence(operator_stack[-1]) >= get_precedence(token)):
                output.append(operator_stack.pop())
            operator_stack.append(token)
            
        # left parenthesis
        elif isinstance(token, TerminalNodeImpl) and token.getText() == '(':
            operator_stack.append(token)
            
        # right parenthesis
        elif isinstance(token, TerminalNodeImpl) and token.getText() == ')':
            while operator_stack and not (
                isinstance(operator_stack[-1], TerminalNodeImpl) and 
                operator_stack[-1].getText() == '('
            ):
                output.append(operator_stack.pop())
                
            if operator_stack:
                operator_stack.pop()
                
            # function call
            if operator_stack and isinstance(operator_stack[-1], mlg1Parser.FunctionCallContext):
                output.append(operator_stack.pop())
    
    while operator_stack:
        top = operator_stack[-1]
        if isinstance(top, TerminalNodeImpl) and top.getText() in ['(', ')']:
            operator_stack.pop()
            continue
        output.append(operator_stack.pop())
    return output


class ExpressionHandler:
    def __init__(self, compiler_state: CompilerState, ctx: mlg1Parser.ExpressionContext, parent_function_name: str):
        self.compiler_state = compiler_state
        flat_expression = flatten_expression(ctx)
        rpn_expression = convert_to_rpn(flat_expression)
        self.expression_values: list[FunctionCallHandler | str] = [parse_primary(compiler_state, t, parent_function_name) for t in rpn_expression]
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
                        error_ctx(self.ctx, self.compiler_state.current_function_token.source_lines, 'Invalid RPN expression.')
            else:
                operand_count += 1
        if operand_count != 1:
            error_ctx(self.ctx, self.compiler_state.current_function_token.source_lines, 'RPN expression has leftover values.')
    
    def _reduce(self):
        stack = deque()

        for value in self.expression_values:
            if value not in OPERATORS:
                const_value = self.compiler_state.constant_namespace.get(value)
                if const_value is None:
                    added_value = value
                else:
                    added_value = str(const_value)
                stack.append(added_value)
            else:
                b = stack.pop()
                if OPERATORS[value].get('unary'):
                    if isinstance(b, str) and is_integer(b):
                        stack.append(str(OPERATORS[value]['function'](int(b))))
                    else:
                        stack.extend([b, value])
                else:
                    a = stack.pop()
                    if isinstance(a, str) and is_integer(a) and isinstance(b, str) and is_integer(b):
                        stack.append(str(OPERATORS[value]['function'](int(a), int(b))))
                    else:
                        stack.extend([a, b, value])
        
        self.expression_values = stack
    

    def generate_code(self, destination: int) -> list[str]:
        base_register: int = ARITHMETIC_REGISTER_ADDRESS
        for value in self.expression_values:
            if isinstance(value, FunctionCallHandler) and not value.is_builtin:
                index = self.compiler_state.function_base_registers[value.function_name]
                if index > base_register:
                    base_register = index
        current_register = base_register
        
        def value_to_string(value: FunctionCallHandler|str) -> str:
            nonlocal current_register
            if isinstance(value, FunctionCallHandler):  # value is a function call
                if value.is_builtin:
                    return_register = destination
                else:
                    return_register = current_register
                    current_register += 1
                function_call_code = value.generate_code(self.parent_function_name, return_register, current_register)
                generated_lines.extend(function_call_code)
                if not value.is_builtin:
                    generated_lines.append(f'mov {return_register} ${RETURN_REGISTER_ADDRESS}')
                return f'${return_register}'

            if is_integer(value):  # value is an integer
                return value
            
            if value in self.compiler_state.constant_namespace:  # value is a constant
                return str(self.compiler_state.constant_namespace[value])
            if value in self.compiler_state.global_namespace:  # value is a global variable
                return f'${self.compiler_state.global_namespace[value]}'
            return f'${self.compiler_state.function_namespaces[self.parent_function_name]["locals"][value]}'  # value is a local variable
        
        def get_arithmetic_register(a: str, b: str) -> str:
            nonlocal current_register
            a_is_register = is_arithmetic_register(a)
            b_is_register = is_arithmetic_register(b)
            amount_registers = a_is_register + b_is_register
            
            if amount_registers == 0:  # neither are registers
                register_string = f'${current_register}'
                current_register += 1
                return register_string
            if amount_registers == 1:  # only 1 is a register
                return a if a_is_register else b
            # both are registers
            current_register -= 1
            return min(a, b)
        
        def get_register(i: int, a: str, b: str|None):
            b = 'placeholder' if b is None else b  # [note 4]
            if i == len(self.expression_values)-1:
                returned_register = destination
            else:
                returned_register = int(get_arithmetic_register(a, b)[1:])
            return returned_register

        generated_lines = []
        stack = deque()
        for i, value in enumerate(self.expression_values):
            if value not in OPERATORS:
                stack.append(value_to_string(value))
            else:
                operator_data = OPERATORS[value]
                instruction_template: str = operator_data['instruction']
                negate_instruction = None
                if operator_data.get('unary'):
                    a = stack.pop()
                    register = get_register(i, a, None)
                    instruction = instruction_template.format(dest=register, a=a)
                else:
                    b = stack.pop()
                    a = stack.pop()
                    register = get_register(i, a, b)
                    instruction = instruction_template.format(dest=register, a=a, b=b)
                    if 'negate' in operator_data:
                        negate_instruction = f'not {register} ${register}'
                
                generated_lines.append(instruction)
                if negate_instruction:
                    generated_lines.append(negate_instruction)
                
                stack.append(f'${register}')
        
        function_base_register_value = self.compiler_state.function_base_registers.get(self.parent_function_name)
        if function_base_register_value is None or current_register > function_base_register_value:
            self.compiler_state.function_base_registers[self.parent_function_name] = current_register
        
        if not generated_lines:
            return [f'mov {destination} {stack[0]}']
        
        # Omit final mov if the expression consists solely of a builtin function call
        last_value = self.expression_values[-1]
        if last_value not in OPERATORS and not \
            (isinstance(last_value, FunctionCallHandler) and last_value.is_builtin):
            generated_lines.append(f'mov {destination} {stack[0]}')
        return generated_lines


def parse_primary(compiler_state: CompilerState, token: mlg1Parser.PrimaryContext, parent_function_name: str) -> ExpressionHandler | FunctionCallHandler | str:
    if isinstance(token, TerminalNode):
        return None
    
    first_child = None
    if token.children:
        first_child = token.children[0]

    if isinstance(first_child, mlg1Parser.ExpressionContext):  # Expression
        return ExpressionHandler(compiler_state, first_child, parent_function_name)
    
    if isinstance(first_child, mlg1Parser.FunctionCallContext):  # Function call
        return FunctionCallHandler.from_token(compiler_state, first_child)
    
    if isinstance(token, mlg1Parser.PrimaryContext):
        name = token.NAME()
        function_namespace = compiler_state.function_namespaces.get(parent_function_name)
        if function_namespace is None:
            function_locals = {}
        else:
            function_locals = function_namespace['locals']
        
        if name is not None and name.getText() not in function_locals \
            and name.getText() not in compiler_state.global_namespace \
            and name.getText() not in compiler_state.constant_namespace:
            error_source_lines = compiler_state.current_function_token.source_lines
            error_ctx(token, error_source_lines, f'Tried to reference undefined variable "{name}"')
        
        return token.getText()

    if isinstance(token, mlg1Parser.OperatorContext):  # Operator
        return token.getText()
    
    if isinstance(token, mlg1Parser.UnaryOperatorContext):
        if token.getText() == '-':  # Unary subtraction operator
            return r'\-'
        return token.getText()

    return None