import lexer.token as tk
from lexer.codetable import CodeTable


def respoper():
    if tk.token.code == CodeTable['='] or tk.token.code == CodeTable['<'] or tk.token.code == CodeTable[
        '>'] or tk.token.code == CodeTable['<='] or tk.token.code == CodeTable['>='] or tk.token.code == CodeTable[
        '<>']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError()
