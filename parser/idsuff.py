import lexer.token as tk
from lexer.codetable import CodeTable


def idsuff():
    if tk.token.code == CodeTable[',']:
        tk.token = next(tk.tg)
        if tk.token.code == CodeTable['IDENTIFIER']:
            tk.token = next(tk.tg)
        else:
            raise SyntaxError()
    else:
        raise SyntaxError()
