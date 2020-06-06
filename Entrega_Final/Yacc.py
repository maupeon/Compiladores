import sys
import ply.yacc as yacc
import ply.lex as lex
from Lex import Lex

class Yacc(Lex):
    def __init__(self, lexer):
        sys.path.insert(0, "../..")
        self.lexer = lexer
        self.stack = []
 
        # Parsing rules

        self.precedence = (
            ('left','GREATERTHAN','LOWERTHAN', 'GREATEREQ', 'LOWEREQ', 'EQEQ', 'DIF'),
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
        '''statement : expression
                     | comparison
                     | if_statement'''
        p[0] = [1]

    def p_expression_binop(self,p):
        '''statement : expression '+' expression
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
        "expression : LPAREN expression RPAREN"
        p[0] = p[2]


    def p_expression_number(self,p):
        "expression : NUMBER"
        p[0] = p[1]
        

    def p_expression_function(self,p):
        '''expression : FUNC NAME LPAREN expression RPAREN TWOPOINTS
                    |   FUNC NAME LPAREN  RPAREN TWOPOINTS'''
        self.stack.append(p[0])
 
    def p_expression_si(self,p):
        '''if_statement : IF LPAREN comparison RPAREN TWOPOINTS statement ENDIF'''
        print("expression",p[6])
        if p[3]:
            p[0] == p[6]

    def p_expression_comparison(self, p):
        '''comparison : expression GREATERTHAN expression
                    | expression LOWERTHAN expression
                    | expression GREATEREQ expression
                    | expression LOWEREQ expression
                    | expression EQEQ expression
                    | expression DIF expression'''
                    
        if p[2] == '>':
            if p[1] > p[3]:
                p[0] = True
            else:
                p[0] = False

        elif p[2] == '<':
            if p[1] < p[3]:
                p[0] = True
            else:
                p[0] = False

        elif p[2] == '>=':
            if p[1] >= p[3]:
                p[0] = True
            else:
                p[0] = False

        elif p[2] == '<=':
            if p[1] <= p[3]:
                p[0] = True
            else:
                p[0] = False

        elif p[2] == '==':
            if p[1] == p[3]:
                p[0] = True
            else:
                p[0] = False

        elif p[2] == '!=':
            if p[1] != p[3]:
                p[0] = True
            else:
                p[0] = False    

  
            

    def p_expression_sino(self,p):
        "expression : ELSE TWOPOINTS"
        p[0] = p[1]

    def p_expression_print(self,p):
        '''expression : PRINT LPAREN NAME RPAREN  
                    |   PRINT LPAREN NUMBER RPAREN 
                   '''
        
        print("AGAP",p[3])

    
    def p_expression_for(self,p):
        '''expression : FOR LPAREN NUMBER COMMA NUMBER COMMA NUMBER RPAREN TWOPOINTS '''
        # for index in range (p[3], p[5], p[7]):
        # 5, 5, 1
        '''.....
        10: for, p[3], p[5], p[7]
        14: finpara
        '''
    
  

    def p_expression_while(self,p):
        '''expression : WHILE LPAREN NUMBER EQEQ NUMBER RPAREN TWOPOINTS
                      | WHILE LPAREN NUMBER DIF NUMBER RPAREN TWOPOINTS
                      | WHILE LPAREN NUMBER GREATERTHAN NUMBER RPAREN TWOPOINTS
                      | WHILE LPAREN NUMBER LOWERTHAN NUMBER RPAREN TWOPOINTS
                      | WHILE LPAREN NUMBER GREATEREQ NUMBER RPAREN TWOPOINTS
                      | WHILE LPAREN NUMBER LOWEREQ NUMBER RPAREN TWOPOINTS
         '''
    
    def p_expression_finfunc(self,p):
        "expression : FINFUNC"
    
    def p_expression_finsi(self,p):
        "expression : ENDIF"
        p[0] = p[1]

    def p_expression_finfor(self,p):
        "expression : ENDFOR"
    
    
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


