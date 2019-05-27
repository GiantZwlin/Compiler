from lexer.codetable import CodeTable
from parser.sentence import sentence
from parser.sentsuff import sentsuff
import lexer.token as tk



def compsent():
    if tk.token.code == CodeTable['BEGIN']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
    sentence()
    sentsuff()
    if tk.token.code == CodeTable['END']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
