import lexer.token as tk
from lexer.codetable import CodeTable
from sentence import sentence


def sentsuff():
    if tk.token.code == CodeTable[';']:
        tk.token = next(tk.tg)
        sentence()
        sentsuff()


