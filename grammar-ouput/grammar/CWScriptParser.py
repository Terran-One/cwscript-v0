# Generated from grammar/CWScript.g4 by ANTLR 4.12.0
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
        4,1,50,370,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,5,0,64,8,0,10,0,12,0,
        67,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,5,2,77,8,2,10,2,12,2,80,9,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,90,8,3,1,4,1,4,1,5,1,5,3,5,
        96,8,5,1,6,1,6,1,6,4,6,101,8,6,11,6,12,6,102,1,6,1,6,1,7,1,7,3,7,
        109,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,10,1,10,5,10,128,8,10,10,10,12,10,131,9,10,1,10,1,10,3,
        10,135,8,10,1,10,1,10,1,10,1,10,1,10,5,10,142,8,10,10,10,12,10,145,
        9,10,3,10,147,8,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,5,10,159,8,10,10,10,12,10,162,9,10,1,11,1,11,1,11,1,11,1,12,
        1,12,1,12,1,12,1,13,1,13,1,13,1,13,5,13,176,8,13,10,13,12,13,179,
        9,13,3,13,181,8,13,1,13,1,13,1,14,1,14,5,14,187,8,14,10,14,12,14,
        190,9,14,1,14,1,14,1,15,1,15,3,15,196,8,15,1,15,1,15,3,15,200,8,
        15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,3,17,216,8,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,224,8,18,
        3,18,226,8,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,21,
        1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,5,24,254,8,24,10,24,12,24,257,9,24,1,25,1,25,1,25,
        1,25,5,25,263,8,25,10,25,12,25,266,9,25,3,25,268,8,25,1,25,1,25,
        1,26,1,26,1,26,1,26,3,26,276,8,26,1,26,1,26,1,26,1,26,1,26,3,26,
        283,8,26,5,26,285,8,26,10,26,12,26,288,9,26,1,26,3,26,291,8,26,3,
        26,293,8,26,1,26,1,26,1,26,1,26,1,26,1,26,5,26,301,8,26,10,26,12,
        26,304,9,26,3,26,306,8,26,1,26,1,26,3,26,310,8,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,5,26,335,8,26,10,26,12,26,338,
        9,26,1,27,1,27,1,27,1,27,1,27,3,27,345,8,27,1,28,1,28,1,28,1,28,
        1,28,1,29,1,29,1,29,1,29,1,29,3,29,357,8,29,1,29,1,29,1,30,1,30,
        5,30,363,8,30,10,30,12,30,366,9,30,1,30,1,30,1,30,0,2,20,52,31,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,56,58,60,0,3,3,0,31,33,35,42,44,44,1,0,48,49,1,0,12,
        13,394,0,65,1,0,0,0,2,70,1,0,0,0,4,72,1,0,0,0,6,89,1,0,0,0,8,91,
        1,0,0,0,10,95,1,0,0,0,12,97,1,0,0,0,14,108,1,0,0,0,16,110,1,0,0,
        0,18,114,1,0,0,0,20,134,1,0,0,0,22,163,1,0,0,0,24,167,1,0,0,0,26,
        171,1,0,0,0,28,184,1,0,0,0,30,193,1,0,0,0,32,201,1,0,0,0,34,215,
        1,0,0,0,36,217,1,0,0,0,38,227,1,0,0,0,40,231,1,0,0,0,42,236,1,0,
        0,0,44,239,1,0,0,0,46,242,1,0,0,0,48,245,1,0,0,0,50,258,1,0,0,0,
        52,309,1,0,0,0,54,344,1,0,0,0,56,346,1,0,0,0,58,351,1,0,0,0,60,360,
        1,0,0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,
        65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,68,69,5,0,0,1,69,1,1,0,
        0,0,70,71,3,4,2,0,71,3,1,0,0,0,72,73,5,31,0,0,73,74,3,10,5,0,74,
        78,5,5,0,0,75,77,3,6,3,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,
        0,78,79,1,0,0,0,79,81,1,0,0,0,80,78,1,0,0,0,81,82,5,6,0,0,82,5,1,
        0,0,0,83,90,3,12,6,0,84,90,3,22,11,0,85,90,3,56,28,0,86,90,3,58,
        29,0,87,90,3,32,16,0,88,90,3,24,12,0,89,83,1,0,0,0,89,84,1,0,0,0,
        89,85,1,0,0,0,89,86,1,0,0,0,89,87,1,0,0,0,89,88,1,0,0,0,90,7,1,0,
        0,0,91,92,7,0,0,0,92,9,1,0,0,0,93,96,5,50,0,0,94,96,3,8,4,0,95,93,
        1,0,0,0,95,94,1,0,0,0,96,11,1,0,0,0,97,98,5,42,0,0,98,100,5,5,0,
        0,99,101,3,14,7,0,100,99,1,0,0,0,101,102,1,0,0,0,102,100,1,0,0,0,
        102,103,1,0,0,0,103,104,1,0,0,0,104,105,5,6,0,0,105,13,1,0,0,0,106,
        109,3,16,8,0,107,109,3,18,9,0,108,106,1,0,0,0,108,107,1,0,0,0,109,
        15,1,0,0,0,110,111,3,10,5,0,111,112,5,11,0,0,112,113,3,20,10,0,113,
        17,1,0,0,0,114,115,3,10,5,0,115,116,5,7,0,0,116,117,3,20,10,0,117,
        118,5,8,0,0,118,119,5,11,0,0,119,120,3,20,10,0,120,19,1,0,0,0,121,
        122,6,10,-1,0,122,135,3,10,5,0,123,124,5,3,0,0,124,129,3,20,10,0,
        125,126,5,9,0,0,126,128,3,20,10,0,127,125,1,0,0,0,128,131,1,0,0,
        0,129,127,1,0,0,0,129,130,1,0,0,0,130,132,1,0,0,0,131,129,1,0,0,
        0,132,133,5,4,0,0,133,135,1,0,0,0,134,121,1,0,0,0,134,123,1,0,0,
        0,135,160,1,0,0,0,136,137,10,5,0,0,137,146,5,29,0,0,138,143,3,20,
        10,0,139,140,5,9,0,0,140,142,3,20,10,0,141,139,1,0,0,0,142,145,1,
        0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,147,1,0,0,0,145,143,1,
        0,0,0,146,138,1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,159,5,
        30,0,0,149,150,10,4,0,0,150,159,5,16,0,0,151,152,10,2,0,0,152,153,
        5,10,0,0,153,159,3,10,5,0,154,155,10,1,0,0,155,156,5,7,0,0,156,157,
        5,48,0,0,157,159,5,8,0,0,158,136,1,0,0,0,158,149,1,0,0,0,158,151,
        1,0,0,0,158,154,1,0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,
        1,0,0,0,161,21,1,0,0,0,162,160,1,0,0,0,163,164,5,33,0,0,164,165,
        3,26,13,0,165,166,3,28,14,0,166,23,1,0,0,0,167,168,5,34,0,0,168,
        169,3,26,13,0,169,170,3,28,14,0,170,25,1,0,0,0,171,180,5,3,0,0,172,
        177,3,30,15,0,173,174,5,9,0,0,174,176,3,30,15,0,175,173,1,0,0,0,
        176,179,1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,181,1,0,0,0,
        179,177,1,0,0,0,180,172,1,0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,
        182,183,5,4,0,0,183,27,1,0,0,0,184,188,5,5,0,0,185,187,3,34,17,0,
        186,185,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,
        189,191,1,0,0,0,190,188,1,0,0,0,191,192,5,6,0,0,192,29,1,0,0,0,193,
        195,3,10,5,0,194,196,5,16,0,0,195,194,1,0,0,0,195,196,1,0,0,0,196,
        199,1,0,0,0,197,198,5,11,0,0,198,200,3,20,10,0,199,197,1,0,0,0,199,
        200,1,0,0,0,200,31,1,0,0,0,201,202,5,44,0,0,202,203,3,10,5,0,203,
        204,3,26,13,0,204,205,5,22,0,0,205,206,3,20,10,0,206,207,3,28,14,
        0,207,33,1,0,0,0,208,216,3,36,18,0,209,216,3,38,19,0,210,216,3,40,
        20,0,211,216,3,42,21,0,212,216,3,44,22,0,213,216,3,46,23,0,214,216,
        3,48,24,0,215,208,1,0,0,0,215,209,1,0,0,0,215,210,1,0,0,0,215,211,
        1,0,0,0,215,212,1,0,0,0,215,213,1,0,0,0,215,214,1,0,0,0,216,35,1,
        0,0,0,217,218,5,38,0,0,218,219,3,52,26,0,219,225,3,60,30,0,220,223,
        5,40,0,0,221,224,3,36,18,0,222,224,3,60,30,0,223,221,1,0,0,0,223,
        222,1,0,0,0,224,226,1,0,0,0,225,220,1,0,0,0,225,226,1,0,0,0,226,
        37,1,0,0,0,227,228,3,52,26,0,228,229,5,14,0,0,229,230,3,52,26,0,
        230,39,1,0,0,0,231,232,5,37,0,0,232,233,3,10,5,0,233,234,5,14,0,
        0,234,235,3,52,26,0,235,41,1,0,0,0,236,237,5,41,0,0,237,238,3,52,
        26,0,238,43,1,0,0,0,239,240,5,43,0,0,240,241,3,52,26,0,241,45,1,
        0,0,0,242,243,5,32,0,0,243,244,3,52,26,0,244,47,1,0,0,0,245,246,
        5,45,0,0,246,255,3,52,26,0,247,248,5,46,0,0,248,249,3,26,13,0,249,
        250,5,47,0,0,250,251,3,10,5,0,251,252,3,28,14,0,252,254,1,0,0,0,
        253,247,1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,256,1,0,0,0,
        256,49,1,0,0,0,257,255,1,0,0,0,258,267,5,3,0,0,259,264,3,52,26,0,
        260,261,5,9,0,0,261,263,3,52,26,0,262,260,1,0,0,0,263,266,1,0,0,
        0,264,262,1,0,0,0,264,265,1,0,0,0,265,268,1,0,0,0,266,264,1,0,0,
        0,267,259,1,0,0,0,267,268,1,0,0,0,268,269,1,0,0,0,269,270,5,4,0,
        0,270,51,1,0,0,0,271,272,6,26,-1,0,272,273,5,36,0,0,273,310,3,52,
        26,9,274,276,3,20,10,0,275,274,1,0,0,0,275,276,1,0,0,0,276,277,1,
        0,0,0,277,292,5,5,0,0,278,286,3,54,27,0,279,280,5,9,0,0,280,282,
        3,54,27,0,281,283,5,9,0,0,282,281,1,0,0,0,282,283,1,0,0,0,283,285,
        1,0,0,0,284,279,1,0,0,0,285,288,1,0,0,0,286,284,1,0,0,0,286,287,
        1,0,0,0,287,290,1,0,0,0,288,286,1,0,0,0,289,291,5,9,0,0,290,289,
        1,0,0,0,290,291,1,0,0,0,291,293,1,0,0,0,292,278,1,0,0,0,292,293,
        1,0,0,0,293,294,1,0,0,0,294,310,5,6,0,0,295,310,7,1,0,0,296,305,
        5,7,0,0,297,302,3,52,26,0,298,299,5,9,0,0,299,301,3,52,26,0,300,
        298,1,0,0,0,301,304,1,0,0,0,302,300,1,0,0,0,302,303,1,0,0,0,303,
        306,1,0,0,0,304,302,1,0,0,0,305,297,1,0,0,0,305,306,1,0,0,0,306,
        307,1,0,0,0,307,310,5,8,0,0,308,310,3,10,5,0,309,271,1,0,0,0,309,
        275,1,0,0,0,309,295,1,0,0,0,309,296,1,0,0,0,309,308,1,0,0,0,310,
        336,1,0,0,0,311,312,10,11,0,0,312,313,7,2,0,0,313,335,3,52,26,12,
        314,315,10,10,0,0,315,316,5,23,0,0,316,335,3,52,26,11,317,318,10,
        13,0,0,318,319,5,15,0,0,319,335,3,10,5,0,320,321,10,12,0,0,321,322,
        5,39,0,0,322,335,3,20,10,0,323,324,10,7,0,0,324,335,3,50,25,0,325,
        326,10,6,0,0,326,335,5,17,0,0,327,328,10,5,0,0,328,335,5,16,0,0,
        329,330,10,4,0,0,330,331,5,7,0,0,331,332,3,52,26,0,332,333,5,8,0,
        0,333,335,1,0,0,0,334,311,1,0,0,0,334,314,1,0,0,0,334,317,1,0,0,
        0,334,320,1,0,0,0,334,323,1,0,0,0,334,325,1,0,0,0,334,327,1,0,0,
        0,334,329,1,0,0,0,335,338,1,0,0,0,336,334,1,0,0,0,336,337,1,0,0,
        0,337,53,1,0,0,0,338,336,1,0,0,0,339,340,3,10,5,0,340,341,5,11,0,
        0,341,342,3,52,26,0,342,345,1,0,0,0,343,345,3,10,5,0,344,339,1,0,
        0,0,344,343,1,0,0,0,345,55,1,0,0,0,346,347,5,35,0,0,347,348,3,10,
        5,0,348,349,3,26,13,0,349,350,3,28,14,0,350,57,1,0,0,0,351,352,5,
        36,0,0,352,353,3,10,5,0,353,356,3,26,13,0,354,355,5,22,0,0,355,357,
        3,20,10,0,356,354,1,0,0,0,356,357,1,0,0,0,357,358,1,0,0,0,358,359,
        3,28,14,0,359,59,1,0,0,0,360,364,5,5,0,0,361,363,3,34,17,0,362,361,
        1,0,0,0,363,366,1,0,0,0,364,362,1,0,0,0,364,365,1,0,0,0,365,367,
        1,0,0,0,366,364,1,0,0,0,367,368,5,6,0,0,368,61,1,0,0,0,36,65,78,
        89,95,102,108,129,134,143,146,158,160,177,180,188,195,199,215,223,
        225,255,264,267,275,282,286,290,292,302,305,309,334,336,344,356,
        364
    ]

class CWScriptParser ( Parser ):

    grammarFileName = "CWScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "','", "'::'", "':'", "'=='", 
                     "'!='", "'='", "'.'", "'?'", "'!'", "'\"'", "'''", 
                     "'`'", "'$'", "'->'", "'??'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'<'", "'>'", "'contract'", "'log'", 
                     "'instantiate'", "'migrate'", "'exec'", "'query'", 
                     "'let'", "'if'", "'is'", "'else'", "'return'", "'state'", 
                     "'fail'", "'fn'", "'send'", "'reply'", "'on'" ]

    symbolicNames = [ "<INVALID>", "WS", "COMMENT", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COMMA", "D_COLON", 
                      "COLON", "EQ_EQ", "NEQ", "EQ", "DOT", "QUESTION", 
                      "BANG", "D_QUOTE", "QUOTE", "BACKTICK", "DOLLAR", 
                      "ARROW", "D_QUE", "PLUS", "MINUS", "MULT", "DIV", 
                      "MOD", "LT", "GT", "CONTRACT", "LOG", "INSTANTIATE", 
                      "MIGRATE", "EXEC", "QUERY", "LET", "IF", "IS", "ELSE", 
                      "RETURN", "STATE", "FAIL", "FN", "SEND", "REPLY", 
                      "ON", "NumLiteral", "StrLiteral", "Ident" ]

    RULE_program = 0
    RULE_topLevelStmt = 1
    RULE_contractDefn = 2
    RULE_contractItem = 3
    RULE_reservedKeyword = 4
    RULE_ident = 5
    RULE_stateBlock = 6
    RULE_stateItem = 7
    RULE_itemDefn = 8
    RULE_mapDefn = 9
    RULE_typeExpr = 10
    RULE_instantiateDefn = 11
    RULE_migrateDefn = 12
    RULE_fnParams = 13
    RULE_fnBody = 14
    RULE_paramDefn = 15
    RULE_fnDefn = 16
    RULE_stmt = 17
    RULE_ifStmt = 18
    RULE_assnStmt = 19
    RULE_letStmt = 20
    RULE_returnStmt = 21
    RULE_failStmt = 22
    RULE_logStmt = 23
    RULE_sendStmt = 24
    RULE_fnArgs = 25
    RULE_expr = 26
    RULE_structMember = 27
    RULE_execDefn = 28
    RULE_queryDefn = 29
    RULE_block = 30

    ruleNames =  [ "program", "topLevelStmt", "contractDefn", "contractItem", 
                   "reservedKeyword", "ident", "stateBlock", "stateItem", 
                   "itemDefn", "mapDefn", "typeExpr", "instantiateDefn", 
                   "migrateDefn", "fnParams", "fnBody", "paramDefn", "fnDefn", 
                   "stmt", "ifStmt", "assnStmt", "letStmt", "returnStmt", 
                   "failStmt", "logStmt", "sendStmt", "fnArgs", "expr", 
                   "structMember", "execDefn", "queryDefn", "block" ]

    EOF = Token.EOF
    WS=1
    COMMENT=2
    LPAREN=3
    RPAREN=4
    LBRACE=5
    RBRACE=6
    LBRACK=7
    RBRACK=8
    COMMA=9
    D_COLON=10
    COLON=11
    EQ_EQ=12
    NEQ=13
    EQ=14
    DOT=15
    QUESTION=16
    BANG=17
    D_QUOTE=18
    QUOTE=19
    BACKTICK=20
    DOLLAR=21
    ARROW=22
    D_QUE=23
    PLUS=24
    MINUS=25
    MULT=26
    DIV=27
    MOD=28
    LT=29
    GT=30
    CONTRACT=31
    LOG=32
    INSTANTIATE=33
    MIGRATE=34
    EXEC=35
    QUERY=36
    LET=37
    IF=38
    IS=39
    ELSE=40
    RETURN=41
    STATE=42
    FAIL=43
    FN=44
    SEND=45
    REPLY=46
    ON=47
    NumLiteral=48
    StrLiteral=49
    Ident=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CWScriptParser.EOF, 0)

        def topLevelStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.TopLevelStmtContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.TopLevelStmtContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CWScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 62
                self.topLevelStmt()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(CWScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopLevelStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def contractDefn(self):
            return self.getTypedRuleContext(CWScriptParser.ContractDefnContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_topLevelStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopLevelStmt" ):
                listener.enterTopLevelStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopLevelStmt" ):
                listener.exitTopLevelStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopLevelStmt" ):
                return visitor.visitTopLevelStmt(self)
            else:
                return visitor.visitChildren(self)




    def topLevelStmt(self):

        localctx = CWScriptParser.TopLevelStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_topLevelStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.contractDefn()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContractDefnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentContext

        def CONTRACT(self):
            return self.getToken(CWScriptParser.CONTRACT, 0)

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def contractItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ContractItemContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ContractItemContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_contractDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContractDefn" ):
                listener.enterContractDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContractDefn" ):
                listener.exitContractDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContractDefn" ):
                return visitor.visitContractDefn(self)
            else:
                return visitor.visitChildren(self)




    def contractDefn(self):

        localctx = CWScriptParser.ContractDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_contractDefn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(CWScriptParser.CONTRACT)
            self.state = 73
            localctx.name = self.ident()
            self.state = 74
            self.match(CWScriptParser.LBRACE)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 22119081574400) != 0):
                self.state = 75
                self.contractItem()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContractItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stateBlock(self):
            return self.getTypedRuleContext(CWScriptParser.StateBlockContext,0)


        def instantiateDefn(self):
            return self.getTypedRuleContext(CWScriptParser.InstantiateDefnContext,0)


        def execDefn(self):
            return self.getTypedRuleContext(CWScriptParser.ExecDefnContext,0)


        def queryDefn(self):
            return self.getTypedRuleContext(CWScriptParser.QueryDefnContext,0)


        def fnDefn(self):
            return self.getTypedRuleContext(CWScriptParser.FnDefnContext,0)


        def migrateDefn(self):
            return self.getTypedRuleContext(CWScriptParser.MigrateDefnContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_contractItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContractItem" ):
                listener.enterContractItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContractItem" ):
                listener.exitContractItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContractItem" ):
                return visitor.visitContractItem(self)
            else:
                return visitor.visitChildren(self)




    def contractItem(self):

        localctx = CWScriptParser.ContractItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_contractItem)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.stateBlock()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.instantiateDefn()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.execDefn()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.queryDefn()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.fnDefn()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 6)
                self.state = 88
                self.migrateDefn()
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


    class ReservedKeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTRACT(self):
            return self.getToken(CWScriptParser.CONTRACT, 0)

        def LOG(self):
            return self.getToken(CWScriptParser.LOG, 0)

        def INSTANTIATE(self):
            return self.getToken(CWScriptParser.INSTANTIATE, 0)

        def EXEC(self):
            return self.getToken(CWScriptParser.EXEC, 0)

        def QUERY(self):
            return self.getToken(CWScriptParser.QUERY, 0)

        def LET(self):
            return self.getToken(CWScriptParser.LET, 0)

        def IF(self):
            return self.getToken(CWScriptParser.IF, 0)

        def IS(self):
            return self.getToken(CWScriptParser.IS, 0)

        def ELSE(self):
            return self.getToken(CWScriptParser.ELSE, 0)

        def RETURN(self):
            return self.getToken(CWScriptParser.RETURN, 0)

        def STATE(self):
            return self.getToken(CWScriptParser.STATE, 0)

        def FN(self):
            return self.getToken(CWScriptParser.FN, 0)

        def getRuleIndex(self):
            return CWScriptParser.RULE_reservedKeyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReservedKeyword" ):
                listener.enterReservedKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReservedKeyword" ):
                listener.exitReservedKeyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReservedKeyword" ):
                return visitor.visitReservedKeyword(self)
            else:
                return visitor.visitChildren(self)




    def reservedKeyword(self):

        localctx = CWScriptParser.ReservedKeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_reservedKeyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 26368951713792) != 0)):
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


    class IdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ident(self):
            return self.getToken(CWScriptParser.Ident, 0)

        def reservedKeyword(self):
            return self.getTypedRuleContext(CWScriptParser.ReservedKeywordContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdent" ):
                return visitor.visitIdent(self)
            else:
                return visitor.visitChildren(self)




    def ident(self):

        localctx = CWScriptParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ident)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(CWScriptParser.Ident)
                pass
            elif token in [31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.reservedKeyword()
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


    class StateBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATE(self):
            return self.getToken(CWScriptParser.STATE, 0)

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def stateItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.StateItemContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.StateItemContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_stateBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateBlock" ):
                listener.enterStateBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateBlock" ):
                listener.exitStateBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateBlock" ):
                return visitor.visitStateBlock(self)
            else:
                return visitor.visitChildren(self)




    def stateBlock(self):

        localctx = CWScriptParser.StateBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stateBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(CWScriptParser.STATE)
            self.state = 98
            self.match(CWScriptParser.LBRACE)
            self.state = 100 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 99
                self.stateItem()
                self.state = 102 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1152268858556416) != 0)):
                    break

            self.state = 104
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def itemDefn(self):
            return self.getTypedRuleContext(CWScriptParser.ItemDefnContext,0)


        def mapDefn(self):
            return self.getTypedRuleContext(CWScriptParser.MapDefnContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_stateItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateItem" ):
                listener.enterStateItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateItem" ):
                listener.exitStateItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateItem" ):
                return visitor.visitStateItem(self)
            else:
                return visitor.visitChildren(self)




    def stateItem(self):

        localctx = CWScriptParser.StateItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stateItem)
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.itemDefn()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.mapDefn()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemDefnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.key = None # IdentContext
            self.ty = None # TypeExprContext

        def COLON(self):
            return self.getToken(CWScriptParser.COLON, 0)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_itemDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItemDefn" ):
                listener.enterItemDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItemDefn" ):
                listener.exitItemDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItemDefn" ):
                return visitor.visitItemDefn(self)
            else:
                return visitor.visitChildren(self)




    def itemDefn(self):

        localctx = CWScriptParser.ItemDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_itemDefn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            localctx.key = self.ident()
            self.state = 111
            self.match(CWScriptParser.COLON)
            self.state = 112
            localctx.ty = self.typeExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapDefnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.prefix = None # IdentContext
            self.key = None # TypeExprContext
            self.ty = None # TypeExprContext

        def LBRACK(self):
            return self.getToken(CWScriptParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(CWScriptParser.RBRACK, 0)

        def COLON(self):
            return self.getToken(CWScriptParser.COLON, 0)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def typeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.TypeExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.TypeExprContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_mapDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapDefn" ):
                listener.enterMapDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapDefn" ):
                listener.exitMapDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapDefn" ):
                return visitor.visitMapDefn(self)
            else:
                return visitor.visitChildren(self)




    def mapDefn(self):

        localctx = CWScriptParser.MapDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_mapDefn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            localctx.prefix = self.ident()
            self.state = 115
            self.match(CWScriptParser.LBRACK)
            self.state = 116
            localctx.key = self.typeExpr(0)
            self.state = 117
            self.match(CWScriptParser.RBRACK)
            self.state = 118
            self.match(CWScriptParser.COLON)
            self.state = 119
            localctx.ty = self.typeExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CWScriptParser.RULE_typeExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TupleTContext(TypeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.TypeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(CWScriptParser.LPAREN, 0)
        def typeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.TypeExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.TypeExprContext,i)

        def RPAREN(self):
            return self.getToken(CWScriptParser.RPAREN, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTupleT" ):
                listener.enterTupleT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTupleT" ):
                listener.exitTupleT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTupleT" ):
                return visitor.visitTupleT(self)
            else:
                return visitor.visitChildren(self)


    class ParamzdTContext(TypeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.TypeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def typeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.TypeExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.TypeExprContext,i)

        def LT(self):
            return self.getToken(CWScriptParser.LT, 0)
        def GT(self):
            return self.getToken(CWScriptParser.GT, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamzdT" ):
                listener.enterParamzdT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamzdT" ):
                listener.exitParamzdT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamzdT" ):
                return visitor.visitParamzdT(self)
            else:
                return visitor.visitChildren(self)


    class OptionTContext(TypeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.TypeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)

        def QUESTION(self):
            return self.getToken(CWScriptParser.QUESTION, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionT" ):
                listener.enterOptionT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionT" ):
                listener.exitOptionT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptionT" ):
                return visitor.visitOptionT(self)
            else:
                return visitor.visitChildren(self)


    class IdentTContext(TypeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.TypeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentT" ):
                listener.enterIdentT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentT" ):
                listener.exitIdentT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentT" ):
                return visitor.visitIdentT(self)
            else:
                return visitor.visitChildren(self)


    class ListTContext(TypeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.TypeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)

        def LBRACK(self):
            return self.getToken(CWScriptParser.LBRACK, 0)
        def NumLiteral(self):
            return self.getToken(CWScriptParser.NumLiteral, 0)
        def RBRACK(self):
            return self.getToken(CWScriptParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListT" ):
                listener.enterListT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListT" ):
                listener.exitListT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListT" ):
                return visitor.visitListT(self)
            else:
                return visitor.visitChildren(self)


    class MemTContext(TypeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.TypeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)

        def D_COLON(self):
            return self.getToken(CWScriptParser.D_COLON, 0)
        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemT" ):
                listener.enterMemT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemT" ):
                listener.exitMemT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemT" ):
                return visitor.visitMemT(self)
            else:
                return visitor.visitChildren(self)



    def typeExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CWScriptParser.TypeExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_typeExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 44, 50]:
                localctx = CWScriptParser.IdentTContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 122
                self.ident()
                pass
            elif token in [3]:
                localctx = CWScriptParser.TupleTContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 123
                self.match(CWScriptParser.LPAREN)
                self.state = 124
                self.typeExpr(0)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 125
                    self.match(CWScriptParser.COMMA)
                    self.state = 126
                    self.typeExpr(0)
                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 132
                self.match(CWScriptParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 158
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = CWScriptParser.ParamzdTContext(self, CWScriptParser.TypeExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typeExpr)
                        self.state = 136
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 137
                        self.match(CWScriptParser.LT)
                        self.state = 146
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1152268858556424) != 0):
                            self.state = 138
                            self.typeExpr(0)
                            self.state = 143
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==9:
                                self.state = 139
                                self.match(CWScriptParser.COMMA)
                                self.state = 140
                                self.typeExpr(0)
                                self.state = 145
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 148
                        self.match(CWScriptParser.GT)
                        pass

                    elif la_ == 2:
                        localctx = CWScriptParser.OptionTContext(self, CWScriptParser.TypeExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typeExpr)
                        self.state = 149
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 150
                        self.match(CWScriptParser.QUESTION)
                        pass

                    elif la_ == 3:
                        localctx = CWScriptParser.MemTContext(self, CWScriptParser.TypeExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typeExpr)
                        self.state = 151
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 152
                        self.match(CWScriptParser.D_COLON)
                        self.state = 153
                        self.ident()
                        pass

                    elif la_ == 4:
                        localctx = CWScriptParser.ListTContext(self, CWScriptParser.TypeExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typeExpr)
                        self.state = 154
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 155
                        self.match(CWScriptParser.LBRACK)
                        self.state = 156
                        self.match(CWScriptParser.NumLiteral)
                        self.state = 157
                        self.match(CWScriptParser.RBRACK)
                        pass

             
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class InstantiateDefnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTANTIATE(self):
            return self.getToken(CWScriptParser.INSTANTIATE, 0)

        def fnParams(self):
            return self.getTypedRuleContext(CWScriptParser.FnParamsContext,0)


        def fnBody(self):
            return self.getTypedRuleContext(CWScriptParser.FnBodyContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_instantiateDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstantiateDefn" ):
                listener.enterInstantiateDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstantiateDefn" ):
                listener.exitInstantiateDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstantiateDefn" ):
                return visitor.visitInstantiateDefn(self)
            else:
                return visitor.visitChildren(self)




    def instantiateDefn(self):

        localctx = CWScriptParser.InstantiateDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_instantiateDefn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(CWScriptParser.INSTANTIATE)
            self.state = 164
            self.fnParams()
            self.state = 165
            self.fnBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MigrateDefnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIGRATE(self):
            return self.getToken(CWScriptParser.MIGRATE, 0)

        def fnParams(self):
            return self.getTypedRuleContext(CWScriptParser.FnParamsContext,0)


        def fnBody(self):
            return self.getTypedRuleContext(CWScriptParser.FnBodyContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_migrateDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMigrateDefn" ):
                listener.enterMigrateDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMigrateDefn" ):
                listener.exitMigrateDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMigrateDefn" ):
                return visitor.visitMigrateDefn(self)
            else:
                return visitor.visitChildren(self)




    def migrateDefn(self):

        localctx = CWScriptParser.MigrateDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_migrateDefn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(CWScriptParser.MIGRATE)
            self.state = 168
            self.fnParams()
            self.state = 169
            self.fnBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FnParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._paramDefn = None # ParamDefnContext
            self.params = list() # of ParamDefnContexts

        def LPAREN(self):
            return self.getToken(CWScriptParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CWScriptParser.RPAREN, 0)

        def paramDefn(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ParamDefnContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ParamDefnContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def getRuleIndex(self):
            return CWScriptParser.RULE_fnParams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnParams" ):
                listener.enterFnParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnParams" ):
                listener.exitFnParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnParams" ):
                return visitor.visitFnParams(self)
            else:
                return visitor.visitChildren(self)




    def fnParams(self):

        localctx = CWScriptParser.FnParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_fnParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(CWScriptParser.LPAREN)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1152268858556416) != 0):
                self.state = 172
                localctx._paramDefn = self.paramDefn()
                localctx.params.append(localctx._paramDefn)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 173
                    self.match(CWScriptParser.COMMA)
                    self.state = 174
                    localctx._paramDefn = self.paramDefn()
                    localctx.params.append(localctx._paramDefn)
                    self.state = 179
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 182
            self.match(CWScriptParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FnBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.StmtContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.StmtContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_fnBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnBody" ):
                listener.enterFnBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnBody" ):
                listener.exitFnBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnBody" ):
                return visitor.visitFnBody(self)
            else:
                return visitor.visitChildren(self)




    def fnBody(self):

        localctx = CWScriptParser.FnBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_fnBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(CWScriptParser.LBRACE)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2040674253799592) != 0):
                self.state = 185
                self.stmt()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 191
            self.match(CWScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDefnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentContext
            self.ty = None # TypeExprContext

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def QUESTION(self):
            return self.getToken(CWScriptParser.QUESTION, 0)

        def COLON(self):
            return self.getToken(CWScriptParser.COLON, 0)

        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_paramDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamDefn" ):
                listener.enterParamDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamDefn" ):
                listener.exitParamDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDefn" ):
                return visitor.visitParamDefn(self)
            else:
                return visitor.visitChildren(self)




    def paramDefn(self):

        localctx = CWScriptParser.ParamDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_paramDefn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            localctx.name = self.ident()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 194
                self.match(CWScriptParser.QUESTION)


            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 197
                self.match(CWScriptParser.COLON)
                self.state = 198
                localctx.ty = self.typeExpr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FnDefnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentContext

        def FN(self):
            return self.getToken(CWScriptParser.FN, 0)

        def fnParams(self):
            return self.getTypedRuleContext(CWScriptParser.FnParamsContext,0)


        def ARROW(self):
            return self.getToken(CWScriptParser.ARROW, 0)

        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)


        def fnBody(self):
            return self.getTypedRuleContext(CWScriptParser.FnBodyContext,0)


        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_fnDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnDefn" ):
                listener.enterFnDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnDefn" ):
                listener.exitFnDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnDefn" ):
                return visitor.visitFnDefn(self)
            else:
                return visitor.visitChildren(self)




    def fnDefn(self):

        localctx = CWScriptParser.FnDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_fnDefn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(CWScriptParser.FN)
            self.state = 202
            localctx.name = self.ident()
            self.state = 203
            self.fnParams()
            self.state = 204
            self.match(CWScriptParser.ARROW)
            self.state = 205
            self.typeExpr(0)
            self.state = 206
            self.fnBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStmt(self):
            return self.getTypedRuleContext(CWScriptParser.IfStmtContext,0)


        def assnStmt(self):
            return self.getTypedRuleContext(CWScriptParser.AssnStmtContext,0)


        def letStmt(self):
            return self.getTypedRuleContext(CWScriptParser.LetStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(CWScriptParser.ReturnStmtContext,0)


        def failStmt(self):
            return self.getTypedRuleContext(CWScriptParser.FailStmtContext,0)


        def logStmt(self):
            return self.getTypedRuleContext(CWScriptParser.LogStmtContext,0)


        def sendStmt(self):
            return self.getTypedRuleContext(CWScriptParser.SendStmtContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = CWScriptParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stmt)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.ifStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.assnStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.letStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 211
                self.returnStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 212
                self.failStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 213
                self.logStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 214
                self.sendStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pred = None # ExprContext
            self.b_t = None # BlockContext

        def IF(self):
            return self.getToken(CWScriptParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.BlockContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(CWScriptParser.ELSE, 0)

        def ifStmt(self):
            return self.getTypedRuleContext(CWScriptParser.IfStmtContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = CWScriptParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(CWScriptParser.IF)
            self.state = 218
            localctx.pred = self.expr(0)
            self.state = 219
            localctx.b_t = self.block()
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 220
                self.match(CWScriptParser.ELSE)
                self.state = 223
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [38]:
                    self.state = 221
                    self.ifStmt()
                    pass
                elif token in [5]:
                    self.state = 222
                    self.block()
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


    class AssnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.lhs = None # ExprContext
            self.rhs = None # ExprContext

        def EQ(self):
            return self.getToken(CWScriptParser.EQ, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_assnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssnStmt" ):
                listener.enterAssnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssnStmt" ):
                listener.exitAssnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssnStmt" ):
                return visitor.visitAssnStmt(self)
            else:
                return visitor.visitChildren(self)




    def assnStmt(self):

        localctx = CWScriptParser.AssnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            localctx.lhs = self.expr(0)
            self.state = 228
            self.match(CWScriptParser.EQ)
            self.state = 229
            localctx.rhs = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(CWScriptParser.LET, 0)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def EQ(self):
            return self.getToken(CWScriptParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_letStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetStmt" ):
                listener.enterLetStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetStmt" ):
                listener.exitLetStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetStmt" ):
                return visitor.visitLetStmt(self)
            else:
                return visitor.visitChildren(self)




    def letStmt(self):

        localctx = CWScriptParser.LetStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_letStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(CWScriptParser.LET)
            self.state = 232
            self.ident()
            self.state = 233
            self.match(CWScriptParser.EQ)
            self.state = 234
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CWScriptParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = CWScriptParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(CWScriptParser.RETURN)
            self.state = 237
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FailStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FAIL(self):
            return self.getToken(CWScriptParser.FAIL, 0)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_failStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFailStmt" ):
                listener.enterFailStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFailStmt" ):
                listener.exitFailStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFailStmt" ):
                return visitor.visitFailStmt(self)
            else:
                return visitor.visitChildren(self)




    def failStmt(self):

        localctx = CWScriptParser.FailStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_failStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(CWScriptParser.FAIL)
            self.state = 240
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOG(self):
            return self.getToken(CWScriptParser.LOG, 0)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_logStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogStmt" ):
                listener.enterLogStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogStmt" ):
                listener.exitLogStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogStmt" ):
                return visitor.visitLogStmt(self)
            else:
                return visitor.visitChildren(self)




    def logStmt(self):

        localctx = CWScriptParser.LogStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_logStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(CWScriptParser.LOG)
            self.state = 243
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SendStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEND(self):
            return self.getToken(CWScriptParser.SEND, 0)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def REPLY(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.REPLY)
            else:
                return self.getToken(CWScriptParser.REPLY, i)

        def fnParams(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.FnParamsContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.FnParamsContext,i)


        def ON(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.ON)
            else:
                return self.getToken(CWScriptParser.ON, i)

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.IdentContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.IdentContext,i)


        def fnBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.FnBodyContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.FnBodyContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_sendStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSendStmt" ):
                listener.enterSendStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSendStmt" ):
                listener.exitSendStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSendStmt" ):
                return visitor.visitSendStmt(self)
            else:
                return visitor.visitChildren(self)




    def sendStmt(self):

        localctx = CWScriptParser.SendStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_sendStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(CWScriptParser.SEND)
            self.state = 246
            self.expr(0)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 247
                self.match(CWScriptParser.REPLY)
                self.state = 248
                self.fnParams()
                self.state = 249
                self.match(CWScriptParser.ON)
                self.state = 250
                self.ident()
                self.state = 251
                self.fnBody()
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FnArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._expr = None # ExprContext
            self.args = list() # of ExprContexts

        def LPAREN(self):
            return self.getToken(CWScriptParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CWScriptParser.RPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def getRuleIndex(self):
            return CWScriptParser.RULE_fnArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnArgs" ):
                listener.enterFnArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnArgs" ):
                listener.exitFnArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnArgs" ):
                return visitor.visitFnArgs(self)
            else:
                return visitor.visitChildren(self)




    def fnArgs(self):

        localctx = CWScriptParser.FnArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_fnArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(CWScriptParser.LPAREN)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1996693788688552) != 0):
                self.state = 259
                localctx._expr = self.expr(0)
                localctx.args.append(localctx._expr)
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 260
                    self.match(CWScriptParser.COMMA)
                    self.state = 261
                    localctx._expr = self.expr(0)
                    localctx.args.append(localctx._expr)
                    self.state = 266
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 269
            self.match(CWScriptParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CWScriptParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NullValExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)

        def D_QUE(self):
            return self.getToken(CWScriptParser.D_QUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullValExpr" ):
                listener.enterNullValExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullValExpr" ):
                listener.exitNullValExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullValExpr" ):
                return visitor.visitNullValExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdentExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentExpr" ):
                listener.enterIdentExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentExpr" ):
                listener.exitIdentExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentExpr" ):
                return visitor.visitIdentExpr(self)
            else:
                return visitor.visitChildren(self)


    class QueryExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def QUERY(self):
            return self.getToken(CWScriptParser.QUERY, 0)
        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryExpr" ):
                listener.enterQueryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryExpr" ):
                listener.exitQueryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryExpr" ):
                return visitor.visitQueryExpr(self)
            else:
                return visitor.visitChildren(self)


    class LitExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def StrLiteral(self):
            return self.getToken(CWScriptParser.StrLiteral, 0)
        def NumLiteral(self):
            return self.getToken(CWScriptParser.NumLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLitExpr" ):
                listener.enterLitExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLitExpr" ):
                listener.exitLitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitExpr" ):
                return visitor.visitLitExpr(self)
            else:
                return visitor.visitChildren(self)


    class TypeCheckExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)

        def IS(self):
            return self.getToken(CWScriptParser.IS, 0)
        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeCheckExpr" ):
                listener.enterTypeCheckExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeCheckExpr" ):
                listener.exitTypeCheckExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeCheckExpr" ):
                return visitor.visitTypeCheckExpr(self)
            else:
                return visitor.visitChildren(self)


    class StructExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)
        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)

        def structMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.StructMemberContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.StructMemberContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructExpr" ):
                listener.enterStructExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructExpr" ):
                listener.exitStructExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructExpr" ):
                return visitor.visitStructExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArrayExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACK(self):
            return self.getToken(CWScriptParser.LBRACK, 0)
        def RBRACK(self):
            return self.getToken(CWScriptParser.RBRACK, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CWScriptParser.COMMA)
            else:
                return self.getToken(CWScriptParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayExp" ):
                listener.enterArrayExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayExp" ):
                listener.exitArrayExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExp" ):
                return visitor.visitArrayExp(self)
            else:
                return visitor.visitChildren(self)


    class IndexExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)

        def LBRACK(self):
            return self.getToken(CWScriptParser.LBRACK, 0)
        def RBRACK(self):
            return self.getToken(CWScriptParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexExpr" ):
                listener.enterIndexExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexExpr" ):
                listener.exitIndexExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexExpr" ):
                return visitor.visitIndexExpr(self)
            else:
                return visitor.visitChildren(self)


    class MemExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)

        def DOT(self):
            return self.getToken(CWScriptParser.DOT, 0)
        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemExpr" ):
                listener.enterMemExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemExpr" ):
                listener.exitMemExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemExpr" ):
                return visitor.visitMemExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnwrapExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)

        def BANG(self):
            return self.getToken(CWScriptParser.BANG, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnwrapExpr" ):
                listener.enterUnwrapExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnwrapExpr" ):
                listener.exitUnwrapExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnwrapExpr" ):
                return visitor.visitUnwrapExpr(self)
            else:
                return visitor.visitChildren(self)


    class IsExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.ExprContext,i)

        def EQ_EQ(self):
            return self.getToken(CWScriptParser.EQ_EQ, 0)
        def NEQ(self):
            return self.getToken(CWScriptParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsExpr" ):
                listener.enterIsExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsExpr" ):
                listener.exitIsExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsExpr" ):
                return visitor.visitIsExpr(self)
            else:
                return visitor.visitChildren(self)


    class NullQExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)

        def QUESTION(self):
            return self.getToken(CWScriptParser.QUESTION, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullQExpr" ):
                listener.enterNullQExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullQExpr" ):
                listener.exitNullQExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullQExpr" ):
                return visitor.visitNullQExpr(self)
            else:
                return visitor.visitChildren(self)


    class FnCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CWScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)

        def fnArgs(self):
            return self.getTypedRuleContext(CWScriptParser.FnArgsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnCallExpr" ):
                listener.enterFnCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnCallExpr" ):
                listener.exitFnCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnCallExpr" ):
                return visitor.visitFnCallExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CWScriptParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                localctx = CWScriptParser.QueryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 272
                self.match(CWScriptParser.QUERY)
                self.state = 273
                self.expr(9)
                pass

            elif la_ == 2:
                localctx = CWScriptParser.StructExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1152268858556424) != 0):
                    self.state = 274
                    self.typeExpr(0)


                self.state = 277
                self.match(CWScriptParser.LBRACE)
                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1152268858556416) != 0):
                    self.state = 278
                    self.structMember()
                    self.state = 286
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 279
                            self.match(CWScriptParser.COMMA)
                            self.state = 280
                            self.structMember()
                            self.state = 282
                            self._errHandler.sync(self)
                            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                            if la_ == 1:
                                self.state = 281
                                self.match(CWScriptParser.COMMA)

                     
                        self.state = 288
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                    self.state = 290
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==9:
                        self.state = 289
                        self.match(CWScriptParser.COMMA)




                self.state = 294
                self.match(CWScriptParser.RBRACE)
                pass

            elif la_ == 3:
                localctx = CWScriptParser.LitExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 295
                _la = self._input.LA(1)
                if not(_la==48 or _la==49):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 4:
                localctx = CWScriptParser.ArrayExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 296
                self.match(CWScriptParser.LBRACK)
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1996693788688552) != 0):
                    self.state = 297
                    self.expr(0)
                    self.state = 302
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==9:
                        self.state = 298
                        self.match(CWScriptParser.COMMA)
                        self.state = 299
                        self.expr(0)
                        self.state = 304
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 307
                self.match(CWScriptParser.RBRACK)
                pass

            elif la_ == 5:
                localctx = CWScriptParser.IdentExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 308
                self.ident()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 334
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = CWScriptParser.IsExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 311
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 312
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 313
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = CWScriptParser.NullValExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 314
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 315
                        self.match(CWScriptParser.D_QUE)
                        self.state = 316
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = CWScriptParser.MemExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 317
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 318
                        self.match(CWScriptParser.DOT)
                        self.state = 319
                        self.ident()
                        pass

                    elif la_ == 4:
                        localctx = CWScriptParser.TypeCheckExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 320
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 321
                        self.match(CWScriptParser.IS)
                        self.state = 322
                        self.typeExpr(0)
                        pass

                    elif la_ == 5:
                        localctx = CWScriptParser.FnCallExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 323
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 324
                        self.fnArgs()
                        pass

                    elif la_ == 6:
                        localctx = CWScriptParser.UnwrapExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 325
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 326
                        self.match(CWScriptParser.BANG)
                        pass

                    elif la_ == 7:
                        localctx = CWScriptParser.NullQExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 327
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 328
                        self.match(CWScriptParser.QUESTION)
                        pass

                    elif la_ == 8:
                        localctx = CWScriptParser.IndexExprContext(self, CWScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 329
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 330
                        self.match(CWScriptParser.LBRACK)
                        self.state = 331
                        self.expr(0)
                        self.state = 332
                        self.match(CWScriptParser.RBRACK)
                        pass

             
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StructMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def COLON(self):
            return self.getToken(CWScriptParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(CWScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_structMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructMember" ):
                listener.enterStructMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructMember" ):
                listener.exitStructMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructMember" ):
                return visitor.visitStructMember(self)
            else:
                return visitor.visitChildren(self)




    def structMember(self):

        localctx = CWScriptParser.StructMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_structMember)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.ident()
                self.state = 340
                self.match(CWScriptParser.COLON)
                self.state = 341
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.ident()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExecDefnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXEC(self):
            return self.getToken(CWScriptParser.EXEC, 0)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def fnParams(self):
            return self.getTypedRuleContext(CWScriptParser.FnParamsContext,0)


        def fnBody(self):
            return self.getTypedRuleContext(CWScriptParser.FnBodyContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_execDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecDefn" ):
                listener.enterExecDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecDefn" ):
                listener.exitExecDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecDefn" ):
                return visitor.visitExecDefn(self)
            else:
                return visitor.visitChildren(self)




    def execDefn(self):

        localctx = CWScriptParser.ExecDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_execDefn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(CWScriptParser.EXEC)
            self.state = 347
            self.ident()
            self.state = 348
            self.fnParams()
            self.state = 349
            self.fnBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryDefnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUERY(self):
            return self.getToken(CWScriptParser.QUERY, 0)

        def ident(self):
            return self.getTypedRuleContext(CWScriptParser.IdentContext,0)


        def fnParams(self):
            return self.getTypedRuleContext(CWScriptParser.FnParamsContext,0)


        def fnBody(self):
            return self.getTypedRuleContext(CWScriptParser.FnBodyContext,0)


        def ARROW(self):
            return self.getToken(CWScriptParser.ARROW, 0)

        def typeExpr(self):
            return self.getTypedRuleContext(CWScriptParser.TypeExprContext,0)


        def getRuleIndex(self):
            return CWScriptParser.RULE_queryDefn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryDefn" ):
                listener.enterQueryDefn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryDefn" ):
                listener.exitQueryDefn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryDefn" ):
                return visitor.visitQueryDefn(self)
            else:
                return visitor.visitChildren(self)




    def queryDefn(self):

        localctx = CWScriptParser.QueryDefnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_queryDefn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(CWScriptParser.QUERY)
            self.state = 352
            self.ident()
            self.state = 353
            self.fnParams()
            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 354
                self.match(CWScriptParser.ARROW)
                self.state = 355
                self.typeExpr(0)


            self.state = 358
            self.fnBody()
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

        def LBRACE(self):
            return self.getToken(CWScriptParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CWScriptParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CWScriptParser.StmtContext)
            else:
                return self.getTypedRuleContext(CWScriptParser.StmtContext,i)


        def getRuleIndex(self):
            return CWScriptParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = CWScriptParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(CWScriptParser.LBRACE)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2040674253799592) != 0):
                self.state = 361
                self.stmt()
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 367
            self.match(CWScriptParser.RBRACE)
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
        self._predicates[10] = self.typeExpr_sempred
        self._predicates[26] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def typeExpr_sempred(self, localctx:TypeExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 4)
         




