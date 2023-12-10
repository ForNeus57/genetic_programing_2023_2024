grammar MiniGP;

prog:   (statement)+;

statement: 
      varDeclaration
    | assignment
    | ifStatement
    | loopStatement
    | ioStatement
    | '{' prog '}'; 

varDeclaration: 'int' ID ('=' expr)? ';';
assignment: ID '=' expr ';';
ifStatement: 'if' '(' condition ')' statement ('else' statement)?;
loopStatement: 'while' '(' condition ')' statement;
ioStatement: ('read' | 'write') '(' ID ')' ';';

condition: expr ('>' | '<' | '==' | '!=' | '>=' | '<=') expr
         | condition ('&&' | '||') condition
         | '!' condition
         | BOOL;

expr: expr ('*' | '/' | '+' | '-') expr
    | ID
    | INT
    | '(' expr ')';

BOOL: 'true' | 'false';
ID: [a-zA-Z]+;
INT: [1-9][0-9]* | '0';
WS: [ \t\r\n]+ -> skip ;