from lexer.codetable import CodeTable
from consdefi import consdefi
from conssuff import conssuff
import lexer.token as tk


def consexpl():
    if tk.token.code == CodeTable['CONST']:
        tk.token = next(tk.tg)
        consdefi()
        conssuff()
        if tk.token.code == CodeTable[';']:
            tk.token = next(tk.tg)
