import lexer.token as tk
from lexer.codetable import CodeTable
from parser.argument import argument


def procedh():
    if tk.token.code == CodeTable['PROCEDURE']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    if tk.token.code == CodeTable['IDENTIFIER']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    argument()
