'''
Mauricio Peón García                    A01024162
Alexandro Francisco Marcelo González    A01021383
Andrés Campos Tams                      A01024385
12 Jun 2020
'''

from ply import *

# Declaración de palabra clave
palabras_clave = (
    'VAR', 'IMPRIMIR', 'SI', 'ENTONCES', 'PARA', 'SIG', 'A','II',
    'FIN', 'FUNC', "FINSI",  'ARREGLO', 'COMENTARIO', 'REGRESAR', 'LIST', 'NEW',
)

# Declaración de tokens
tokens = palabras_clave + (
    'IGUAL', 'MAS', 'MENOS', 'MULTIPLICACION', 'DIVISION', 'POTENCIA',
    'IPAREN', 'DPAREN', 'MEQ', 'MEI', 'MAQ', 'MAI', 'DIF',
    'COMA', 'ENTERO', 'FLOTANTE', 'CADENA',
    'PALABRA', 'LINEA'
)

# Se ignora el tab
t_ignore = ' \t'

# Definición de comentarios
def t_COMENTARIO(t):
    r'\# .*'
    return t

# Definición de palabra
def t_PALABRA(t):
    r'[A-Z][A-Z0-9]*'
    if t.value in palabras_clave:
        t.type = t.value
    return t

# Definición de tokens por expresión regular
t_IGUAL = r'\='
t_II = r'\=\='
t_MAS = r'\+'
t_MULTIPLICACION = r'\*'
t_MENOS = r'-'
t_POTENCIA = r'\^'
t_DIVISION = r'/'
t_IPAREN = r'\('
t_DPAREN = r'\)'
t_MEQ = r'<'
t_MEI = r'<='
t_MAQ = r'>'
t_MAI = r'>='
t_DIF = r'!='
t_COMA = r'\,'
t_ENTERO = r'\d+'
t_FLOTANTE = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_CADENA = r'\".*?\"'

# Definición de salto de línea
def t_LINEA(t):
    r'\n'
    t.lexer.lineno += 1
    return t

# Definición de error
def t_error(t):
    print("Caracter ilegal %s" % t.value[0])
    t.lexer.skip(1)

lex.lex(debug=0)
