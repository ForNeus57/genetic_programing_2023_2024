# Generated from MiniGP.g4 by ANTLR 4.13.1
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
        4,1,28,98,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,3,2,39,8,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,55,8,4,1,5,1,
        5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,3,7,79,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,88,
        8,8,1,8,1,8,1,8,5,8,93,8,8,10,8,12,8,96,9,8,1,8,0,1,16,9,0,2,4,6,
        8,10,12,14,16,0,4,1,0,11,12,1,0,13,18,1,0,19,20,1,0,22,25,101,0,
        19,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,0,6,42,1,0,0,0,8,47,1,0,0,0,10,
        56,1,0,0,0,12,62,1,0,0,0,14,78,1,0,0,0,16,87,1,0,0,0,18,20,3,2,1,
        0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,
        0,0,0,23,33,3,4,2,0,24,33,3,6,3,0,25,33,3,8,4,0,26,33,3,10,5,0,27,
        33,3,12,6,0,28,29,5,1,0,0,29,30,3,0,0,0,30,31,5,2,0,0,31,33,1,0,
        0,0,32,23,1,0,0,0,32,24,1,0,0,0,32,25,1,0,0,0,32,26,1,0,0,0,32,27,
        1,0,0,0,32,28,1,0,0,0,33,3,1,0,0,0,34,35,5,3,0,0,35,38,5,26,0,0,
        36,37,5,4,0,0,37,39,3,16,8,0,38,36,1,0,0,0,38,39,1,0,0,0,39,40,1,
        0,0,0,40,41,5,5,0,0,41,5,1,0,0,0,42,43,5,26,0,0,43,44,5,4,0,0,44,
        45,3,16,8,0,45,46,5,5,0,0,46,7,1,0,0,0,47,48,5,6,0,0,48,49,5,7,0,
        0,49,50,3,14,7,0,50,51,5,8,0,0,51,54,3,2,1,0,52,53,5,9,0,0,53,55,
        3,2,1,0,54,52,1,0,0,0,54,55,1,0,0,0,55,9,1,0,0,0,56,57,5,10,0,0,
        57,58,5,7,0,0,58,59,3,14,7,0,59,60,5,8,0,0,60,61,3,2,1,0,61,11,1,
        0,0,0,62,63,7,0,0,0,63,64,5,7,0,0,64,65,5,26,0,0,65,66,5,8,0,0,66,
        67,5,5,0,0,67,13,1,0,0,0,68,69,3,16,8,0,69,70,7,1,0,0,70,71,3,16,
        8,0,71,79,1,0,0,0,72,73,3,16,8,0,73,74,7,2,0,0,74,75,3,16,8,0,75,
        79,1,0,0,0,76,77,5,21,0,0,77,79,3,14,7,0,78,68,1,0,0,0,78,72,1,0,
        0,0,78,76,1,0,0,0,79,15,1,0,0,0,80,81,6,8,-1,0,81,88,5,26,0,0,82,
        88,5,27,0,0,83,84,5,7,0,0,84,85,3,16,8,0,85,86,5,8,0,0,86,88,1,0,
        0,0,87,80,1,0,0,0,87,82,1,0,0,0,87,83,1,0,0,0,88,94,1,0,0,0,89,90,
        10,4,0,0,90,91,7,3,0,0,91,93,3,16,8,5,92,89,1,0,0,0,93,96,1,0,0,
        0,94,92,1,0,0,0,94,95,1,0,0,0,95,17,1,0,0,0,96,94,1,0,0,0,7,21,32,
        38,54,78,87,94
    ]

class MiniGPParser ( Parser ):

    grammarFileName = "MiniGP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'int'", "'='", "';'", "'if'", 
                     "'('", "')'", "'else'", "'while'", "'read'", "'write'", 
                     "'>'", "'<'", "'=='", "'!='", "'>='", "'<='", "'&&'", 
                     "'||'", "'!'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_varDeclaration = 2
    RULE_assignment = 3
    RULE_ifStatement = 4
    RULE_loopStatement = 5
    RULE_ioStatement = 6
    RULE_condition = 7
    RULE_expr = 8

    ruleNames =  [ "prog", "statement", "varDeclaration", "assignment", 
                   "ifStatement", "loopStatement", "ioStatement", "condition", 
                   "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    ID=26
    INT=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGPParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MiniGPParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 67116106) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclaration(self):
            return self.getTypedRuleContext(MiniGPParser.VarDeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MiniGPParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniGPParser.IfStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(MiniGPParser.LoopStatementContext,0)


        def ioStatement(self):
            return self.getTypedRuleContext(MiniGPParser.IoStatementContext,0)


        def prog(self):
            return self.getTypedRuleContext(MiniGPParser.ProgContext,0)


        def getRuleIndex(self):
            return MiniGPParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGPParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.varDeclaration()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.assignment()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.ifStatement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.loopStatement()
                pass
            elif token in [11, 12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 27
                self.ioStatement()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 6)
                self.state = 28
                self.match(MiniGPParser.T__0)
                self.state = 29
                self.prog()
                self.state = 30
                self.match(MiniGPParser.T__1)
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


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGPParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGPParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGPParser.RULE_varDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = MiniGPParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(MiniGPParser.T__2)
            self.state = 35
            self.match(MiniGPParser.ID)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 36
                self.match(MiniGPParser.T__3)
                self.state = 37
                self.expr(0)


            self.state = 40
            self.match(MiniGPParser.T__4)
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

        def ID(self):
            return self.getToken(MiniGPParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGPParser.ExprContext,0)


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
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(MiniGPParser.ID)
            self.state = 43
            self.match(MiniGPParser.T__3)
            self.state = 44
            self.expr(0)
            self.state = 45
            self.match(MiniGPParser.T__4)
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

        def condition(self):
            return self.getTypedRuleContext(MiniGPParser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.StatementContext,i)


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
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(MiniGPParser.T__5)
            self.state = 48
            self.match(MiniGPParser.T__6)
            self.state = 49
            self.condition()
            self.state = 50
            self.match(MiniGPParser.T__7)
            self.state = 51
            self.statement()
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 52
                self.match(MiniGPParser.T__8)
                self.state = 53
                self.statement()


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

        def condition(self):
            return self.getTypedRuleContext(MiniGPParser.ConditionContext,0)


        def statement(self):
            return self.getTypedRuleContext(MiniGPParser.StatementContext,0)


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
        self.enterRule(localctx, 10, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(MiniGPParser.T__9)
            self.state = 57
            self.match(MiniGPParser.T__6)
            self.state = 58
            self.condition()
            self.state = 59
            self.match(MiniGPParser.T__7)
            self.state = 60
            self.statement()
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

        def ID(self):
            return self.getToken(MiniGPParser.ID, 0)

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
        self.enterRule(localctx, 12, self.RULE_ioStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 63
            self.match(MiniGPParser.T__6)
            self.state = 64
            self.match(MiniGPParser.ID)
            self.state = 65
            self.match(MiniGPParser.T__7)
            self.state = 66
            self.match(MiniGPParser.T__4)
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.ExprContext,i)


        def condition(self):
            return self.getTypedRuleContext(MiniGPParser.ConditionContext,0)


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
        self._la = 0 # Token type
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.expr(0)
                self.state = 69
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 70
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.expr(0)
                self.state = 73
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 74
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.match(MiniGPParser.T__20)
                self.state = 77
                self.condition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGPParser.ID, 0)

        def INT(self):
            return self.getToken(MiniGPParser.INT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.ExprContext,i)


        def getRuleIndex(self):
            return MiniGPParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGPParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.state = 81
                self.match(MiniGPParser.ID)
                pass
            elif token in [27]:
                self.state = 82
                self.match(MiniGPParser.INT)
                pass
            elif token in [7]:
                self.state = 83
                self.match(MiniGPParser.T__6)
                self.state = 84
                self.expr(0)
                self.state = 85
                self.match(MiniGPParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGPParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 89
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 90
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 91
                    self.expr(5) 
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         




