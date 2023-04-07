grammar CWScript;

options {
	language = Python3;
}

// parser rules
program: topLevelStmt* EOF;
compilationUnit: topLevelStmt* EOF;

namespace: ident D_COLON;
topLevelStmt: contractDefn | interfaceDefn | importStmt;

contractDefn:
    CONTRACT name = ident (IMPLEMENTS ifaces = pathList)? (EXTENDS ident)? LBRACE contractItem* RBRACE;

interfaceDefn:
	INTERFACE name = ident LBRACE interfaceItem* RBRACE;

importStmt: IMPORT;

path:
	root = D_COLON? (segments += ident) (
		D_COLON segments += ident
	)*;

pathList: paths += path (COMMA paths += path)*;

contractItem:
	stateBlock
	| instantiateDefn
	| execDefn
	| queryDefn
	| fnDefn
	| migrateDefn;

interfaceItem: instantiateDecl | execDecl | queryDecl | fnDecl | structDefn;

instantiateDecl: INSTANTIATE fnParams;

execDecl: EXEC ident fnParams;

queryDecl: QUERY ident fnParams (ARROW typeExpr)?;

fnDecl: FN ident fnParams ARROW typeExpr;

reservedKeyword:
	CONTRACT
	| LOG
	| INSTANTIATE
	| EXEC
	| QUERY
	| LET
	| IF
	| IS
	| ELSE
	| RETURN
	| STATE
	| FN
	| NONE;

ident: Ident | reservedKeyword;

stateBlock: STATE LBRACE stateItem+ RBRACE;
stateItem: itemDefn | mapDefn;
itemDefn: key = ident COLON ty = typeExpr;
mapDefn:
	prefix = ident LBRACK key = typeExpr RBRACK COLON ty = typeExpr;

typeExpr:
	path											# IdentT
	| typeExpr LT (typeExpr (COMMA typeExpr)*)? GT	# ParamzdT
	| typeExpr QUESTION								# OptionT
	| LPAREN typeExpr (COMMA typeExpr)* RPAREN		# TupleT
	| typeExpr D_COLON ident						# MemT
	| typeExpr LBRACK NumLiteral? RBRACK			# ListT
	| structDefn                                    # StructT
	| NONE                                          # None;

instantiateDefn: INSTANTIATE fnParams fnBody;
migrateDefn: MIGRATE fnParams fnBody;
fnDefn: FN name = ident fnParams? (ARROW typeExpr)? fnBody?;
fnParams: LPAREN (params+=paramDefn (COMMA params+=paramDefn)*)? RPAREN | LPAREN RPAREN;
fnBody: LBRACE RBRACE | LBRACE stmt* RBRACE;
paramDefn: name = ident QUESTION? (COLON ty = typeExpr)?;
fnCallArgs: LPAREN (args += expr (COMMA args += expr)*)? RPAREN;

stmt:
	ifStmt
	| assnStmt
	| expr INC   
	| letStmt
	| returnStmt
	| failStmt
	| forStmt
	| logStmt
	| sendStmt
	| arrayMethodCallStmt
	| tryCatchStmt;

tryCatchStmt: TRY block (CATCH LPAREN ident RPAREN block)?;
arrayMethodCallStmt: expr DOT ident LPAREN (expr (COMMA expr)*)? RPAREN;
literal: StrLiteral | NumLiteral;
ifStmt: IF pred = orExpr b_t = block (ELSE (ifStmt | block))?
    | IF LPAREN letStmt RPAREN pred = orExpr b_t = block (ELSE (ifStmt | block))?;
orExpr: andExpr (OR andExpr)*;
andExpr: equalityExpr (AND equalityExpr)*;
equalityExpr: relationExpr (EQ_EQ relationExpr | NEQ relationExpr)*;
relationExpr: additionExpr ((GT | LT | GT_EQ | LT_EQ) additionExpr)*;
additionExpr: multiplicationExpr ((PLUS | MINUS) multiplicationExpr)*;
multiplicationExpr: unaryExpr ((MULT | DIV | MOD) unaryExpr)*;
unaryExpr: (BANG | MINUS | NOT)? primaryExpr;
primaryExpr: LPAREN expr RPAREN | literal | Ident | expr (QUESTION DOT Ident fnCallArgs?)?;
assnStmt: lhs = expr (EQ | INC | DEC | HASH_MINUS_EQ | HASH_PLUS_EQ) TRY? rhs = expr SEMI_COLON?;
letStmt: LET lhs = ident EQ rhs = letRhs;
lambdaExpr: ident FATARROW expr | fnArgs FATARROW expr;
letRhs: (expr | nullQExpr | fnDecl | nullCoalescingExpr | letRhsBody);
nullCoalescingExpr: expr D_QUE (expr | lambdaExpr) | expr D_QUE expr;
nullLambdaExpr: D_QUE lambdaExpr;
letRhsBody: expr (ARROW structDefn)? | tupleExpr SEMI_COLON?;
tupleExpr: LPAREN (expr (COMMA expr)*)? RPAREN;
nullQExpr: expr QUESTION;
structDefn: STRUCT name = ident? LBRACE structField* RBRACE;
structField: ident (QUESTION)? COLON typeExpr (COMMA)?;
returnStmt: RETURN expr;
failStmt: FAIL expr;
forStmt: FOR ident IN expr b_t = block;
logStmt: LOG ident? fnCallArgs? expr?;
sendStmt: SEND expr (REPLY fnParams ON ident fnBody)*;
fnArgs: LPAREN (args += expr (COMMA args += expr)*)? RPAREN;
expr:
    expr DOT ident                                        # MemExpr
    | expr D_COLON ident                                   # NamespaceExpr
    | expr D_COLON ident LPAREN (expr (COMMA expr)*)? RPAREN # MethodCallExpr
    | expr IS typeExpr                                     # TypeCheckExpr
    | expr (EQ_EQ | NEQ) expr                              # IsExpr
    | expr D_QUE expr                                      # NullCoalesceExpr
    | QUERY expr                                           # QueryExpr
    | typeExpr? LBRACE (structMember (COMMA structMember COMMA?)*)? RBRACE # StructExpr
    | expr fnArgs                                          # FnCallExpr
    | expr BANG                                            # UnwrapExpr
    | expr QUESTION                                        # nullValExpr
    | expr LBRACK expr RBRACK                               # IndexExpr
    | (StrLiteral | NumLiteral)                             # LitExpr
    | LBRACK (expr (COMMA expr)*)? RBRACK                   # ArrayExp
    | expr HASH MINUS EQ expr                               # CheckSubExp
    | ident                                                 # IdentExp
    | expr DOT ident fnArgs                                 # MethodCallExpr
    | expr DOT MAP LPAREN ident FATARROW expr (COMMA ident FATARROW expr)* RPAREN # MapExpr
    | expr FATARROW fnBody                                  # ArrowFnCallExpr
    | expr DOT ident fnCallArgs?                            # MemberFnCallExpr
    | expr LBRACK expr RBRACK DOT ident fnArgs              # IndexMethodCallExpr;

structMember: ident COLON expr | ident;
execDefn: EXEC ident fnParams fnBody;
queryDefn: QUERY ident fnParams (ARROW typeExpr)? fnBody;
block: LBRACE stmt* RBRACE;


WS: [ \t\r\n] -> channel(HIDDEN);
COMMENT: '//' ~[\r\n\u2028\u2029]* -> skip;

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';
D_COLON: '::';
SEMI_COLON: ';';
COLON: ':';
EQ_EQ: '==';
NEQ: '!=';
EQ: '=';
DOT: '.';
QUESTION: '?';
BANG: '!';
D_QUOTE: '"';
QUOTE: '\'';
BACKTICK: '`';
DOLLAR: '$';
ARROW: '->';
FATARROW: '=>';
D_QUE: '??';
HASH:  '#';
INC: '+=';
DEC: '-=';
GT_EQ: '>=';
LT_EQ: '<=';
HASH_MINUS_EQ: '#-=';
HASH_PLUS_EQ: '#+=';

// punctuation

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
LT: '<';
GT: '>';

// keywords

CONTRACT: 'contract';
IMPLEMENTS: 'implements';
EXTENDS: 'extends';
IMPORT: 'import';
INTERFACE: 'interface';
FOR: 'for';
IN: 'in';
LOG: 'log';
INSTANTIATE: 'instantiate';
MIGRATE: 'migrate';
EXEC: 'exec';
QUERY: 'query';
LET: 'let';
IF: 'if';
IS: 'is';
ELSE: 'else';
RETURN: 'return';
STATE: 'state';
FAIL: 'fail';
FN: 'fn';
SEND: 'send';
REPLY: 'reply';
ON: 'on';
STRUCT: 'struct';
NONE: 'none';
MAP: 'map';
AND: 'and' | 'AND';
OR: 'or' | 'OR';
NOT: 'not';
TRY: 'try';
CATCH: 'catch';

NumLiteral: [0-9]+;
StrLiteral: '"' ~["]* '"';
Ident: [a-zA-Z_] [a-zA-Z_0-9]*;