from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from antlr4 import FileStream
from antlr4.CommonTokenStream import CommonTokenStream

from src.antlr.MiniGPLexer import MiniGPLexer
from src.antlr.MiniGPParser import MiniGPParser
from src.antlr.MiniGPVisitor import MiniGPVisitor

from src.genetic.interpreter.input_output import InputOutputOperation, ConsoleInputOutputOperation
from src.genetic.interpreter.variables import Variable


class InterpreterErrors(Enum):
    VARIABLE_NOT_DECLARED = 'Variable: \"{}\" attempted read operation before declaration!'
    VARIABLE_DOUBLE_DECLARATION = 'Variable: \"{}\" was already declared in this scope!'
    CONSTANT_VARIABLE_ASSIGMENT = 'Attempt was made to assign value: \"{}\" to constant variable \"{}\"!'
    WRONG_TYPE_TO_VARIABLE_ASSIGMENT = 'Cannot assign: \"{}\" type variable with: \"{}\" type!'
    READ_ASSIGMENT_TO_CONSTANT = 'Attempted to assign read input value to variable: \"{}\"!'

    @staticmethod
    def raise_error(error_type: InterpreterErrors, *msg_args):
        raise Exception(error_type.value.format(*msg_args))


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
            InterpreterErrors.raise_error(InterpreterErrors.VARIABLE_DOUBLE_DECLARATION, variable_name)

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
            InterpreterErrors.raise_error(InterpreterErrors.VARIABLE_DOUBLE_DECLARATION, variable_name)

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
            InterpreterErrors.raise_error(InterpreterErrors.VARIABLE_NOT_DECLARED, variable_name)

        if variable.type == 'int' and ctx.condition() is not None:
            InterpreterErrors.raise_error(InterpreterErrors.VARIABLE_DOUBLE_DECLARATION, 'int', 'bool')

        if variable.type == 'bool' and ctx.expression() is not None:
            InterpreterErrors.raise_error(InterpreterErrors.VARIABLE_DOUBLE_DECLARATION, 'bool', 'int')

        value: Union[bool, int] = self.visit(ctx.getChild(2))

        if variable.is_constant:
            InterpreterErrors.raise_error(InterpreterErrors.CONSTANT_VARIABLE_ASSIGMENT, value, variable_name)

        variable.value = value

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
            InterpreterErrors.raise_error(InterpreterErrors.VARIABLE_NOT_DECLARED, variable_name)

        if ctx.WRITE() is not None:
            self.mode.write(variable.value)

        elif ctx.READ() is not None:
            if variable.is_constant:
                InterpreterErrors.raise_error(InterpreterErrors.READ_ASSIGMENT_TO_CONSTANT, variable_name)

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
                InterpreterErrors.raise_error(InterpreterErrors.VARIABLE_NOT_DECLARED, variable_name)

            if variable.type == 'bool':
                InterpreterErrors.raise_error(InterpreterErrors.VARIABLE_DOUBLE_DECLARATION, 'int', 'bool')

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
                InterpreterErrors.raise_error(InterpreterErrors.VARIABLE_NOT_DECLARED, variable_name)

            if variable.type == 'int':
                InterpreterErrors.raise_error(InterpreterErrors.VARIABLE_DOUBLE_DECLARATION, 'bool', 'int')

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
