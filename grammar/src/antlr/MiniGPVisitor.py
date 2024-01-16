# Generated from C:/Users/domin/IdeaProjects/genetic_programing_2023_2024/grammar/MiniGP.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniGPParser import MiniGPParser
else:
    from MiniGPParser import MiniGPParser

# This class defines a complete generic visitor for a parse tree produced by MiniGPParser.

class MiniGPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGPParser#program.
    def visitProgram(self, ctx:MiniGPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#executionBlock.
    def visitExecutionBlock(self, ctx:MiniGPParser.ExecutionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MiniGPParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#integerDeclaration.
    def visitIntegerDeclaration(self, ctx:MiniGPParser.IntegerDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#booleanDeclaration.
    def visitBooleanDeclaration(self, ctx:MiniGPParser.BooleanDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#assignment.
    def visitAssignment(self, ctx:MiniGPParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#ifStatement.
    def visitIfStatement(self, ctx:MiniGPParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#loopStatement.
    def visitLoopStatement(self, ctx:MiniGPParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#ioStatement.
    def visitIoStatement(self, ctx:MiniGPParser.IoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#condition.
    def visitCondition(self, ctx:MiniGPParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#expression.
    def visitExpression(self, ctx:MiniGPParser.ExpressionContext):
        return self.visitChildren(ctx)



del MiniGPParser