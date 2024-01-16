from __future__ import annotations

from enum import Enum
from typing import Optional, Union, Final, Callable
from functools import wraps

from antlr4 import FileStream, InputStream
from antlr4.CommonTokenStream import CommonTokenStream

from src.antlr.MiniGPLexer import MiniGPLexer
from src.antlr.MiniGPParser import MiniGPParser
from src.antlr.MiniGPVisitor import MiniGPVisitor

from src.genetic.interpreter.input_output import InputOutputOperation
from src.genetic.interpreter.variables import Variable


class InterpreterErrors(Enum):
    VARIABLE_NOT_DECLARED = 'Variable: \"{}\" attempted read operation before declaration!'
    VARIABLE_DOUBLE_DECLARATION = 'Variable: \"{}\" was already declared in this scope!'
    CONSTANT_VARIABLE_ASSIGMENT = 'Attempt was made to assign value: \"{}\" to constant variable \"{}\"!'
    WRONG_TYPE_TO_VARIABLE_ASSIGMENT = 'Cannot assign: \"{}\" type variable with: \"{}\" type!'
    READ_ASSIGMENT_TO_CONSTANT = 'Attempted to assign read input value to variable: \"{}\"!'
    ITERATION_LIMIT_EXCEEDED = 'Interpreter exceeded executed instruction limit!'

    @staticmethod
    def raise_error(error_type: InterpreterErrors, *msg_args):
        raise Exception(error_type.value.format(*msg_args))


class Interpreter(MiniGPVisitor):
    instructions_limit: Final[int] = 400

    def __init__(self, mode: InputOutputOperation):
        self.variables: dict[str, Variable] = {}
        self.mode: InputOutputOperation = mode
        self.const_information: bool = False
        self.used_instructions: int = 0

    @staticmethod
    def limit(function: Callable):
        @wraps(function)
        def wrapper(self, *args, **kwargs):
            if self.used_instructions > Interpreter.instructions_limit:
                InterpreterErrors.raise_error(InterpreterErrors.ITERATION_LIMIT_EXCEEDED)

            self.used_instructions += 1
            return function(self, *args, **kwargs)

        return wrapper

    @limit
    def visitProgram(self, ctx: MiniGPParser.ProgramContext):
        """
        program :
           executionBlock EOF
           ;
        """

        return self.visitChildren(ctx)

    @limit
    def visitExecutionBlock(self, ctx: MiniGPParser.ExecutionBlockContext):
        """
        executionBlock :
           LBRACE (statement)+ RBRACE
           ;
        """
        return self.visitChildren(ctx)

    @limit
    def visitVarDeclaration(self, ctx: MiniGPParser.VarDeclarationContext):
        # varDeclaration :
        #    (CONST)? (integerDeclaration | booleanDeclaration) SEMICOLON
        #    ;

        is_constant: bool = ctx.CONST() is not None

        self.const_information = False
        if is_constant:
            self.visit(ctx.getChild(1))
        else:
            self.visit(ctx.getChild(0))

    @limit
    def visitIntegerDeclaration(self, ctx: MiniGPParser.IntegerDeclarationContext):
        # integerDeclaration :
        #    INT_TYPE VAR ASSIGMENT_OPERATOR expression
        #    ;

        variable_name = ctx.VAR().getText()

        self.variables[variable_name] = (
            Variable(self.const_information,
                     'int',
                     self.visit(ctx.expression()))
        )

    @limit
    def visitBooleanDeclaration(self, ctx: MiniGPParser.BooleanDeclarationContext):
        # booleanDeclaration :
        #    BOOL_TYPE VAR ASSIGMENT_OPERATOR condition
        #    ;
        variable_name = ctx.VAR().getText()

        self.variables[variable_name] = (
            Variable(self.const_information,
                     'bool',
                     self.visit(ctx.condition()))
        )

    @limit
    def visitAssignment(self, ctx: MiniGPParser.AssignmentContext):
        # assignment :
        #    VAR ASSIGMENT_OPERATOR (expression | condition) SEMICOLON
        #    ;

        variable_name = ctx.VAR().getText()
        variable: Optional[Variable] = self.variables.get(variable_name)

        if variable is None:
            self.variables[variable_name] = Variable(False, 'int', self.mode.read('int'))
            return

        if variable.type == 'int' and ctx.condition() is not None:
            value: int = int(self.visit(ctx.condition()))
            variable.value = value
            return

        if variable.type == 'bool' and ctx.expression() is not None:
            value: bool = bool(self.visit(ctx.condition()))
            variable.value = value
            return

        value: Union[bool, int] = self.visit(ctx.getChild(2))

        if variable.is_constant:
            InterpreterErrors.raise_error(InterpreterErrors.CONSTANT_VARIABLE_ASSIGMENT, value, variable_name)

        variable.value = value

    @limit
    def visitIfStatement(self, ctx: MiniGPParser.IfStatementContext):
        # ifStatement :
        #    IF LPAREN condition RPAREN executionBlock (ELSE executionBlock)?
        #    ;

        condition = self.visit(ctx.condition())
        if condition:
            self.visit(ctx.executionBlock(0))

        elif ctx.executionBlock(1) is not None:
            self.visit(ctx.executionBlock(1))

    @limit
    def visitLoopStatement(self, ctx: MiniGPParser.LoopStatementContext):
        # loopStatement :
        #    WHILE LPAREN condition RPAREN executionBlock
        #    ;

        condition = self.visit(ctx.condition())
        while condition:
            self.visit(ctx.executionBlock())
            condition = self.visit(ctx.condition())

    @limit
    def visitIoStatement(self, ctx: MiniGPParser.IoStatementContext):
        # ioStatement :
        #    (WRITE | READ) LPAREN VAR RPAREN SEMICOLON
        #    ;

        variable_name: str = ctx.VAR().getText()
        variable: Optional[Variable] = self.variables.get(variable_name)

        if variable is None:
            return

        if ctx.WRITE() is not None:
            print(variable_name, variable)
            self.mode.write(variable.value)

        elif ctx.READ() is not None:
            if variable.is_constant:
                InterpreterErrors.raise_error(InterpreterErrors.READ_ASSIGMENT_TO_CONSTANT, variable_name)

            print(variable_name, variable)
            variable.value = self.mode.read(variable.type)

    @limit
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
                self.variables[variable_name] = Variable(False, 'int', self.mode.read('int'))
                return

            if variable.type == 'bool':
                return int(variable.value)

            return variable.value

        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.EXPRESSION_OPERATOR().getText()

        if left is None:
            left = self.mode.read('int')

        if right is None:
            right = self.mode.read('int')

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
                return int(left / right)

        raise ValueError(f'Unknown operator: {operator}')

    @limit
    def visitCondition(self, ctx: MiniGPParser.ConditionContext):
        # condition :
        #    LPAREN condition CONDITION_OPERATOR condition RPAREN
        #    | LPAREN expression EXPRESSION_COMPARISON_OPERATOR expression RPAREN
        #    | condition
        #    | BOOL
        #    | VAR
        #    ;
        if ctx.getChildCount() == 1:
            if ctx.BOOL() is not None:
                return bool(ctx.BOOL().getText())

            variable_name: str = ctx.VAR().getText()
            variable: Optional[Variable] = self.variables.get(variable_name)

            if variable is None:
                self.variables[variable_name] = Variable(False, 'bool', self.mode.read('bool'))
                return

            if variable.type == 'int':
                return bool(variable.value)

            return variable.value

        if ctx.getChildCount() == 4:
            return not self.visit(ctx.condition(0))

        left = self.visit(ctx.getChild(1))
        right = self.visit(ctx.getChild(3))

        if left is None:
            left = self.mode.read('bool')

        if right is None:
            right = self.mode.read('bool')

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

        raise ValueError(f'Unknown operator: {operator}')

    @staticmethod
    def interpret(program: str, mode: InputOutputOperation, is_path_like: bool = True) \
            -> Optional[InputOutputOperation]:
        input_stream = FileStream(program) if is_path_like else InputStream(program)
        lexer = MiniGPLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MiniGPParser(stream)

        # try:
        tree = parser.program()
        interpreter = Interpreter(mode)
        try:
            interpreter.visit(tree)
        except StopIteration as error:
            print(error)
        except Exception as error:
            print(error)
        finally:
            return interpreter.mode

        # except Exception as error:
        #     print(error)
