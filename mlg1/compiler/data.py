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
    called_functions: set[str]


class FunctionNamespace(TypedDict):
    parameter_count: int
    locals: dict[str, int]


class DataEntry(TypedDict):
    data_type: str
    operation: str
    data: str
    var_address: int|None = None


@dataclass
class Namespaces:
    current_local_namespace: FunctionNamespace | None
    local_namespaces: dict[str, FunctionNamespace] = default_field({})
    constant_namespace: dict[str, int] = default_field({})
    global_namespace: dict[str, int] = default_field(GLOBAL_NAMESPACE)


@dataclass
class ContextOverride:
    source_file: str
    source_lines: list[str]


@dataclass
class InitialPassData:
    meta_variables: dict[str, int] = default_field(META_VAR_DEFAULTS)
    included_files: set[str] = default_field(set())
    function_tokens: dict[str, FunctionToken] = default_field({})
    data_entries: dict[str, DataEntry] = default_field({})
    constant_namespace: dict[str, int] = default_field({})

    # Each contains a tuple of (token, source file)
    global_var_tokens: list[tuple[mlg1Parser.GlobalVarDeclarationContext, ContextOverride]] = default_field([])
    global_array_tokens: list[tuple[mlg1Parser.GlobalArrayDeclarationContext, ContextOverride]] = default_field([])

    def __post_init__(self):
        # Add default meta var values to constant namespace
        for meta_var_name, default_value in META_VAR_DEFAULTS.items():
            self.constant_namespace[meta_var_name.upper()] = default_value


@dataclass
class MemoryPassData:
    meta_variables: dict[str, int]
    constant_namespace: dict[str, int]
    data_entries: dict[str, DataEntry]
    function_tokens: dict[str, FunctionToken]
    global_var_tokens: list[tuple[mlg1Parser.GlobalVarDeclarationContext, ContextOverride]]
    global_array_tokens: list[tuple[mlg1Parser.GlobalArrayDeclarationContext, ContextOverride]]

    current_address: int = LOCAL_VAR_ADDRESS

    global_namespace: dict[str, int] = default_field(GLOBAL_NAMESPACE)
    local_namespaces: dict[str, FunctionNamespace] = default_field({})

    string_vars: dict[int, int] = default_field({})

    include_return_subroutine: bool = False


@dataclass
class CodegenPassData:
    compiler_flags: CompilerFlags
    function_tokens: dict[str, FunctionToken]
    meta_variables: dict[str, int]
    constant_namespace: dict[str, int]
    global_namespace: dict[str, int]
    global_var_tokens: list[tuple[mlg1Parser.GlobalVarDeclarationContext, ContextOverride]]
    global_array_tokens: list[tuple[mlg1Parser.GlobalArrayDeclarationContext, ContextOverride]]
    local_namespaces: dict[str, FunctionNamespace]
    string_vars: dict[int, int]
    include_return_subroutine: bool

    current_function_token: FunctionToken | None = None

    function_base_registers: dict[str, int] = default_field({})    

    def get_current_local_namespace(self):
        """Returns the namespace of the current function."""
        if self.current_function_token is None:
            return None
        return self.local_namespaces[self.current_function_token.name]

    def get_namespaces(self):
        return Namespaces(
            self.get_current_local_namespace(),
            self.local_namespaces,
            self.constant_namespace,
            self.global_namespace
        )
