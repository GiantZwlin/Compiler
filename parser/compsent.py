from lexer.codetable import CodeTable
from sentence import sentence
from sentsuff import sentsuff
import lexer.token as tk


def compsent():
    # 复合语句
    if tk.token.code == CodeTable['BEGIN']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("SyntaxError at line:{},column:{}".format(tk.token.line, tk.token.column))
    sentence()
    sentsuff()
    if tk.token.code == CodeTable['END']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("SyntaxError at line:{},column:{}".format(tk.token.line, tk.token.column))
