import os
import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen

url = 'https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_2024'
req = Request(url ,headers ={'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req).read()
mydata = webpage.decode("utf8")
f=open('Timelines/2024.html','w',encoding="utf-8")
f.write(mydata)
f.close
