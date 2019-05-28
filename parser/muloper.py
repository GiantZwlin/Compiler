import lexer.token as tk
from lexer.codetable import CodeTable


def muloper():
    if tk.token.code == CodeTable['*'] or tk.token.code == CodeTable['/']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘*’ or '/' ")
