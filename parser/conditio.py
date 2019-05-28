from lexer.codetable import CodeTable
from express import express
from respoper import respoper
import lexer.token as tk


def conditio():
    if tk.token.code == CodeTable['ODD']:
        tk.token = next(tk.tg)
        express()
    else:
        express()
        respoper()
        express()
