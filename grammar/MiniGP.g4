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
         | expr ('&&' | '||') expr
         | '!' condition;

expr: expr ('*' | '/' | '+' | '-') expr
    | ID
    | INT
    | '(' expr ')';

ID: [a-zA-Z]+;
INT: [1-9][0-9]* | '0';y
WS: [ \t\r\n]+ -> skip ;