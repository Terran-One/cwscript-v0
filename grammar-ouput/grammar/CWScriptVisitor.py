# Generated from grammar/CWScript.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CWScriptParser import CWScriptParser
else:
    from CWScriptParser import CWScriptParser

# This class defines a complete generic visitor for a parse tree produced by CWScriptParser.

class CWScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CWScriptParser#program.
    def visitProgram(self, ctx:CWScriptParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#topLevelStmt.
    def visitTopLevelStmt(self, ctx:CWScriptParser.TopLevelStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#contractDefn.
    def visitContractDefn(self, ctx:CWScriptParser.ContractDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#contractItem.
    def visitContractItem(self, ctx:CWScriptParser.ContractItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#reservedKeyword.
    def visitReservedKeyword(self, ctx:CWScriptParser.ReservedKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ident.
    def visitIdent(self, ctx:CWScriptParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#stateBlock.
    def visitStateBlock(self, ctx:CWScriptParser.StateBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#stateItem.
    def visitStateItem(self, ctx:CWScriptParser.StateItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#itemDefn.
    def visitItemDefn(self, ctx:CWScriptParser.ItemDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#mapDefn.
    def visitMapDefn(self, ctx:CWScriptParser.MapDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#TupleT.
    def visitTupleT(self, ctx:CWScriptParser.TupleTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ParamzdT.
    def visitParamzdT(self, ctx:CWScriptParser.ParamzdTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#OptionT.
    def visitOptionT(self, ctx:CWScriptParser.OptionTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#IdentT.
    def visitIdentT(self, ctx:CWScriptParser.IdentTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ListT.
    def visitListT(self, ctx:CWScriptParser.ListTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#MemT.
    def visitMemT(self, ctx:CWScriptParser.MemTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#instantiateDefn.
    def visitInstantiateDefn(self, ctx:CWScriptParser.InstantiateDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#migrateDefn.
    def visitMigrateDefn(self, ctx:CWScriptParser.MigrateDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#fnParams.
    def visitFnParams(self, ctx:CWScriptParser.FnParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#fnBody.
    def visitFnBody(self, ctx:CWScriptParser.FnBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#paramDefn.
    def visitParamDefn(self, ctx:CWScriptParser.ParamDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#fnDefn.
    def visitFnDefn(self, ctx:CWScriptParser.FnDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#stmt.
    def visitStmt(self, ctx:CWScriptParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ifStmt.
    def visitIfStmt(self, ctx:CWScriptParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#assnStmt.
    def visitAssnStmt(self, ctx:CWScriptParser.AssnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#letStmt.
    def visitLetStmt(self, ctx:CWScriptParser.LetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#returnStmt.
    def visitReturnStmt(self, ctx:CWScriptParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#failStmt.
    def visitFailStmt(self, ctx:CWScriptParser.FailStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#logStmt.
    def visitLogStmt(self, ctx:CWScriptParser.LogStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#sendStmt.
    def visitSendStmt(self, ctx:CWScriptParser.SendStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#fnArgs.
    def visitFnArgs(self, ctx:CWScriptParser.FnArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#NullValExpr.
    def visitNullValExpr(self, ctx:CWScriptParser.NullValExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#IdentExpr.
    def visitIdentExpr(self, ctx:CWScriptParser.IdentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#QueryExpr.
    def visitQueryExpr(self, ctx:CWScriptParser.QueryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#LitExpr.
    def visitLitExpr(self, ctx:CWScriptParser.LitExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#TypeCheckExpr.
    def visitTypeCheckExpr(self, ctx:CWScriptParser.TypeCheckExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#StructExpr.
    def visitStructExpr(self, ctx:CWScriptParser.StructExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#ArrayExp.
    def visitArrayExp(self, ctx:CWScriptParser.ArrayExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#IndexExpr.
    def visitIndexExpr(self, ctx:CWScriptParser.IndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#MemExpr.
    def visitMemExpr(self, ctx:CWScriptParser.MemExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#UnwrapExpr.
    def visitUnwrapExpr(self, ctx:CWScriptParser.UnwrapExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#IsExpr.
    def visitIsExpr(self, ctx:CWScriptParser.IsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#NullQExpr.
    def visitNullQExpr(self, ctx:CWScriptParser.NullQExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#FnCallExpr.
    def visitFnCallExpr(self, ctx:CWScriptParser.FnCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#structMember.
    def visitStructMember(self, ctx:CWScriptParser.StructMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#execDefn.
    def visitExecDefn(self, ctx:CWScriptParser.ExecDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#queryDefn.
    def visitQueryDefn(self, ctx:CWScriptParser.QueryDefnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CWScriptParser#block.
    def visitBlock(self, ctx:CWScriptParser.BlockContext):
        return self.visitChildren(ctx)



del CWScriptParser