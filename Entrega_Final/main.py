from Lex1 import Lex
from Yacc import Yacc
import ply.lex as lex
import ply.yacc as yacc

import sys
sys.path.insert(0, "../..")

lexer = Lex()
lexer.build()

my_yacc = Yacc(lexer)
my_yacc.build()
   
data = open("test", "r")
data_tokens = data.read()
lexer.test(data_tokens)
data = open("test", "r")
lines = data.readlines() 
print(lines)
s = data

for line in lines:
    if line != '\n':
        my_yacc.parse_(line)

# while True:
#     try:
#         s = data
#     except EOFError:
#         break
#     if not s:
#         continue
#     my_yacc.parse_(s)