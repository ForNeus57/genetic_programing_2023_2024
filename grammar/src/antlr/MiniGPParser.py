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
        4,1,22,117,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,4,1,32,8,1,11,1,12,1,33,1,1,1,1,1,2,3,2,39,8,2,1,2,1,2,3,
        2,43,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,
        1,5,1,5,3,5,61,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,72,8,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,
        9,105,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,115,8,10,
        1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,1,1,0,15,16,120,0,22,1,
        0,0,0,2,25,1,0,0,0,4,38,1,0,0,0,6,46,1,0,0,0,8,51,1,0,0,0,10,56,
        1,0,0,0,12,64,1,0,0,0,14,73,1,0,0,0,16,79,1,0,0,0,18,104,1,0,0,0,
        20,114,1,0,0,0,22,23,3,2,1,0,23,24,5,0,0,1,24,1,1,0,0,0,25,31,5,
        8,0,0,26,32,3,4,2,0,27,32,3,10,5,0,28,32,3,12,6,0,29,32,3,14,7,0,
        30,32,3,16,8,0,31,26,1,0,0,0,31,27,1,0,0,0,31,28,1,0,0,0,31,29,1,
        0,0,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,
        35,1,0,0,0,35,36,5,9,0,0,36,3,1,0,0,0,37,39,5,3,0,0,38,37,1,0,0,
        0,38,39,1,0,0,0,39,42,1,0,0,0,40,43,3,6,3,0,41,43,3,8,4,0,42,40,
        1,0,0,0,42,41,1,0,0,0,43,44,1,0,0,0,44,45,5,10,0,0,45,5,1,0,0,0,
        46,47,5,4,0,0,47,48,5,21,0,0,48,49,5,11,0,0,49,50,3,20,10,0,50,7,
        1,0,0,0,51,52,5,5,0,0,52,53,5,21,0,0,53,54,5,11,0,0,54,55,3,18,9,
        0,55,9,1,0,0,0,56,57,5,21,0,0,57,60,5,11,0,0,58,61,3,20,10,0,59,
        61,3,18,9,0,60,58,1,0,0,0,60,59,1,0,0,0,61,62,1,0,0,0,62,63,5,10,
        0,0,63,11,1,0,0,0,64,65,5,19,0,0,65,66,5,6,0,0,66,67,3,18,9,0,67,
        68,5,7,0,0,68,71,3,2,1,0,69,70,5,20,0,0,70,72,3,2,1,0,71,69,1,0,
        0,0,71,72,1,0,0,0,72,13,1,0,0,0,73,74,5,18,0,0,74,75,5,6,0,0,75,
        76,3,18,9,0,76,77,5,7,0,0,77,78,3,2,1,0,78,15,1,0,0,0,79,80,7,0,
        0,0,80,81,5,6,0,0,81,82,5,21,0,0,82,83,5,7,0,0,83,84,5,10,0,0,84,
        17,1,0,0,0,85,86,5,6,0,0,86,87,3,20,10,0,87,88,5,13,0,0,88,89,3,
        20,10,0,89,90,5,7,0,0,90,105,1,0,0,0,91,92,5,6,0,0,92,93,3,18,9,
        0,93,94,5,14,0,0,94,95,3,18,9,0,95,96,5,7,0,0,96,105,1,0,0,0,97,
        98,5,17,0,0,98,99,5,6,0,0,99,100,3,18,9,0,100,101,5,7,0,0,101,105,
        1,0,0,0,102,105,5,1,0,0,103,105,5,21,0,0,104,85,1,0,0,0,104,91,1,
        0,0,0,104,97,1,0,0,0,104,102,1,0,0,0,104,103,1,0,0,0,105,19,1,0,
        0,0,106,107,5,6,0,0,107,108,3,20,10,0,108,109,5,12,0,0,109,110,3,
        20,10,0,110,111,5,7,0,0,111,115,1,0,0,0,112,115,5,2,0,0,113,115,
        5,21,0,0,114,106,1,0,0,0,114,112,1,0,0,0,114,113,1,0,0,0,115,21,
        1,0,0,0,8,31,33,38,42,60,71,104,114
    ]

class MiniGPParser ( Parser ):

    grammarFileName = "MiniGP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'const'", "'int'", 
                     "'bool'", "'('", "')'", "'{'", "'}'", "';'", "'='", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'read'", "'write'", 
                     "'!'", "'while'", "'if'", "'else'" ]

    symbolicNames = [ "<INVALID>", "BOOL", "INT", "CONST", "INT_TYPE", "BOOL_TYPE", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMICOLON", 
                      "ASSIGMENT_OPERATOR", "EXPRESSION_OPERATOR", "EXPRESSION_COMPARISON_OPERATOR", 
                      "CONDITION_OPERATOR", "READ", "WRITE", "NEGATION_OPERATOR", 
                      "WHILE", "IF", "ELSE", "VAR", "WHITESPACE" ]

    RULE_program = 0
    RULE_executionBlock = 1
    RULE_varDeclaration = 2
    RULE_integerDeclaration = 3
    RULE_booleanDeclaration = 4
    RULE_assignment = 5
    RULE_ifStatement = 6
    RULE_loopStatement = 7
    RULE_ioStatement = 8
    RULE_condition = 9
    RULE_expression = 10

    ruleNames =  [ "program", "executionBlock", "varDeclaration", "integerDeclaration", 
                   "booleanDeclaration", "assignment", "ifStatement", "loopStatement", 
                   "ioStatement", "condition", "expression" ]

    EOF = Token.EOF
    BOOL=1
    INT=2
    CONST=3
    INT_TYPE=4
    BOOL_TYPE=5
    LPAREN=6
    RPAREN=7
    LBRACE=8
    RBRACE=9
    SEMICOLON=10
    ASSIGMENT_OPERATOR=11
    EXPRESSION_OPERATOR=12
    EXPRESSION_COMPARISON_OPERATOR=13
    CONDITION_OPERATOR=14
    READ=15
    WRITE=16
    NEGATION_OPERATOR=17
    WHILE=18
    IF=19
    ELSE=20
    VAR=21
    WHITESPACE=22

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
            self.state = 22
            self.executionBlock()
            self.state = 23
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

        def varDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGPParser.VarDeclarationContext)
            else:
                return self.getTypedRuleContext(MiniGPParser.VarDeclarationContext,i)


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
            self.state = 25
            self.match(MiniGPParser.LBRACE)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 4, 5]:
                    self.state = 26
                    self.varDeclaration()
                    pass
                elif token in [21]:
                    self.state = 27
                    self.assignment()
                    pass
                elif token in [19]:
                    self.state = 28
                    self.ifStatement()
                    pass
                elif token in [18]:
                    self.state = 29
                    self.loopStatement()
                    pass
                elif token in [15, 16]:
                    self.state = 30
                    self.ioStatement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2981944) != 0)):
                    break

            self.state = 35
            self.match(MiniGPParser.RBRACE)
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

        def SEMICOLON(self):
            return self.getToken(MiniGPParser.SEMICOLON, 0)

        def integerDeclaration(self):
            return self.getTypedRuleContext(MiniGPParser.IntegerDeclarationContext,0)


        def booleanDeclaration(self):
            return self.getTypedRuleContext(MiniGPParser.BooleanDeclarationContext,0)


        def CONST(self):
            return self.getToken(MiniGPParser.CONST, 0)

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
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 37
                self.match(MiniGPParser.CONST)


            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 40
                self.integerDeclaration()
                pass
            elif token in [5]:
                self.state = 41
                self.booleanDeclaration()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 44
            self.match(MiniGPParser.SEMICOLON)
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
        self.enterRule(localctx, 6, self.RULE_integerDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(MiniGPParser.INT_TYPE)
            self.state = 47
            self.match(MiniGPParser.VAR)
            self.state = 48
            self.match(MiniGPParser.ASSIGMENT_OPERATOR)
            self.state = 49
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

        def BOOL_TYPE(self):
            return self.getToken(MiniGPParser.BOOL_TYPE, 0)

        def VAR(self):
            return self.getToken(MiniGPParser.VAR, 0)

        def ASSIGMENT_OPERATOR(self):
            return self.getToken(MiniGPParser.ASSIGMENT_OPERATOR, 0)

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
        self.enterRule(localctx, 8, self.RULE_booleanDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MiniGPParser.BOOL_TYPE)
            self.state = 52
            self.match(MiniGPParser.VAR)
            self.state = 53
            self.match(MiniGPParser.ASSIGMENT_OPERATOR)
            self.state = 54
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
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(MiniGPParser.VAR)
            self.state = 57
            self.match(MiniGPParser.ASSIGMENT_OPERATOR)
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 58
                self.expression()
                pass

            elif la_ == 2:
                self.state = 59
                self.condition()
                pass


            self.state = 62
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
        self.enterRule(localctx, 12, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(MiniGPParser.IF)
            self.state = 65
            self.match(MiniGPParser.LPAREN)
            self.state = 66
            self.condition()
            self.state = 67
            self.match(MiniGPParser.RPAREN)
            self.state = 68
            self.executionBlock()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 69
                self.match(MiniGPParser.ELSE)
                self.state = 70
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
        self.enterRule(localctx, 14, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(MiniGPParser.WHILE)
            self.state = 74
            self.match(MiniGPParser.LPAREN)
            self.state = 75
            self.condition()
            self.state = 76
            self.match(MiniGPParser.RPAREN)
            self.state = 77
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

        def LPAREN(self):
            return self.getToken(MiniGPParser.LPAREN, 0)

        def VAR(self):
            return self.getToken(MiniGPParser.VAR, 0)

        def RPAREN(self):
            return self.getToken(MiniGPParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGPParser.SEMICOLON, 0)

        def READ(self):
            return self.getToken(MiniGPParser.READ, 0)

        def WRITE(self):
            return self.getToken(MiniGPParser.WRITE, 0)

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
        self.enterRule(localctx, 16, self.RULE_ioStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 80
            self.match(MiniGPParser.LPAREN)
            self.state = 81
            self.match(MiniGPParser.VAR)
            self.state = 82
            self.match(MiniGPParser.RPAREN)
            self.state = 83
            self.match(MiniGPParser.SEMICOLON)
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
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(MiniGPParser.LPAREN)
                self.state = 86
                self.expression()
                self.state = 87
                self.match(MiniGPParser.EXPRESSION_COMPARISON_OPERATOR)
                self.state = 88
                self.expression()
                self.state = 89
                self.match(MiniGPParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(MiniGPParser.LPAREN)
                self.state = 92
                self.condition()
                self.state = 93
                self.match(MiniGPParser.CONDITION_OPERATOR)
                self.state = 94
                self.condition()
                self.state = 95
                self.match(MiniGPParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.match(MiniGPParser.NEGATION_OPERATOR)
                self.state = 98
                self.match(MiniGPParser.LPAREN)
                self.state = 99
                self.condition()
                self.state = 100
                self.match(MiniGPParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.match(MiniGPParser.BOOL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 103
                self.match(MiniGPParser.VAR)
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
        self.enterRule(localctx, 20, self.RULE_expression)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(MiniGPParser.LPAREN)
                self.state = 107
                self.expression()
                self.state = 108
                self.match(MiniGPParser.EXPRESSION_OPERATOR)
                self.state = 109
                self.expression()
                self.state = 110
                self.match(MiniGPParser.RPAREN)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(MiniGPParser.INT)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
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





