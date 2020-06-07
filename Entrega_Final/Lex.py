import ply.lex as lex

class Lex:
    reserved = {
            'si' : 'IF',
            'finsi': 'ENDIF',
            'sal': 'PRINT',
            'finpara': 'ENDFOR',
            'var':'VAR',
            'then' : 'THEN',
            'sino' : 'ELSE',
            'finsino': 'ENDELSE',
            'mientras' : 'WHILE',
            'para' : 'FOR',
            'func': 'FUNC',
            'finfunc': 'FINFUNC',
            'regresa': 'REGRESA'
        }
    
    # List of token names.   This is always required
    tokens = [
            'NAME', 
            'NUMBER',
            'PLUS',
            'MINUS',
            'TIMES',
            'DIVIDE',
            'LPAREN',
            'RPAREN',
            'EQEQ',
            'DIF',
            'COMMA',
            'GREATERTHAN',
            'LOWERTHAN',
            'GREATEREQ',
            'LOWEREQ',
            'TWOPOINTS']+ list(reserved.values())

    literals = ['=', '+', '-', '*', '/', '(', ')',':',',','>','<']

# Tokens

    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_ANY_ignore  = ' \t\n'
    t_TWOPOINTS  = r'\:'
    t_EQEQ  = r'\=\='
    t_DIF  = r'\!\='
    t_COMMA = r'\,'
    t_GREATERTHAN = r'\>'
    t_LOWERTHAN = r'\<'
    t_GREATEREQ = r'\>\='
    t_LOWEREQ = r'\<\='



    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'NAME')    # Check for reserved words
        return t

    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
    
    def n_line(self):
        print("HOLAMAU", self.lexer.next)

    # Build the lexer
    def build(self,**kwargs):
        self.errors = []
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self,data):
        self.errors = []
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok: break
             print(tok)

    def report(self):
        return self.errors