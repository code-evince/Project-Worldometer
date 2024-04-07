import sys
import os
import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen

sys.stderr = open(os.devnull, 'w')

##----------------------global var...----------------
covidnews = []

###------------------------------DEFINING TOKENS---------------------------###
tokens = ('BEGININFO', 'ENDINFO', 'NBSP', 'OPENH3', 'CLOSEH3', 'OPENTABLE',
          'CLOSETABLE', 'OPENROW', 'CLOSEROW', 'CONTENT','GARBAGE')

t_ignore = '\t'

###############----------------------Tokenizer Rules---------------------###############
def t_BEGININFO(t):
    r'<div.id="siteSub".class="noprint">From.Wikipedia,.the.free.encyclopedia[^>]*>'
    return t

def t_ENDINFO(t):
    # r'<span.class="mw-headline".id="See_also">See.also[^>]*>'
    # r'<span.class="mw-headline".id="Summary">Summary[^>]*'
    r'<h2[^>]*><span.class="mw-headline".id="Summary">Summary</span>.*?<\/h2>|<h2[^>]*><span.class="mw-headline".id="See_also">See.also</span>.*?<\/h2>|<h2[^>]*><span.class="mw-headline".id="References">References</span>.*?<\/h2>'
    return t

def t_OPENH3(t):
    r'<h2.*?>'
    return t

def t_CLOSEH3(t):
    r'</h2.*?>'
    return t

def t_NBSP(t):
    r'\&\#[0-9]+;'
    # return t

def t_ignore_all(t):
    r'<h4>|</h4>|<i>|</i>|</b>|<b>|<ul>|</ul>|<li>|</li>|</p>|<p>|<img.*?>|<style.*?>.*?</style>|<figure[^>]*>.*?<\/figure>|<script.*?>.*?</script>|<sup.*?>.*?</sup>|<span.*?>|</span>|<a.href.*?>|</a>|<span.class="mw-editsection">.*?]</span></span>'
    pass

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

def t_CONTENT(t):
    r'[A-Za-z0-9/.,()\'\\:\-;– ]+'
    return t

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)

####################----------------------GRAMMAR RULES----------------------########################
def p_start(p):
    '''start : table'''
    p[0] = p[1]

def p_skipall(p):
    '''skipall : OPENTABLE skipall
                | CLOSETABLE skipall
                | OPENROW skipall
                | CLOSEROW skipall
                | CONTENT skipall
                | empty'''

def p_skiptag(p):
    '''skiptag : CONTENT skiptag
            | empty'''

def p_table(p):
    '''table : BEGININFO skipall news skiptag ENDINFO'''
    # print(p[3])
    covidnews.append(p[3])

def p_date(p):
    '''date : OPENH3 CONTENT textdata CLOSEH3'''
    p[0] = '\n'+p[2]
    # print(p[0])

def p_textdata(p):
    '''textdata : CONTENT textdata
                | empty'''
    if len(p) == 3:
        p[0] = p[1]+' '+p[2]
    else:
        p[0] = ""

def p_news(p):
    '''news : date skiptag picktable textdata news
            | date textdata news
            | empty'''
    # if len(p) == 5:
    #     p[0] = p[1]+'::'+p[2]+''+p[3]+'\n'+p[4]
    #     # p[0] = p[1]+'::'+p[3]+'\n'+p[4]
    if len(p) == 6:
        p[0] = p[1]+'::'+p[3]+''+p[4]+'\n'+p[5]
        # p[0] = p[1]+'::'+p[4]+'\n'+p[5]
    elif len(p) == 4:
        p[0] = p[1]+'::'+p[2]+'\n'+p[3]
    else:
        p[0] = ""
    # print('News:\n', p[0])

def p_picktable(p):
    '''picktable : OPENTABLE handlerow CLOSETABLE'''
    p[0] = p[2]

def p_handlerow(p):
    '''handlerow : OPENROW tabledata CLOSEROW handlerow
                | empty'''
    if len(p) == 5:
        p[0] = p[2]+'\n'+p[4]
    else:
        p[0] = ""

def p_tabledata(p):
    '''tabledata : CONTENT tabledata
                | empty'''
    if len(p) == 3:
        p[0] = p[1]+'\t|\t'+p[2]
    else:
        p[0] = ""
    
def p_content(p):
    '''content : CONTENT
            | empty'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    pass

#########-------------------------DRIVER FUNCTION----------------------#######
def runparser(name, url):
    covidnews.clear()
    # downloading required webpage
    req = Request(url, headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f = open(f'{name}.html','w',encoding="utf-8")
    f.write(mydata)
    f.close

    # read html for parsing the webpage
    file_obj = open(f'{name}.html','r',encoding="utf-8")
    data = file_obj.read()
    
    lexer = lex.lex()  #creating lex...
    lexer.input(data)
    # for tok in lexer:
    #     print(tok)
    # Open a file for writing
    with open("module_wikipedia/tokens.txt", "w", encoding = "utf-8") as file:
        for tok in lexer:
            # print(tok)
            file.write(str(tok))
            file.write('\n')

    parser = yacc.yacc() #creating parser...
    parser.parse(data)

    print(f'Fetched News from {name}!!')
    file_obj.close()

    return covidnews


if __name__ == "__main__":
    #
    url = "https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_Singapore_(2022)"
    name = "module_wikipedia/try"
    # url = "https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_Malaysia_(2023)"

    covidnews = runparser(name, url)
    print('##########################\n\n')
    for news in covidnews:
        print(news)