grammar MiniGP;

program:
	executionBlock EOF
	;

executionBlock:
	LBRACE (assignment | ifStatement | loopStatement | ioStatement)+ RBRACE
	;

assignment:
	VAR ASSIGMENT_OPERATOR expression SEMICOLON
	;

ifStatement:
	IF LPAREN condition RPAREN executionBlock (ELSE executionBlock)?
	;

loopStatement:
	WHILE LPAREN condition RPAREN executionBlock
	;

ioStatement:
	READ LPAREN VAR RPAREN SEMICOLON
	|   WRITE LPAREN expression RPAREN SEMICOLON
	;

expression:
	LPAREN expression EXPRESSION_OPERATOR expression RPAREN
    |   INT
    |   VAR
    ;

condition:
	LPAREN expression EXPRESSION_COMPARISON_OPERATOR expression RPAREN
	|   LPAREN condition CONDITION_OPERATOR condition RPAREN
	|   NEGATION_OPERATOR LPAREN condition RPAREN
	|   BOOL
	;

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMICOLON: ';';
ASSIGMENT_OPERATOR: '=';
EXPRESSION_OPERATOR: ('*' | '/' | '+' | '-');
EXPRESSION_COMPARISON_OPERATOR: ('>' | '<' | '==' | '!=' | '>=' | '<=');
CONDITION_OPERATOR: ('&&' | '||');
NEGATION_OPERATOR: '!';
READ: 'read';
WRITE: 'write';
WHILE: 'while';
IF: 'if';
ELSE: 'else';
BOOL: 'true' | 'false';
INT: (('-')?[1-9][0-9]*) | '0';
VAR: [a-zA-Z][a-zA-Z0-9_]*;

WHITESPACE: [ \t\r\n]+ -> skip;