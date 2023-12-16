# Generated from ./grammar/MiniGP.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,32,189,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,
        0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,
        1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,16,
        1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,
        1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,
        1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,161,8,28,
        1,29,3,29,164,8,29,1,29,1,29,5,29,168,8,29,10,29,12,29,171,9,29,
        1,29,3,29,174,8,29,1,30,1,30,5,30,178,8,30,10,30,12,30,181,9,30,
        1,31,4,31,184,8,31,11,31,12,31,185,1,31,1,31,0,0,32,1,1,3,2,5,3,
        7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,
        31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,
        53,27,55,28,57,29,59,30,61,31,63,32,1,0,5,1,0,49,57,1,0,48,57,2,
        0,65,90,97,122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,
        194,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,
        0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,
        0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,
        0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,
        0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,
        0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,
        0,61,1,0,0,0,0,63,1,0,0,0,1,65,1,0,0,0,3,67,1,0,0,0,5,69,1,0,0,0,
        7,75,1,0,0,0,9,79,1,0,0,0,11,81,1,0,0,0,13,83,1,0,0,0,15,88,1,0,
        0,0,17,91,1,0,0,0,19,93,1,0,0,0,21,95,1,0,0,0,23,100,1,0,0,0,25,
        106,1,0,0,0,27,111,1,0,0,0,29,117,1,0,0,0,31,119,1,0,0,0,33,121,
        1,0,0,0,35,124,1,0,0,0,37,127,1,0,0,0,39,130,1,0,0,0,41,133,1,0,
        0,0,43,136,1,0,0,0,45,139,1,0,0,0,47,141,1,0,0,0,49,143,1,0,0,0,
        51,145,1,0,0,0,53,147,1,0,0,0,55,149,1,0,0,0,57,160,1,0,0,0,59,173,
        1,0,0,0,61,175,1,0,0,0,63,183,1,0,0,0,65,66,5,123,0,0,66,2,1,0,0,
        0,67,68,5,125,0,0,68,4,1,0,0,0,69,70,5,99,0,0,70,71,5,111,0,0,71,
        72,5,110,0,0,72,73,5,115,0,0,73,74,5,116,0,0,74,6,1,0,0,0,75,76,
        5,105,0,0,76,77,5,110,0,0,77,78,5,116,0,0,78,8,1,0,0,0,79,80,5,61,
        0,0,80,10,1,0,0,0,81,82,5,59,0,0,82,12,1,0,0,0,83,84,5,98,0,0,84,
        85,5,111,0,0,85,86,5,111,0,0,86,87,5,108,0,0,87,14,1,0,0,0,88,89,
        5,105,0,0,89,90,5,102,0,0,90,16,1,0,0,0,91,92,5,40,0,0,92,18,1,0,
        0,0,93,94,5,41,0,0,94,20,1,0,0,0,95,96,5,101,0,0,96,97,5,108,0,0,
        97,98,5,115,0,0,98,99,5,101,0,0,99,22,1,0,0,0,100,101,5,119,0,0,
        101,102,5,104,0,0,102,103,5,105,0,0,103,104,5,108,0,0,104,105,5,
        101,0,0,105,24,1,0,0,0,106,107,5,114,0,0,107,108,5,101,0,0,108,109,
        5,97,0,0,109,110,5,100,0,0,110,26,1,0,0,0,111,112,5,119,0,0,112,
        113,5,114,0,0,113,114,5,105,0,0,114,115,5,116,0,0,115,116,5,101,
        0,0,116,28,1,0,0,0,117,118,5,62,0,0,118,30,1,0,0,0,119,120,5,60,
        0,0,120,32,1,0,0,0,121,122,5,61,0,0,122,123,5,61,0,0,123,34,1,0,
        0,0,124,125,5,33,0,0,125,126,5,61,0,0,126,36,1,0,0,0,127,128,5,62,
        0,0,128,129,5,61,0,0,129,38,1,0,0,0,130,131,5,60,0,0,131,132,5,61,
        0,0,132,40,1,0,0,0,133,134,5,38,0,0,134,135,5,38,0,0,135,42,1,0,
        0,0,136,137,5,124,0,0,137,138,5,124,0,0,138,44,1,0,0,0,139,140,5,
        94,0,0,140,46,1,0,0,0,141,142,5,33,0,0,142,48,1,0,0,0,143,144,5,
        42,0,0,144,50,1,0,0,0,145,146,5,47,0,0,146,52,1,0,0,0,147,148,5,
        43,0,0,148,54,1,0,0,0,149,150,5,45,0,0,150,56,1,0,0,0,151,152,5,
        84,0,0,152,153,5,114,0,0,153,154,5,117,0,0,154,161,5,101,0,0,155,
        156,5,70,0,0,156,157,5,97,0,0,157,158,5,108,0,0,158,159,5,115,0,
        0,159,161,5,101,0,0,160,151,1,0,0,0,160,155,1,0,0,0,161,58,1,0,0,
        0,162,164,5,45,0,0,163,162,1,0,0,0,163,164,1,0,0,0,164,165,1,0,0,
        0,165,169,7,0,0,0,166,168,7,1,0,0,167,166,1,0,0,0,168,171,1,0,0,
        0,169,167,1,0,0,0,169,170,1,0,0,0,170,174,1,0,0,0,171,169,1,0,0,
        0,172,174,5,48,0,0,173,163,1,0,0,0,173,172,1,0,0,0,174,60,1,0,0,
        0,175,179,7,2,0,0,176,178,7,3,0,0,177,176,1,0,0,0,178,181,1,0,0,
        0,179,177,1,0,0,0,179,180,1,0,0,0,180,62,1,0,0,0,181,179,1,0,0,0,
        182,184,7,4,0,0,183,182,1,0,0,0,184,185,1,0,0,0,185,183,1,0,0,0,
        185,186,1,0,0,0,186,187,1,0,0,0,187,188,6,31,0,0,188,64,1,0,0,0,
        7,0,160,163,169,173,179,185,1,6,0,0
    ]

class MiniGPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    BOOL = 29
    INT = 30
    VAR = 31
    WHITESPACE = 32

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'const'", "'int'", "'='", "';'", "'bool'", "'if'", 
            "'('", "')'", "'else'", "'while'", "'read'", "'write'", "'>'", 
            "'<'", "'=='", "'!='", "'>='", "'<='", "'&&'", "'||'", "'^'", 
            "'!'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "BOOL", "INT", "VAR", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "BOOL", "INT", "VAR", "WHITESPACE" ]

    grammarFileName = "MiniGP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


