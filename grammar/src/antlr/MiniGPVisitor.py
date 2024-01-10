# Generated from ./grammar/MiniGP.g4 by ANTLR 4.13.1
from antlr import *
if "." in __name__:
    from .MiniGPParser import MiniGPParser
else:
    from MiniGPParser import MiniGPParser


# This class defines a complete generic visitor for a parse tree produced by MiniGPParser.

class MiniGPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGPParser#program.
    def visitProgram(self, ctx:MiniGPParser.ProgramContext):
        # program:
        #  executionBlock EOF
        #  ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#executionBlock.
    def visitExecutionBlock(self, ctx:MiniGPParser.ExecutionBlockContext):
        # executionBlock:
        #   '{' (statement)+ '}'
        #   ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#statement.
    def visitStatement(self, ctx:MiniGPParser.StatementContext):
        # statement:
        #   varDeclaration
        #   | assignment
        #   | ifStatement
        #   | loopStatement
        #   | ioStatement
        #   ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MiniGPParser.VarDeclarationContext):
        # varDeclaration:
        #   ('const')? (integerDeclaration | booleanDeclaration) ';'
        #   ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#integerDeclaration.
    def visitIntegerDeclaration(self, ctx:MiniGPParser.IntegerDeclarationContext):
        # integerDeclaration:
        #   'int' VAR ('=' expression)?
        #   ;
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniGPParser#booleanDeclaration.
    def visitBooleanDeclaration(self, ctx:MiniGPParser.BooleanDeclarationContext):
        # booleanDeclaration:
        #   'bool' VAR ('=' expression)?
        #   ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#assignment.
    def visitAssignment(self, ctx:MiniGPParser.AssignmentContext):
        # assignment:
        #   VAR '=' (expression | condition) ';'
        #   ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#ifStatement.
    def visitIfStatement(self, ctx:MiniGPParser.IfStatementContext):
        # ifStatement:
        #   'if' '(' condition ')' executionBlock ('else' executionBlock)?
        #   ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#loopStatement.
    def visitLoopStatement(self, ctx:MiniGPParser.LoopStatementContext):
        # loopStatement:
        #   'while' '(' condition ')' executionBlock
        #   ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#ioStatement.
    def visitIoStatement(self, ctx:MiniGPParser.IoStatementContext):
        # ioStatement:
        # ('read' | 'write') '(' VAR ')' ';'
        # ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#condition.
    def visitCondition(self, ctx:MiniGPParser.ConditionContext):
        # condition:
        #   expression ('==' | '!=' | '<' | '>' | '<=' | '>=') expression
        #   | '(' condition ('&&' | '||' | '^') condition ')'
        #   | '!' '(' condition ')'
        #   | VAR  
        #   | BOOL
        #   ;
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGPParser#expression.
    def visitExpression(self, ctx:MiniGPParser.ExpressionContext):
        # expression:
        #   '(' expression ('*' | '/' | '+' | '-') expression ')'
        #   | VAR
        #   | INT
        
        return self.visitChildren(ctx)



del MiniGPParser