# Generated from ./grammar/MiniGP.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniGPParser import MiniGPParser
else:
    from MiniGPParser import MiniGPParser

# This class defines a complete listener for a parse tree produced by MiniGPParser.
class MiniGPListener(ParseTreeListener):

    # Enter a parse tree produced by MiniGPParser#program.
    def enterProgram(self, ctx:MiniGPParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniGPParser#program.
    def exitProgram(self, ctx:MiniGPParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniGPParser#executionBlock.
    def enterExecutionBlock(self, ctx:MiniGPParser.ExecutionBlockContext):
        pass

    # Exit a parse tree produced by MiniGPParser#executionBlock.
    def exitExecutionBlock(self, ctx:MiniGPParser.ExecutionBlockContext):
        pass


    # Enter a parse tree produced by MiniGPParser#statement.
    def enterStatement(self, ctx:MiniGPParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniGPParser#statement.
    def exitStatement(self, ctx:MiniGPParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniGPParser#varDeclaration.
    def enterVarDeclaration(self, ctx:MiniGPParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by MiniGPParser#varDeclaration.
    def exitVarDeclaration(self, ctx:MiniGPParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by MiniGPParser#integerDeclaration.
    def enterIntegerDeclaration(self, ctx:MiniGPParser.IntegerDeclarationContext):
        pass

    # Exit a parse tree produced by MiniGPParser#integerDeclaration.
    def exitIntegerDeclaration(self, ctx:MiniGPParser.IntegerDeclarationContext):
        pass


    # Enter a parse tree produced by MiniGPParser#booleanDeclaration.
    def enterBooleanDeclaration(self, ctx:MiniGPParser.BooleanDeclarationContext):
        pass

    # Exit a parse tree produced by MiniGPParser#booleanDeclaration.
    def exitBooleanDeclaration(self, ctx:MiniGPParser.BooleanDeclarationContext):
        pass


    # Enter a parse tree produced by MiniGPParser#assignment.
    def enterAssignment(self, ctx:MiniGPParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MiniGPParser#assignment.
    def exitAssignment(self, ctx:MiniGPParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MiniGPParser#ifStatement.
    def enterIfStatement(self, ctx:MiniGPParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MiniGPParser#ifStatement.
    def exitIfStatement(self, ctx:MiniGPParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MiniGPParser#loopStatement.
    def enterLoopStatement(self, ctx:MiniGPParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by MiniGPParser#loopStatement.
    def exitLoopStatement(self, ctx:MiniGPParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by MiniGPParser#ioStatement.
    def enterIoStatement(self, ctx:MiniGPParser.IoStatementContext):
        pass

    # Exit a parse tree produced by MiniGPParser#ioStatement.
    def exitIoStatement(self, ctx:MiniGPParser.IoStatementContext):
        pass


    # Enter a parse tree produced by MiniGPParser#condition.
    def enterCondition(self, ctx:MiniGPParser.ConditionContext):
        pass

    # Exit a parse tree produced by MiniGPParser#condition.
    def exitCondition(self, ctx:MiniGPParser.ConditionContext):
        pass


    # Enter a parse tree produced by MiniGPParser#expression.
    def enterExpression(self, ctx:MiniGPParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniGPParser#expression.
    def exitExpression(self, ctx:MiniGPParser.ExpressionContext):
        pass



del MiniGPParser