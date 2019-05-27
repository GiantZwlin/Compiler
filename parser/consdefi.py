from lexer.codetable import CodeTable
import lexer.token as tk


def consdefi():
    if tk.token.code == CodeTable['IDENTIFIER']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    if tk.token.code == CodeTable['=']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    if tk.token.code == CodeTable['UNSIGNED']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
