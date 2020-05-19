import sys
import ply.yacc as yacc
import ply.lex as lex
from Lex1 import Lex

class Yacc(Lex):
    def __init__(self, lexer):
        sys.path.insert(0, "../..")
        self.lexer = lexer
 
        # Parsing rules

        self.precedence = (
            ('left', '+', '-'),
            ('left', '*', '/','%'),
            ('right', 'UMINUS'),
        )

        # dictionary of names
        self.names = {}

    def p_statement_assign(self,p):
        'statement : NAME "=" expression'
        self.names[p[1]] = p[3]


    def p_statement_expr(self,p):
        'statement : expression'
        print(p[1])


    def p_expression_binop(self,p):
        '''expression : expression '+' expression
                    | expression '-' expression
                    | expression '*' expression
                    | expression '/' expression
                    | expression '%' expression'''
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
        elif p[2] == '%':
            p[0] = p[1] % p[3]


    def p_expression_uminus(self,p):
        "expression : '-' expression %prec UMINUS"
        p[0] = -p[2]


    def p_expression_group(self,p):
        "expression : '(' expression ')'"
        p[0] = p[2]


    def p_expression_number(self,p):
        "expression : NUMBER"
        p[0] = p[1]


    def p_expression_name(self,p):
        "expression : NAME"
        try:
            p[0] = self.names[p[1]]
        except LookupError:
            print("Undefined name '%s'" % p[1])
            p[0] = 0


    def p_error(self,p):
        if p:
            print("Syntax error at '%s'" % p.value)
        else:
            print("Syntax error at EOF")
    
    def build(self,**kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse_(self,s):
        self.parser.parse(s)


