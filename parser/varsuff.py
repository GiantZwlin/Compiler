import lexer.token as tk
from lexer.codetable import CodeTable
from parser.vandefi import vandefi


def varsuff():
    if tk.token.code != CodeTable['BEGIN'] and tk.token.code != CodeTable['PROCEDURE']:
        vandefi()
        varsuff()
