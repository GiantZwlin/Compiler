import lexer.token as tk
from lexer.codetable import CodeTable
from parser.factor import factor
from parser.muloper import muloper


def factsuff():
    if tk.token.code == CodeTable['*'] or tk.token.code == CodeTable['/']:
        muloper()
        factor()
        factsuff()
