import lexer.token as tk
from lexer.codetable import CodeTable
from parser.consdefi import consdefi


def conssuff():
    if tk.token.code == CodeTable[',']:
        tk.token = next(tk.tg)
        consdefi()
        conssuff()
