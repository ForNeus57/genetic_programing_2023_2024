grammar MiniGP;

prog:
	executionBlock
	;

executionBlock:
	'{' (statement)+ '}'
	;

statement: 
	varDeclaration
    |   assignment
    |   ifStatement
    |   loopStatement
    |   ioStatement
    ;

varDeclaration:
	('const')? (integerDeclaration | booleanDeclaration)
	;

integerDeclaration:
	'int' VAR ('=' expr)? ';'
	;

booleanDeclaration:
	'bool' VAR ('=' condition)? ';'
	;

assignment:
	VAR '=' (expr | condition) ';'
	;

ifStatement:
	'if' '(' condition ')' executionBlock ('else' executionBlock)?
	;

loopStatement:
	'while' '(' condition ')' executionBlock
	;

ioStatement:
	('read' | 'write') '(' VAR ')' ';'
	;

condition:
	expr ('>' | '<' | '==' | '!=' | '>=' | '<=') expr
	|	condition ('==' | '!=') condition
	|   condition ('&&' | '||' | '^') condition
	|   '!' condition
	|   BOOL
	|   VAR
	;

expr:
	expr ('*' | '/' | '+' | '-') expr
    |   VAR
    |   INT
    |   '(' expr ')'
    ;

BOOL: 'true' | 'false';
INT: (('-')?[1-9][0-9]*) | '0';
VAR: [a-zA-Z][a-zA-Z0-9_]*;
WHITESPACE: [ \t\r\n]+ -> skip;