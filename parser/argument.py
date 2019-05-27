import lexer.token as tk
from lexer.codetable import CodeTable
from parser.typeil import typeil


def argument():
    if tk.token.code == CodeTable['(']:
        tk.token = next(tk.tg)
        if tk.token.code == CodeTable['IDENTIFIER']:
            tk.token = next(tk.tg)
        else:
            raise SyntaxError()
        if tk.token.code == CodeTable[':']:
            tk.token = next(tk.tg)
        else:
            raise SyntaxError()
        typeil()
        if tk.token.code == CodeTable[')']:
            tk.token = next(tk.tg)
        else:
            raise SyntaxError()
