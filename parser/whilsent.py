import lexer.token as tk
from lexer.codetable import CodeTable
from parser.conditio import conditio
from parser.sentence import sentence


def whilsent():
    if tk.token.code == CodeTable['WHILE']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    conditio()
    if tk.token.code == CodeTable['IDENTIFIER']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    sentence()
