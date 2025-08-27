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
        4,1,41,257,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,
        0,5,0,68,8,0,10,0,12,0,71,9,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,92,8,5,1,5,1,5,1,5,
        1,6,1,6,1,6,5,6,100,8,6,10,6,12,6,103,9,6,1,7,1,7,5,7,107,8,7,10,
        7,12,7,110,9,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,118,8,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,130,8,9,1,10,1,10,1,10,1,11,1,11,1,
        11,5,11,138,8,11,10,11,12,11,141,9,11,1,12,1,12,1,12,1,12,3,12,147,
        8,12,3,12,149,8,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,3,14,163,8,14,1,14,3,14,166,8,14,1,15,1,15,1,15,1,
        15,5,15,172,8,15,10,15,12,15,175,9,15,1,15,3,15,178,8,15,1,16,1,
        16,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,
        19,1,19,3,19,196,8,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,
        20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,23,3,23,215,8,23,1,23,1,
        23,1,24,1,24,1,24,5,24,222,8,24,10,24,12,24,225,9,24,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,3,25,234,8,25,1,25,1,25,1,25,1,25,5,25,240,
        8,25,10,25,12,25,243,9,25,1,26,1,26,1,26,1,27,1,27,1,27,3,27,251,
        8,27,1,28,1,28,1,29,1,29,1,29,0,1,50,30,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,0,2,
        1,0,22,24,2,0,22,22,25,34,259,0,63,1,0,0,0,2,72,1,0,0,0,4,76,1,0,
        0,0,6,79,1,0,0,0,8,83,1,0,0,0,10,87,1,0,0,0,12,96,1,0,0,0,14,104,
        1,0,0,0,16,117,1,0,0,0,18,129,1,0,0,0,20,131,1,0,0,0,22,134,1,0,
        0,0,24,142,1,0,0,0,26,150,1,0,0,0,28,154,1,0,0,0,30,167,1,0,0,0,
        32,179,1,0,0,0,34,184,1,0,0,0,36,187,1,0,0,0,38,191,1,0,0,0,40,204,
        1,0,0,0,42,207,1,0,0,0,44,209,1,0,0,0,46,211,1,0,0,0,48,218,1,0,
        0,0,50,233,1,0,0,0,52,244,1,0,0,0,54,250,1,0,0,0,56,252,1,0,0,0,
        58,254,1,0,0,0,60,62,3,16,8,0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,
        1,0,0,0,63,64,1,0,0,0,64,69,1,0,0,0,65,63,1,0,0,0,66,68,3,10,5,0,
        67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,1,1,0,
        0,0,71,69,1,0,0,0,72,73,5,1,0,0,73,74,5,35,0,0,74,75,5,38,0,0,75,
        3,1,0,0,0,76,77,5,2,0,0,77,78,5,39,0,0,78,5,1,0,0,0,79,80,5,3,0,
        0,80,81,5,37,0,0,81,82,5,39,0,0,82,7,1,0,0,0,83,84,5,4,0,0,84,85,
        5,37,0,0,85,86,3,50,25,0,86,9,1,0,0,0,87,88,5,5,0,0,88,89,5,37,0,
        0,89,91,5,6,0,0,90,92,3,12,6,0,91,90,1,0,0,0,91,92,1,0,0,0,92,93,
        1,0,0,0,93,94,5,7,0,0,94,95,3,14,7,0,95,11,1,0,0,0,96,101,5,37,0,
        0,97,98,5,8,0,0,98,100,5,37,0,0,99,97,1,0,0,0,100,103,1,0,0,0,101,
        99,1,0,0,0,101,102,1,0,0,0,102,13,1,0,0,0,103,101,1,0,0,0,104,108,
        5,9,0,0,105,107,3,18,9,0,106,105,1,0,0,0,107,110,1,0,0,0,108,106,
        1,0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,110,108,1,0,0,0,111,112,
        5,10,0,0,112,15,1,0,0,0,113,118,3,2,1,0,114,118,3,4,2,0,115,118,
        3,6,3,0,116,118,3,8,4,0,117,113,1,0,0,0,117,114,1,0,0,0,117,115,
        1,0,0,0,117,116,1,0,0,0,118,17,1,0,0,0,119,130,3,20,10,0,120,130,
        3,26,13,0,121,130,3,28,14,0,122,130,3,46,23,0,123,130,3,40,20,0,
        124,130,3,42,21,0,125,130,3,44,22,0,126,130,3,30,15,0,127,130,3,
        36,18,0,128,130,3,38,19,0,129,119,1,0,0,0,129,120,1,0,0,0,129,121,
        1,0,0,0,129,122,1,0,0,0,129,123,1,0,0,0,129,124,1,0,0,0,129,125,
        1,0,0,0,129,126,1,0,0,0,129,127,1,0,0,0,129,128,1,0,0,0,130,19,1,
        0,0,0,131,132,5,36,0,0,132,133,3,22,11,0,133,21,1,0,0,0,134,139,
        3,24,12,0,135,136,5,8,0,0,136,138,3,24,12,0,137,135,1,0,0,0,138,
        141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,23,1,0,0,0,141,139,
        1,0,0,0,142,148,5,37,0,0,143,146,5,11,0,0,144,147,3,50,25,0,145,
        147,5,39,0,0,146,144,1,0,0,0,146,145,1,0,0,0,147,149,1,0,0,0,148,
        143,1,0,0,0,148,149,1,0,0,0,149,25,1,0,0,0,150,151,5,37,0,0,151,
        152,5,11,0,0,152,153,3,50,25,0,153,27,1,0,0,0,154,155,5,36,0,0,155,
        156,5,37,0,0,156,157,5,12,0,0,157,158,3,50,25,0,158,165,5,13,0,0,
        159,160,5,11,0,0,160,162,5,12,0,0,161,163,3,48,24,0,162,161,1,0,
        0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,166,5,13,0,0,165,159,1,0,
        0,0,165,166,1,0,0,0,166,29,1,0,0,0,167,168,5,14,0,0,168,169,3,50,
        25,0,169,173,3,14,7,0,170,172,3,32,16,0,171,170,1,0,0,0,172,175,
        1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,177,1,0,0,0,175,173,
        1,0,0,0,176,178,3,34,17,0,177,176,1,0,0,0,177,178,1,0,0,0,178,31,
        1,0,0,0,179,180,5,15,0,0,180,181,5,14,0,0,181,182,3,50,25,0,182,
        183,3,14,7,0,183,33,1,0,0,0,184,185,5,15,0,0,185,186,3,14,7,0,186,
        35,1,0,0,0,187,188,5,16,0,0,188,189,3,50,25,0,189,190,3,14,7,0,190,
        37,1,0,0,0,191,192,5,17,0,0,192,195,5,6,0,0,193,196,3,20,10,0,194,
        196,3,26,13,0,195,193,1,0,0,0,195,194,1,0,0,0,195,196,1,0,0,0,196,
        197,1,0,0,0,197,198,5,18,0,0,198,199,3,50,25,0,199,200,5,18,0,0,
        200,201,3,26,13,0,201,202,5,7,0,0,202,203,3,14,7,0,203,39,1,0,0,
        0,204,205,5,19,0,0,205,206,3,50,25,0,206,41,1,0,0,0,207,208,5,20,
        0,0,208,43,1,0,0,0,209,210,5,21,0,0,210,45,1,0,0,0,211,212,5,37,
        0,0,212,214,5,6,0,0,213,215,3,48,24,0,214,213,1,0,0,0,214,215,1,
        0,0,0,215,216,1,0,0,0,216,217,5,7,0,0,217,47,1,0,0,0,218,223,3,50,
        25,0,219,220,5,8,0,0,220,222,3,50,25,0,221,219,1,0,0,0,222,225,1,
        0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,49,1,0,0,0,225,223,1,0,
        0,0,226,227,6,25,-1,0,227,234,3,54,27,0,228,234,3,52,26,0,229,230,
        5,6,0,0,230,231,3,50,25,0,231,232,5,7,0,0,232,234,1,0,0,0,233,226,
        1,0,0,0,233,228,1,0,0,0,233,229,1,0,0,0,234,241,1,0,0,0,235,236,
        10,2,0,0,236,237,3,58,29,0,237,238,3,50,25,3,238,240,1,0,0,0,239,
        235,1,0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,
        51,1,0,0,0,243,241,1,0,0,0,244,245,3,56,28,0,245,246,3,50,25,0,246,
        53,1,0,0,0,247,251,5,37,0,0,248,251,5,38,0,0,249,251,3,46,23,0,250,
        247,1,0,0,0,250,248,1,0,0,0,250,249,1,0,0,0,251,55,1,0,0,0,252,253,
        7,0,0,0,253,57,1,0,0,0,254,255,7,1,0,0,255,59,1,0,0,0,20,63,69,91,
        101,108,117,129,139,146,148,162,165,173,177,195,214,223,233,241,
        250
    ]

class mlg1Parser ( Parser ):

    grammarFileName = "mlg1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'", "'include'", "'$'", "'define'", 
                     "'fn'", "'('", "')'", "','", "'{'", "'}'", "'='", "'['", 
                     "']'", "'if'", "'else'", "'while'", "'for'", "';'", 
                     "'return'", "'break'", "'continue'", "'-'", "'!'", 
                     "'&'", "'+'", "'*'", "'/'", "'%'", "'<'", "'>'", "'<='", 
                     "'>='", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "META_VARIABLE_NAME", 
                      "VARIABLE_KEYWORD", "NAME", "INTEGER", "STRING", "LINE_COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_metaVariable = 1
    RULE_includeFile = 2
    RULE_loadFile = 3
    RULE_constantDefinition = 4
    RULE_function = 5
    RULE_parameterList = 6
    RULE_block = 7
    RULE_headerStatement = 8
    RULE_statement = 9
    RULE_variableDeclaration = 10
    RULE_declaredVariablesList = 11
    RULE_declaredVariable = 12
    RULE_assignment = 13
    RULE_arrayDeclaration = 14
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
                   "constantDefinition", "function", "parameterList", "block", 
                   "headerStatement", "statement", "variableDeclaration", 
                   "declaredVariablesList", "declaredVariable", "assignment", 
                   "arrayDeclaration", "ifStatement", "elseIfClause", "elseClause", 
                   "whileLoop", "forLoop", "returnStatement", "breakStatement", 
                   "continueStatement", "functionCall", "expressionList", 
                   "expression", "unaryExpression", "primary", "unaryOperator", 
                   "operator" ]

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
    T__32=33
    T__33=34
    META_VARIABLE_NAME=35
    VARIABLE_KEYWORD=36
    NAME=37
    INTEGER=38
    STRING=39
    LINE_COMMENT=40
    WS=41

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
            while _la==5:
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

        def expression(self):
            return self.getTypedRuleContext(mlg1Parser.ExpressionContext,0)


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
            self.expression(0)
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
        self.enterRule(localctx, 10, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(mlg1Parser.T__4)
            self.state = 88
            self.match(mlg1Parser.NAME)
            self.state = 89
            self.match(mlg1Parser.T__5)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 90
                self.parameterList()


            self.state = 93
            self.match(mlg1Parser.T__6)
            self.state = 94
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
        self.enterRule(localctx, 12, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(mlg1Parser.NAME)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 97
                self.match(mlg1Parser.T__7)
                self.state = 98
                self.match(mlg1Parser.NAME)
                self.state = 103
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
        self.enterRule(localctx, 14, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(mlg1Parser.T__8)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 206162313216) != 0):
                self.state = 105
                self.statement()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self.match(mlg1Parser.T__9)
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
        self.enterRule(localctx, 16, self.RULE_headerStatement)
        try:
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.metaVariable()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.includeFile()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.loadFile()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 116
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
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.arrayDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 122
                self.functionCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 123
                self.returnStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 124
                self.breakStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 125
                self.continueStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 126
                self.ifStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 127
                self.whileLoop()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 128
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

        def declaredVariablesList(self):
            return self.getTypedRuleContext(mlg1Parser.DeclaredVariablesListContext,0)


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
        self.enterRule(localctx, 20, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(mlg1Parser.VARIABLE_KEYWORD)
            self.state = 132
            self.declaredVariablesList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredVariablesListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaredVariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mlg1Parser.DeclaredVariableContext)
            else:
                return self.getTypedRuleContext(mlg1Parser.DeclaredVariableContext,i)


        def getRuleIndex(self):
            return mlg1Parser.RULE_declaredVariablesList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaredVariablesList" ):
                listener.enterDeclaredVariablesList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaredVariablesList" ):
                listener.exitDeclaredVariablesList(self)




    def declaredVariablesList(self):

        localctx = mlg1Parser.DeclaredVariablesListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_declaredVariablesList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.declaredVariable()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 135
                self.match(mlg1Parser.T__7)
                self.state = 136
                self.declaredVariable()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(mlg1Parser.NAME, 0)

        def expression(self):
            return self.getTypedRuleContext(mlg1Parser.ExpressionContext,0)


        def STRING(self):
            return self.getToken(mlg1Parser.STRING, 0)

        def getRuleIndex(self):
            return mlg1Parser.RULE_declaredVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaredVariable" ):
                listener.enterDeclaredVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaredVariable" ):
                listener.exitDeclaredVariable(self)




    def declaredVariable(self):

        localctx = mlg1Parser.DeclaredVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declaredVariable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(mlg1Parser.NAME)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 143
                self.match(mlg1Parser.T__10)
                self.state = 146
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6, 22, 23, 24, 37, 38]:
                    self.state = 144
                    self.expression(0)
                    pass
                elif token in [39]:
                    self.state = 145
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
        self.enterRule(localctx, 26, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(mlg1Parser.NAME)
            self.state = 151
            self.match(mlg1Parser.T__10)
            self.state = 152
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

        def expression(self):
            return self.getTypedRuleContext(mlg1Parser.ExpressionContext,0)


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
        self.enterRule(localctx, 28, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(mlg1Parser.VARIABLE_KEYWORD)
            self.state = 155
            self.match(mlg1Parser.NAME)
            self.state = 156
            self.match(mlg1Parser.T__11)
            self.state = 157
            self.expression(0)
            self.state = 158
            self.match(mlg1Parser.T__12)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 159
                self.match(mlg1Parser.T__10)
                self.state = 160
                self.match(mlg1Parser.T__11)
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 412346220608) != 0):
                    self.state = 161
                    self.expressionList()


                self.state = 164
                self.match(mlg1Parser.T__12)


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
            self.state = 167
            self.match(mlg1Parser.T__13)
            self.state = 168
            self.expression(0)
            self.state = 169
            self.block()
            self.state = 173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 170
                    self.elseIfClause() 
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 176
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
            self.state = 179
            self.match(mlg1Parser.T__14)
            self.state = 180
            self.match(mlg1Parser.T__13)
            self.state = 181
            self.expression(0)
            self.state = 182
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
            self.state = 184
            self.match(mlg1Parser.T__14)
            self.state = 185
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
            self.state = 187
            self.match(mlg1Parser.T__15)
            self.state = 188
            self.expression(0)
            self.state = 189
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
            self.state = 191
            self.match(mlg1Parser.T__16)
            self.state = 192
            self.match(mlg1Parser.T__5)
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.state = 193
                self.variableDeclaration()
                pass
            elif token in [37]:
                self.state = 194
                self.assignment()
                pass
            elif token in [18]:
                pass
            else:
                pass
            self.state = 197
            self.match(mlg1Parser.T__17)
            self.state = 198
            self.expression(0)
            self.state = 199
            self.match(mlg1Parser.T__17)
            self.state = 200
            self.assignment()
            self.state = 201
            self.match(mlg1Parser.T__6)
            self.state = 202
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
            self.state = 204
            self.match(mlg1Parser.T__18)
            self.state = 205
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
            self.state = 207
            self.match(mlg1Parser.T__19)
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
            self.state = 209
            self.match(mlg1Parser.T__20)
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
            self.state = 211
            self.match(mlg1Parser.NAME)
            self.state = 212
            self.match(mlg1Parser.T__5)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 412346220608) != 0):
                self.state = 213
                self.expressionList()


            self.state = 216
            self.match(mlg1Parser.T__6)
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
            self.state = 218
            self.expression(0)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 219
                self.match(mlg1Parser.T__7)
                self.state = 220
                self.expression(0)
                self.state = 225
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
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37, 38]:
                self.state = 227
                self.primary()
                pass
            elif token in [22, 23, 24]:
                self.state = 228
                self.unaryExpression()
                pass
            elif token in [6]:
                self.state = 229
                self.match(mlg1Parser.T__5)
                self.state = 230
                self.expression(0)
                self.state = 231
                self.match(mlg1Parser.T__6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = mlg1Parser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 235
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 236
                    self.operator()
                    self.state = 237
                    self.expression(3) 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
            self.state = 244
            self.unaryOperator()
            self.state = 245
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
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(mlg1Parser.NAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(mlg1Parser.INTEGER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
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
            self.state = 252
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
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
            self.state = 254
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34330378240) != 0)):
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
         




