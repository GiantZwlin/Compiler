import lexer.token as tk
from lexer.codetable import CodeTable
from parser.idsuff import idsuff
from parser.typeil import typeil


def vandefi():
    if tk.token.code == CodeTable['IDENTIFIER']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    idsuff()
    if tk.token.code == CodeTable['IDENTIFIER']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    typeil()
