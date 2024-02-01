from __future__ import annotations

from typing import Optional, Union, Final, Callable, TypeVar, final
from functools import wraps

from antlr4 import FileStream, InputStream
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.error.ErrorListener import ConsoleErrorListener

from src.antlr.MiniGPLexer import MiniGPLexer
from src.antlr.MiniGPParser import MiniGPParser
from src.antlr.MiniGPVisitor import MiniGPVisitor
from src.antlr.ExceptionErrorListener import ExceptionErrorListener

from src.genetic.interpreter.input_output import InputOutputOperation
from src.genetic.interpreter.variables import Variable

T = TypeVar('T')


@final
class Interpreter(MiniGPVisitor):
    def __init__(self, mode: InputOutputOperation, instructions_limit: int = 400) -> None:
        self.variables: dict[str, Variable] = {}
        self.mode: InputOutputOperation = mode
        self.used_instructions: int = 0
        self.instructions_limit: Final[int] = instructions_limit

    @staticmethod
    def limit(function: Callable):
        @wraps(function)
        def wrapper(self, *args, **kwargs):
            if self.used_instructions > self.instructions_limit:
                raise StopIteration('Interpreter exceeded executed instruction limit!')

            self.used_instructions += 1
            return function(self, *args, **kwargs)

        return wrapper

    @limit
    def visitProgram(self, ctx: MiniGPParser.ProgramContext) -> None:
        """
        program :
           executionBlock EOF
           ;
        """

        self.visit(ctx.executionBlock())

    @limit
    def visitExecutionBlock(self, ctx: MiniGPParser.ExecutionBlockContext) -> None:
        """
        executionBlock:
            LBRACE (integerDeclaration | booleanDeclaration | assignment | ifStatement | loopStatement | ioStatement)+ RBRACE
            ;
        """
        self.visitChildren(ctx)

    @limit
    def visitIntegerDeclaration(self, ctx: MiniGPParser.IntegerDeclarationContext) -> None:
        """
        integerDeclaration:
            INT_TYPE VAR ASSIGMENT_OPERATOR expression SEMICOLON
            ;
        """

        variable_name = ctx.VAR().getText()

        self.variables[variable_name] = Variable('int', self.visit(ctx.expression()))

    @limit
    def visitBooleanDeclaration(self, ctx: MiniGPParser.BooleanDeclarationContext) -> None:
        """
        booleanDeclaration:
            BOOL_TYPE VAR ASSIGMENT_OPERATOR condition SEMICOLON
            ;
        """
        variable_name = ctx.VAR().getText()

        self.variables[variable_name] = Variable('bool', self.visit(ctx.condition()))

    @limit
    def visitAssignment(self, ctx: MiniGPParser.AssignmentContext) -> None:
        """
        assignment:
            VAR ASSIGMENT_OPERATOR (expression | condition) SEMICOLON
            ;
        """

        variable_name = ctx.VAR().getText()
        variable: Optional[Variable] = self.variables.get(variable_name)

        if variable is None:
            self.variables[variable_name] = Variable('int', self.mode.read('int'))
            variable = self.variables[variable_name]

        if variable.type == 'int' and ctx.condition() is not None:
            value: int = int(self.visit(ctx.condition()))
            variable.value = value
            return

        if variable.type == 'bool' and ctx.expression() is not None:
            value: bool = bool(self.visit(ctx.expression()))
            variable.value = value
            return

        value: Union[bool, int] = self.visit(ctx.getChild(2))

        variable.value = value

    @limit
    def visitIfStatement(self, ctx: MiniGPParser.IfStatementContext) -> None:
        """
        ifStatement:
            IF LPAREN condition RPAREN executionBlock (ELSE executionBlock)?
            ;
        """

        if self.visit(ctx.condition()):
            self.visit(ctx.executionBlock(0))

        elif ctx.executionBlock(1) is not None:
            self.visit(ctx.executionBlock(1))

    @limit
    def visitLoopStatement(self, ctx: MiniGPParser.LoopStatementContext) -> None:
        """
        loopStatement:
            WHILE LPAREN condition RPAREN executionBlock
            ;
        """

        while self.visit(ctx.condition()):
            self.visit(ctx.executionBlock())

    @limit
    def visitIoStatement(self, ctx: MiniGPParser.IoStatementContext) -> None:
        """
        ioStatement:
            READ LPAREN VAR RPAREN SEMICOLON
            |   WRITE LPAREN (expression | condition) RPAREN SEMICOLON
            ;
        """

        if ctx.WRITE() is not None:
            self.mode.write(self.visit(ctx.getChild(2)))

        elif ctx.READ() is not None:
            variable_name: str = ctx.VAR().getText()
            variable: Optional[Variable] = self.variables.get(variable_name)

            if variable is None:
                self.variables[variable_name] = Variable('int', self.mode.read('int'))
                variable = self.variables[variable_name]

            variable.value = self.mode.read(variable.type)

    @limit
    def visitExpression(self, ctx: MiniGPParser.ExpressionContext) -> int:
        """
        expression:
            LPAREN expression EXPRESSION_OPERATOR expression RPAREN
            |   INT
            |   VAR
            ;
        """

        if ctx.getChildCount() == 1:
            if ctx.INT() is not None:
                return int(ctx.INT().getText())

            variable_name: str = ctx.VAR().getText()
            variable: Optional[Variable] = self.variables.get(variable_name)

            if variable is None:
                self.variables[variable_name] = Variable('int', self.mode.read('int'))
                variable = self.variables[variable_name]

            if variable.type == 'bool':
                return int(variable.value)

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
                if right == 0:
                    return left
                return left // right

    @limit
    def visitCondition(self, ctx: MiniGPParser.ConditionContext) -> bool:
        """
        condition:
            LPAREN expression EXPRESSION_COMPARISON_OPERATOR expression RPAREN
            |   LPAREN condition CONDITION_OPERATOR condition RPAREN
            |   NEGATION_OPERATOR LPAREN condition RPAREN
            |   BOOL
            |   VAR
            ;
        """

        if ctx.getChildCount() == 1:
            if ctx.BOOL() is not None:
                return str(ctx.BOOL().getText()) == "true"

            variable_name: str = ctx.VAR().getText()
            variable: Optional[Variable] = self.variables.get(variable_name)

            if variable is None:
                self.variables[variable_name] = Variable('bool', self.mode.read('bool'))
                variable = self.variables[variable_name]

            if variable.type == 'int':
                return bool(variable.value)

            return variable.value

        if ctx.getChildCount() == 4:
            return not self.visit(ctx.condition(0))

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

    @staticmethod
    def interpret(program: str, mode: T, is_path_like: bool = False, **kwargs) -> Optional[T]:
        input_stream = FileStream(program) if is_path_like else InputStream(program)
        lexer = MiniGPLexer(input_stream)
        lexer.removeErrorListeners()
        stream = CommonTokenStream(lexer)
        parser = MiniGPParser(stream)
        parser.removeErrorListener(ConsoleErrorListener.INSTANCE)
        parser.addErrorListener(ExceptionErrorListener())

        # try:
        tree = parser.program()
        interpreter = Interpreter(mode, **kwargs)
        try:
            interpreter.visit(tree)
        except StopIteration:
            pass
        finally:
            return interpreter.mode
