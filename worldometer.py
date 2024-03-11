import ply.lex as lex
import openai
import time
import ply.yacc as yacc
from urllib.request import Request, urlopen
import re

import sys
import os
sys.stderr = open(os.devnull,'w')

###DEFINING TOKENS###
tokens = ['BEGINTABLE', 
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE','spa','spo','OPENPARA','CLOSEPARA','STOP','STOP1']
t_ignore = '\t'
a=[]
b=[]
def truncate_paragraph(paragraph, max_words):
    words = paragraph.split()
    truncated_paragraph = ' '.join(words[:max_words])
    truncated_paragraph += "..."
    return truncated_paragraph
###############Tokenizer Rules################
def t_spa(t):
    r'(&\#160)|(&amp)|(&\#91;[0-9]*&\#93;)|(\&)'

def t_spo(t):
    r'\&[a-z]+;'
def t_BEGINTABLE(t):
     r'<div.class="mw-content-ltr.mw-parser-output".lang="en".dir="ltr">'
     return t
def t_STOP(t):
     r'<h2><span.class="mw-headline".id="Governing_body">Governing.body</span>'
     return t

def t_STOP1(t):
     r'<span.class="mw-headline".id="International_grounds">International.grounds</span>'   
     return t


def t_OPENHEADER(t):
    r'<th[^>]*>'
    return t
def t_OPENPARA(t):
    r'<p[^>]*'
    return t
def t_CLOSEPARA(t):
    r'</p[^>]*'
    return t
def t_CLOSEHEADER(t):
    r'</th[^>]*>'
    return t

def t_OPENSTYLE(t):
    r'<style[^>]*>'


def t_CLOSEDIV(t):
    r'</div[^>]*>'


def t_OPENDATA(t):
    r'<td[^>]*>'
    return t

def t_OPENDIV(t):
    r'<div[^>]*>'

def t_CLOSEHREF(t):
    r'</a[^>]*>'
def t_CLOSESTYLE(t):
    r'</style[^>]*>'

def t_OPENSPAN(t):
    r'<span[^>]*>'

def t_CLOSESPAN(t):
    r'</span[^>]*>'

def t_CLOSEDATA(t):
    r'</td[^>]*>'
    return t

def t_OPENHREF(t):
    r'<a[^>]*>'

def t_CONTENT(t):
    r"[A-Za-z0-9, /–.'_]+"
    return t


def t_error(t):
    t.lexer.skip(1)

def t_GARBAGE(t):
    r'<[^>]*>'

                                        # the grammar 
    

def p_start(p):
    '''start : team'''
    p[0] = p[1]


def p_team(p):
    '''team : BEGINTABLE skiptag paragraph '''  

def p_paragraph(p):
    '''paragraph : OPENPARA content CLOSEPARA skiptag paragraph
                 | STOP skipall
                 | STOP1 skipall
                 | empty '''  
    if(len(p)==6):
        b.append(p[2])
def p_skipall(p):
    '''skipall : OPENHREF skiptag
               | CONTENT skiptag
               | OPENDATA skiptag
               | CLOSEDATA skiptag
               | CLOSEHREF skiptag
               | OPENHEADER skiptag
               | OPENPARA skiptag
               | CLOSEPARA skiptag
               | CLOSEHEADER skiptag
               | OPENROW skiptag
               | empty'''     
def p_content(p):
    '''content : CONTENT content
               | empty'''
    if len(p) == 3:
        p[0]=p[1]+p[2]
    if len(p)==2:
        p[0]=''
    


def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    pass

def p_skiptag(p):
    '''skiptag : OPENHREF skiptag
               | CONTENT skiptag
               | OPENDATA skiptag
               | CLOSEDATA skiptag
               | CLOSEHREF skiptag
               | OPENHEADER skiptag
               | CLOSEHEADER skiptag
               | OPENROW skiptag
               | empty'''

#########DRIVER FUNCTION#######
def main():
    player = input("Team Name  = ")    
    formatted_name = player.title().replace(" ", "_")
    formatted_name += '_national_cricket_team'
    req = Request(f'https://en.wikipedia.org/wiki/{formatted_name}',headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    player2 = "https://en.wikipedia.org/wiki/"
    mydata = webpage.decode("utf8")
    f=open('team.html','w',encoding="utf-8")
    f.write(mydata)
    f.close()
    with open("api_key.txt") as f:
        api_key = f.read()


    file_obj= open('team.html','r',encoding="utf-8")
    
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    # for tok in lexer:
    #     print(tok)

            
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()
    b.reverse()
    para = " ".join(b)
    print("------------------------------ Original Text -------------------------------")
    print()
    new_para=truncate_paragraph(para,2000)
    print(new_para)
    print(len(para))
    print(len(new_para)," words")
    print("Generating summary ...")



    system_prompt = "You are an AI assistant capable text summrization in 200 words "
    user_prompt = new_para
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": system_prompt
        },
        {
        "role": "user",
        "content": user_prompt
        }
        ],

    )
    # print(response)
    
    print("------------------------------  SUMMARY ---------------------------------")
    print()
    summary = response.choices[0]['message']['content']
    print(summary)
    print()
    print('Original :',len(new_para)," words")
    print('Summary  :',len(summary)," words")
    print("Reduction = ",(len(para) - len(summary))/len(para)*100,"%")
    print()
    exit=1
    while (exit):
        print("Pick one of the options : ")
        print("1. Stadium Information")
        print("2. Current Squad")
        print("3. Coaching Staff")
        print("4. Current set of ICC rankings")
        print("0. EXIT")
        inp = int(input())
        if(inp==0):
            exit=0
            continue
        if(inp==1):
            stadium.main()
            continue
        if(inp==2):
            squad.main()
            continue
        if(inp==3):
            coaching.main()
            continue
        if(inp==4):
            ranking.main()
            continue



if __name__ == '__main__':
    main()
sys.stderr = sys.__stderr__