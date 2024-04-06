import ply.lex as lex
import ply.yacc as yacc
import os
import requests
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

def t_TABLEH(t):
    r'<table[^>]*>'
    # return t

def t_THEAD_OPEN(t):
    r'<thead[^>]*>'
    return t

def t_THEAD_CLOSE(t):
    r'</thead[^>]*>'
    return t

def t_TABLET(t):
    r'</table[^>]*>'
    # return t


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
    r'[A-Za-z0-9–/\+.()]+'
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



def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | OPENHREF skiptag
               | CLOSEHREF skiptag
               | OPENDATA skiptag
               | CLOSEDATA skiptag
               | OPENHEADER skiptag
               | CLOSEHEADER skiptag
               | THEAD_OPEN skiptag
               | THEAD_CLOSE skiptag
               | OPENTABLE skiptag
               | CLOSETABLE skiptag
               | CLOSEROW skiptag
               | empty'''
   

def p_table(p):
    '''table : BEGINTABLEA skiptag OPENROW startrow CLOSETABLE
    ''' 


def p_startrow(p):
    ''' startrow : firstrow CLOSEROW startrow
                 | OPENROW getcell CLOSEROW startrow
                 | empty
       '''
    if(len(p)==4):
        p[0] = p[1]
    if(len(p)==5):
        p[0]=p[2]
    

            
def p_firstrow(p):
    '''firstrow : OPENDATA content CLOSEDATA firstrow
                | empty
    '''
    
    if(len(p)==5):
        p[0]=p[2]
        # print(p[2])


def p_content(p):
    '''content : CONTENT CONTENT CONTENT CONTENT
                | CONTENT CONTENT CONTENT
                | CONTENT CONTENT
                | CONTENT
                | empty
    '''
    if(len(p)==5):
        p[0]=p[1]+p[2]+p[3]+p[4]
        myList.append(p[1]+p[2]+p[3]+p[4])
    if(len(p)==4):
        p[0]=p[1]+p[2]+p[3]
        myList.append(p[1]+p[2]+p[3])
    if(len(p)==3):
        p[0]=p[1]+p[2]
        myList.append(p[1]+p[2])
    if(len(p)==2):
        p[0]=p[1]
        myList.append(p[1])
    

def p_getcell(p):
    '''getcell : OPENDATA content CLOSEDATA skipdata getcell
               | empty
    '''
    if(len(p)==5):
        p[0]=p[2]
def p_skipdata(p):
    '''skipdata : CONTENT skipdata
               | CLOSEDATA skipdata
               | empty'''
def p_error(p):
    pass
def p_empty(p):
    '''empty :'''
    pass

def download_page(url, file_name):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(response.content)
            print(f"Page downloaded successfully as {file_name} !!")
        else:
            print(f"Failed to download page: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
#########DRIVER FUNCTION#######
def main():

    url = "https://www.worldometers.info/coronavirus/"
    file_name = "module_worldometer/Worldometer_home.html"
    download_page(url, file_name)

    print('Wait for Parsing...')
    file_obj= open('module_worldometer/Worldometer_home.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    # with open('module_worldometer/new.txt','w') as p:
    #     for tok in lexer:
    #         p.write(str(tok)+'\n')
    parser = yacc.yacc()
   
    parser.parse(data)
    file_obj.close()

    for i in range (len(myList)):
        if (myList[i] ==  None or myList[i]=='N/A'):
            myList[i]=0
            
    while(len(myList)):
        new = myList[:15]
        final.append(new)
        del myList[:22]
    return final


if __name__ == '__main__':
    main() 
