import lexer.token as tk
from lexer.codetable import CodeTable
import assipro
import compsent
import ifsent
import read
import whilsent
import write


def sentence():
    if tk.token.code == CodeTable['IDENTIFIER']:
        assipro.assipro()
    elif tk.token.code == CodeTable['IF']:
        ifsent.ifsent()
    elif tk.token.code == CodeTable['WHILE']:
        whilsent.whilsent()
    elif tk.token.code == CodeTable['READ']:
        read.read()
    elif tk.token.code == CodeTable['WRITE']:
        write.write()
    elif tk.token.code == CodeTable['BEGIN']:
        compsent.compsent()
