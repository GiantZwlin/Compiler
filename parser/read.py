import lexer.token as tk
from lexer.codetable import CodeTable
from idsuff import idsuff


def read():
    if tk.token.code == CodeTable['READ']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    if tk.token.code == CodeTable['(']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    if tk.token.code == CodeTable['IDENTIFIER']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    idsuff()
    if tk.token.code == CodeTable[')']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()



