import ply.lex as lex
import ply.yacc as yacc
import warnings
warnings.filterwarnings("ignore")
import sys
import os
sys.stderr = open(os.devnull,'w')

dates=[]
values=[]
values1=[]

###DEFINING TOKENS###
tokens = ['BEGIN','CLOSEBAR','BEGINCAT','BEGINDATA','CONTENT']
t_ignore = '\t '

###############Tokenizer Rules################


def t_BEGIN(t):
    r'Highcharts.chart\(\'cases-cured-daily\','
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
    '''start : BEGIN skiptag BEGINCAT content CLOSEBAR skipdata BEGINDATA CONTENT CLOSEBAR skipdata BEGINDATA CONTENT CLOSEBAR'''

    values.append(p[8])
    values1.append(p[12])

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



#########DRIVER FUNCTION#######
def main(file,token_file):
    file_obj = open(file, 'r', encoding="utf-8")
    data = file_obj.read()
    lexer = lex.lex()
    lexer.input(data)  
    # with open(token_file, 'w', encoding='utf-8') as file:
    #     for tok in lexer:
    #         file.write(str(tok))
    #         file.write('\n')
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()
    a = dates
    if(len(a)==0):
        a = [0 for i in range (1499)]
        b = [0 for i in range(1499)]
        return a,b
    new_dates = list(filter(lambda x : x.strip() != ',', dates))

    new_dates.reverse()
    recovered = values[0].split(',')
    new_cases = values1[0].split(',')
    
    # print(new_dates)
    # print(recovered)
    # print(new_cases)
    return recovered,new_cases

def fetchRecover_NewCases(country):
 
    a,b =main(f'module_worldometer/html/{country}.html','new.txt')
    return a,b
    


# country = input("enter: ")
# fetchRecover_NewCases(country)



sys.stderr = sys.__stderr__