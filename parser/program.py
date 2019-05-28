from block import block
from lexer.codetable import CodeTable
from proghead import proghead
import lexer.token as tk


def program():
    proghead()
    block()
    if tk.token.code == CodeTable['.']:
        print("Success")
    else:
        raise SyntaxError("There should be a ‘.’ ")
