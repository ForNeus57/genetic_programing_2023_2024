# Generated from C:/Users/domin/IdeaProjects/genetic_programing_2023_2024/grammar/MiniGP.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,119,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,4,1,31,8,1,11,1,12,1,32,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,53,8,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,3,5,64,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,81,8,7,1,7,1,7,1,7,3,7,86,8,7,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,3,8,96,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,117,8,9,1,9,0,
        0,10,0,2,4,6,8,10,12,14,16,18,0,0,124,0,20,1,0,0,0,2,23,1,0,0,0,
        4,36,1,0,0,0,6,42,1,0,0,0,8,48,1,0,0,0,10,56,1,0,0,0,12,65,1,0,0,
        0,14,85,1,0,0,0,16,95,1,0,0,0,18,116,1,0,0,0,20,21,3,2,1,0,21,22,
        5,0,0,1,22,1,1,0,0,0,23,30,5,3,0,0,24,31,3,4,2,0,25,31,3,6,3,0,26,
        31,3,8,4,0,27,31,3,10,5,0,28,31,3,12,6,0,29,31,3,14,7,0,30,24,1,
        0,0,0,30,25,1,0,0,0,30,26,1,0,0,0,30,27,1,0,0,0,30,28,1,0,0,0,30,
        29,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,34,1,0,0,
        0,34,35,5,4,0,0,35,3,1,0,0,0,36,37,5,11,0,0,37,38,5,20,0,0,38,39,
        5,6,0,0,39,40,3,16,8,0,40,41,5,5,0,0,41,5,1,0,0,0,42,43,5,12,0,0,
        43,44,5,20,0,0,44,45,5,6,0,0,45,46,3,18,9,0,46,47,5,5,0,0,47,7,1,
        0,0,0,48,49,5,20,0,0,49,52,5,6,0,0,50,53,3,16,8,0,51,53,3,18,9,0,
        52,50,1,0,0,0,52,51,1,0,0,0,53,54,1,0,0,0,54,55,5,5,0,0,55,9,1,0,
        0,0,56,57,5,16,0,0,57,58,5,1,0,0,58,59,3,18,9,0,59,60,5,2,0,0,60,
        63,3,2,1,0,61,62,5,17,0,0,62,64,3,2,1,0,63,61,1,0,0,0,63,64,1,0,
        0,0,64,11,1,0,0,0,65,66,5,15,0,0,66,67,5,1,0,0,67,68,3,18,9,0,68,
        69,5,2,0,0,69,70,3,2,1,0,70,13,1,0,0,0,71,72,5,13,0,0,72,73,5,1,
        0,0,73,74,5,20,0,0,74,75,5,2,0,0,75,86,5,5,0,0,76,77,5,14,0,0,77,
        80,5,1,0,0,78,81,3,16,8,0,79,81,3,18,9,0,80,78,1,0,0,0,80,79,1,0,
        0,0,81,82,1,0,0,0,82,83,5,2,0,0,83,84,5,5,0,0,84,86,1,0,0,0,85,71,
        1,0,0,0,85,76,1,0,0,0,86,15,1,0,0,0,87,88,5,1,0,0,88,89,3,16,8,0,
        89,90,5,7,0,0,90,91,3,16,8,0,91,92,5,2,0,0,92,96,1,0,0,0,93,96,5,
        19,0,0,94,96,5,20,0,0,95,87,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,
        96,17,1,0,0,0,97,98,5,1,0,0,98,99,3,16,8,0,99,100,5,8,0,0,100,101,
        3,16,8,0,101,102,5,2,0,0,102,117,1,0,0,0,103,104,5,1,0,0,104,105,
        3,18,9,0,105,106,5,9,0,0,106,107,3,18,9,0,107,108,5,2,0,0,108,117,
        1,0,0,0,109,110,5,10,0,0,110,111,5,1,0,0,111,112,3,18,9,0,112,113,
        5,2,0,0,113,117,1,0,0,0,114,117,5,18,0,0,115,117,5,20,0,0,116,97,
        1,0,0,0,116,103,1,0,0,0,116,109,1,0,0,0,116,114,1,0,0,0,116,115,
        1,0,0,0,117,19,1,0,0,0,8,30,32,52,63,80,85,95,116
    ]

class MiniGPParser ( Parser ):

    grammarFileName = "MiniGP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'='", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'!'", "'int'", 
                     "'bool'", "'read'", "'write'", "'while'", "'if'", "'else'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "SEMICOLON", "ASSIGMENT_OPERATOR", "EXPRESSION_OPERATOR", 
                      "EXPRESSION_COMPARISON_OPERATOR", "CONDITION_OPERATOR", 
                      "NEGATION_OPERATOR", "INT_TYPE", "BOOL_TYPE", "READ", 
                      "WRITE", "WHILE", "IF", "ELSE", "BOOL", "INT", "VAR", 
                      "WHITESPACE" ]

    RULE_program = 0
    RULE_executionBlock = 1
    RULE_integerDeclaration = 2
    RULE_booleanDeclaration = 3
    RULE_assignment = 4
    RULE_ifStatement = 5
    RULE_loopStatement = 6
    RULE_ioStatement = 7
    RULE_expression = 8
    RULE_condition = 9

    ruleNames =  [ "program", "executionBlock", "integerDeclaration", "booleanDeclaration", 
                   "assignment", "ifStatement", "loopStatement", "ioStatement", 
                   "expression", "condition" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    LBRACE=3
    RBRACE=4
    SEMICOLON=5
    ASSIGMENT_OPERATOR=6
    EXPRESSION_OPERATOR=7
    EXPRESSION_COMPARISON_OPERATOR=8
    CONDITION_OPERATOR=9
    NEGATION_OPERATOR=10
    INT_TYPE=11
    BOOL_TYPE=12
    READ=13
    WRITE=14
    WHILE=15
    IF=16
    ELSE=17
    BOOL=18
    INT=19
    VAR=20
    WHITESPACE=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def executionBlock(self):
            return self.getTypedRuleContext(MiniGPParser.ExecutionBlockContext,0)


        def EOF(self):
            return self.getToken(MiniGPParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGPParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.executionBlock()
            self.state = 21
            self.match(MiniGPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExecutionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGPParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGPParser.RBRACE, 0)

        def integerDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.IntegerDeclarationContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.IntegerDeclarationContext,i)


        def booleanDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.BooleanDeclarationContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.BooleanDeclarationContext,i)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.AssignmentContext,i)


        def ifStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.IfStatementContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.IfStatementContext,i)


        def loopStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.LoopStatementContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.LoopStatementContext,i)


        def ioStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.IoStatementContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.IoStatementContext,i)


        def getRuleIndex(self):
            return MiniGPParser.RULE_executionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecutionBlock" ):
                listener.enterExecutionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecutionBlock" ):
                listener.exitExecutionBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecutionBlock" ):
                return visitor.visitExecutionBlock(self)
            else:
                return visitor.visitChildren(self)




    def executionBlock(self):

        localctx = MiniGPParser.ExecutionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_executionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(MiniGPParser.LBRACE)
            self.state = 30 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11]:
                    self.state = 24
                    self.integerDeclaration()
                    pass
                elif token in [12]:
                    self.state = 25
                    self.booleanDeclaration()
                    pass
                elif token in [20]:
                    self.state = 26
                    self.assignment()
                    pass
                elif token in [16]:
                    self.state = 27
                    self.ifStatement()
                    pass
                elif token in [15]:
                    self.state = 28
                    self.loopStatement()
                    pass
                elif token in [13, 14]:
                    self.state = 29
                    self.ioStatement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 32 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1177600) != 0)):
                    break

            self.state = 34
            self.match(MiniGPParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(MiniGPParser.INT_TYPE, 0)

        def VAR(self):
            return self.getToken(MiniGPParser.VAR, 0)

        def ASSIGMENT_OPERATOR(self):
            return self.getToken(MiniGPParser.ASSIGMENT_OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGPParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGPParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGPParser.RULE_integerDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegerDeclaration" ):
                listener.enterIntegerDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegerDeclaration" ):
                listener.exitIntegerDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerDeclaration" ):
                return visitor.visitIntegerDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def integerDeclaration(self):

        localctx = MiniGPParser.IntegerDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_integerDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(MiniGPParser.INT_TYPE)
            self.state = 37
            self.match(MiniGPParser.VAR)
            self.state = 38
            self.match(MiniGPParser.ASSIGMENT_OPERATOR)
            self.state = 39
            self.expression()
            self.state = 40
            self.match(MiniGPParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL_TYPE(self):
            return self.getToken(MiniGPParser.BOOL_TYPE, 0)

        def VAR(self):
            return self.getToken(MiniGPParser.VAR, 0)

        def ASSIGMENT_OPERATOR(self):
            return self.getToken(MiniGPParser.ASSIGMENT_OPERATOR, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGPParser.ConditionContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGPParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGPParser.RULE_booleanDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanDeclaration" ):
                listener.enterBooleanDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanDeclaration" ):
                listener.exitBooleanDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanDeclaration" ):
                return visitor.visitBooleanDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def booleanDeclaration(self):

        localctx = MiniGPParser.BooleanDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_booleanDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(MiniGPParser.BOOL_TYPE)
            self.state = 43
            self.match(MiniGPParser.VAR)
            self.state = 44
            self.match(MiniGPParser.ASSIGMENT_OPERATOR)
            self.state = 45
            self.condition()
            self.state = 46
            self.match(MiniGPParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGPParser.VAR, 0)

        def ASSIGMENT_OPERATOR(self):
            return self.getToken(MiniGPParser.ASSIGMENT_OPERATOR, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGPParser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGPParser.ExpressionContext,0)


        def condition(self):
            return self.getTypedRuleContext(MiniGPParser.ConditionContext,0)


        def getRuleIndex(self):
            return MiniGPParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniGPParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(MiniGPParser.VAR)
            self.state = 49
            self.match(MiniGPParser.ASSIGMENT_OPERATOR)
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 50
                self.expression()
                pass

            elif la_ == 2:
                self.state = 51
                self.condition()
                pass


            self.state = 54
            self.match(MiniGPParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGPParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGPParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGPParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGPParser.RPAREN, 0)

        def executionBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.ExecutionBlockContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.ExecutionBlockContext,i)


        def ELSE(self):
            return self.getToken(MiniGPParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniGPParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniGPParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(MiniGPParser.IF)
            self.state = 57
            self.match(MiniGPParser.LPAREN)
            self.state = 58
            self.condition()
            self.state = 59
            self.match(MiniGPParser.RPAREN)
            self.state = 60
            self.executionBlock()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 61
                self.match(MiniGPParser.ELSE)
                self.state = 62
                self.executionBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MiniGPParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MiniGPParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGPParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGPParser.RPAREN, 0)

        def executionBlock(self):
            return self.getTypedRuleContext(MiniGPParser.ExecutionBlockContext,0)


        def getRuleIndex(self):
            return MiniGPParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = MiniGPParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(MiniGPParser.WHILE)
            self.state = 66
            self.match(MiniGPParser.LPAREN)
            self.state = 67
            self.condition()
            self.state = 68
            self.match(MiniGPParser.RPAREN)
            self.state = 69
            self.executionBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IoStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(MiniGPParser.READ, 0)

        def LPAREN(self):
            return self.getToken(MiniGPParser.LPAREN, 0)

        def VAR(self):
            return self.getToken(MiniGPParser.VAR, 0)

        def RPAREN(self):
            return self.getToken(MiniGPParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGPParser.SEMICOLON, 0)

        def WRITE(self):
            return self.getToken(MiniGPParser.WRITE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGPParser.ExpressionContext,0)


        def condition(self):
            return self.getTypedRuleContext(MiniGPParser.ConditionContext,0)


        def getRuleIndex(self):
            return MiniGPParser.RULE_ioStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIoStatement" ):
                listener.enterIoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIoStatement" ):
                listener.exitIoStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIoStatement" ):
                return visitor.visitIoStatement(self)
            else:
                return visitor.visitChildren(self)




    def ioStatement(self):

        localctx = MiniGPParser.IoStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ioStatement)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(MiniGPParser.READ)
                self.state = 72
                self.match(MiniGPParser.LPAREN)
                self.state = 73
                self.match(MiniGPParser.VAR)
                self.state = 74
                self.match(MiniGPParser.RPAREN)
                self.state = 75
                self.match(MiniGPParser.SEMICOLON)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(MiniGPParser.WRITE)
                self.state = 77
                self.match(MiniGPParser.LPAREN)
                self.state = 80
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 78
                    self.expression()
                    pass

                elif la_ == 2:
                    self.state = 79
                    self.condition()
                    pass


                self.state = 82
                self.match(MiniGPParser.RPAREN)
                self.state = 83
                self.match(MiniGPParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGPParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.ExpressionContext,i)


        def EXPRESSION_OPERATOR(self):
            return self.getToken(MiniGPParser.EXPRESSION_OPERATOR, 0)

        def RPAREN(self):
            return self.getToken(MiniGPParser.RPAREN, 0)

        def INT(self):
            return self.getToken(MiniGPParser.INT, 0)

        def VAR(self):
            return self.getToken(MiniGPParser.VAR, 0)

        def getRuleIndex(self):
            return MiniGPParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniGPParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(MiniGPParser.LPAREN)
                self.state = 88
                self.expression()
                self.state = 89
                self.match(MiniGPParser.EXPRESSION_OPERATOR)
                self.state = 90
                self.expression()
                self.state = 91
                self.match(MiniGPParser.RPAREN)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(MiniGPParser.INT)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.match(MiniGPParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGPParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.ExpressionContext,i)


        def EXPRESSION_COMPARISON_OPERATOR(self):
            return self.getToken(MiniGPParser.EXPRESSION_COMPARISON_OPERATOR, 0)

        def RPAREN(self):
            return self.getToken(MiniGPParser.RPAREN, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.ConditionContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.ConditionContext,i)


        def CONDITION_OPERATOR(self):
            return self.getToken(MiniGPParser.CONDITION_OPERATOR, 0)

        def NEGATION_OPERATOR(self):
            return self.getToken(MiniGPParser.NEGATION_OPERATOR, 0)

        def BOOL(self):
            return self.getToken(MiniGPParser.BOOL, 0)

        def VAR(self):
            return self.getToken(MiniGPParser.VAR, 0)

        def getRuleIndex(self):
            return MiniGPParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniGPParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.match(MiniGPParser.LPAREN)
                self.state = 98
                self.expression()
                self.state = 99
                self.match(MiniGPParser.EXPRESSION_COMPARISON_OPERATOR)
                self.state = 100
                self.expression()
                self.state = 101
                self.match(MiniGPParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.match(MiniGPParser.LPAREN)
                self.state = 104
                self.condition()
                self.state = 105
                self.match(MiniGPParser.CONDITION_OPERATOR)
                self.state = 106
                self.condition()
                self.state = 107
                self.match(MiniGPParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.match(MiniGPParser.NEGATION_OPERATOR)
                self.state = 110
                self.match(MiniGPParser.LPAREN)
                self.state = 111
                self.condition()
                self.state = 112
                self.match(MiniGPParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 114
                self.match(MiniGPParser.BOOL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 115
                self.match(MiniGPParser.VAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





