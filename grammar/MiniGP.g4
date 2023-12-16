grammar MiniGP;

program:
	executionBlock EOF
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
	('const')? (integerDeclaration | booleanDeclaration) ';'
	;

integerDeclaration:
	'int' VAR ('=' expression)?
	;

booleanDeclaration:
	'bool' VAR ('=' condition)?
	;

assignment:
	VAR '=' (expression | condition) ';'
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
	expression ('>' | '<' | '==' | '!=' | '>=' | '<=') expression
	|   condition ('&&' | '||' | '^') condition
	|   '!' '(' condition ')'
	|   VAR
	|   BOOL
	;

expression:
	expression ('*' | '/' | '+' | '-') expression
    |   VAR
    |   INT
    ;

BOOL: 'True' | 'False';
INT: (('-')?[1-9][0-9]*) | '0';
VAR: [a-zA-Z][a-zA-Z0-9_]*;

WHITESPACE: [ \t\r\n]+ -> skip;