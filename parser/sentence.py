import lexer.token as tk
from lexer.codetable import CodeTable
from parser.assipro import assipro
from parser.compsent import compsent
from parser.ifsent import ifsent
from parser.read import read
from parser.whilsent import whilsent
from parser.write import write


def sentence():
    if tk.token.code == CodeTable['PROCEDURE']:
        assipro()
    elif tk.token.code == CodeTable['PROCEDURE']:
        ifsent()
    elif tk.token.code == CodeTable['PROCEDURE']:
        whilsent()
    elif tk.token.code == CodeTable['PROCEDURE']:
        read()
    elif tk.token.code == CodeTable['PROCEDURE']:
        write()
    elif tk.token.code == CodeTable['PROCEDURE']:
        compsent()
