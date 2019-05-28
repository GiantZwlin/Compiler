import lexer.token as tk
from lexer.codetable import CodeTable
from idsuff import idsuff


def read():
    if tk.token.code == CodeTable['READ']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘READ’ ")
    if tk.token.code == CodeTable['(']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘)’ ")
    if tk.token.code == CodeTable['IDENTIFIER']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘IDENTIFIER’ ")
    idsuff()
    if tk.token.code == CodeTable[')']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘)’ ")



