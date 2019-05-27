import lexer.token as tk
from lexer.codetable import CodeTable
from parser.block import block
from parser.procedh import procedh
from parser.procsuff import procsuff


def procdefi():
    if tk.token.code != CodeTable['BEGIN']:
        procedh()
        block()
        if tk.token.code == CodeTable[';']:
            next(tk.tg)
        else:
            raise SyntaxError()
        procsuff()

