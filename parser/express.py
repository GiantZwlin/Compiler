import lexer.token as tk
from lexer.codetable import CodeTable
from term import term
from termsuff import termsuff


def express():
    if tk.token.code == CodeTable['+'] or tk.token.code == CodeTable['-']:
        tk.token = next(tk.tg)
    term()
    termsuff()
