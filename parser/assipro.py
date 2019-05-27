import lexer.token as tk
from lexer.codetable import CodeTable
from parser.suffix import suffix


def assipro():
    if tk.token.code == CodeTable['IDENTIFIER']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    suffix()
