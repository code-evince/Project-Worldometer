import ply.lex as lex
import ply.yacc as yacc
import numpy as np
from tabulate import tabulate
l = [0]
medal = []
###DEFINING TOKENS###
tokens = ('BEGINTABLE', 'CONTENT', 'GARBAGE')
t_ignore = ' |\t'

###############Tokenizer Rules################
def t_BEGINTABLE(t):
    r'<span.class="mw-headline".id="([^"]+)">1.(?:January|February|March|April|May|June|July|August|September|October|November|December)<\/span>'
    return t

def t_CONTENT(t):
    r'[A-Za-z0-9, ]+'
    return t

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : table'''
    p[0] = p[1]

def p_table(p):
    '''table : BEGINTABLE '''

def p_error(p):
    pass

#########DRIVER FUNCTION#######
def main():
    file_obj= open('Timelines/2019.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    with open('temp.txt', 'w', encoding="utf-8") as file:
        for tok in lexer:
            file.write(str(tok) + '\n')
            
    parser = yacc.yacc()
    parser.parse(data)
    
    
if __name__ == '__main__':
    main()