# Generated from mlg1.g4 by ANTLR 4.13.2
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
        4,1,39,252,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,
        0,5,0,68,8,0,10,0,12,0,71,9,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,3,5,89,8,5,1,5,1,5,1,6,1,6,1,6,1,6,
        3,6,97,8,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,105,8,7,10,7,12,7,108,9,7,
        1,8,1,8,5,8,112,8,8,10,8,12,8,115,9,8,1,8,1,8,1,9,1,9,1,9,1,9,3,
        9,123,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,
        135,8,10,1,11,1,11,1,11,1,11,1,11,3,11,142,8,11,1,12,1,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,156,8,13,1,13,3,
        13,159,8,13,1,14,1,14,1,15,1,15,1,15,1,15,5,15,167,8,15,10,15,12,
        15,170,9,15,1,15,3,15,173,8,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,
        1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,3,19,191,8,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,22,1,22,
        1,23,1,23,1,23,3,23,210,8,23,1,23,1,23,1,24,1,24,1,24,5,24,217,8,
        24,10,24,12,24,220,9,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,
        229,8,25,1,25,1,25,1,25,1,25,5,25,235,8,25,10,25,12,25,238,9,25,
        1,26,1,26,1,26,1,27,1,27,1,27,3,27,246,8,27,1,28,1,28,1,29,1,29,
        1,29,0,1,50,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,0,3,1,0,35,36,2,0,5,5,23,23,
        2,0,5,5,24,32,253,0,63,1,0,0,0,2,72,1,0,0,0,4,76,1,0,0,0,6,79,1,
        0,0,0,8,83,1,0,0,0,10,88,1,0,0,0,12,92,1,0,0,0,14,101,1,0,0,0,16,
        109,1,0,0,0,18,122,1,0,0,0,20,134,1,0,0,0,22,136,1,0,0,0,24,143,
        1,0,0,0,26,147,1,0,0,0,28,160,1,0,0,0,30,162,1,0,0,0,32,174,1,0,
        0,0,34,179,1,0,0,0,36,182,1,0,0,0,38,186,1,0,0,0,40,199,1,0,0,0,
        42,202,1,0,0,0,44,204,1,0,0,0,46,206,1,0,0,0,48,213,1,0,0,0,50,228,
        1,0,0,0,52,239,1,0,0,0,54,245,1,0,0,0,56,247,1,0,0,0,58,249,1,0,
        0,0,60,62,3,18,9,0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,
        64,1,0,0,0,64,69,1,0,0,0,65,63,1,0,0,0,66,68,3,12,6,0,67,66,1,0,
        0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,1,1,0,0,0,71,69,
        1,0,0,0,72,73,5,1,0,0,73,74,5,33,0,0,74,75,5,36,0,0,75,3,1,0,0,0,
        76,77,5,2,0,0,77,78,5,37,0,0,78,5,1,0,0,0,79,80,5,3,0,0,80,81,5,
        35,0,0,81,82,5,37,0,0,82,7,1,0,0,0,83,84,5,4,0,0,84,85,5,35,0,0,
        85,86,3,10,5,0,86,9,1,0,0,0,87,89,5,5,0,0,88,87,1,0,0,0,88,89,1,
        0,0,0,89,90,1,0,0,0,90,91,5,36,0,0,91,11,1,0,0,0,92,93,5,6,0,0,93,
        94,5,35,0,0,94,96,5,7,0,0,95,97,3,14,7,0,96,95,1,0,0,0,96,97,1,0,
        0,0,97,98,1,0,0,0,98,99,5,8,0,0,99,100,3,16,8,0,100,13,1,0,0,0,101,
        106,5,35,0,0,102,103,5,9,0,0,103,105,5,35,0,0,104,102,1,0,0,0,105,
        108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,15,1,0,0,0,108,106,
        1,0,0,0,109,113,5,10,0,0,110,112,3,20,10,0,111,110,1,0,0,0,112,115,
        1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,113,
        1,0,0,0,116,117,5,11,0,0,117,17,1,0,0,0,118,123,3,2,1,0,119,123,
        3,4,2,0,120,123,3,6,3,0,121,123,3,8,4,0,122,118,1,0,0,0,122,119,
        1,0,0,0,122,120,1,0,0,0,122,121,1,0,0,0,123,19,1,0,0,0,124,135,3,
        22,11,0,125,135,3,24,12,0,126,135,3,26,13,0,127,135,3,46,23,0,128,
        135,3,40,20,0,129,135,3,42,21,0,130,135,3,44,22,0,131,135,3,30,15,
        0,132,135,3,36,18,0,133,135,3,38,19,0,134,124,1,0,0,0,134,125,1,
        0,0,0,134,126,1,0,0,0,134,127,1,0,0,0,134,128,1,0,0,0,134,129,1,
        0,0,0,134,130,1,0,0,0,134,131,1,0,0,0,134,132,1,0,0,0,134,133,1,
        0,0,0,135,21,1,0,0,0,136,137,5,34,0,0,137,138,5,35,0,0,138,141,5,
        12,0,0,139,142,3,50,25,0,140,142,5,37,0,0,141,139,1,0,0,0,141,140,
        1,0,0,0,142,23,1,0,0,0,143,144,5,35,0,0,144,145,5,12,0,0,145,146,
        3,50,25,0,146,25,1,0,0,0,147,148,5,34,0,0,148,149,5,35,0,0,149,150,
        5,13,0,0,150,151,3,28,14,0,151,158,5,14,0,0,152,153,5,12,0,0,153,
        155,5,13,0,0,154,156,3,48,24,0,155,154,1,0,0,0,155,156,1,0,0,0,156,
        157,1,0,0,0,157,159,5,14,0,0,158,152,1,0,0,0,158,159,1,0,0,0,159,
        27,1,0,0,0,160,161,7,0,0,0,161,29,1,0,0,0,162,163,5,15,0,0,163,164,
        3,50,25,0,164,168,3,16,8,0,165,167,3,32,16,0,166,165,1,0,0,0,167,
        170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,172,1,0,0,0,170,
        168,1,0,0,0,171,173,3,34,17,0,172,171,1,0,0,0,172,173,1,0,0,0,173,
        31,1,0,0,0,174,175,5,16,0,0,175,176,5,15,0,0,176,177,3,50,25,0,177,
        178,3,16,8,0,178,33,1,0,0,0,179,180,5,16,0,0,180,181,3,16,8,0,181,
        35,1,0,0,0,182,183,5,17,0,0,183,184,3,50,25,0,184,185,3,16,8,0,185,
        37,1,0,0,0,186,187,5,18,0,0,187,190,5,7,0,0,188,191,3,22,11,0,189,
        191,3,24,12,0,190,188,1,0,0,0,190,189,1,0,0,0,190,191,1,0,0,0,191,
        192,1,0,0,0,192,193,5,19,0,0,193,194,3,50,25,0,194,195,5,19,0,0,
        195,196,3,24,12,0,196,197,5,8,0,0,197,198,3,16,8,0,198,39,1,0,0,
        0,199,200,5,20,0,0,200,201,3,50,25,0,201,41,1,0,0,0,202,203,5,21,
        0,0,203,43,1,0,0,0,204,205,5,22,0,0,205,45,1,0,0,0,206,207,5,35,
        0,0,207,209,5,7,0,0,208,210,3,48,24,0,209,208,1,0,0,0,209,210,1,
        0,0,0,210,211,1,0,0,0,211,212,5,8,0,0,212,47,1,0,0,0,213,218,3,50,
        25,0,214,215,5,9,0,0,215,217,3,50,25,0,216,214,1,0,0,0,217,220,1,
        0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,49,1,0,0,0,220,218,1,0,
        0,0,221,222,6,25,-1,0,222,229,3,54,27,0,223,229,3,52,26,0,224,225,
        5,7,0,0,225,226,3,50,25,0,226,227,5,8,0,0,227,229,1,0,0,0,228,221,
        1,0,0,0,228,223,1,0,0,0,228,224,1,0,0,0,229,236,1,0,0,0,230,231,
        10,2,0,0,231,232,3,58,29,0,232,233,3,50,25,3,233,235,1,0,0,0,234,
        230,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,
        51,1,0,0,0,238,236,1,0,0,0,239,240,3,56,28,0,240,241,3,50,25,0,241,
        53,1,0,0,0,242,246,5,35,0,0,243,246,5,36,0,0,244,246,3,46,23,0,245,
        242,1,0,0,0,245,243,1,0,0,0,245,244,1,0,0,0,246,55,1,0,0,0,247,248,
        7,1,0,0,248,57,1,0,0,0,249,250,7,2,0,0,250,59,1,0,0,0,19,63,69,88,
        96,106,113,122,134,141,155,158,168,172,190,209,218,228,236,245
    ]

class mlg1Parser ( Parser ):

    grammarFileName = "mlg1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'", "'include'", "'$'", "'define'", 
                     "'-'", "'fn'", "'('", "')'", "','", "'{'", "'}'", "'='", 
                     "'['", "']'", "'if'", "'else'", "'while'", "'for'", 
                     "';'", "'return'", "'break'", "'continue'", "'!'", 
                     "'+'", "'*'", "'/'", "'%'", "'<'", "'>'", "'<='", "'>='", 
                     "'=='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "META_VARIABLE_NAME", "VARIABLE_KEYWORD", 
                      "NAME", "INTEGER", "STRING", "LINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_metaVariable = 1
    RULE_includeFile = 2
    RULE_loadFile = 3
    RULE_constantDefinition = 4
    RULE_signedInteger = 5
    RULE_function = 6
    RULE_parameterList = 7
    RULE_block = 8
    RULE_headerStatement = 9
    RULE_statement = 10
    RULE_variableDeclaration = 11
    RULE_assignment = 12
    RULE_arrayDeclaration = 13
    RULE_arraySize = 14
    RULE_ifStatement = 15
    RULE_elseIfClause = 16
    RULE_elseClause = 17
    RULE_whileLoop = 18
    RULE_forLoop = 19
    RULE_returnStatement = 20
    RULE_breakStatement = 21
    RULE_continueStatement = 22
    RULE_functionCall = 23
    RULE_expressionList = 24
    RULE_expression = 25
    RULE_unaryExpression = 26
    RULE_primary = 27
    RULE_unaryOperator = 28
    RULE_operator = 29

    ruleNames =  [ "program", "metaVariable", "includeFile", "loadFile", 
                   "constantDefinition", "signedInteger", "function", "parameterList", 
                   "block", "headerStatement", "statement", "variableDeclaration", 
                   "assignment", "arrayDeclaration", "arraySize", "ifStatement", 
                   "elseIfClause", "elseClause", "whileLoop", "forLoop", 
                   "returnStatement", "breakStatement", "continueStatement", 
                   "functionCall", "expressionList", "expression", "unaryExpression", 
                   "primary", "unaryOperator", "operator" ]

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
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    META_VARIABLE_NAME=33
    VARIABLE_KEYWORD=34
    NAME=35
    INTEGER=36
    STRING=37
    LINE_COMMENT=38
    WS=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def headerStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mlg1Parser.HeaderStatementContext)
            else:
                return self.getTypedRuleContext(mlg1Parser.HeaderStatementContext,i)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mlg1Parser.FunctionContext)
            else:
                return self.getTypedRuleContext(mlg1Parser.FunctionContext,i)


        def getRuleIndex(self):
            return mlg1Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = mlg1Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self.state = 60
                self.headerStatement()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 66
                self.function()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetaVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def META_VARIABLE_NAME(self):
            return self.getToken(mlg1Parser.META_VARIABLE_NAME, 0)

        def INTEGER(self):
            return self.getToken(mlg1Parser.INTEGER, 0)

        def getRuleIndex(self):
            return mlg1Parser.RULE_metaVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetaVariable" ):
                listener.enterMetaVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetaVariable" ):
                listener.exitMetaVariable(self)




    def metaVariable(self):

        localctx = mlg1Parser.MetaVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_metaVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(mlg1Parser.T__0)
            self.state = 73
            self.match(mlg1Parser.META_VARIABLE_NAME)
            self.state = 74
            self.match(mlg1Parser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncludeFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(mlg1Parser.STRING, 0)

        def getRuleIndex(self):
            return mlg1Parser.RULE_includeFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncludeFile" ):
                listener.enterIncludeFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncludeFile" ):
                listener.exitIncludeFile(self)




    def includeFile(self):

        localctx = mlg1Parser.IncludeFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_includeFile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(mlg1Parser.T__1)
            self.state = 77
            self.match(mlg1Parser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(mlg1Parser.NAME, 0)

        def STRING(self):
            return self.getToken(mlg1Parser.STRING, 0)

        def getRuleIndex(self):
            return mlg1Parser.RULE_loadFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadFile" ):
                listener.enterLoadFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadFile" ):
                listener.exitLoadFile(self)




    def loadFile(self):

        localctx = mlg1Parser.LoadFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_loadFile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(mlg1Parser.T__2)
            self.state = 80
            self.match(mlg1Parser.NAME)
            self.state = 81
            self.match(mlg1Parser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(mlg1Parser.NAME, 0)

        def signedInteger(self):
            return self.getTypedRuleContext(mlg1Parser.SignedIntegerContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_constantDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantDefinition" ):
                listener.enterConstantDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantDefinition" ):
                listener.exitConstantDefinition(self)




    def constantDefinition(self):

        localctx = mlg1Parser.ConstantDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constantDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(mlg1Parser.T__3)
            self.state = 84
            self.match(mlg1Parser.NAME)
            self.state = 85
            self.signedInteger()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignedIntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(mlg1Parser.INTEGER, 0)

        def getRuleIndex(self):
            return mlg1Parser.RULE_signedInteger

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignedInteger" ):
                listener.enterSignedInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignedInteger" ):
                listener.exitSignedInteger(self)




    def signedInteger(self):

        localctx = mlg1Parser.SignedIntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_signedInteger)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 87
                self.match(mlg1Parser.T__4)


            self.state = 90
            self.match(mlg1Parser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(mlg1Parser.NAME, 0)

        def block(self):
            return self.getTypedRuleContext(mlg1Parser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(mlg1Parser.ParameterListContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = mlg1Parser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(mlg1Parser.T__5)
            self.state = 93
            self.match(mlg1Parser.NAME)
            self.state = 94
            self.match(mlg1Parser.T__6)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 95
                self.parameterList()


            self.state = 98
            self.match(mlg1Parser.T__7)
            self.state = 99
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(mlg1Parser.NAME)
            else:
                return self.getToken(mlg1Parser.NAME, i)

        def getRuleIndex(self):
            return mlg1Parser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)




    def parameterList(self):

        localctx = mlg1Parser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(mlg1Parser.NAME)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 102
                self.match(mlg1Parser.T__8)
                self.state = 103
                self.match(mlg1Parser.NAME)
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mlg1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(mlg1Parser.StatementContext,i)


        def getRuleIndex(self):
            return mlg1Parser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = mlg1Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(mlg1Parser.T__9)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 51547373568) != 0):
                self.state = 110
                self.statement()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.match(mlg1Parser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def metaVariable(self):
            return self.getTypedRuleContext(mlg1Parser.MetaVariableContext,0)


        def includeFile(self):
            return self.getTypedRuleContext(mlg1Parser.IncludeFileContext,0)


        def loadFile(self):
            return self.getTypedRuleContext(mlg1Parser.LoadFileContext,0)


        def constantDefinition(self):
            return self.getTypedRuleContext(mlg1Parser.ConstantDefinitionContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_headerStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderStatement" ):
                listener.enterHeaderStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderStatement" ):
                listener.exitHeaderStatement(self)




    def headerStatement(self):

        localctx = mlg1Parser.HeaderStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_headerStatement)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.metaVariable()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.includeFile()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.loadFile()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self.constantDefinition()
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(mlg1Parser.VariableDeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(mlg1Parser.AssignmentContext,0)


        def arrayDeclaration(self):
            return self.getTypedRuleContext(mlg1Parser.ArrayDeclarationContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(mlg1Parser.FunctionCallContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(mlg1Parser.ReturnStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(mlg1Parser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(mlg1Parser.ContinueStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(mlg1Parser.IfStatementContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(mlg1Parser.WhileLoopContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(mlg1Parser.ForLoopContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = mlg1Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statement)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.arrayDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.functionCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.returnStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
                self.breakStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 130
                self.continueStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 131
                self.ifStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 132
                self.whileLoop()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 133
                self.forLoop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_KEYWORD(self):
            return self.getToken(mlg1Parser.VARIABLE_KEYWORD, 0)

        def NAME(self):
            return self.getToken(mlg1Parser.NAME, 0)

        def expression(self):
            return self.getTypedRuleContext(mlg1Parser.ExpressionContext,0)


        def STRING(self):
            return self.getToken(mlg1Parser.STRING, 0)

        def getRuleIndex(self):
            return mlg1Parser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = mlg1Parser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(mlg1Parser.VARIABLE_KEYWORD)
            self.state = 137
            self.match(mlg1Parser.NAME)
            self.state = 138
            self.match(mlg1Parser.T__11)
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 7, 23, 35, 36]:
                self.state = 139
                self.expression(0)
                pass
            elif token in [37]:
                self.state = 140
                self.match(mlg1Parser.STRING)
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(mlg1Parser.NAME, 0)

        def expression(self):
            return self.getTypedRuleContext(mlg1Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = mlg1Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(mlg1Parser.NAME)
            self.state = 144
            self.match(mlg1Parser.T__11)
            self.state = 145
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_KEYWORD(self):
            return self.getToken(mlg1Parser.VARIABLE_KEYWORD, 0)

        def NAME(self):
            return self.getToken(mlg1Parser.NAME, 0)

        def arraySize(self):
            return self.getTypedRuleContext(mlg1Parser.ArraySizeContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(mlg1Parser.ExpressionListContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_arrayDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayDeclaration" ):
                listener.enterArrayDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayDeclaration" ):
                listener.exitArrayDeclaration(self)




    def arrayDeclaration(self):

        localctx = mlg1Parser.ArrayDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(mlg1Parser.VARIABLE_KEYWORD)
            self.state = 148
            self.match(mlg1Parser.NAME)
            self.state = 149
            self.match(mlg1Parser.T__12)
            self.state = 150
            self.arraySize()
            self.state = 151
            self.match(mlg1Parser.T__13)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 152
                self.match(mlg1Parser.T__11)
                self.state = 153
                self.match(mlg1Parser.T__12)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 103087603872) != 0):
                    self.state = 154
                    self.expressionList()


                self.state = 157
                self.match(mlg1Parser.T__13)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraySizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(mlg1Parser.INTEGER, 0)

        def NAME(self):
            return self.getToken(mlg1Parser.NAME, 0)

        def getRuleIndex(self):
            return mlg1Parser.RULE_arraySize

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArraySize" ):
                listener.enterArraySize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArraySize" ):
                listener.exitArraySize(self)




    def arraySize(self):

        localctx = mlg1Parser.ArraySizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arraySize)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            _la = self._input.LA(1)
            if not(_la==35 or _la==36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def expression(self):
            return self.getTypedRuleContext(mlg1Parser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(mlg1Parser.BlockContext,0)


        def elseIfClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mlg1Parser.ElseIfClauseContext)
            else:
                return self.getTypedRuleContext(mlg1Parser.ElseIfClauseContext,i)


        def elseClause(self):
            return self.getTypedRuleContext(mlg1Parser.ElseClauseContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = mlg1Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(mlg1Parser.T__14)
            self.state = 163
            self.expression(0)
            self.state = 164
            self.block()
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 165
                    self.elseIfClause() 
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 171
                self.elseClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(mlg1Parser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(mlg1Parser.BlockContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_elseIfClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseIfClause" ):
                listener.enterElseIfClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseIfClause" ):
                listener.exitElseIfClause(self)




    def elseIfClause(self):

        localctx = mlg1Parser.ElseIfClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_elseIfClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(mlg1Parser.T__15)
            self.state = 175
            self.match(mlg1Parser.T__14)
            self.state = 176
            self.expression(0)
            self.state = 177
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(mlg1Parser.BlockContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_elseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseClause" ):
                listener.enterElseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseClause" ):
                listener.exitElseClause(self)




    def elseClause(self):

        localctx = mlg1Parser.ElseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_elseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(mlg1Parser.T__15)
            self.state = 180
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(mlg1Parser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(mlg1Parser.BlockContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)




    def whileLoop(self):

        localctx = mlg1Parser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(mlg1Parser.T__16)
            self.state = 183
            self.expression(0)
            self.state = 184
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(mlg1Parser.ExpressionContext,0)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mlg1Parser.AssignmentContext)
            else:
                return self.getTypedRuleContext(mlg1Parser.AssignmentContext,i)


        def block(self):
            return self.getTypedRuleContext(mlg1Parser.BlockContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(mlg1Parser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)




    def forLoop(self):

        localctx = mlg1Parser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(mlg1Parser.T__17)
            self.state = 187
            self.match(mlg1Parser.T__6)
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.state = 188
                self.variableDeclaration()
                pass
            elif token in [35]:
                self.state = 189
                self.assignment()
                pass
            elif token in [19]:
                pass
            else:
                pass
            self.state = 192
            self.match(mlg1Parser.T__18)
            self.state = 193
            self.expression(0)
            self.state = 194
            self.match(mlg1Parser.T__18)
            self.state = 195
            self.assignment()
            self.state = 196
            self.match(mlg1Parser.T__7)
            self.state = 197
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(mlg1Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = mlg1Parser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(mlg1Parser.T__19)
            self.state = 200
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mlg1Parser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)




    def breakStatement(self):

        localctx = mlg1Parser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(mlg1Parser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mlg1Parser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)




    def continueStatement(self):

        localctx = mlg1Parser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(mlg1Parser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(mlg1Parser.NAME, 0)

        def expressionList(self):
            return self.getTypedRuleContext(mlg1Parser.ExpressionListContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = mlg1Parser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(mlg1Parser.NAME)
            self.state = 207
            self.match(mlg1Parser.T__6)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 103087603872) != 0):
                self.state = 208
                self.expressionList()


            self.state = 211
            self.match(mlg1Parser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mlg1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(mlg1Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return mlg1Parser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = mlg1Parser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.expression(0)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 214
                self.match(mlg1Parser.T__8)
                self.state = 215
                self.expression(0)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def primary(self):
            return self.getTypedRuleContext(mlg1Parser.PrimaryContext,0)


        def unaryExpression(self):
            return self.getTypedRuleContext(mlg1Parser.UnaryExpressionContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mlg1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(mlg1Parser.ExpressionContext,i)


        def operator(self):
            return self.getTypedRuleContext(mlg1Parser.OperatorContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mlg1Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35, 36]:
                self.state = 222
                self.primary()
                pass
            elif token in [5, 23]:
                self.state = 223
                self.unaryExpression()
                pass
            elif token in [7]:
                self.state = 224
                self.match(mlg1Parser.T__6)
                self.state = 225
                self.expression(0)
                self.state = 226
                self.match(mlg1Parser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = mlg1Parser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 230
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 231
                    self.operator()
                    self.state = 232
                    self.expression(3) 
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryOperator(self):
            return self.getTypedRuleContext(mlg1Parser.UnaryOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(mlg1Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)




    def unaryExpression(self):

        localctx = mlg1Parser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_unaryExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.unaryOperator()
            self.state = 240
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(mlg1Parser.NAME, 0)

        def INTEGER(self):
            return self.getToken(mlg1Parser.INTEGER, 0)

        def functionCall(self):
            return self.getTypedRuleContext(mlg1Parser.FunctionCallContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = mlg1Parser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_primary)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.match(mlg1Parser.NAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.match(mlg1Parser.INTEGER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mlg1Parser.RULE_unaryOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOperator" ):
                listener.enterUnaryOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOperator" ):
                listener.exitUnaryOperator(self)




    def unaryOperator(self):

        localctx = mlg1Parser.UnaryOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_unaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            _la = self._input.LA(1)
            if not(_la==5 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mlg1Parser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = mlg1Parser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8573157408) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[25] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




