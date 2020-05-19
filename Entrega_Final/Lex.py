class Lex:
    def __init__(self):
        self.reserved = {
            'si' : 'IF',
            'then' : 'THEN',
            'sino' : 'ELSE',
            'mientras' : 'WHILE',
            'para' : 'FOR'
        }
        # List of token names.   This is always required
        self.tokens = [
            'NUMBER',
            'PLUS',
            'MINUS',
            'TIMES',
            'DIVIDE',
            'LPAREN',
            'RPAREN',
            'NAME'
        ] + list(self.reserved.values())

        # Regular expression rules for simple tokens
        self.t_PLUS    = r'\+'
        self.t_MINUS   = r'-'
        self.t_TIMES   = r'\*'
        self.t_DIVIDE  = r'/'
        self.t_LPAREN  = r'\('
        self.t_RPAREN  = r'\)'
        self.t_ignore  = ' \t'
        self.t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

        self.literals = ['=', '+', '-', '*', '/', '(', ')']
        
    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'ID')    # Check for reserved words
        return t
    # A regular expression rule with some action code
    def t_NUMBER(self,t):
        r'\d+'
        t.value = int(t.value)    
        return t

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)


    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    
