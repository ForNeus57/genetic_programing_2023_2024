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
        4,1,19,94,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,4,1,25,8,1,11,1,12,1,26,
        1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,43,8,
        3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,3,5,62,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,72,8,6,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,3,7,92,8,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,0,96,0,16,1,0,0,0,
        2,19,1,0,0,0,4,30,1,0,0,0,6,35,1,0,0,0,8,44,1,0,0,0,10,61,1,0,0,
        0,12,71,1,0,0,0,14,91,1,0,0,0,16,17,3,2,1,0,17,18,5,0,0,1,18,1,1,
        0,0,0,19,24,5,3,0,0,20,25,3,4,2,0,21,25,3,6,3,0,22,25,3,8,4,0,23,
        25,3,10,5,0,24,20,1,0,0,0,24,21,1,0,0,0,24,22,1,0,0,0,24,23,1,0,
        0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,28,1,0,0,0,28,29,
        5,4,0,0,29,3,1,0,0,0,30,31,5,18,0,0,31,32,5,6,0,0,32,33,3,12,6,0,
        33,34,5,5,0,0,34,5,1,0,0,0,35,36,5,14,0,0,36,37,5,1,0,0,37,38,3,
        14,7,0,38,39,5,2,0,0,39,42,3,2,1,0,40,41,5,15,0,0,41,43,3,2,1,0,
        42,40,1,0,0,0,42,43,1,0,0,0,43,7,1,0,0,0,44,45,5,13,0,0,45,46,5,
        1,0,0,46,47,3,14,7,0,47,48,5,2,0,0,48,49,3,2,1,0,49,9,1,0,0,0,50,
        51,5,11,0,0,51,52,5,1,0,0,52,53,5,18,0,0,53,54,5,2,0,0,54,62,5,5,
        0,0,55,56,5,12,0,0,56,57,5,1,0,0,57,58,3,12,6,0,58,59,5,2,0,0,59,
        60,5,5,0,0,60,62,1,0,0,0,61,50,1,0,0,0,61,55,1,0,0,0,62,11,1,0,0,
        0,63,64,5,1,0,0,64,65,3,12,6,0,65,66,5,7,0,0,66,67,3,12,6,0,67,68,
        5,2,0,0,68,72,1,0,0,0,69,72,5,17,0,0,70,72,5,18,0,0,71,63,1,0,0,
        0,71,69,1,0,0,0,71,70,1,0,0,0,72,13,1,0,0,0,73,74,5,1,0,0,74,75,
        3,12,6,0,75,76,5,8,0,0,76,77,3,12,6,0,77,78,5,2,0,0,78,92,1,0,0,
        0,79,80,5,1,0,0,80,81,3,14,7,0,81,82,5,9,0,0,82,83,3,14,7,0,83,84,
        5,2,0,0,84,92,1,0,0,0,85,86,5,10,0,0,86,87,5,1,0,0,87,88,3,14,7,
        0,88,89,5,2,0,0,89,92,1,0,0,0,90,92,5,16,0,0,91,73,1,0,0,0,91,79,
        1,0,0,0,91,85,1,0,0,0,91,90,1,0,0,0,92,15,1,0,0,0,6,24,26,42,61,
        71,91
    ]

class MiniGPParser ( Parser ):

    grammarFileName = "MiniGP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'='", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'!'", "'read'", 
                     "'write'", "'while'", "'if'", "'else'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "SEMICOLON", "ASSIGMENT_OPERATOR", "EXPRESSION_OPERATOR", 
                      "EXPRESSION_COMPARISON_OPERATOR", "CONDITION_OPERATOR", 
                      "NEGATION_OPERATOR", "READ", "WRITE", "WHILE", "IF", 
                      "ELSE", "BOOL", "INT", "VAR", "WHITESPACE" ]

    RULE_program = 0
    RULE_executionBlock = 1
    RULE_assignment = 2
    RULE_ifStatement = 3
    RULE_loopStatement = 4
    RULE_ioStatement = 5
    RULE_expression = 6
    RULE_condition = 7

    ruleNames =  [ "program", "executionBlock", "assignment", "ifStatement", 
                   "loopStatement", "ioStatement", "expression", "condition" ]

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
    READ=11
    WRITE=12
    WHILE=13
    IF=14
    ELSE=15
    BOOL=16
    INT=17
    VAR=18
    WHITESPACE=19

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
            self.state = 16
            self.executionBlock()
            self.state = 17
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
            self.state = 19
            self.match(MiniGPParser.LBRACE)
            self.state = 24 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [18]:
                    self.state = 20
                    self.assignment()
                    pass
                elif token in [14]:
                    self.state = 21
                    self.ifStatement()
                    pass
                elif token in [13]:
                    self.state = 22
                    self.loopStatement()
                    pass
                elif token in [11, 12]:
                    self.state = 23
                    self.ioStatement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 26 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 292864) != 0)):
                    break

            self.state = 28
            self.match(MiniGPParser.RBRACE)
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

        def expression(self):
            return self.getTypedRuleContext(MiniGPParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGPParser.SEMICOLON, 0)

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
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(MiniGPParser.VAR)
            self.state = 31
            self.match(MiniGPParser.ASSIGMENT_OPERATOR)
            self.state = 32
            self.expression()
            self.state = 33
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
        self.enterRule(localctx, 6, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(MiniGPParser.IF)
            self.state = 36
            self.match(MiniGPParser.LPAREN)
            self.state = 37
            self.condition()
            self.state = 38
            self.match(MiniGPParser.RPAREN)
            self.state = 39
            self.executionBlock()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 40
                self.match(MiniGPParser.ELSE)
                self.state = 41
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
        self.enterRule(localctx, 8, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(MiniGPParser.WHILE)
            self.state = 45
            self.match(MiniGPParser.LPAREN)
            self.state = 46
            self.condition()
            self.state = 47
            self.match(MiniGPParser.RPAREN)
            self.state = 48
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
        self.enterRule(localctx, 10, self.RULE_ioStatement)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(MiniGPParser.READ)
                self.state = 51
                self.match(MiniGPParser.LPAREN)
                self.state = 52
                self.match(MiniGPParser.VAR)
                self.state = 53
                self.match(MiniGPParser.RPAREN)
                self.state = 54
                self.match(MiniGPParser.SEMICOLON)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(MiniGPParser.WRITE)
                self.state = 56
                self.match(MiniGPParser.LPAREN)
                self.state = 57
                self.expression()
                self.state = 58
                self.match(MiniGPParser.RPAREN)
                self.state = 59
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
        self.enterRule(localctx, 12, self.RULE_expression)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(MiniGPParser.LPAREN)
                self.state = 64
                self.expression()
                self.state = 65
                self.match(MiniGPParser.EXPRESSION_OPERATOR)
                self.state = 66
                self.expression()
                self.state = 67
                self.match(MiniGPParser.RPAREN)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(MiniGPParser.INT)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
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
        self.enterRule(localctx, 14, self.RULE_condition)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.match(MiniGPParser.LPAREN)
                self.state = 74
                self.expression()
                self.state = 75
                self.match(MiniGPParser.EXPRESSION_COMPARISON_OPERATOR)
                self.state = 76
                self.expression()
                self.state = 77
                self.match(MiniGPParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(MiniGPParser.LPAREN)
                self.state = 80
                self.condition()
                self.state = 81
                self.match(MiniGPParser.CONDITION_OPERATOR)
                self.state = 82
                self.condition()
                self.state = 83
                self.match(MiniGPParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.match(MiniGPParser.NEGATION_OPERATOR)
                self.state = 86
                self.match(MiniGPParser.LPAREN)
                self.state = 87
                self.condition()
                self.state = 88
                self.match(MiniGPParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.match(MiniGPParser.BOOL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





