import lexer.token as tk
from lexer.codetable import CodeTable


def typeil():
    if tk.token.code == CodeTable['INTEGER'] or tk.token.code == CodeTable['LONG']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("There should be a ‘INTEGER’ or 'LONG' ")
