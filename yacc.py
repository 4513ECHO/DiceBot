import ply.yacc as yacc
from dicelex import tokens
import random

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
    ('right', 'DICE')
)

names = {}

def p_statement_assign(p):
    """statement : NAME EQUALS expression"""
    names[p[1]] = p[3]

def p_statement_expr(p):
    """statement : expression"""
    p[0] = p[1]

def p_expression_binop(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression DICE expression"""
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == 'D' or p[2] == 'd':
        r = 0
        for x in range(p[1]):
            r += random.randint(1, p[3])
        p[0] = r

def p_expression_uminus(p):
    """expression : MINUS expression %prec UMINUS"""
    p[0] = -p[2]

def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]

def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = p[1]

def p_expression_name(p):
    """expression : NAME"""
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name \"%s\"" % p)
        p[0] = 0

def p_error(p):
    print("Syntax error in input")

yacc.yacc()
