# Generated from mlg1.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .mlg1Parser import mlg1Parser
else:
    from mlg1Parser import mlg1Parser

# This class defines a complete listener for a parse tree produced by mlg1Parser.
class mlg1Listener(ParseTreeListener):

    # Enter a parse tree produced by mlg1Parser#program.
    def enterProgram(self, ctx:mlg1Parser.ProgramContext):
        pass

    # Exit a parse tree produced by mlg1Parser#program.
    def exitProgram(self, ctx:mlg1Parser.ProgramContext):
        pass


    # Enter a parse tree produced by mlg1Parser#metaVariable.
    def enterMetaVariable(self, ctx:mlg1Parser.MetaVariableContext):
        pass

    # Exit a parse tree produced by mlg1Parser#metaVariable.
    def exitMetaVariable(self, ctx:mlg1Parser.MetaVariableContext):
        pass


    # Enter a parse tree produced by mlg1Parser#includeFile.
    def enterIncludeFile(self, ctx:mlg1Parser.IncludeFileContext):
        pass

    # Exit a parse tree produced by mlg1Parser#includeFile.
    def exitIncludeFile(self, ctx:mlg1Parser.IncludeFileContext):
        pass


    # Enter a parse tree produced by mlg1Parser#loadFile.
    def enterLoadFile(self, ctx:mlg1Parser.LoadFileContext):
        pass

    # Exit a parse tree produced by mlg1Parser#loadFile.
    def exitLoadFile(self, ctx:mlg1Parser.LoadFileContext):
        pass


    # Enter a parse tree produced by mlg1Parser#constantDefinition.
    def enterConstantDefinition(self, ctx:mlg1Parser.ConstantDefinitionContext):
        pass

    # Exit a parse tree produced by mlg1Parser#constantDefinition.
    def exitConstantDefinition(self, ctx:mlg1Parser.ConstantDefinitionContext):
        pass


    # Enter a parse tree produced by mlg1Parser#signedInteger.
    def enterSignedInteger(self, ctx:mlg1Parser.SignedIntegerContext):
        pass

    # Exit a parse tree produced by mlg1Parser#signedInteger.
    def exitSignedInteger(self, ctx:mlg1Parser.SignedIntegerContext):
        pass


    # Enter a parse tree produced by mlg1Parser#function.
    def enterFunction(self, ctx:mlg1Parser.FunctionContext):
        pass

    # Exit a parse tree produced by mlg1Parser#function.
    def exitFunction(self, ctx:mlg1Parser.FunctionContext):
        pass


    # Enter a parse tree produced by mlg1Parser#parameterList.
    def enterParameterList(self, ctx:mlg1Parser.ParameterListContext):
        pass

    # Exit a parse tree produced by mlg1Parser#parameterList.
    def exitParameterList(self, ctx:mlg1Parser.ParameterListContext):
        pass


    # Enter a parse tree produced by mlg1Parser#block.
    def enterBlock(self, ctx:mlg1Parser.BlockContext):
        pass

    # Exit a parse tree produced by mlg1Parser#block.
    def exitBlock(self, ctx:mlg1Parser.BlockContext):
        pass


    # Enter a parse tree produced by mlg1Parser#statement.
    def enterStatement(self, ctx:mlg1Parser.StatementContext):
        pass

    # Exit a parse tree produced by mlg1Parser#statement.
    def exitStatement(self, ctx:mlg1Parser.StatementContext):
        pass


    # Enter a parse tree produced by mlg1Parser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:mlg1Parser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by mlg1Parser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:mlg1Parser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by mlg1Parser#assignment.
    def enterAssignment(self, ctx:mlg1Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by mlg1Parser#assignment.
    def exitAssignment(self, ctx:mlg1Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by mlg1Parser#arrayDeclaration.
    def enterArrayDeclaration(self, ctx:mlg1Parser.ArrayDeclarationContext):
        pass

    # Exit a parse tree produced by mlg1Parser#arrayDeclaration.
    def exitArrayDeclaration(self, ctx:mlg1Parser.ArrayDeclarationContext):
        pass


    # Enter a parse tree produced by mlg1Parser#arraySize.
    def enterArraySize(self, ctx:mlg1Parser.ArraySizeContext):
        pass

    # Exit a parse tree produced by mlg1Parser#arraySize.
    def exitArraySize(self, ctx:mlg1Parser.ArraySizeContext):
        pass


    # Enter a parse tree produced by mlg1Parser#ifStatement.
    def enterIfStatement(self, ctx:mlg1Parser.IfStatementContext):
        pass

    # Exit a parse tree produced by mlg1Parser#ifStatement.
    def exitIfStatement(self, ctx:mlg1Parser.IfStatementContext):
        pass


    # Enter a parse tree produced by mlg1Parser#elseStatement.
    def enterElseStatement(self, ctx:mlg1Parser.ElseStatementContext):
        pass

    # Exit a parse tree produced by mlg1Parser#elseStatement.
    def exitElseStatement(self, ctx:mlg1Parser.ElseStatementContext):
        pass


    # Enter a parse tree produced by mlg1Parser#whileLoop.
    def enterWhileLoop(self, ctx:mlg1Parser.WhileLoopContext):
        pass

    # Exit a parse tree produced by mlg1Parser#whileLoop.
    def exitWhileLoop(self, ctx:mlg1Parser.WhileLoopContext):
        pass


    # Enter a parse tree produced by mlg1Parser#returnStatement.
    def enterReturnStatement(self, ctx:mlg1Parser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by mlg1Parser#returnStatement.
    def exitReturnStatement(self, ctx:mlg1Parser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by mlg1Parser#breakStatement.
    def enterBreakStatement(self, ctx:mlg1Parser.BreakStatementContext):
        pass

    # Exit a parse tree produced by mlg1Parser#breakStatement.
    def exitBreakStatement(self, ctx:mlg1Parser.BreakStatementContext):
        pass


    # Enter a parse tree produced by mlg1Parser#continueStatement.
    def enterContinueStatement(self, ctx:mlg1Parser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by mlg1Parser#continueStatement.
    def exitContinueStatement(self, ctx:mlg1Parser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by mlg1Parser#functionCall.
    def enterFunctionCall(self, ctx:mlg1Parser.FunctionCallContext):
        pass

    # Exit a parse tree produced by mlg1Parser#functionCall.
    def exitFunctionCall(self, ctx:mlg1Parser.FunctionCallContext):
        pass


    # Enter a parse tree produced by mlg1Parser#expressionList.
    def enterExpressionList(self, ctx:mlg1Parser.ExpressionListContext):
        pass

    # Exit a parse tree produced by mlg1Parser#expressionList.
    def exitExpressionList(self, ctx:mlg1Parser.ExpressionListContext):
        pass


    # Enter a parse tree produced by mlg1Parser#expression.
    def enterExpression(self, ctx:mlg1Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by mlg1Parser#expression.
    def exitExpression(self, ctx:mlg1Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by mlg1Parser#unaryExpression.
    def enterUnaryExpression(self, ctx:mlg1Parser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by mlg1Parser#unaryExpression.
    def exitUnaryExpression(self, ctx:mlg1Parser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by mlg1Parser#primary.
    def enterPrimary(self, ctx:mlg1Parser.PrimaryContext):
        pass

    # Exit a parse tree produced by mlg1Parser#primary.
    def exitPrimary(self, ctx:mlg1Parser.PrimaryContext):
        pass


    # Enter a parse tree produced by mlg1Parser#unaryOperator.
    def enterUnaryOperator(self, ctx:mlg1Parser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by mlg1Parser#unaryOperator.
    def exitUnaryOperator(self, ctx:mlg1Parser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by mlg1Parser#operator.
    def enterOperator(self, ctx:mlg1Parser.OperatorContext):
        pass

    # Exit a parse tree produced by mlg1Parser#operator.
    def exitOperator(self, ctx:mlg1Parser.OperatorContext):
        pass



del mlg1Parser