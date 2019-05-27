from lexer.codetable import CodeTable
from parser.express import express
from parser.respoper import respoper
import lexer.token as tk


def conditio():
    if tk.token.code == CodeTable['ODD']:
        tk.token = next(tk.tg)
        express()
    else:
        express()
        respoper()
        express()
