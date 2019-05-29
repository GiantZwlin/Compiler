import re

from lexer.codetable import CodeTable

REGEX = [
    ('PROGRAM', r'\b[Pp][Rr][Oo][Gg][Rr][Aa][Mm]\b'),
    ('CONST', r'\b[Cc][Oo][Nn][Ss][Tt]\b'),
    ('VAR', r'\b[Vv][Aa][Rr]\b'),
    ('INTEGER', r'[Ii][Nn][Tt][Ee][Gg][Ee][Rr]'),
    ('LONG', '[Ll][Oo][Nn][Gg]'),
    ('PROCEDURE', r'\b[Pp][Rr][Oo][Cc][Ee][Dd][Uu][Rr][Ee]\b'),
    ('IF', r'\b[Ii][Ff]\b'),
    ('THEN', r'\b[Tt][Hh][Ee][Nn]\b'),
    ("WHILE", r'\b[Ww][Hh][Ii][Ll][Ee]\b'),
    ('DO', r'\b[Dd][Oo]\b'),
    ('READ', r'\b[Rr][Ee][Aa][Dd]\b'),
    ('WRITE', r'\b[Ww][Rr][Ii][Tt][Ee]\b'),
    ('BEGIN', r'\b[Bb][Ee][Gg][Ii][Nn]\b'),
    ('END', r'\b[Ee][Nn][Dd]\b'),
    ('ODD', r'\b[Oo][Dd][Dd]\b'),
    ('PLUS', r'\+'),
    ('MINUS', r'\-'),
    ('MUlTIPLY', r'\*'),
    ('DIVISION', r'\/'),
    ('EQUAL', r'(?<!:)='),
    ('NOTEQUAL', r'<>'),
    ('LT', r'<(?![=>])'),
    ('LET', r'<='),
    ('GT', r'>(?![=])'),
    ('GET', r'>='),
    ('COMMA', r','),
    ('DOT', r'\.'),
    ('SEMICOLON', r';'),
    ('COLON', r':(?!=)'),
    ('ASSIGN', r':='),
    ('LEFTBRACKETS', r'\('),
    ('RIGHTBRACKETS', r'\)'),
    ('UNSIGNED', '(?<![a-zA-Z])\d+'),
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),
    ('SHARP', r'#'),
    ('NEWLINE', r'\n'),
]


class Lexer:
    def __init__(self, file):
        self.file = file

    def get_token(self):
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in REGEX)
        line_num = 1
        line_start = 0
        tokens = []
        with open(self.file) as f:
            for mo in re.finditer(tok_regex, f.read()):
                type_t = mo.lastgroup
                value = mo.group()
                column = mo.start() - line_start
                if type_t == 'NEWLINE':
                    line_start = mo.end()
                    line_num += 1
                    continue
                tokens.append(Token(
                    type_t=type_t,
                    value=value,
                    code=CodeTable[type_t],
                    line=line_num,
                    column=column
                ))
        for tk in tokens:
            yield tk


class Token:

    def __init__(self, type_t, value, code, line, column):
        self.type_t = type_t
        self.value = value
        self.code = code
        self.line = line
        self.column = column

    def __str__(self):
        return "< {} , {} >".format(self.type_t, self.value)


lexer = Lexer('/home/memoria/PycharmProjects/Compiler/lexer/example')
tg = lexer.get_token()

token = next(tg)
