import lexer.token as tk
from lexer.codetable import CodeTable
from suffix import suffix


def assipro():
    if tk.token.code == CodeTable['IDENTIFIER']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘IDENTIFIER’ ")
    suffix()
