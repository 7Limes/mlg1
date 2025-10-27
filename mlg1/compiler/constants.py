CALL_STACK_POINTER_ADDRESS = 14

RETURN_REGISTER_ADDRESS = 15
RETURN_ARITHMETIC_ADDRESS = 16

ARITHMETIC_REGISTER_ADDRESS = 17
AMOUNT_ARITHMETIC_REGISTERS = 15

CALL_STACK_DATA_ADDRESS = ARITHMETIC_REGISTER_ADDRESS + AMOUNT_ARITHMETIC_REGISTERS
CALL_STACK_SIZE = 32

LOCAL_VAR_ADDRESS = CALL_STACK_DATA_ADDRESS + CALL_STACK_SIZE


DEFAULT_INDENT_SIZE = 4


RETURN_ROUTINE_TEMPLATE = [
    'return:',
    f'{{ws}}sub {CALL_STACK_POINTER_ADDRESS} ${CALL_STACK_POINTER_ADDRESS} 1',
    f'{{ws}}movp {RETURN_ARITHMETIC_ADDRESS} ${CALL_STACK_POINTER_ADDRESS}',
    f'{{ws}}jmp ${RETURN_ARITHMETIC_ADDRESS} 1'
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

ENTRYPOINT_FUNCTIONS = {'start', 'tick'}


BUILTIN_FUNCTIONS = {
    'color': [
        'color {a0} {a1} {a2}'
    ],
    'point': [
        'point {a0} {a1}'
    ],
    'line': [
        'line {a0} {a1} {a2} {a3}'
    ],
    'rect': [
        'rect {a0} {a1} {a2} {a3}'
    ],
    'get': [
        'movp {return_register} {a0}'
    ],
    'set': [
        'mov {a0} {a1}'
    ],
    'putchar': [
        'putc {a0}'
    ],
    'getpixel': [
        'getp {return_register} {a0} {a1}'
    ],
    'setchannel': [
        'setch {a0} {a1} {a2} {a3}'
    ]
}

BUILTIN_FUNCTION_ARGUMENT_COUNTS = {
    'color': 3,
    'point': 2,
    'line': 4,
    'rect': 4,
    'get': 1,
    'set': 2,
    'putchar': 1,
    'getpixel': 2,
    'setchannel': 4
}


def get_return_routine(indent_size: int) -> list[str]:
    """
    Generates the return subroutine.
    """
    return list(map(
        lambda s: s.format(ws=f'{" "*indent_size}'),
        RETURN_ROUTINE_TEMPLATE
    ))
