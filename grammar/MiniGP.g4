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
ifStatement: 'if' '(' expr ')' statement ('else' statement)?;
loopStatement: 'while' '(' expr ')' statement;
ioStatement: ('read' | 'write') '(' ID ')' ';';

expr: expr ('*' | '/' | '+' | '-') expr
    | expr ('>' | '<' | '==' | '!=' | '>=' | '<=') expr
    | expr ('&&' | '||') expr
    | '!' expr
    | ID
    | INT
    | '(' expr ')';

ID: [a-zA-Z]+;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip ;
