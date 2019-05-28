from lexer.codetable import CodeTable
from sentence import sentence
from sentsuff import sentsuff
import lexer.token as tk


def compsent():
    # 复合语句
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
