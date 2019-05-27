import lexer.token as tk
from lexer.codetable import CodeTable
from parser.express import express


def suffix():
    if tk.token.code == CodeTable[':']:
        tk.token = next(tk.tg)
        if tk.token.code == CodeTable['=']:
            tk.token = next(tk.tg)
        else:
            raise SyntaxError()
        express()
    elif tk.token.code == CodeTable['(']:
        tk.token = next(tk.tg)
        express()
        if tk.token.code == CodeTable[')']:
            tk.token = next(tk.tg)
        else:
            raise SyntaxError()
