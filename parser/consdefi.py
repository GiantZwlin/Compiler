from lexer.codetable import CodeTable
import lexer.token as tk


def consdefi():
    if tk.token.code == CodeTable['IDENTIFIER']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘IDENTIFIER’ ")
    if tk.token.code == CodeTable['=']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘=’ ")
    if tk.token.code == CodeTable['UNSIGNED']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘UNSIGNED’ ")
