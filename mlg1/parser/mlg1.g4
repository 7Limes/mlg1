grammar mlg1;

program: metaVariable* loadFile* constantDefinition* function+;

META_VARIABLE_NAME: 'width'|'height'|'memory'|'tickrate';
metaVariable: '#' META_VARIABLE_NAME INTEGER;

loadFile: '$' NAME STRING;

constantDefinition: 'define' NAME INTEGER;

function: 'fn' NAME '(' parameterList? ')' block;

parameterList: NAME (',' NAME)*;

block: '{' statement* '}';

statement
    : variableDeclaration
    | assignment
    | functionCall
    | returnStatement
    | ifStatement
    | whileLoop
    ;

variableDeclaration: VARIABLE_KEYWORD NAME '=' (expression | STRING);
assignment: NAME '=' expression;

ifStatement: 'if' expression block ('else' elseStatement)?;

elseStatement: block | ifStatement;

whileLoop: 'while' expression block;

returnStatement: 'return' expression;

functionCall: NAME '(' argumentList? ')';

argumentList: expression (',' expression)*;

expression
    : primary
    | unaryExpression
    | expression operator expression
    | '(' expression ')'
    ;

unaryExpression
    : unaryOperator expression
    ;

primary
    : NAME
    | INTEGER
    | functionCall
    ;

unaryOperator
    : '-'
    | '!'
    ;

operator
    : '+'
    | '-'
    | '*'
    | '/'
    | '%'
    | '<'
    | '=='
    ;

VARIABLE_KEYWORD: ('let' | 'global');
NAME: [a-zA-Z_][a-zA-Z0-9_]*;
INTEGER: [0-9]+;
STRING: '"' ( ESC | ~["\r\n\\] )* '"';
fragment ESC: '\\' ["\\/bfnrt];
LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;