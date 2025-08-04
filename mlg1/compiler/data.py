from dataclasses import dataclass, field
import copy
from typing import TypedDict
from mlg1.compiler.constants import *
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


class FunctionNamespace(TypedDict):
    parameter_count: int
    locals: dict[str, int]


@dataclass
class CompilerState:
    compiler_flags: CompilerFlags
    meta_variables: dict[str, int] = default_field(META_VAR_DEFAULTS)
    function_namespaces: dict[str, FunctionNamespace] = default_field({})
    global_namespace: dict[str, int] = default_field(GLOBAL_NAMESPACE)
    constant_namespace: dict[str, int] = default_field({})
    string_vars: dict[int, int] = default_field({})
    contains_return: bool = False
    data_entries: dict[str, dict[str, str]] = default_field({})
    current_address: int = LOCAL_VAR_ADDRESS
    heap_address: int = -1

    function_tokens: list[FunctionToken] = default_field([])
    current_function_token: FunctionToken | None = None
    called_functions: set[str] = default_field({'start', 'tick'})

    function_base_registers: dict[str, int] = default_field({})

    def get_current_namespace(self):
        """Returns the namespace of the current function."""
        if self.current_function_token is None:
            return None
        return self.function_namespaces[self.current_function_token.name]
