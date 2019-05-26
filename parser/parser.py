from lexer.token import *
from lexer.codetable import CodeTable

tg = get_next_token("./lex.out")
# try:
#     while True:
#         print(next(tg))
# except:
#     pass
ll = ['program',
      'proghead',
      'block',
      'consexpl',
      'consdefi',
      'varexl',
      'conssuff',
      'vandefi',
      'varsuff',
      'procdefi',
      'typeil',
      'procedh',
      'procsuff',
      'assipro',
      'sentence',
      'suffix',
      'ifsent',
      'read',
      'whilsent',
      'idsuff',
      'Write',
      'compsent',
      'Exprsuff',
      'sentsuff',
      'Conditio',
      'termsuff',
      'Express',
      'term',
      'Factsuff',
      'argument',
      'Factor',
      'addoper',
      'Muloper',
      'respoper']

for name in ll:
    name = name.lower()
    with open(name + '.py', "w") as f:
        f.write("def {}():\n\tpass".format(name))
if __name__ == '__main__':
    pass
