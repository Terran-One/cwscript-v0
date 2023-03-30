from typing import List, Any
from dataclasses import dataclass

Expr = Any
TypeExpr = Any


class AST:
    pass


@dataclass
class ContractDefn(AST):
    name: str
    items: List[Any]


@dataclass
class StateBlock(AST):
    items: List[Any]


@dataclass
class StateItem(AST):
    key: str
    val_ty: Any  # TypeExpr


@dataclass
class StateMap(AST):
    prefix: str
    key: str
    val_ty: TypeExpr


@dataclass
class InstantiateDefn(AST):
    params: List[Any]
    body: List[Any]


@dataclass
class IfStmt(AST):
    pred: Any
    b_t: Any
    b_n: Any
    b_f: Any


@dataclass
class FnDefn(AST):
    name: str
    params: List[Any]
    ret_ty: TypeExpr
    body: List[Any]


class ExecDefn(FnDefn):
    pass


class QueryDefn(FnDefn):
    pass


class MigrateDefn(InstantiateDefn):
    pass


@dataclass
class LetStmt(AST):
    sym: str
    val: Expr


@dataclass
class AssnStmt(AST):
    lhs: Expr
    rhs: Expr


@dataclass
class QueryExpr(AST):
    arg: Expr


@dataclass
class ReturnStmt(AST):
    arg: Expr


@dataclass
class FnCallExpr(AST):
    fn: Expr
    args: List[Expr]


@dataclass
class NoneQExpr(AST):
    """arg?"""

    arg: Expr


@dataclass
class UnwrapExpr(AST):
    """arg!"""

    arg: Expr


@dataclass
class FailStmt(AST):
    arg: Expr


@dataclass
class LogStmt(AST):
    arg: Expr


@dataclass
class IndexExpr(AST):
    """<obj>[key]"""

    obj: Expr
    key: Expr


@dataclass
class MemExpr(AST):
    """<obj>.<key>"""

    obj: Expr
    key: str


@dataclass
class StrLiteral(AST):
    val: str


@dataclass
class IntLiteral(AST):
    val: str


@dataclass
class BinOpExpr(AST):
    op: str
    lhs: Expr
    rhs: Expr


@dataclass
class IsExpr(AST):
    lhs: any
    rhs: any


@dataclass
class SendStmt(AST):
    arg: Expr
    replies: List[Any]


@dataclass
class StructExpr(AST):
    ty: TypeExpr
    members: List[Any]
