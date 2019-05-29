import lexer.token as tk
from lexer.codetable import CodeTable
from express import express


def suffix():
    # 后缀
    if tk.token.code == CodeTable[':=']:
        tk.token = next(tk.tg)
        express()
    elif tk.token.code == CodeTable['(']:
        tk.token = next(tk.tg)
        express()
        if tk.token.code == CodeTable[')']:
            tk.token = next(tk.tg)
        else:
            raise SyntaxError("SyntaxError at line:{},column:{}".format(tk.token.line, tk.token.column))
