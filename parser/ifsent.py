import lexer.token as tk
from lexer.codetable import CodeTable
import conditio
import sentence


def ifsent():
    if tk.token.code == CodeTable['IF']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘IF’ ")
    conditio.conditio()
    if tk.token.code == CodeTable['THEN']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘THEN’ ")
    sentence.sentence()
