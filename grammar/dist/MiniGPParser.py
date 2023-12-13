# Generated from ./grammar/MiniGP.g4 by ANTLR 4.13.1
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
        4,1,32,137,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,1,4,
        1,29,8,1,11,1,12,1,30,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,40,8,2,1,3,
        3,3,43,8,3,1,3,1,3,3,3,47,8,3,1,4,1,4,1,4,1,4,3,4,53,8,4,1,4,1,4,
        1,5,1,5,1,5,1,5,3,5,61,8,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,69,8,6,1,
        6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,80,8,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,3,10,107,8,10,1,10,1,10,1,10,1,10,1,
        10,1,10,5,10,115,8,10,10,10,12,10,118,9,10,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,3,11,127,8,11,1,11,1,11,1,11,5,11,132,8,11,10,11,12,
        11,135,9,11,1,11,0,2,20,22,12,0,2,4,6,8,10,12,14,16,18,20,22,0,5,
        1,0,13,14,1,0,15,20,1,0,17,18,1,0,21,23,1,0,25,28,144,0,24,1,0,0,
        0,2,26,1,0,0,0,4,39,1,0,0,0,6,42,1,0,0,0,8,48,1,0,0,0,10,56,1,0,
        0,0,12,64,1,0,0,0,14,72,1,0,0,0,16,81,1,0,0,0,18,87,1,0,0,0,20,106,
        1,0,0,0,22,126,1,0,0,0,24,25,3,2,1,0,25,1,1,0,0,0,26,28,5,1,0,0,
        27,29,3,4,2,0,28,27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,
        0,0,0,31,32,1,0,0,0,32,33,5,2,0,0,33,3,1,0,0,0,34,40,3,6,3,0,35,
        40,3,12,6,0,36,40,3,14,7,0,37,40,3,16,8,0,38,40,3,18,9,0,39,34,1,
        0,0,0,39,35,1,0,0,0,39,36,1,0,0,0,39,37,1,0,0,0,39,38,1,0,0,0,40,
        5,1,0,0,0,41,43,5,3,0,0,42,41,1,0,0,0,42,43,1,0,0,0,43,46,1,0,0,
        0,44,47,3,8,4,0,45,47,3,10,5,0,46,44,1,0,0,0,46,45,1,0,0,0,47,7,
        1,0,0,0,48,49,5,4,0,0,49,52,5,31,0,0,50,51,5,5,0,0,51,53,3,22,11,
        0,52,50,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,55,5,6,0,0,55,9,1,
        0,0,0,56,57,5,7,0,0,57,60,5,31,0,0,58,59,5,5,0,0,59,61,3,20,10,0,
        60,58,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,63,5,6,0,0,63,11,1,
        0,0,0,64,65,5,31,0,0,65,68,5,5,0,0,66,69,3,22,11,0,67,69,3,20,10,
        0,68,66,1,0,0,0,68,67,1,0,0,0,69,70,1,0,0,0,70,71,5,6,0,0,71,13,
        1,0,0,0,72,73,5,8,0,0,73,74,5,9,0,0,74,75,3,20,10,0,75,76,5,10,0,
        0,76,79,3,2,1,0,77,78,5,11,0,0,78,80,3,2,1,0,79,77,1,0,0,0,79,80,
        1,0,0,0,80,15,1,0,0,0,81,82,5,12,0,0,82,83,5,9,0,0,83,84,3,20,10,
        0,84,85,5,10,0,0,85,86,3,2,1,0,86,17,1,0,0,0,87,88,7,0,0,0,88,89,
        5,9,0,0,89,90,5,31,0,0,90,91,5,10,0,0,91,92,5,6,0,0,92,19,1,0,0,
        0,93,94,6,10,-1,0,94,95,3,22,11,0,95,96,7,1,0,0,96,97,3,22,11,0,
        97,107,1,0,0,0,98,99,5,24,0,0,99,107,3,20,10,4,100,101,5,9,0,0,101,
        102,3,20,10,0,102,103,5,10,0,0,103,107,1,0,0,0,104,107,5,29,0,0,
        105,107,5,31,0,0,106,93,1,0,0,0,106,98,1,0,0,0,106,100,1,0,0,0,106,
        104,1,0,0,0,106,105,1,0,0,0,107,116,1,0,0,0,108,109,10,6,0,0,109,
        110,7,2,0,0,110,115,3,20,10,7,111,112,10,5,0,0,112,113,7,3,0,0,113,
        115,3,20,10,6,114,108,1,0,0,0,114,111,1,0,0,0,115,118,1,0,0,0,116,
        114,1,0,0,0,116,117,1,0,0,0,117,21,1,0,0,0,118,116,1,0,0,0,119,120,
        6,11,-1,0,120,127,5,31,0,0,121,127,5,30,0,0,122,123,5,9,0,0,123,
        124,3,22,11,0,124,125,5,10,0,0,125,127,1,0,0,0,126,119,1,0,0,0,126,
        121,1,0,0,0,126,122,1,0,0,0,127,133,1,0,0,0,128,129,10,4,0,0,129,
        130,7,4,0,0,130,132,3,22,11,5,131,128,1,0,0,0,132,135,1,0,0,0,133,
        131,1,0,0,0,133,134,1,0,0,0,134,23,1,0,0,0,135,133,1,0,0,0,13,30,
        39,42,46,52,60,68,79,106,114,116,126,133
    ]

class MiniGPParser ( Parser ):

    grammarFileName = "MiniGP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'const'", "'int'", "'='", 
                     "';'", "'bool'", "'if'", "'('", "')'", "'else'", "'while'", 
                     "'read'", "'write'", "'>'", "'<'", "'=='", "'!='", 
                     "'>='", "'<='", "'&&'", "'||'", "'^'", "'!'", "'*'", 
                     "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOOL", "INT", "VAR", "WHITESPACE" ]

    RULE_prog = 0
    RULE_executionBlock = 1
    RULE_statement = 2
    RULE_varDeclaration = 3
    RULE_integerDeclaration = 4
    RULE_booleanDeclaration = 5
    RULE_assignment = 6
    RULE_ifStatement = 7
    RULE_loopStatement = 8
    RULE_ioStatement = 9
    RULE_condition = 10
    RULE_expr = 11

    ruleNames =  [ "prog", "executionBlock", "statement", "varDeclaration", 
                   "integerDeclaration", "booleanDeclaration", "assignment", 
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
    T__25=26
    T__26=27
    T__27=28
    BOOL=29
    INT=30
    VAR=31
    WHITESPACE=32

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

        def executionBlock(self):
            return self.getTypedRuleContext(MiniGPParser.ExecutionBlockContext,0)


        def getRuleIndex(self):
            return MiniGPParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = MiniGPParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.executionBlock()
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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGPParser.RULE_executionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecutionBlock" ):
                listener.enterExecutionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecutionBlock" ):
                listener.exitExecutionBlock(self)




    def executionBlock(self):

        localctx = MiniGPParser.ExecutionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_executionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(MiniGPParser.T__0)
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self.statement()
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2147512728) != 0)):
                    break

            self.state = 32
            self.match(MiniGPParser.T__1)
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


        def getRuleIndex(self):
            return MiniGPParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MiniGPParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.varDeclaration()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.assignment()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.ifStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.loopStatement()
                pass
            elif token in [13, 14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 38
                self.ioStatement()
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

        def integerDeclaration(self):
            return self.getTypedRuleContext(MiniGPParser.IntegerDeclarationContext,0)


        def booleanDeclaration(self):
            return self.getTypedRuleContext(MiniGPParser.BooleanDeclarationContext,0)


        def getRuleIndex(self):
            return MiniGPParser.RULE_varDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)




    def varDeclaration(self):

        localctx = MiniGPParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 41
                self.match(MiniGPParser.T__2)


            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 44
                self.integerDeclaration()
                pass
            elif token in [7]:
                self.state = 45
                self.booleanDeclaration()
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


    class IntegerDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGPParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGPParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGPParser.RULE_integerDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegerDeclaration" ):
                listener.enterIntegerDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegerDeclaration" ):
                listener.exitIntegerDeclaration(self)




    def integerDeclaration(self):

        localctx = MiniGPParser.IntegerDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_integerDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(MiniGPParser.T__3)
            self.state = 49
            self.match(MiniGPParser.VAR)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 50
                self.match(MiniGPParser.T__4)
                self.state = 51
                self.expr(0)


            self.state = 54
            self.match(MiniGPParser.T__5)
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

        def VAR(self):
            return self.getToken(MiniGPParser.VAR, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGPParser.ConditionContext,0)


        def getRuleIndex(self):
            return MiniGPParser.RULE_booleanDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanDeclaration" ):
                listener.enterBooleanDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanDeclaration" ):
                listener.exitBooleanDeclaration(self)




    def booleanDeclaration(self):

        localctx = MiniGPParser.BooleanDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_booleanDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(MiniGPParser.T__6)
            self.state = 57
            self.match(MiniGPParser.VAR)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 58
                self.match(MiniGPParser.T__4)
                self.state = 59
                self.condition(0)


            self.state = 62
            self.match(MiniGPParser.T__5)
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

        def expr(self):
            return self.getTypedRuleContext(MiniGPParser.ExprContext,0)


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




    def assignment(self):

        localctx = MiniGPParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(MiniGPParser.VAR)
            self.state = 65
            self.match(MiniGPParser.T__4)
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 66
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 67
                self.condition(0)
                pass


            self.state = 70
            self.match(MiniGPParser.T__5)
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


        def executionBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.ExecutionBlockContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.ExecutionBlockContext,i)


        def getRuleIndex(self):
            return MiniGPParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = MiniGPParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(MiniGPParser.T__7)
            self.state = 73
            self.match(MiniGPParser.T__8)
            self.state = 74
            self.condition(0)
            self.state = 75
            self.match(MiniGPParser.T__9)
            self.state = 76
            self.executionBlock()
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 77
                self.match(MiniGPParser.T__10)
                self.state = 78
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

        def condition(self):
            return self.getTypedRuleContext(MiniGPParser.ConditionContext,0)


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




    def loopStatement(self):

        localctx = MiniGPParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(MiniGPParser.T__11)
            self.state = 82
            self.match(MiniGPParser.T__8)
            self.state = 83
            self.condition(0)
            self.state = 84
            self.match(MiniGPParser.T__9)
            self.state = 85
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

        def VAR(self):
            return self.getToken(MiniGPParser.VAR, 0)

        def getRuleIndex(self):
            return MiniGPParser.RULE_ioStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIoStatement" ):
                listener.enterIoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIoStatement" ):
                listener.exitIoStatement(self)




    def ioStatement(self):

        localctx = MiniGPParser.IoStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ioStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 88
            self.match(MiniGPParser.T__8)
            self.state = 89
            self.match(MiniGPParser.VAR)
            self.state = 90
            self.match(MiniGPParser.T__9)
            self.state = 91
            self.match(MiniGPParser.T__5)
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


        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.ConditionContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.ConditionContext,i)


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



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGPParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_condition, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 94
                self.expr(0)
                self.state = 95
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 96
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 98
                self.match(MiniGPParser.T__23)
                self.state = 99
                self.condition(4)
                pass

            elif la_ == 3:
                self.state = 100
                self.match(MiniGPParser.T__8)
                self.state = 101
                self.condition(0)
                self.state = 102
                self.match(MiniGPParser.T__9)
                pass

            elif la_ == 4:
                self.state = 104
                self.match(MiniGPParser.BOOL)
                pass

            elif la_ == 5:
                self.state = 105
                self.match(MiniGPParser.VAR)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 114
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = MiniGPParser.ConditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 108
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 109
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 110
                        self.condition(7)
                        pass

                    elif la_ == 2:
                        localctx = MiniGPParser.ConditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 111
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 112
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 113
                        self.condition(6)
                        pass

             
                self.state = 118
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGPParser.VAR, 0)

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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGPParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.state = 120
                self.match(MiniGPParser.VAR)
                pass
            elif token in [30]:
                self.state = 121
                self.match(MiniGPParser.INT)
                pass
            elif token in [9]:
                self.state = 122
                self.match(MiniGPParser.T__8)
                self.state = 123
                self.expr(0)
                self.state = 124
                self.match(MiniGPParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGPParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 128
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 129
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 130
                    self.expr(5) 
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self._predicates[10] = self.condition_sempred
        self._predicates[11] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




