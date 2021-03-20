import ply.lex as lex

tokens = (
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'NAME',
    'DICE'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DICE = r'(D|d)'

t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'

def t_STRING(t):
    r"""(\"|\').*(\"|\')"""
    t.value = str(t.value)[1:-1]
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r"""^[a-zA-Z^(D|d)_]\w*"""
    return t

def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(t)


lex.lex(debug=0)
