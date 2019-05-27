import lexer.token as tk
from lexer.codetable import CodeTable
from parser.vandefi import vandefi
from parser.varsuff import varsuff


def varexl():
    if tk.token.code == CodeTable['VAR']:
        tk.token = next(tk.tg)
    vandefi()
    varsuff()
