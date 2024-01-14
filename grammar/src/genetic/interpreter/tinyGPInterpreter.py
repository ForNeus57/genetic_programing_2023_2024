from typing import Optional

from antlr4 import FileStream
from antlr4.CommonTokenStream import CommonTokenStream

from src.antlr.MiniGPLexer import MiniGPLexer
from src.antlr.MiniGPParser import MiniGPParser
from src.antlr.MiniGPVisitor import MiniGPVisitor

from src.genetic.interpreter.input_output import InputOutputOperation, ConsoleInputOutputOperation
from src.genetic.interpreter.variables import Variable


class Interpreter(MiniGPVisitor):
    def __init__(self, mode: InputOutputOperation):
        self.variables: dict[str, Variable] = {}
        self.mode: InputOutputOperation = mode
        self.const_information: bool = False

    def visitProgram(self, ctx: MiniGPParser.ProgramContext):
        """
        program :
           executionBlock EOF
           ;
        """

        return self.visitChildren(ctx)

    def visitExecutionBlock(self, ctx: MiniGPParser.ExecutionBlockContext):
        """
        executionBlock :
           LBRACE (statement)+ RBRACE
           ;
        """
        return self.visitChildren(ctx)

    def visitStatement(self, ctx: MiniGPParser.StatementContext):
        # statement :
        #    varDeclaration
        #    | assignment
        #    | ifStatement
        #    | loopStatement
        #    | ioStatement
        #    ;

        return self.visitChildren(ctx)

    def visitVarDeclaration(self, ctx: MiniGPParser.VarDeclarationContext):
        # varDeclaration :
        #    (CONST)? (integerDeclaration | booleanDeclaration) SEMICOLON
        #    ;

        is_constant: bool = ctx.CONST() is not None

        self.const_information = is_constant
        if is_constant:
            self.visit(ctx.getChild(1))
        else:
            self.visit(ctx.getChild(0))

    def visitIntegerDeclaration(self, ctx: MiniGPParser.IntegerDeclarationContext):
        # integerDeclaration :
        #    INT_TYPE VAR (ASSIGMENT_OPERATOR expression)?
        #    ;

        variable_name = ctx.VAR().getText()

        if self.variables.get(variable_name) is not None:
            raise Exception('Variable already declared!')

        self.variables[variable_name] = (
            Variable(self.const_information,
                     'int',
                     self.visit(ctx.expression()) if ctx.expression() is not None else None)
        )

        return self.visitChildren(ctx)

    def visitBooleanDeclaration(self, ctx: MiniGPParser.BooleanDeclarationContext):
        # booleanDeclaration :
        #    BOOL_TYPE VAR (ASSIGMENT_OPERATOR expression)?
        #    ;
        variable_name = ctx.VAR().getText()

        if self.variables.get(variable_name) is not None:
            raise Exception('Variable already declared!')

        self.variables[variable_name] = (
            Variable(self.const_information,
                     'bool',
                     self.visit(ctx.expression()) if ctx.expression() is not None else None)
        )

        return self.visitChildren(ctx)

    def visitAssignment(self, ctx: MiniGPParser.AssignmentContext):
        # assignment :
        #    VAR ASSIGMENT_OPERATOR (expression | condition) SEMICOLON
        #    ;

        variable_name = ctx.VAR().getText()
        variable: Optional[Variable] = self.variables.get(variable_name)

        if variable is None:
            raise Exception('Variable not declared!')

        if variable.is_constant and variable.value is not None:
            raise Exception('Cannot assign to constant variable!')

        if variable.type == 'int' and ctx.condition() is not None:
            raise Exception('Cannot assign bool condition to int variable')

        if variable.type == 'bool' and ctx.expression() is not None:
            raise Exception('Cannot assign int expression to bool variable')

        if ctx.condition() is not None:
            variable.value = self.visit(ctx.condition())
        else:
            variable.value = self.visit(ctx.expression())

        return self.visitChildren(ctx)

    def visitIfStatement(self, ctx: MiniGPParser.IfStatementContext):
        # ifStatement :
        #    IF LPAREN condition RPAREN executionBlock (ELSE executionBlock)?
        #    ;

        condition = self.visit(ctx.condition())
        if condition:
            self.visit(ctx.executionBlock(0))

        elif ctx.executionBlock(1) is not None:
            self.visit(ctx.executionBlock(1))

    def visitLoopStatement(self, ctx: MiniGPParser.LoopStatementContext):
        # loopStatement :
        #    WHILE LPAREN condition RPAREN executionBlock
        #    ;

        condition = self.visit(ctx.condition())
        while condition:
            self.visit(ctx.executionBlock())
            condition = self.visit(ctx.condition())

    def visitIoStatement(self, ctx: MiniGPParser.IoStatementContext):
        # ioStatement :
        #    (WRITE | READ) LPAREN VAR RPAREN SEMICOLON
        #    ;

        variable_name: str = ctx.VAR().getText()
        variable: Optional[Variable] = self.variables.get(variable_name)

        if variable is None:
            raise Exception('Variable not declared!')

        if ctx.WRITE() is not None:
            self.mode.write(variable.value)

        elif ctx.READ() is not None:
            if variable.is_constant:
                raise Exception('Cannot assign to constant variable!')

            variable.value = self.mode.read(variable.type)

    def visitExpression(self, ctx: MiniGPParser.ExpressionContext):
        # expression :
        #    INT
        #    | VAR
        #    | LPAREN expression EXPRESSION_OPERATOR expression RPAREN
        #    ;

        if ctx.getChildCount() == 1:
            if ctx.INT() is not None:
                return int(ctx.INT().getText())

            variable_name: str = ctx.VAR().getText()
            variable: Optional[Variable] = self.variables.get(variable_name)

            if variable is None:
                raise Exception('Variable not declared!')

            if variable.type != 'int':
                raise Exception('Variable is not int!')

            return variable.value

        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.EXPRESSION_OPERATOR().getText()

        match operator:
            case '+':
                return left + right

            case '-':
                return left - right

            case '*':
                return left * right

            case '/':
                return left / right

            case _:
                raise Exception('Unknown operator')

    def visitCondition(self, ctx: MiniGPParser.ConditionContext):
        # condition :
        #    LPAREN condition CONDITION_OPERATOR condition RPAREN
        #    | LPAREN expression EXPRESSION_COMPARISON_OPERATOR expression RPAREN
        #    | BOOL
        #    | VAR
        #    ;
        if ctx.getChildCount() == 1:
            if ctx.BOOL() is not None:
                return bool(ctx.BOOL().getText())

            variable_name: str = ctx.VAR().getText()
            variable: Optional[Variable] = self.variables.get(variable_name)

            if variable is None:
                raise Exception('Variable not declared')

            if variable.type != 'bool':
                raise Exception('Variable is not bool')

            return variable.value

        left = self.visit(ctx.getChild(1))
        right = self.visit(ctx.getChild(3))
        operator = ctx.getChild(2).getText()

        match operator:
            case '<':
                return left < right

            case '>':
                return left > right

            case '<=':
                return left <= right

            case '>=':
                return left >= right

            case '==':
                return left == right

            case '!=':
                return left != right

            case '&&':
                return left and right

            case '||':
                return left or right

            case '^':
                return left != right

            case _:
                raise Exception('Unknown operator')

    # BOOL: 'True' | 'False';
    # INT: (('-')?[1-9][0-9]*) | '0';
    # CONST: 'const';
    # INT_TYPE: 'int';
    # BOOL_TYPE: 'bool';
    # LPAREN: '(';
    # RPAREN: ')';
    # LBRACE: '{';
    # RBRACE: '}';
    # SEMICOLON: ';';
    # ASSIGMENT_OPERATOR: '=';
    # EXPRESION_OPERATOR: ('*' | '/' | '+' | '-');
    # EXPRESION_COMPARASON_OPERATOR: ('>' | '<' | '==' | '!=' | '>=' | '<=');
    # CONDITION_OPERATOR: ('&&' | '||' | '^');
    # READ: 'read';
    # WRITE: 'write';
    # NEGATION_OPERATOR: '!';
    # WHILE: 'while';
    # IF: 'if';
    # ELSE: 'else';
    # VAR: [a-zA-Z][a-zA-Z0-9_]*;

    # WHITESPACE: [ \t\r\n]+ -> skip;


def interpret(program: str):
    input_stream = FileStream(program)
    lexer = MiniGPLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniGPParser(stream)
    try:
        tree = parser.program()
        interpreter = Interpreter(ConsoleInputOutputOperation())
        interpreter.visit(tree)
        return interpreter.variables

    except Exception as e:
        print(e)
        return None
