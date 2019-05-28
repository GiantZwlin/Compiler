import lexer.token as tk
from lexer.codetable import CodeTable
import conditio
import sentence


def whilsent():
    if tk.token.code == CodeTable['WHILE']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    conditio.conditio()
    if tk.token.code == CodeTable['DO']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    sentence.sentence()
