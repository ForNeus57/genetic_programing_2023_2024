# Generated from MiniGP.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniGPParser import MiniGPParser
else:
    from MiniGPParser import MiniGPParser

# This class defines a complete generic visitor for a parse tree produced by MiniGPParser.

class MiniGPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGPParser#prog.
    def visitProg(self, ctx:MiniGPParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#statement.
    def visitStatement(self, ctx:MiniGPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MiniGPParser.VarDeclarationContext):
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


    # Visit a parse tree produced by MiniGPParser#expr.
    def visitExpr(self, ctx:MiniGPParser.ExprContext):
        return self.visitChildren(ctx)



del MiniGPParser