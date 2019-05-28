import lexer.token as tk
from lexer.codetable import CodeTable
import express


def factor():
    if tk.token.code == CodeTable['IDENTIFIER'] or tk.token.code == CodeTable['UNSIGNED']:
        tk.token = next(tk.tg)
    elif tk.token.code == CodeTable['(']:
        express.express("There should be a ‘(’ ")
        if tk.token.code == CodeTable[')']:
            tk.token = next(tk.tg)
        else:
            raise SyntaxError("There should be a ‘)’ ")
    else:
        raise SyntaxError("There should be a ‘IDENTIFIER’ or 'UNSIGNED' ")
