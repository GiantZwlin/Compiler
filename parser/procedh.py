import lexer.token as tk
from lexer.codetable import CodeTable
from argument import argument


def procedh():
    # 过程首部
    if tk.token.code == CodeTable['PROCEDURE']:
        tk.token = next(tk.tg)
        if tk.token.code == CodeTable['IDENTIFIER']:
            tk.token = next(tk.tg)
        else:
            raise SyntaxError("SyntaxError at line:{},column:{}".format(tk.token.line, tk.token.column))
        argument()
        if tk.token.code == CodeTable[';']:
            tk.token = next(tk.tg)
        else:
            raise SyntaxError("SyntaxError at line:{},column:{}".format(tk.token.line, tk.token.column))
