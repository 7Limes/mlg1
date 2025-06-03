import dataclasses
from mlg1.compiler.constants import *
from mlg1.compiler.util import error


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
    """
    Contains user provided flags for the compiler to use.
    """
    
    include_source: bool


@dataclasses.dataclass
class CompilerState:
    source_lines: list[str]
    compiler_flags: CompilerFlags
    meta_variables: dict[str, int]
    function_namespaces: dict[str, dict[str, list[str]|dict[str, int]]]
    global_namespace: dict[str, int]
    constant_namespace: dict[str, int]
    string_vars: dict[int, int]
    contains_return: bool
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