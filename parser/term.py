import lexer.token as tk
from lexer.codetable import CodeTable
from parser.factor import factor
from parser.factsuff import factsuff


def term():
    factor()
    factsuff()
