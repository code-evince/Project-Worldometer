import ply.lex as lex
import ply.yacc as yacc
import warnings
# warnings.filterwarnings("ignore")
import sys
import os
# sys.stderr = open(os.devnull,'w')

dates=[]
values=[]

###DEFINING TOKENS###
tokens = ['BEGIN','CLOSEBAR','BEGINCAT','BEGINDATA','CONTENT']
t_ignore = '\t '

###############Tokenizer Rules################


def t_BEGIN(t):
    r'Highcharts.chart\(\'graph-active-cases-total\','
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
    '''start : BEGIN skiptag BEGINCAT content CLOSEBAR skipdata BEGINDATA CONTENT CLOSEBAR'''
    print('start ')
    values.append(p[8])
def p_content(p):
    '''content : CONTENT content
                | empty '''
    if(len(p)==3):
        dates.append(p[1])
def p_skiptag(p):
    '''skiptag : CLOSEBAR skiptag
                | BEGINDATA skiptag
                | CONTENT skiptag
                | empty
    '''

def p_skipdata(p):
    '''skipdata : CLOSEBAR skipdata
                | CONTENT skipdata
                | BEGINCAT skiptag
                | empty
    '''
def p_error(p):
    pass
def p_empty(p):
    '''empty :'''
    pass
####################functions########################
import sys


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
    new_dates = list(filter(lambda x : x.strip() != ',', dates))

    new_dates.reverse()
    new_values = values[0].split(',')
    print(new_dates)
    print(new_values)
    # print(len(new_dates))
    # print(len(new_values))


def get_daily_cases_data(country):
 
    main(f'html/{country}.html','new.txt')


if __name__ == '__main__':

    country = input('give country ')
    get_daily_cases_data(country)
    


# sys.stderr = sys.__stderr__