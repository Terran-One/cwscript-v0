grammar CWScript;

options {
  language=Python3;
}

// parser rules
program: topLevelStmt* EOF;

topLevelStmt:
  contractDefn;

contractDefn: CONTRACT name=ident LBRACE contractItem* RBRACE;

contractItem:
    stateBlock
    | instantiateDefn
    | execDefn
    | queryDefn
    | fnDefn
    | migrateDefn;

reservedKeyword:
    CONTRACT | LOG | INSTANTIATE | EXEC | QUERY | LET | IF | IS | ELSE | RETURN | STATE | FN;

ident: Ident | reservedKeyword;

stateBlock: STATE LBRACE stateItem+ RBRACE;
stateItem: itemDefn | mapDefn;
itemDefn: key=ident COLON ty=typeExpr;
mapDefn: prefix=ident LBRACK key=typeExpr RBRACK COLON ty=typeExpr;

typeExpr:
    ident # IdentT
    | typeExpr LT (typeExpr (COMMA typeExpr)*)? GT # ParamzdT
    | typeExpr QUESTION # OptionT
    | LPAREN typeExpr (COMMA typeExpr)* RPAREN # TupleT
    | typeExpr D_COLON ident # MemT
    | typeExpr LBRACK NumLiteral RBRACK # ListT;

instantiateDefn: INSTANTIATE fnParams fnBody;
migrateDefn: MIGRATE fnParams fnBody;
fnParams: LPAREN (params+=paramDefn (COMMA params+=paramDefn)*)? RPAREN;
fnBody: LBRACE stmt* RBRACE;
paramDefn: name=ident QUESTION? (COLON ty=typeExpr)?;

fnDefn: FN name=ident fnParams ARROW typeExpr fnBody;

stmt:
    ifStmt
    | assnStmt
    | letStmt
    | returnStmt
    | failStmt
    | logStmt
    | sendStmt;

ifStmt:
    IF pred=expr b_t=block (ELSE (ifStmt | block))?;
assnStmt:
    lhs=expr EQ rhs=expr;
letStmt:
    LET ident EQ expr;
returnStmt:
    RETURN expr;
failStmt:
    FAIL expr;
logStmt:
    LOG expr;
sendStmt:
    SEND expr (REPLY fnParams ON ident fnBody)*;

fnArgs: LPAREN (args+=expr (COMMA args+=expr)*)? RPAREN;

expr:
    expr DOT ident # MemExpr
    | expr IS typeExpr # TypeCheckExpr
    | expr (EQ_EQ | NEQ) expr # IsExpr
    | expr D_QUE expr       #NullValExpr
    | QUERY expr # QueryExpr
    | typeExpr? LBRACE (structMember (COMMA structMember COMMA?)* COMMA?)? RBRACE # StructExpr
    | expr fnArgs # FnCallExpr
    | expr BANG # UnwrapExpr
    | expr QUESTION # NullQExpr
    | expr LBRACK expr RBRACK # IndexExpr
    | (StrLiteral | NumLiteral) # LitExpr
    | LBRACK (expr (COMMA expr)*)? RBRACK #ArrayExp
    | ident # IdentExpr;

structMember: ident COLON expr | ident;
execDefn: EXEC ident fnParams fnBody;
queryDefn: QUERY ident fnParams (ARROW typeExpr)? fnBody;
block: LBRACE stmt* RBRACE;


WS: [ \t\r\n] -> channel(HIDDEN);
COMMENT:'//' ~[\r\n\u2028\u2029]* -> skip;

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';
D_COLON: '::';
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
D_QUE: '??';


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

NumLiteral: [0-9]+;
StrLiteral: '"' ~["]* '"';
Ident: [a-zA-Z_] [a-zA-Z_0-9]*;
