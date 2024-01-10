from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream

from antlr4.MiniGPLexer import MiniGPLexer
from antlr4.MiniGPParser import MiniGPParser
from antlr4.MiniGPVisitor import MiniGPVisitor


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
        self.variables[ctx.variableName().getText()] = {
            'is_const': False,
            'value': None,
            'type': 'int' if ctx.integerDeclaration() else 'bool'
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
    input_stream = InputStream(program)
    lexer = MiniGPLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniGPParser(stream)
    try:
        tree = parser.program()
        interpreter = Interpreter()
        interpreter.visit(tree)
        return interpreter.variables
    except:
        print('SAAAA')
        return None
