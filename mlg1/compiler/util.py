import sys
import re
from antlr4 import ParserRuleContext
from mlg1.compiler.constants import ARITHMETIC_REGISTER_ADDRESS, AMOUNT_ARITHMETIC_REGISTERS


INTEGER_REGEX = re.compile(r'-?\d+')

COLOR_ERROR = '\x1b[31m'
COLOR_RESET = '\x1b[0m'


class CodeWriter:
    def __init__(self, indent_size: int):
        self.lines: list[str] = []
        self.indent_size = indent_size
        self.indent_level = 0
        self.last_line: str = ''

    def add_line(self, line: str, from_start: bool=False):
        wrote_line = ' '*self.indent_level*self.indent_size + line
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


def is_integer(s: str) -> bool:
    return bool(INTEGER_REGEX.match(s))


def error(position: tuple[int, int], line_text: str, message: str):
    print(f'{COLOR_ERROR}ERROR:', message)
    print(f'{position[0]+1} | {line_text}')
    print(f'{" " * (len(str(position[0]+1))+3+position[1])}^{COLOR_RESET}')
    sys.exit(1)

def get_ctx_pos(ctx: ParserRuleContext) -> tuple[int, int]:
    return ctx.start.line, ctx.start.column

def error_ctx(ctx: ParserRuleContext, source_lines: list[str], message: str):
    line, column = get_ctx_pos(ctx)
    error((line-1, column), source_lines[line-1], message)

def generic_error(message: str):
    print(f'{COLOR_ERROR}{message}{COLOR_RESET}')

    
def is_arithmetic_register(value: str) -> bool:
    is_register = value[0] == '$'
    if is_register:
        register_number = int(value[1:])
        return is_register and register_number >= ARITHMETIC_REGISTER_ADDRESS and \
                register_number < ARITHMETIC_REGISTER_ADDRESS+AMOUNT_ARITHMETIC_REGISTERS
    return False