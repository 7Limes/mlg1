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
        4,1,32,224,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,5,0,64,8,0,10,0,
        12,0,67,9,0,1,0,5,0,70,8,0,10,0,12,0,73,9,0,1,0,4,0,76,8,0,11,0,
        12,0,77,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,5,3,5,96,8,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,104,8,6,1,6,1,6,1,
        6,1,7,1,7,1,7,5,7,112,8,7,10,7,12,7,115,9,7,1,8,1,8,5,8,119,8,8,
        10,8,12,8,122,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,133,8,
        9,1,10,1,10,1,10,1,10,1,10,3,10,140,8,10,1,11,1,11,1,11,1,11,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,154,8,12,1,12,3,12,157,8,
        12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,14,166,8,14,1,15,1,15,3,
        15,170,8,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,3,
        18,182,8,18,1,18,1,18,1,19,1,19,1,19,5,19,189,8,19,10,19,12,19,192,
        9,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,201,8,20,1,20,1,20,
        1,20,1,20,5,20,207,8,20,10,20,12,20,210,9,20,1,21,1,21,1,21,1,22,
        1,22,1,22,3,22,218,8,22,1,23,1,23,1,24,1,24,1,24,0,1,40,25,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        0,3,1,0,28,29,2,0,5,5,19,19,2,0,5,5,20,25,225,0,53,1,0,0,0,2,79,
        1,0,0,0,4,83,1,0,0,0,6,86,1,0,0,0,8,90,1,0,0,0,10,95,1,0,0,0,12,
        99,1,0,0,0,14,108,1,0,0,0,16,116,1,0,0,0,18,132,1,0,0,0,20,134,1,
        0,0,0,22,141,1,0,0,0,24,145,1,0,0,0,26,158,1,0,0,0,28,160,1,0,0,
        0,30,169,1,0,0,0,32,171,1,0,0,0,34,175,1,0,0,0,36,178,1,0,0,0,38,
        185,1,0,0,0,40,200,1,0,0,0,42,211,1,0,0,0,44,217,1,0,0,0,46,219,
        1,0,0,0,48,221,1,0,0,0,50,52,3,2,1,0,51,50,1,0,0,0,52,55,1,0,0,0,
        53,51,1,0,0,0,53,54,1,0,0,0,54,59,1,0,0,0,55,53,1,0,0,0,56,58,3,
        4,2,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,
        65,1,0,0,0,61,59,1,0,0,0,62,64,3,6,3,0,63,62,1,0,0,0,64,67,1,0,0,
        0,65,63,1,0,0,0,65,66,1,0,0,0,66,71,1,0,0,0,67,65,1,0,0,0,68,70,
        3,8,4,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,
        72,75,1,0,0,0,73,71,1,0,0,0,74,76,3,12,6,0,75,74,1,0,0,0,76,77,1,
        0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,1,1,0,0,0,79,80,5,1,0,0,80,
        81,5,26,0,0,81,82,5,29,0,0,82,3,1,0,0,0,83,84,5,2,0,0,84,85,5,30,
        0,0,85,5,1,0,0,0,86,87,5,3,0,0,87,88,5,28,0,0,88,89,5,30,0,0,89,
        7,1,0,0,0,90,91,5,4,0,0,91,92,5,28,0,0,92,93,3,10,5,0,93,9,1,0,0,
        0,94,96,5,5,0,0,95,94,1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,0,97,98,
        5,29,0,0,98,11,1,0,0,0,99,100,5,6,0,0,100,101,5,28,0,0,101,103,5,
        7,0,0,102,104,3,14,7,0,103,102,1,0,0,0,103,104,1,0,0,0,104,105,1,
        0,0,0,105,106,5,8,0,0,106,107,3,16,8,0,107,13,1,0,0,0,108,113,5,
        28,0,0,109,110,5,9,0,0,110,112,5,28,0,0,111,109,1,0,0,0,112,115,
        1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,15,1,0,0,0,115,113,1,
        0,0,0,116,120,5,10,0,0,117,119,3,18,9,0,118,117,1,0,0,0,119,122,
        1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,123,1,0,0,0,122,120,
        1,0,0,0,123,124,5,11,0,0,124,17,1,0,0,0,125,133,3,20,10,0,126,133,
        3,22,11,0,127,133,3,24,12,0,128,133,3,36,18,0,129,133,3,34,17,0,
        130,133,3,28,14,0,131,133,3,32,16,0,132,125,1,0,0,0,132,126,1,0,
        0,0,132,127,1,0,0,0,132,128,1,0,0,0,132,129,1,0,0,0,132,130,1,0,
        0,0,132,131,1,0,0,0,133,19,1,0,0,0,134,135,5,27,0,0,135,136,5,28,
        0,0,136,139,5,12,0,0,137,140,3,40,20,0,138,140,5,30,0,0,139,137,
        1,0,0,0,139,138,1,0,0,0,140,21,1,0,0,0,141,142,5,28,0,0,142,143,
        5,12,0,0,143,144,3,40,20,0,144,23,1,0,0,0,145,146,5,27,0,0,146,147,
        5,28,0,0,147,148,5,13,0,0,148,149,3,26,13,0,149,156,5,14,0,0,150,
        151,5,12,0,0,151,153,5,13,0,0,152,154,3,38,19,0,153,152,1,0,0,0,
        153,154,1,0,0,0,154,155,1,0,0,0,155,157,5,14,0,0,156,150,1,0,0,0,
        156,157,1,0,0,0,157,25,1,0,0,0,158,159,7,0,0,0,159,27,1,0,0,0,160,
        161,5,15,0,0,161,162,3,40,20,0,162,165,3,16,8,0,163,164,5,16,0,0,
        164,166,3,30,15,0,165,163,1,0,0,0,165,166,1,0,0,0,166,29,1,0,0,0,
        167,170,3,16,8,0,168,170,3,28,14,0,169,167,1,0,0,0,169,168,1,0,0,
        0,170,31,1,0,0,0,171,172,5,17,0,0,172,173,3,40,20,0,173,174,3,16,
        8,0,174,33,1,0,0,0,175,176,5,18,0,0,176,177,3,40,20,0,177,35,1,0,
        0,0,178,179,5,28,0,0,179,181,5,7,0,0,180,182,3,38,19,0,181,180,1,
        0,0,0,181,182,1,0,0,0,182,183,1,0,0,0,183,184,5,8,0,0,184,37,1,0,
        0,0,185,190,3,40,20,0,186,187,5,9,0,0,187,189,3,40,20,0,188,186,
        1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,39,1,
        0,0,0,192,190,1,0,0,0,193,194,6,20,-1,0,194,201,3,44,22,0,195,201,
        3,42,21,0,196,197,5,7,0,0,197,198,3,40,20,0,198,199,5,8,0,0,199,
        201,1,0,0,0,200,193,1,0,0,0,200,195,1,0,0,0,200,196,1,0,0,0,201,
        208,1,0,0,0,202,203,10,2,0,0,203,204,3,48,24,0,204,205,3,40,20,3,
        205,207,1,0,0,0,206,202,1,0,0,0,207,210,1,0,0,0,208,206,1,0,0,0,
        208,209,1,0,0,0,209,41,1,0,0,0,210,208,1,0,0,0,211,212,3,46,23,0,
        212,213,3,40,20,0,213,43,1,0,0,0,214,218,5,28,0,0,215,218,5,29,0,
        0,216,218,3,36,18,0,217,214,1,0,0,0,217,215,1,0,0,0,217,216,1,0,
        0,0,218,45,1,0,0,0,219,220,7,1,0,0,220,47,1,0,0,0,221,222,7,2,0,
        0,222,49,1,0,0,0,20,53,59,65,71,77,95,103,113,120,132,139,153,156,
        165,169,181,190,200,208,217
    ]

class mlg1Parser ( Parser ):

    grammarFileName = "mlg1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'", "'%include'", "'$'", "'define'", 
                     "'-'", "'fn'", "'('", "')'", "','", "'{'", "'}'", "'='", 
                     "'['", "']'", "'if'", "'else'", "'while'", "'return'", 
                     "'!'", "'+'", "'*'", "'/'", "'%'", "'<'", "'=='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "META_VARIABLE_NAME", "VARIABLE_KEYWORD", 
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
    RULE_statement = 9
    RULE_variableDeclaration = 10
    RULE_assignment = 11
    RULE_arrayDeclaration = 12
    RULE_arraySize = 13
    RULE_ifStatement = 14
    RULE_elseStatement = 15
    RULE_whileLoop = 16
    RULE_returnStatement = 17
    RULE_functionCall = 18
    RULE_expressionList = 19
    RULE_expression = 20
    RULE_unaryExpression = 21
    RULE_primary = 22
    RULE_unaryOperator = 23
    RULE_operator = 24

    ruleNames =  [ "program", "metaVariable", "includeFile", "loadFile", 
                   "constantDefinition", "signedInteger", "function", "parameterList", 
                   "block", "statement", "variableDeclaration", "assignment", 
                   "arrayDeclaration", "arraySize", "ifStatement", "elseStatement", 
                   "whileLoop", "returnStatement", "functionCall", "expressionList", 
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
    META_VARIABLE_NAME=26
    VARIABLE_KEYWORD=27
    NAME=28
    INTEGER=29
    STRING=30
    LINE_COMMENT=31
    WS=32

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

        def metaVariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mlg1Parser.MetaVariableContext)
            else:
                return self.getTypedRuleContext(mlg1Parser.MetaVariableContext,i)


        def includeFile(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mlg1Parser.IncludeFileContext)
            else:
                return self.getTypedRuleContext(mlg1Parser.IncludeFileContext,i)


        def loadFile(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mlg1Parser.LoadFileContext)
            else:
                return self.getTypedRuleContext(mlg1Parser.LoadFileContext,i)


        def constantDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mlg1Parser.ConstantDefinitionContext)
            else:
                return self.getTypedRuleContext(mlg1Parser.ConstantDefinitionContext,i)


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
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 50
                self.metaVariable()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 56
                self.includeFile()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 62
                self.loadFile()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 68
                self.constantDefinition()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                self.function()
                self.state = 77 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6):
                    break

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
            self.state = 79
            self.match(mlg1Parser.T__0)
            self.state = 80
            self.match(mlg1Parser.META_VARIABLE_NAME)
            self.state = 81
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
            self.state = 83
            self.match(mlg1Parser.T__1)
            self.state = 84
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
            self.state = 86
            self.match(mlg1Parser.T__2)
            self.state = 87
            self.match(mlg1Parser.NAME)
            self.state = 88
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
            self.state = 90
            self.match(mlg1Parser.T__3)
            self.state = 91
            self.match(mlg1Parser.NAME)
            self.state = 92
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
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 94
                self.match(mlg1Parser.T__4)


            self.state = 97
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
            self.state = 99
            self.match(mlg1Parser.T__5)
            self.state = 100
            self.match(mlg1Parser.NAME)
            self.state = 101
            self.match(mlg1Parser.T__6)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 102
                self.parameterList()


            self.state = 105
            self.match(mlg1Parser.T__7)
            self.state = 106
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
            self.state = 108
            self.match(mlg1Parser.NAME)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 109
                self.match(mlg1Parser.T__8)
                self.state = 110
                self.match(mlg1Parser.NAME)
                self.state = 115
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
            self.state = 116
            self.match(mlg1Parser.T__9)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 403079168) != 0):
                self.state = 117
                self.statement()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self.match(mlg1Parser.T__10)
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


        def ifStatement(self):
            return self.getTypedRuleContext(mlg1Parser.IfStatementContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(mlg1Parser.WhileLoopContext,0)


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
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.arrayDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 128
                self.functionCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 129
                self.returnStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 130
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 131
                self.whileLoop()
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
        self.enterRule(localctx, 20, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(mlg1Parser.VARIABLE_KEYWORD)
            self.state = 135
            self.match(mlg1Parser.NAME)
            self.state = 136
            self.match(mlg1Parser.T__11)
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 7, 19, 28, 29]:
                self.state = 137
                self.expression(0)
                pass
            elif token in [30]:
                self.state = 138
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
        self.enterRule(localctx, 22, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(mlg1Parser.NAME)
            self.state = 142
            self.match(mlg1Parser.T__11)
            self.state = 143
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
        self.enterRule(localctx, 24, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(mlg1Parser.VARIABLE_KEYWORD)
            self.state = 146
            self.match(mlg1Parser.NAME)
            self.state = 147
            self.match(mlg1Parser.T__12)
            self.state = 148
            self.arraySize()
            self.state = 149
            self.match(mlg1Parser.T__13)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 150
                self.match(mlg1Parser.T__11)
                self.state = 151
                self.match(mlg1Parser.T__12)
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 805830816) != 0):
                    self.state = 152
                    self.expressionList()


                self.state = 155
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
        self.enterRule(localctx, 26, self.RULE_arraySize)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
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


        def elseStatement(self):
            return self.getTypedRuleContext(mlg1Parser.ElseStatementContext,0)


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
        self.enterRule(localctx, 28, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(mlg1Parser.T__14)
            self.state = 161
            self.expression(0)
            self.state = 162
            self.block()
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 163
                self.match(mlg1Parser.T__15)
                self.state = 164
                self.elseStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(mlg1Parser.BlockContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(mlg1Parser.IfStatementContext,0)


        def getRuleIndex(self):
            return mlg1Parser.RULE_elseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseStatement" ):
                listener.enterElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseStatement" ):
                listener.exitElseStatement(self)




    def elseStatement(self):

        localctx = mlg1Parser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_elseStatement)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.block()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.ifStatement()
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
        self.enterRule(localctx, 32, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(mlg1Parser.T__16)
            self.state = 172
            self.expression(0)
            self.state = 173
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
        self.enterRule(localctx, 34, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(mlg1Parser.T__17)
            self.state = 176
            self.expression(0)
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
        self.enterRule(localctx, 36, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(mlg1Parser.NAME)
            self.state = 179
            self.match(mlg1Parser.T__6)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 805830816) != 0):
                self.state = 180
                self.expressionList()


            self.state = 183
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
        self.enterRule(localctx, 38, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.expression(0)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 186
                self.match(mlg1Parser.T__8)
                self.state = 187
                self.expression(0)
                self.state = 192
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28, 29]:
                self.state = 194
                self.primary()
                pass
            elif token in [5, 19]:
                self.state = 195
                self.unaryExpression()
                pass
            elif token in [7]:
                self.state = 196
                self.match(mlg1Parser.T__6)
                self.state = 197
                self.expression(0)
                self.state = 198
                self.match(mlg1Parser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = mlg1Parser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 202
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 203
                    self.operator()
                    self.state = 204
                    self.expression(3) 
                self.state = 210
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
        self.enterRule(localctx, 42, self.RULE_unaryExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.unaryOperator()
            self.state = 212
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
        self.enterRule(localctx, 44, self.RULE_primary)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(mlg1Parser.NAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(mlg1Parser.INTEGER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
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
        self.enterRule(localctx, 46, self.RULE_unaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not(_la==5 or _la==19):
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
        self.enterRule(localctx, 48, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060320) != 0)):
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
        self._predicates[20] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




