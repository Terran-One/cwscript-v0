# Generated from grammar/CWScript.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CWScriptParser import CWScriptParser
else:
    from CWScriptParser import CWScriptParser

# This class defines a complete listener for a parse tree produced by CWScriptParser.
class CWScriptListener(ParseTreeListener):

    # Enter a parse tree produced by CWScriptParser#program.
    def enterProgram(self, ctx:CWScriptParser.ProgramContext):
        pass

    # Exit a parse tree produced by CWScriptParser#program.
    def exitProgram(self, ctx:CWScriptParser.ProgramContext):
        pass


    # Enter a parse tree produced by CWScriptParser#topLevelStmt.
    def enterTopLevelStmt(self, ctx:CWScriptParser.TopLevelStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#topLevelStmt.
    def exitTopLevelStmt(self, ctx:CWScriptParser.TopLevelStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#contractDefn.
    def enterContractDefn(self, ctx:CWScriptParser.ContractDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#contractDefn.
    def exitContractDefn(self, ctx:CWScriptParser.ContractDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#contractItem.
    def enterContractItem(self, ctx:CWScriptParser.ContractItemContext):
        pass

    # Exit a parse tree produced by CWScriptParser#contractItem.
    def exitContractItem(self, ctx:CWScriptParser.ContractItemContext):
        pass


    # Enter a parse tree produced by CWScriptParser#reservedKeyword.
    def enterReservedKeyword(self, ctx:CWScriptParser.ReservedKeywordContext):
        pass

    # Exit a parse tree produced by CWScriptParser#reservedKeyword.
    def exitReservedKeyword(self, ctx:CWScriptParser.ReservedKeywordContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ident.
    def enterIdent(self, ctx:CWScriptParser.IdentContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ident.
    def exitIdent(self, ctx:CWScriptParser.IdentContext):
        pass


    # Enter a parse tree produced by CWScriptParser#stateBlock.
    def enterStateBlock(self, ctx:CWScriptParser.StateBlockContext):
        pass

    # Exit a parse tree produced by CWScriptParser#stateBlock.
    def exitStateBlock(self, ctx:CWScriptParser.StateBlockContext):
        pass


    # Enter a parse tree produced by CWScriptParser#stateItem.
    def enterStateItem(self, ctx:CWScriptParser.StateItemContext):
        pass

    # Exit a parse tree produced by CWScriptParser#stateItem.
    def exitStateItem(self, ctx:CWScriptParser.StateItemContext):
        pass


    # Enter a parse tree produced by CWScriptParser#itemDefn.
    def enterItemDefn(self, ctx:CWScriptParser.ItemDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#itemDefn.
    def exitItemDefn(self, ctx:CWScriptParser.ItemDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#mapDefn.
    def enterMapDefn(self, ctx:CWScriptParser.MapDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#mapDefn.
    def exitMapDefn(self, ctx:CWScriptParser.MapDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#TupleT.
    def enterTupleT(self, ctx:CWScriptParser.TupleTContext):
        pass

    # Exit a parse tree produced by CWScriptParser#TupleT.
    def exitTupleT(self, ctx:CWScriptParser.TupleTContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ParamzdT.
    def enterParamzdT(self, ctx:CWScriptParser.ParamzdTContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ParamzdT.
    def exitParamzdT(self, ctx:CWScriptParser.ParamzdTContext):
        pass


    # Enter a parse tree produced by CWScriptParser#OptionT.
    def enterOptionT(self, ctx:CWScriptParser.OptionTContext):
        pass

    # Exit a parse tree produced by CWScriptParser#OptionT.
    def exitOptionT(self, ctx:CWScriptParser.OptionTContext):
        pass


    # Enter a parse tree produced by CWScriptParser#IdentT.
    def enterIdentT(self, ctx:CWScriptParser.IdentTContext):
        pass

    # Exit a parse tree produced by CWScriptParser#IdentT.
    def exitIdentT(self, ctx:CWScriptParser.IdentTContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ListT.
    def enterListT(self, ctx:CWScriptParser.ListTContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ListT.
    def exitListT(self, ctx:CWScriptParser.ListTContext):
        pass


    # Enter a parse tree produced by CWScriptParser#MemT.
    def enterMemT(self, ctx:CWScriptParser.MemTContext):
        pass

    # Exit a parse tree produced by CWScriptParser#MemT.
    def exitMemT(self, ctx:CWScriptParser.MemTContext):
        pass


    # Enter a parse tree produced by CWScriptParser#instantiateDefn.
    def enterInstantiateDefn(self, ctx:CWScriptParser.InstantiateDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#instantiateDefn.
    def exitInstantiateDefn(self, ctx:CWScriptParser.InstantiateDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#migrateDefn.
    def enterMigrateDefn(self, ctx:CWScriptParser.MigrateDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#migrateDefn.
    def exitMigrateDefn(self, ctx:CWScriptParser.MigrateDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#fnParams.
    def enterFnParams(self, ctx:CWScriptParser.FnParamsContext):
        pass

    # Exit a parse tree produced by CWScriptParser#fnParams.
    def exitFnParams(self, ctx:CWScriptParser.FnParamsContext):
        pass


    # Enter a parse tree produced by CWScriptParser#fnBody.
    def enterFnBody(self, ctx:CWScriptParser.FnBodyContext):
        pass

    # Exit a parse tree produced by CWScriptParser#fnBody.
    def exitFnBody(self, ctx:CWScriptParser.FnBodyContext):
        pass


    # Enter a parse tree produced by CWScriptParser#paramDefn.
    def enterParamDefn(self, ctx:CWScriptParser.ParamDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#paramDefn.
    def exitParamDefn(self, ctx:CWScriptParser.ParamDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#fnDefn.
    def enterFnDefn(self, ctx:CWScriptParser.FnDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#fnDefn.
    def exitFnDefn(self, ctx:CWScriptParser.FnDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#stmt.
    def enterStmt(self, ctx:CWScriptParser.StmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#stmt.
    def exitStmt(self, ctx:CWScriptParser.StmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ifStmt.
    def enterIfStmt(self, ctx:CWScriptParser.IfStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ifStmt.
    def exitIfStmt(self, ctx:CWScriptParser.IfStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#assnStmt.
    def enterAssnStmt(self, ctx:CWScriptParser.AssnStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#assnStmt.
    def exitAssnStmt(self, ctx:CWScriptParser.AssnStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#letStmt.
    def enterLetStmt(self, ctx:CWScriptParser.LetStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#letStmt.
    def exitLetStmt(self, ctx:CWScriptParser.LetStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#returnStmt.
    def enterReturnStmt(self, ctx:CWScriptParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#returnStmt.
    def exitReturnStmt(self, ctx:CWScriptParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#failStmt.
    def enterFailStmt(self, ctx:CWScriptParser.FailStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#failStmt.
    def exitFailStmt(self, ctx:CWScriptParser.FailStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#logStmt.
    def enterLogStmt(self, ctx:CWScriptParser.LogStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#logStmt.
    def exitLogStmt(self, ctx:CWScriptParser.LogStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#sendStmt.
    def enterSendStmt(self, ctx:CWScriptParser.SendStmtContext):
        pass

    # Exit a parse tree produced by CWScriptParser#sendStmt.
    def exitSendStmt(self, ctx:CWScriptParser.SendStmtContext):
        pass


    # Enter a parse tree produced by CWScriptParser#fnArgs.
    def enterFnArgs(self, ctx:CWScriptParser.FnArgsContext):
        pass

    # Exit a parse tree produced by CWScriptParser#fnArgs.
    def exitFnArgs(self, ctx:CWScriptParser.FnArgsContext):
        pass


    # Enter a parse tree produced by CWScriptParser#NullValExpr.
    def enterNullValExpr(self, ctx:CWScriptParser.NullValExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#NullValExpr.
    def exitNullValExpr(self, ctx:CWScriptParser.NullValExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#IdentExpr.
    def enterIdentExpr(self, ctx:CWScriptParser.IdentExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#IdentExpr.
    def exitIdentExpr(self, ctx:CWScriptParser.IdentExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#QueryExpr.
    def enterQueryExpr(self, ctx:CWScriptParser.QueryExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#QueryExpr.
    def exitQueryExpr(self, ctx:CWScriptParser.QueryExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#LitExpr.
    def enterLitExpr(self, ctx:CWScriptParser.LitExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#LitExpr.
    def exitLitExpr(self, ctx:CWScriptParser.LitExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#TypeCheckExpr.
    def enterTypeCheckExpr(self, ctx:CWScriptParser.TypeCheckExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#TypeCheckExpr.
    def exitTypeCheckExpr(self, ctx:CWScriptParser.TypeCheckExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#StructExpr.
    def enterStructExpr(self, ctx:CWScriptParser.StructExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#StructExpr.
    def exitStructExpr(self, ctx:CWScriptParser.StructExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#ArrayExp.
    def enterArrayExp(self, ctx:CWScriptParser.ArrayExpContext):
        pass

    # Exit a parse tree produced by CWScriptParser#ArrayExp.
    def exitArrayExp(self, ctx:CWScriptParser.ArrayExpContext):
        pass


    # Enter a parse tree produced by CWScriptParser#IndexExpr.
    def enterIndexExpr(self, ctx:CWScriptParser.IndexExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#IndexExpr.
    def exitIndexExpr(self, ctx:CWScriptParser.IndexExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#MemExpr.
    def enterMemExpr(self, ctx:CWScriptParser.MemExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#MemExpr.
    def exitMemExpr(self, ctx:CWScriptParser.MemExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#UnwrapExpr.
    def enterUnwrapExpr(self, ctx:CWScriptParser.UnwrapExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#UnwrapExpr.
    def exitUnwrapExpr(self, ctx:CWScriptParser.UnwrapExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#IsExpr.
    def enterIsExpr(self, ctx:CWScriptParser.IsExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#IsExpr.
    def exitIsExpr(self, ctx:CWScriptParser.IsExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#NullQExpr.
    def enterNullQExpr(self, ctx:CWScriptParser.NullQExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#NullQExpr.
    def exitNullQExpr(self, ctx:CWScriptParser.NullQExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#FnCallExpr.
    def enterFnCallExpr(self, ctx:CWScriptParser.FnCallExprContext):
        pass

    # Exit a parse tree produced by CWScriptParser#FnCallExpr.
    def exitFnCallExpr(self, ctx:CWScriptParser.FnCallExprContext):
        pass


    # Enter a parse tree produced by CWScriptParser#structMember.
    def enterStructMember(self, ctx:CWScriptParser.StructMemberContext):
        pass

    # Exit a parse tree produced by CWScriptParser#structMember.
    def exitStructMember(self, ctx:CWScriptParser.StructMemberContext):
        pass


    # Enter a parse tree produced by CWScriptParser#execDefn.
    def enterExecDefn(self, ctx:CWScriptParser.ExecDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#execDefn.
    def exitExecDefn(self, ctx:CWScriptParser.ExecDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#queryDefn.
    def enterQueryDefn(self, ctx:CWScriptParser.QueryDefnContext):
        pass

    # Exit a parse tree produced by CWScriptParser#queryDefn.
    def exitQueryDefn(self, ctx:CWScriptParser.QueryDefnContext):
        pass


    # Enter a parse tree produced by CWScriptParser#block.
    def enterBlock(self, ctx:CWScriptParser.BlockContext):
        pass

    # Exit a parse tree produced by CWScriptParser#block.
    def exitBlock(self, ctx:CWScriptParser.BlockContext):
        pass



del CWScriptParser