import lexer.token as tk
from lexer.codetable import CodeTable
from addoper import addoper
from term import term


def termsuff():
    if tk.token.code == CodeTable['+'] or tk.token.code == CodeTable['-']:
        addoper()
        term()
        termsuff()
