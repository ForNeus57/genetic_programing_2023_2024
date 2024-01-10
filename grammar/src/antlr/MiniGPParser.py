# Generated from ./grammar/MiniGP.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,32,124,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,1,1,
        1,4,1,30,8,1,11,1,12,1,31,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,41,8,2,
        1,3,3,3,44,8,3,1,3,1,3,3,3,48,8,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,56,
        8,4,1,5,1,5,1,5,1,5,3,5,62,8,5,1,6,1,6,1,6,1,6,3,6,68,8,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,79,8,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,112,
        8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,122,8,11,1,11,
        0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,4,1,0,13,14,1,0,15,20,1,
        0,21,23,1,0,25,28,128,0,24,1,0,0,0,2,27,1,0,0,0,4,40,1,0,0,0,6,43,
        1,0,0,0,8,51,1,0,0,0,10,57,1,0,0,0,12,63,1,0,0,0,14,71,1,0,0,0,16,
        80,1,0,0,0,18,86,1,0,0,0,20,111,1,0,0,0,22,121,1,0,0,0,24,25,3,2,
        1,0,25,26,5,0,0,1,26,1,1,0,0,0,27,29,5,1,0,0,28,30,3,4,2,0,29,28,
        1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,33,1,0,0,0,
        33,34,5,2,0,0,34,3,1,0,0,0,35,41,3,6,3,0,36,41,3,12,6,0,37,41,3,
        14,7,0,38,41,3,16,8,0,39,41,3,18,9,0,40,35,1,0,0,0,40,36,1,0,0,0,
        40,37,1,0,0,0,40,38,1,0,0,0,40,39,1,0,0,0,41,5,1,0,0,0,42,44,5,3,
        0,0,43,42,1,0,0,0,43,44,1,0,0,0,44,47,1,0,0,0,45,48,3,8,4,0,46,48,
        3,10,5,0,47,45,1,0,0,0,47,46,1,0,0,0,48,49,1,0,0,0,49,50,5,4,0,0,
        50,7,1,0,0,0,51,52,5,5,0,0,52,55,5,31,0,0,53,54,5,6,0,0,54,56,3,
        22,11,0,55,53,1,0,0,0,55,56,1,0,0,0,56,9,1,0,0,0,57,58,5,7,0,0,58,
        61,5,31,0,0,59,60,5,6,0,0,60,62,3,20,10,0,61,59,1,0,0,0,61,62,1,
        0,0,0,62,11,1,0,0,0,63,64,5,31,0,0,64,67,5,6,0,0,65,68,3,22,11,0,
        66,68,3,20,10,0,67,65,1,0,0,0,67,66,1,0,0,0,68,69,1,0,0,0,69,70,
        5,4,0,0,70,13,1,0,0,0,71,72,5,8,0,0,72,73,5,9,0,0,73,74,3,20,10,
        0,74,75,5,10,0,0,75,78,3,2,1,0,76,77,5,11,0,0,77,79,3,2,1,0,78,76,
        1,0,0,0,78,79,1,0,0,0,79,15,1,0,0,0,80,81,5,12,0,0,81,82,5,9,0,0,
        82,83,3,20,10,0,83,84,5,10,0,0,84,85,3,2,1,0,85,17,1,0,0,0,86,87,
        7,0,0,0,87,88,5,9,0,0,88,89,5,31,0,0,89,90,5,10,0,0,90,91,5,4,0,
        0,91,19,1,0,0,0,92,93,5,9,0,0,93,94,3,22,11,0,94,95,7,1,0,0,95,96,
        3,22,11,0,96,97,5,10,0,0,97,112,1,0,0,0,98,99,5,9,0,0,99,100,3,20,
        10,0,100,101,7,2,0,0,101,102,3,20,10,0,102,103,5,10,0,0,103,112,
        1,0,0,0,104,105,5,24,0,0,105,106,5,9,0,0,106,107,3,20,10,0,107,108,
        5,10,0,0,108,112,1,0,0,0,109,112,5,31,0,0,110,112,5,29,0,0,111,92,
        1,0,0,0,111,98,1,0,0,0,111,104,1,0,0,0,111,109,1,0,0,0,111,110,1,
        0,0,0,112,21,1,0,0,0,113,114,5,9,0,0,114,115,3,22,11,0,115,116,7,
        3,0,0,116,117,3,22,11,0,117,118,5,10,0,0,118,122,1,0,0,0,119,122,
        5,31,0,0,120,122,5,30,0,0,121,113,1,0,0,0,121,119,1,0,0,0,121,120,
        1,0,0,0,122,23,1,0,0,0,10,31,40,43,47,55,61,67,78,111,121
    ]

class MiniGPParser ( Parser ):

    grammarFileName = "MiniGP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'const'", "';'", "'int'", 
                     "'='", "'bool'", "'if'", "'('", "')'", "'else'", "'while'", 
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

    RULE_program = 0
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
    RULE_expression = 11

    ruleNames =  [ "program", "executionBlock", "statement", "varDeclaration", 
                   "integerDeclaration", "booleanDeclaration", "assignment", 
                   "ifStatement", "loopStatement", "ioStatement", "condition", 
                   "expression" ]

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
            self.state = 24
            self.executionBlock()
            self.state = 25
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
            self.state = 27
            self.match(MiniGPParser.T__0)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.statement()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2147512744) != 0)):
                    break

            self.state = 33
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGPParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 5, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.varDeclaration()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.assignment()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.ifStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.loopStatement()
                pass
            elif token in [13, 14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 39
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = MiniGPParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 42
                self.match(MiniGPParser.T__2)


            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 45
                self.integerDeclaration()
                pass
            elif token in [7]:
                self.state = 46
                self.booleanDeclaration()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 49
            self.match(MiniGPParser.T__3)
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

        def expression(self):
            return self.getTypedRuleContext(MiniGPParser.ExpressionContext,0)


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
        self.enterRule(localctx, 8, self.RULE_integerDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MiniGPParser.T__4)
            self.state = 52
            self.match(MiniGPParser.VAR)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 53
                self.match(MiniGPParser.T__5)
                self.state = 54
                self.expression()


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanDeclaration" ):
                return visitor.visitBooleanDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def booleanDeclaration(self):

        localctx = MiniGPParser.BooleanDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_booleanDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MiniGPParser.T__6)
            self.state = 58
            self.match(MiniGPParser.VAR)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 59
                self.match(MiniGPParser.T__5)
                self.state = 60
                self.condition()


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
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(MiniGPParser.VAR)
            self.state = 64
            self.match(MiniGPParser.T__5)
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 65
                self.expression()
                pass

            elif la_ == 2:
                self.state = 66
                self.condition()
                pass


            self.state = 69
            self.match(MiniGPParser.T__3)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniGPParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(MiniGPParser.T__7)
            self.state = 72
            self.match(MiniGPParser.T__8)
            self.state = 73
            self.condition()
            self.state = 74
            self.match(MiniGPParser.T__9)
            self.state = 75
            self.executionBlock()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 76
                self.match(MiniGPParser.T__10)
                self.state = 77
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = MiniGPParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(MiniGPParser.T__11)
            self.state = 81
            self.match(MiniGPParser.T__8)
            self.state = 82
            self.condition()
            self.state = 83
            self.match(MiniGPParser.T__9)
            self.state = 84
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIoStatement" ):
                return visitor.visitIoStatement(self)
            else:
                return visitor.visitChildren(self)




    def ioStatement(self):

        localctx = MiniGPParser.IoStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ioStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 87
            self.match(MiniGPParser.T__8)
            self.state = 88
            self.match(MiniGPParser.VAR)
            self.state = 89
            self.match(MiniGPParser.T__9)
            self.state = 90
            self.match(MiniGPParser.T__3)
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.ExpressionContext,i)


        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.ConditionContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.ConditionContext,i)


        def VAR(self):
            return self.getToken(MiniGPParser.VAR, 0)

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
        self.enterRule(localctx, 20, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(MiniGPParser.T__8)
                self.state = 93
                self.expression()
                self.state = 94
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 95
                self.expression()
                self.state = 96
                self.match(MiniGPParser.T__9)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(MiniGPParser.T__8)
                self.state = 99
                self.condition()
                self.state = 100
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 101
                self.condition()
                self.state = 102
                self.match(MiniGPParser.T__9)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.match(MiniGPParser.T__23)
                self.state = 105
                self.match(MiniGPParser.T__8)
                self.state = 106
                self.condition()
                self.state = 107
                self.match(MiniGPParser.T__9)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 109
                self.match(MiniGPParser.VAR)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 110
                self.match(MiniGPParser.BOOL)
                pass


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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.ExpressionContext,i)


        def VAR(self):
            return self.getToken(MiniGPParser.VAR, 0)

        def INT(self):
            return self.getToken(MiniGPParser.INT, 0)

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
        self.enterRule(localctx, 22, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(MiniGPParser.T__8)
                self.state = 114
                self.expression()
                self.state = 115
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 116
                self.expression()
                self.state = 117
                self.match(MiniGPParser.T__9)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(MiniGPParser.VAR)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.match(MiniGPParser.INT)
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





