import ply.lex as lex
import ply.yacc as yacc
import numpy as np
from tabulate import tabulate
import re

st = []
cont = []
et = []
###DEFINING TOKENS###
tokens = ('BEGINTABLE', 'ENDTABLE', 'CONTENT', 'GARBAGE')
t_ignore = ' |\t'

###############Tokenizer Rules################
def t_BEGINTABLE(t):
    r'<span.class="mw-headline".id="([^"]+)">1.(?:January|February|March|April|May|June|July|August|September|October|November|December)<\/span>'
    return t

def t_ENDTABLE(t):
    r'<span.class="mw-headline".id="Summary">Summary</span>|<span.class="mw-headline".id="See_also">See.also</span>'
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
    '''table : bt content et'''

def p_bt(p):
    '''
    bt : BEGINTABLE
    '''
    st.append(p[1])

def p_et(p):
    '''
    et : ENDTABLE
    '''

def p_content(p):
    '''
    content : CONTENT content
            | empty
    '''
    if len(p) == 3:
        cont.append(p[1])
    
def p_empty(p):
    '''
    empty :
    '''
    pass
    

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
    file.close()

    parser = yacc.yacc()
    parser.parse(data)

    with open('2019.txt', 'w', encoding='utf-8') as file1:
        for i in st:
            input_string = str(i)
            regex = r'<span[^>]*>(.*?)<\/span>'
            match = re.search(regex, input_string)
            if match:
                date = match.group(1)
                print(date)
            file1.write(date + '\n')
        for i in reversed(cont):
            file1.write(str(i) + '\n')
    
    file1.close()
    
    
if __name__ == '__main__':
    main()