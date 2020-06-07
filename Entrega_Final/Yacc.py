import sys
import ply.yacc as yacc
import ply.lex as lex
from Lex import Lex

class Yacc(Lex):
    def __init__(self, lexer):
        sys.path.insert(0, "../..")
        self.lexer = lexer
        self.lines = 0

        # Parsing rules

        self.precedence = (
            ('left','GREATERTHAN','LOWERTHAN', 'GREATEREQ', 'LOWEREQ', 'EQEQ', 'DIF'),
            ('left', '+', '-'),
            ('left', '*', '/','%'),
            ('if', 'IF'), 
            ('left', 'ELSE'),
            ('right', 'UMINUS'),
        )

        # dictionary of names
        self.names = {}

    def p_statement_assign(self,p):
        'statement : NAME "=" expression'
        self.names[p[1]] = p[3]


    def p_statement_expr(self,p):
        '''statement : expression
                     | if_statement'''
        print("line:",self.lines,", Solito",p[1])

    def p_print(self,p):
        '''print : PRINT LPAREN NAME RPAREN
                | PRINT LPAREN NUMBER RPAREN
                '''
        print("line:",self.lines,", Print",p[3])

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

    def p_statements_expr(self,p):
        '''statements : statement
                    | statements statement
                    | statements print
        '''
        p[0] = p[1]

    def p_expression_if(self,p):
        '''if_statement : IF LPAREN comparison RPAREN TWOPOINTS then_statement ENDIF
        '''
        print("EVALUANDO:",p[3])
        if p[3] == True:
            p[0] = p[6]
        else:
            p[0] = p[7]

        print("line:",self.lines,", SOY UN IF:", p[0:])

    def p_expression_then(self,p):
        '''then_statement : if_statement
                        |  expression
                        |  statement
                        |  statements
        '''
        print("line:",self.lines,", SOY UN THEN:", p[0:])
    
    def p_expression_else(self,p):
        '''
        else_statement :    ELSE expression ENDELSE
                    |   ELSE if_statement ENDELSE
                    |   empty
        '''
        print("line:",self.lines,", SOY UN ELSE:", p[0:])

    def p_empty(self, p):
        ''' empty : ''
        '''
    
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


    def p_error(self,p):
        if p:
            print("Syntax error at '%s'" % p.value,"in line: ", self.lines)
        else:
            print("Syntax error at EOF")
    
    def build(self,**kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse_(self,s):
        self.lines+=1
        self.parser.parse(s)