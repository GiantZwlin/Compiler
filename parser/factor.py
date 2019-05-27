import lexer.token as tk
from lexer.codetable import CodeTable
from parser.express import express


def factor():
    if tk.token.code == CodeTable['IDENTIFIER'] or tk.token.code == CodeTable['UNSIGNED']:
        next(tk.tg)
    elif tk.token.code == CodeTable['(']:
        express()
        if tk.token.code == CodeTable[')']:
            next(tk.tg)
        else:
            raise SyntaxError()
    else:
        raise SyntaxError()
