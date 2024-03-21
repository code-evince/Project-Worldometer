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
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE','spa','spo')
t_ignore = '\t'

myList = []
final=[]

###############Tokenizer Rules################
def t_BEGINTABLEA(t):
    r'<h2><span.class="mw-headline".id="League_stage">League.stage</span>'
    return t

def t_SEPA(t):
    r'<div.style=\"width:.100[^>]*>'
    return t

def t_TABLEH(t):
    r'<table[^>]*>'
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
    r'<tr[^>]*>'
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
    r'[A-Za-z0-9–.()/ ]+'
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
    p[0] = p[1]

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
    '''table : BEGINTABLEA skiptag SEPA TABLEH tabledata TABLET nexttable
                | empty 
    ''' 

def p_nexttable(p):
    '''nexttable : SEPA TABLEH tabledata TABLET skiptag nexttable
                   | TABLEH tabledata TABLET skiptag nexttable
                   | empty 

    '''

    # if(len(p)==7):
    #     myList.append("*")

def p_tabledata(p):
    '''tabledata : OPENTABLE OPENROW datacell CLOSEROW CLOSETABLE
    ''' 
    if(len(p)==6):
        p[0] = p[3]
    

def p_datacell(p):
    '''datacell : OPENDATA output CLOSEDATA datacell
            | empty '''
    if(len(p)==5):
        p[0]= p[2]
    if(len(p)==2):
        myList.append("*")
    

def p_output(p):
    '''output : CONTENT  output
                | empty '''
    if(len(p)==3):
        p[0]=p[1] 
        if(p[0]!=" "):
            print(p[1])
            myList.append(p[1])
    
            
        

    

        

def p_error(p):
    pass
#########DRIVER FUNCTION#######
def main():
    for i in range(1):
        file_obj= open('ICC.html','r',encoding="utf-8")
        data=file_obj.read()
        lexer = lex.lex()
        lexer.input(data)
        # for tok in lexer:
        #     print(tok)
        parser = yacc.yacc()
        print("*************************************************************************************************")
        parser.parse(data)
        file_obj.close()
 
        a=[]
        b=[]
        date=[]
        match=[]
        result=[]

        flag=0
        for i in myList:
            if(i=='*'):
                flag+=1
                continue
            if(flag==0):
                date.append(i)
            if(flag==1):
                match.append(i)
            if(flag==2):
                result.append(i)
            if(flag==3):
                flag=0
                b.append(date)
                b.append(match)
                b.append(result)
                date=[]
                match=[]
                result=[]
                a.append(b)
                b=[]
        print(a)
        head=['date','match','result']
        print(tabulate(a, head, tablefmt="fancy_grid"))
        num=1
        while(num!=0):
            print("Enter 1 to get information about Match b/w 2 countries")
            print("Enter 0 to exit")
            g = int(input("Enter : "))
            if(g==0):
                num=0
                continue
            c1 = input("Country 1 : ")
            c2 = input("Country 2 : ")
            f1=0
            for i in range(len(a)):
                for k in a[i][1]:
                    if(k==c1):
                        f1+=1
                    if(k==c2):
                        f1+=1
                    if(f1==2):
                        print(a[i])
                        f1=0
                f1=0
                       
            
            



if __name__ == '__main__':
    main() 
