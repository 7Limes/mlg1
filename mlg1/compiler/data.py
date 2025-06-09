from dataclasses import dataclass, field
import copy
from mlg1.compiler.constants import *
from mlg1.compiler.util import error, is_arithmetic_register
from mlg1.parser.mlg1Parser import mlg1Parser


def default_field(obj):
    return field(default_factory=lambda: copy.copy(obj))


@dataclass
class CompilerFlags:
    """
    Contains user provided flags for the compiler to use.
    """
    
    include_source: bool
    indent_size: int


@dataclass
class FunctionToken:
    token: mlg1Parser.FunctionContext
    name: str
    source_file: str
    source_lines: list[str]


@dataclass
class CompilerState:
    compiler_flags: CompilerFlags
    meta_variables: dict[str, int] = default_field(META_VAR_DEFAULTS)
    function_namespaces: dict[str, dict[str, list[str]|dict[str, int]]] = default_field({})
    global_namespace: dict[str, int] = default_field(GLOBAL_NAMESPACE)
    constant_namespace: dict[str, int] = default_field({})
    string_vars: dict[int, int] = default_field({})
    contains_return: bool = False
    data_entries: dict[str, dict[str, str]] = default_field({})
    current_address: int = LOCAL_VAR_ADDRESS
    heap_address: int = -1

    function_tokens: list[FunctionToken] = default_field([])
    current_function_token: FunctionToken | None = None

    used_registers: list[str] = default_field([])


    def get_first_unused_register(self) -> str:
        for i in range(ARITHMETIC_REGISTER_ADDRESS, ARITHMETIC_REGISTER_ADDRESS+AMOUNT_ARITHMETIC_REGISTERS):
            register = f'${i}'
            if register not in self.used_registers:
                self.used_registers.append(register)
                return register
        error((-1, -1), '', 'Ran out of arithmetic registers!')


    def get_arithmetic_register(self, a: str, b: str) -> str:
        a_is_register = is_arithmetic_register(a)
        b_is_register = is_arithmetic_register(b)
        amount_registers = a_is_register + b_is_register
        
        if amount_registers == 0:  # neither are registers
            return self.get_first_unused_register()
        if amount_registers == 1:  # only 1 is a register
            return a if a_is_register else b
        # both are registers
        self.used_registers.remove(max(a, b))
        return min(a, b)