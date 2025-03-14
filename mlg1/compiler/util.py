import sys
import re
from antlr4 import ParserRuleContext


INTEGER_REGEX = re.compile(r'-?\d+')

COLOR_ERROR = '\x1b[31m'
COLOR_RESET = '\x1b[0m'


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