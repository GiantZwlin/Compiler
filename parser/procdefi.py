import lexer.token as tk
from lexer.codetable import CodeTable
import block
import procedh
import procsuff


# def procdefi():
#     # 过程说明部分
#     if tk.token.code != CodeTable['BEGIN']:
#         procedh.procedh()
#         block.block()
#         if tk.token.code == CodeTable[';']:
#             next(tk.tg)
#         else:
#             raise SyntaxError()
#         procsuff.procsuff()

def procdefi():
    # 过程说明部分
    if tk.token.code == CodeTable['PROCEDURE']:
        procedh.procedh()
        block.block()
        if tk.token.code == CodeTable[';']:
            tk.token=next(tk.tg)
        else:
            raise SyntaxError()
        procsuff.procsuff()