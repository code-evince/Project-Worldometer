import os
import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen

url = 'https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_Singapore_(2022)'
req = Request(url ,headers ={'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req).read()
mydata = webpage.decode("utf8")
f=open('Countries/Singapore_2022.html','w',encoding="utf-8")
f.write(mydata)
f.close
