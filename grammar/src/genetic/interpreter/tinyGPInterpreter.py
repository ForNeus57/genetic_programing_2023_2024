from antlr4 import FileStream
from antlr4.CommonTokenStream import CommonTokenStream

from src.antlr.MiniGPLexer import MiniGPLexer
from src.antlr.MiniGPParser import MiniGPParser
from src.antlr.MiniGPVisitor import MiniGPVisitor


class Interpreter(MiniGPVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx: MiniGPParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitExecutionBlock(self, ctx: MiniGPParser.ExecutionBlockContext):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx: MiniGPParser.StatementContext):
        return self.visitChildren(ctx)

    def visitVarDeclaration(self, ctx: MiniGPParser.VarDeclarationContext):

        def is_const(ctx: MiniGPParser.VarDeclarationContext):
            return ctx.CONST() is not None

        # def get_value(ctx: MiniGPParser.VarDeclarationContext):
        #
        #     if ctx.expression() is not None:
        #         return self.visit(ctx.expression())
        #     else:
        #         return None

        def get_type(ctx: MiniGPParser.VarDeclarationContext):
            if ctx.integerDeclaration() is not None:
                return 'int'
            else:
                return 'bool'

        self.variables[ctx.getText()] = {
            'is_const': is_const(ctx),
            'value': get_value(ctx),
            'type': get_type(ctx)
        }
        return self.visitChildren(ctx)

    def visitIntegerDeclaration(self, ctx: MiniGPParser.IntegerDeclarationContext):
        return self.visitChildren(ctx)

    def visitBooleanDeclaration(self, ctx: MiniGPParser.BooleanDeclarationContext):
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx: MiniGPParser.AssignmentContext):
        return self.visitChildren(ctx)

    def visitIfStatement(self, ctx: MiniGPParser.IfStatementContext):
        return self.visitChildren(ctx)

    def visitLoopStatement(self, ctx: MiniGPParser.LoopStatementContext):
        return self.visitChildren(ctx)

    def visitIoStatement(self, ctx: MiniGPParser.IoStatementContext):
        return self.visitChildren(ctx)

    def visitExpression(self, ctx: MiniGPParser.ExpressionContext):
        return self.visitChildren(ctx)

    def visitCondition(self, ctx: MiniGPParser.ConditionContext):
        return self.visitChildren(ctx)


def interpret(program: str):
    input_stream = FileStream(program)
    lexer = MiniGPLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniGPParser(stream)
    try:
        tree = parser.program()
        interpreter = Interpreter()
        interpreter.visit(tree)
        return interpreter.variables
    except Exception as e:
        print(e)
        return None
