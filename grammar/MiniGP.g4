grammar MiniGP;

program:
	executionBlock EOF
	;

executionBlock:
	LBRACE (integerDeclaration | booleanDeclaration | assignment | ifStatement | loopStatement | ioStatement)+ RBRACE
	;

integerDeclaration:
	INT_TYPE VAR ASSIGMENT_OPERATOR expression SEMICOLON
	;

booleanDeclaration:
	BOOL_TYPE VAR ASSIGMENT_OPERATOR condition SEMICOLON
	;

assignment:
	VAR ASSIGMENT_OPERATOR (expression | condition) SEMICOLON
	;

ifStatement:
	IF LPAREN condition RPAREN executionBlock (ELSE executionBlock)?
	;

loopStatement:
	WHILE LPAREN condition RPAREN executionBlock
	;

ioStatement:
	(READ | WRITE) LPAREN VAR RPAREN SEMICOLON
	;

condition:
	LPAREN expression EXPRESSION_COMPARISON_OPERATOR expression RPAREN
	|   LPAREN condition CONDITION_OPERATOR condition RPAREN
	|   NEGATION_OPERATOR LPAREN condition RPAREN
	|   BOOL
	|   VAR
	;

expression:
	LPAREN expression EXPRESSION_OPERATOR expression RPAREN
    |   INT
    |   VAR
    ;

BOOL: 'True' | 'False';
INT: (('-')?[1-9][0-9]*) | '0';
INT_TYPE: 'int';
BOOL_TYPE: 'bool';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMICOLON: ';';
ASSIGMENT_OPERATOR: '=';
EXPRESSION_OPERATOR: ('*' | '/' | '+' | '-');
EXPRESSION_COMPARISON_OPERATOR: ('>' | '<' | '==' | '!=' | '>=' | '<=');
CONDITION_OPERATOR: ('&&' | '||');
READ: 'read';
WRITE: 'write';
NEGATION_OPERATOR: '!';
WHILE: 'while';
IF: 'if';
ELSE: 'else';
VAR: [a-zA-Z][a-zA-Z0-9_]*;

WHITESPACE: [ \t\r\n]+ -> skip;