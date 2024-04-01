from fileinput import filename
from operator import le
import ply.lex as lex
import ply.yacc as yacc
import sys
import subprocess
from itertools import groupby
import re
import os
from urllib.request import Request, urlopen
import os
from datetime import datetime



list_urls=[]

tokens = ('BEGINDATE','NUMBER','CONTENT','ENDTABLE', 'GARBAGE')
    
t_ignore = '\t'


def t_BEGINDATE(t):
    r'[0-9]+.(January|February|March|April|May|June|July|August|September|October|November|December)'
    return t

def t_ENDTABLE(t):
    # r'<span.class="mw-headline".id="References">References</span>'
    r'<span.class="mw-headline".id="See_also">See.also</span>'
    return t


def t_NUMBER(t):
    r'[0-9]+'
    return t

def t_CONTENT(t):
    r'[A-Za-z0-9, ]+'
    return t

def t_GARBAGE(t):
    r'<[^>]*>'
    # return t

def t_error(t):
    t.lexer.skip(1)

##grammar

def p_start(p):
    '''start : table'''
    print('####### ')

def p_table(p):
    '''table : handlerow ENDTABLE'''

def p_handlerow(p):
    '''handlerow : begin content 
                 | empty'''

def p_begin(p):
    '''begin : BEGINDATE'''
    print(f'\n{p[1]} : ')

def p_content(p):
    '''content : handlecontent content
               | empty '''
    
def p_handlecontent(p):
    '''handlecontent : CONTENT
                     | NUMBER'''
    print(f'{p[1]}')
    # print(p[1])

def p_empty(p):
    '''empty :'''
    pass

    
def p_error(p):
    # print('syntax error : ')
    pass






file_obj= open(f'Responses/1_2020_Responses.html','r',encoding="utf-8")
data=file_obj.read()
# Lexical analysis
lexer = lex.lex()
lexer.input(data)

# Write tokens to a file for debugging
with open('tokens.txt', 'w') as output_file:
    for tok in lexer:
        output_file.write(f'{tok}\n')

# Parsing
parser = yacc.yacc()
parser.parse(data)
file_obj.close()



