import lexer.token as tk
from lexer.codetable import CodeTable
from express import express


def exprsuff():
    if tk.token.code == CodeTable[',']:
        tk.token == next(tk.tg)
        express()
        exprsuff()
