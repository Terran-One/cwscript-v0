from antlr4 import FileStream, CommonTokenStream

from typing import Any, List
from dataclasses import dataclass

from CWScriptVisitor import CWScriptVisitor
from CWScriptParser import CWScriptParser
from CWScriptLexer import CWScriptLexer
from ast_nodes import *


class CWSVisitor(CWScriptVisitor):

  def visitProgram(self, ctx: CWScriptParser.ProgramContext):
    pass

# build a lexer
input_stream = FileStream("examples/TerraSwap/TerraSwapFactory.rs")
lexer = CWScriptLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = CWScriptParser(tokens)

tree = parser.program()

ast_builder = CWSVisitor()
ast = ast_builder.visitProgram(tree)
# execute(ast)

print(ast)