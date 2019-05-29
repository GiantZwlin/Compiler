import lexer.token as tk
from lexer.codetable import CodeTable
from typeil import typeil


def argument():
    if tk.token.code == CodeTable['(']:
        tk.token = next(tk.tg)
        if tk.token.code == CodeTable['IDENTIFIER']:
            tk.token = next(tk.tg)
        else:
            raise SyntaxError("SyntaxError at line:{},column:{}".format(tk.token.line, tk.token.column))
        if tk.token.code == CodeTable[':']:
            tk.token = next(tk.tg)
        else:
            raise SyntaxError("SyntaxError at line:{},column:{}".format(tk.token.line, tk.token.column))
        typeil()
        if tk.token.code == CodeTable[')']:
            tk.token = next(tk.tg)
        else:
            raise SyntaxError("SyntaxError at line:{},column:{}".format(tk.token.line, tk.token.column))
