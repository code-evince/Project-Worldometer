import ply.lex as lex
import ply.yacc as yacc
import warnings
# warnings.filterwarnings("ignore")
import sys
import os
# sys.stderr = open(os.devnull,'w')

dates = open('temp/dates.txt', 'w')
data = open('temp/data.txt', 'w')
coaches = {}

###DEFINING TOKENS###
tokens = ['BEGIN','COMMA','DOUBLECOMMA','CLOSEBAR','BEGINCAT','BEGINDATA','CONTENT']
t_ignore = '\t '

###############Tokenizer Rules################


def t_BEGIN(t):
    r'Highcharts.chart\(\'graph-active-cases-total\','
    return t

# def t_BEGIN(t):
#     r'Highcharts.chart(\'graph-deaths-daily\','
#     return t

def t_COMMA(t):
    r','
    return t

def t_DOUBLECOMMA(t):
    r'"'
    return t

def t_CLOSEBAR(t):
    r']'
    return t

def t_BEGINCAT(t):
    r'categories:.\['
    return t

def t_BEGINDATA(t):
    r'data:.\['
    return t

def t_CONTENT(t):
    r'\[[a-zA-Z0-9]*\] | [A-Za-z0-9,\/ ().-]+ '
    return t

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : BEGIN skipall BEGINCAT handle_comma_data CLOSEBAR skipalldata BEGINDATA handle_data CLOSEBAR'''
    print('start ')

# 'BEGIN','COMMA','DOUBLECOMMA','CLOSEBAR','BEGINCAT','BEGINDATA'

def p_handle_comma_data(p):
    '''handle_comma_data : DOUBLECOMMA content_rec DOUBLECOMMA COMMA handle_comma_data
                    | DOUBLECOMMA content_rec DOUBLECOMMA'''
    dates.write(p[2]+'\n')
    print(p[2]+'\n')

# def p_handle_comma_data(p):
#     '''handle_comma_data : DOUBLECOMMA content_rec COMMA content_rec DOUBLECOMMA COMMA handle_comma_data
#                     | DOUBLECOMMA content_rec COMMA content_rec DOUBLECOMMA '''
#     dates.write(p[2]+p[4]+'\n')
#     print(p[2]+p[4]+'\n')
    
def p_handle_data(p):
    '''handle_data : content_rec COMMA handle_data
                    | content_rec '''
    data.write(p[1]+'\n')
    
def p_skipall(p):
    '''skipall : CONTENT skipall
                | COMMA skipall
                | DOUBLECOMMA skipall
                | CLOSEBAR skipall
                | BEGINDATA skipall
               | empty'''
    
def p_skipalldata(p):
    '''skipalldata : CONTENT skipalldata
                | COMMA skipalldata
                | DOUBLECOMMA skipalldata
                | CLOSEBAR skipalldata
                | BEGINCAT skipalldata
               | empty'''

def p_content_rec(p):
    '''content_rec : CONTENT content_rec
                    | empty'''
    if(len(p)==3):
        p[0] = p[1]+p[2]
    else:
        p[0] = p[1]

def p_empty(p):
    '''empty :'''
    p[0] = ''

def p_error(p):
    pass


####################functions########################
import sys

from urllib.request import Request, urlopen
def download_webpage(url,file):
    req = Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f=open(file,'w',encoding="utf-8")
    f.write(mydata)
    f.close


#########DRIVER FUNCTION#######
def main(file,token_file):
    file_obj = open(file, 'r', encoding="utf-8")
    data = file_obj.read()
    lexer = lex.lex()
    lexer.input(data)  
    with open(token_file, 'w', encoding='utf-8') as file:
        for tok in lexer:
            file.write(str(tok))
            file.write('\n')
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()

import os
def delte_file(file_name):
    file_path = str(os.getcwd())+'\\'+file_name
    if os.path.exists(file_path):
        os.remove(file_path)

def get_daily_cases_data(website_url):
    global coaches
    download_webpage(website_url,'webpages/daily_cases_data.html')
    main('webpages/daily_cases_data.html','tokens/token_daily_cases_data.txt')
    # delte_file('webpages/death_data.html')
    # delte_file('tokens/token_death_data.txt')
    ans = coaches.copy()
    coaches = {}
    return ans

if __name__ == '__main__':
    # website_url= sys.argv[1]
    countries = ['Brazil']
    countries = [country.lower() for country in countries]
    links = ['https://www.worldometers.info/coronavirus/country/'+ctry for ctry in countries]
    for link in links :
        print(get_daily_cases_data(link))
        # coaches = {}
    

data.close()
dates.close()

# sys.stderr = sys.__stderr__