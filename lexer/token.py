import re


class Token:
    REGEX = r'< (?P<word>.*) , (?P<code>-?\w+) >'

    def __init__(self, token):
        match = re.search(self.REGEX, token)
        self.word = match.group('word')
        self.code = int(match.group('code'))

    def __str__(self):
        return "< {} , {} >".format(self.word, self.code)


def get_next_token(lexfile):
    with open(lexfile) as f:
        token_list = f.readlines()
    now, cnt = 0, len(token_list)
    while now < cnt:
        ret = Token(token_list[now])
        now += 1
        print(ret)
        yield ret


tg = get_next_token("/home/memoria/PycharmProjects/Compiler/lex.out")

token = next(tg)
