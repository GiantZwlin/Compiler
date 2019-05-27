from lexer.codetable import CodeTable
from parser.consdefi import consdefi
from parser.conssuff import conssuff
import lexer.token as tk


def consexpl():
    if tk.token.code == CodeTable['BEGIN']:
        tk.token = next(tk.tg)
    consdefi()
    conssuff()
