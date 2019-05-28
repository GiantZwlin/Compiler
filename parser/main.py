import lexer.token as tk
from parser.program import program

if __name__ == '__main__':
    try:
        program()
        print("Success")
    except:
        pass
