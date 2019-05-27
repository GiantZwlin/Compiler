import lexer.token as tk
from lexer.codetable import CodeTable
from parser.conditio import conditio
from parser.sentence import sentence


def ifsent():
    if tk.token.code == CodeTable['IF']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    conditio()
    if tk.token.code == CodeTable['THEN']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    sentence()
