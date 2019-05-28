import lexer.token as tk
from lexer.codetable import CodeTable


def proghead():
    if tk.token.code == CodeTable['PROGRAM']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘PROGRAM’")
    if tk.token.code == CodeTable['IDENTIFIER']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    if tk.token.code == CodeTable[';']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
