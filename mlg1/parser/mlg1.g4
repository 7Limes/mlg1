grammar mlg1;

program: headerStatement* function*;

META_VARIABLE_NAME: 'width'|'height'|'memory'|'tickrate';
metaVariable: '#' META_VARIABLE_NAME INTEGER;

includeFile: 'include' STRING;

FILE_OPERATION: 'raw'|'pack'|'img';
loadFile: '$' NAME FILE_OPERATION STRING;

constantDefinition: 'define' NAME expression;
    
function: 'fn' NAME '(' parameterList? ')' block;

parameterList: NAME (',' NAME)*;

block: '{' statement* '}';

headerStatement
    : metaVariable
    | includeFile
    | loadFile
    | constantDefinition
    | globalVarDeclaration
    | globalArrayDeclaration
    ;

statement
    : localVarDeclaration
    | assignment
    | localArrayDeclaration
    | functionCall
    | returnStatement
    | breakStatement
    | continueStatement
    | ifStatement
    | whileLoop
    | forLoop
    ;

// Variable declaration and assignment 
globalVarDeclaration: 'global' declaredVariablesList;
localVarDeclaration: 'let' declaredVariablesList;
declaredVariablesList: declaredVariable (',' declaredVariable)*;
declaredVariable: NAME ('=' (expression | STRING))?;

assignment: NAME '=' expression;

// Array declarations
globalArrayDeclaration: 'global' NAME '[' expression? ']' ('=' '[' expressionList? ']')?;
localArrayDeclaration: 'let' NAME '[' expression? ']' ('=' '[' expressionList? ']')?;

// Conditionals
ifStatement: 'if' expression block elseIfClause* elseClause?;
elseIfClause: 'else' 'if' expression block;
elseClause: 'else' block;

// Loops
whileLoop: 'while' expression block;
forLoop: 'for' '(' (localVarDeclaration | assignment)? ';' expression ';' assignment ')' block;
breakStatement: 'break';
continueStatement: 'continue';

returnStatement: 'return' expression;


functionCall: NAME '(' expressionList? ')';
expressionList: expression (',' expression)*;

expression
    : primary
    | unaryExpression
    | expression operator expression
    | '(' expression ')'
    ;

unaryExpression: unaryOperator expression;

primary
    : NAME
    | INTEGER
    | functionCall
    ;

unaryOperator
    : '-'
    | '!'
    | '&'
    ;

operator
    : '+'
    | '-'
    | '*'
    | '/'
    | '%'
    | '<'
    | '>'
    | '<='
    | '>='
    | '=='
    | '!='
    ;

NAME: [a-zA-Z_][a-zA-Z0-9_]*;
INTEGER: [0-9]+;
STRING: '"' ( ESC | ~["\r\n\\] )* '"';
fragment ESC: '\\' ["\\/bfnrt];
LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;