import ply.lex as lex

tokens = (
    'NAME',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'DICE',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DICE = r'D|d'

t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'^[a-zA-Z][a-zA-Z0-9]*'
    return t

def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(t)

lexer = lex.lex()

data =  '''
 3 + 4 * 10
(2 + 5)/ 3
2 D 4 + 1
'''

lexer.input(data)

if __name__ == '__main__':
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
