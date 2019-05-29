import lexer.token as tk
import block
from lexer.codetable import CodeTable
import procedh


def procsuff():
    if tk.token.code != CodeTable['BEGIN']:
        procedh.procedh()
        block.block()
        if tk.token.code == CodeTable[';']:
            tk.token = next(tk.tg)
        else:
            raise SyntaxError("SyntaxError at line:{},column:{}".format(tk.token.line, tk.token.column))
        procsuff()
