import ply.lex as lex
import ply.yacc as yacc
import os
import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen
import numpy as np
from tabulate import tabulate




###DEFINING TOKENS###
tokens = ('BEGINTABLEA','TABLEH','TABLET','SEPA',
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE','spa','spo','THEAD_OPEN','THEAD_CLOSE')
t_ignore = '\t'

myList = []
final=[]

##############Tokenizer Rules################
def t_BEGINTABLEA(t):
    r'<table.id="main_table_countries_yesterday".class="table.table-bordered.table-hover.main_table_countries".style="width:100%;margin-top:.0px.!important;display:none;">'
    return t

def t_SEPA(t):
    r'<div.style=\"width:.100[^>]*>'
    return t

def t_TABLEH(t):
    r'<table[^>]*>'
    return t
def t_THEAD_OPEN(t):
    r'<thead[^>]*>'
    return t

def t_THEAD_CLOSE(t):
    r'</thead[^>]*>'
    return t

def t_TABLET(t):
    r'</table[^>]*>'
    return t


def t_spa(t):
    r'..91.[0-9]..93.'

def t_spo(t):
    r'\&[a-z]+;'

def t_OPENTABLE(t):
    r'<tbody[^>]*>'
    return t

def t_CLOSETABLE(t):
    r'</tbody[^>]*>'
    return t

def t_OPENROW(t):
    r'<tr.style[^>]*>'
    return t

def t_CLOSEROW(t):
    r'</tr[^>]*>'
    return t

def t_OPENHEADER(t):
    r'<th[^>]*>'
    return t

def t_CLOSEHEADER(t):
    r'</th[^>]*>'
    return t

def t_OPENHREF(t):
    r'<a[^>]*>'
    # return t

def t_CLOSEHREF(t):
    r'</a[^>]*>'
    # return t

def t_OPENDATA(t):
    r'<td[^>]*>'
    return t

def t_CLOSEDATA(t):
    r'</td[^>]*>'
    return t
def t_V(t):
    r'v'
def t_D(t):
    r'd'



def t_CONTENT(t):
    r'[A-Za-z0-9–.()]+'
    return t

def t_OPENDIV(t):
    r'<div[^>]*>'
    # return t

def t_CLOSEDIV(t):
    r'</div[^>]*>'
    # return t

def t_CLOSESTYLE(t):
    r'</style[^>]*>'
    # return t

def t_OPENSPAN(t):
    r'<span[^>]*>'
    # return t

def t_CLOSESPAN(t):
    r'</span[^>]*>'
    # return t

def t_GARBAGE(t):
    r'<[^>]*>'
    # return t

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
										#GRAMMAR RULES

def p_start(p):
    '''start : table'''

def p_empty(p):
    '''empty :'''
    pass

def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | OPENHREF skiptag
               | CLOSEHREF skiptag
               | OPENDATA skiptag
               | CLOSEDATA skiptag
               | OPENHEADER skiptag
               | CLOSEHEADER skiptag
               | empty'''
   

def p_table(p):
    '''table : BEGINTABLEA skiptag OPENROW  startrow CLOSETABLE
                | empty 
    ''' 


def p_startrow(p):
    ''' startrow : firstrow CLOSEROW startrow
                 | OPENROW getcell CLOSEROW startrow
                 | empty
       '''
            
        
def p_firstrow(p):
    '''firstrow : OPENDATA content CLOSEDATA
    '''

def p_content(p):
    '''content : CONTENT 
                | CONTENT CONTENT 
                | empty
    '''
def p_getcell(p):
    '''getcell : OPENDATA content CLOSEDATA'''
def p_error(p):
    pass
#########DRIVER FUNCTION#######
def main():
    
    file_obj= open('Worldometer_home.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    with open('new.txt','w') as p:
        for tok in lexer:
            p.write(str(tok)+'\n')
    parser = yacc.yacc()
    print("*************************************************************************************************")
    parser.parse(data)
    file_obj.close()

            



if __name__ == '__main__':
    main() 
