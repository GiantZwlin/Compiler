import lexer.token as tk
from lexer.codetable import CodeTable
from idsuff import idsuff
from typeil import typeil


def vandefi():
    if tk.token.code == CodeTable['IDENTIFIER']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    idsuff()
    if tk.token.code == CodeTable[':']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    typeil()
    if tk.token.code == CodeTable[';']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
