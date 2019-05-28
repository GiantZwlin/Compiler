import lexer.token as tk
from lexer.codetable import CodeTable


def write():
    if tk.token.code == CodeTable['WRITE']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘WRITE’ ")
    if tk.token.code == CodeTable['(']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘(’ ")
    if tk.token.code == CodeTable['IDENTIFIER']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘IDENTIFIER’ ")
    if tk.token.code == CodeTable[')']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘)’ ")
