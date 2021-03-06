'''
Mauricio Peón García                    A01024162
Alexandro Francisco Marcelo González    A01021383
Andrés Campos Tams                      A01024385
12 Jun 2020
'''

from ply import *
import Lex

# Recibe los tokens
tokens = Lex.tokens

#Definición de precedencia
precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('left', 'POTENCIA'),
    ('right', 'UMENOS')
)
cont = 1

# Definición de toda la gramática
def p_programa(p):
    '''programa : programa declaracion
               | declaracion'''
    global cont
    
    if len(p) == 2 and p[1]:
        p[0] = {}
        stat = p[1]
        p[0][cont] = stat
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = {}
        if p[2]:
            stat = p[2]
            p[0][cont] = stat
    cont+=1

def p_programa_error(p):
    '''programa : error'''
    p[0] = None
    p.parser.error = 1

def p_declaracion(p):
    '''declaracion : instruccion LINEA'''
    global cont
    if isinstance(p[1], str):
        print("%s %s %s" % (p[1], "EN LINEA", cont))
        p[0] = None
        p.parser.error = 1
    else:
        p[0] = (p[1])


def p_declaracion_blanca(p):
    '''declaracion : LINEA'''
    p[0] = (0, ('BLANCA', p[1]))


def p_declaracion_mala(p):
    '''declaracion : error LINEA
                    | error'''
    global cont
    print("Declaracion errónea en linea %d" % cont)
    p[0] = None
    p.parser.error = 1

def p_instruccion_salto(p):
    '''instruccion : SALTO ENTERO'''
    p[0] = ('SALTO', p[2])
    

def p_instruccion_var(p):
    '''instruccion : VAR variable IGUAL expr
                    | VAR variable IGUAL cadena'''
    p[0] = ('VAR', p[2], p[4])

def p_cadena(p):
    '''cadena : CADENA'''
    p[0] = ('CADENA', p[1].replace("\"",""))

def p_instruccion_imprimir(p):
    '''instruccion : IMPRIMIR IPAREN plista DPAREN'''
    p[0] = ('IMPRIMIR', p[3])

        
def p_instruccion_imprimir_vacio(p):
    '''instruccion : IMPRIMIR'''
    p[0] = ('IMPRIMIR', [], None)


def p_instruccion_finsi(p):
    '''instruccion : FINSI'''
    p[0] = ('FINSI', )


def p_instruccion_si(p):
    '''instruccion : SI IPAREN comparacion DPAREN ENTONCES ENTERO
                    | SI IPAREN comparacion DPAREN ENTONCES'''
    if len(p) == 7:
        p[0] = ('SI', p[3], int(p[6]))
    else:
        p[0] = ('SI', p[3], None)

def p_instruccion_para(p):
    '''instruccion : PARA PALABRA IGUAL expr A expr'''
    p[0] = ('PARA', p[2], p[4], p[6])

def p_instruccion_sig(p):
    '''instruccion : SIG PALABRA'''

    p[0] = ('SIG', p[2])


def p_instruccion_fin(p):
    '''instruccion : FIN'''
    p[0] = ('FIN',)


def p_instruccion_comentario(p):
    '''instruccion : COMENTARIO'''
    p[0] = ('COMENTARIO', p[1])

def p_instruccion_func_expr(p):
    '''instruccion : FUNC PALABRA IPAREN PALABRA DPAREN IGUAL expr'''
    p[0] = ('FUNC', p[2], p[4], p[7])


def p_instruccion_func(p):
    '''instruccion : FUNC PALABRA IPAREN DPAREN'''
    p[0] = ('FUNC', p[2], None, None)


def p_instruccion_func_ir(p):
    '''instruccion : PALABRA IPAREN DPAREN'''
    p[0] = ('IRFUNC', p[1])

def p_instruccion_func_fin(p):
    '''instruccion : FINFUNC PALABRA'''
    p[0] = ('FINFUNC', p[2])


def p_instruccion_arreglo(p):
    '''instruccion : ARREGLO arreglolista'''
    p[0] = ('ARREGLO', p[2])


def p_arreglolista(p):
    '''arreglolista : arreglolista COMA elementoarreglo
               | elementoarreglo'''
    if len(p) == 4:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]

def p_elementoarreglo_individual(p):
    '''elementoarreglo : PALABRA IPAREN ENTERO DPAREN'''
    p[0] = (p[1], eval(p[3]), 0)


def p_elementoarreglo_doble(p):
    '''elementoarreglo : PALABRA IPAREN ENTERO COMA ENTERO DPAREN'''
    p[0] = (p[1], eval(p[3]), eval(p[5]))

def p_expr_binaria(p):
    '''expr : expr MAS expr
            | expr MENOS expr
            | expr MULTIPLICACION expr
            | expr DIVISION expr
            | expr POTENCIA expr'''

    p[0] = ('BINOP', p[2], p[1], p[3])


def p_expr_numero(p):
    '''expr : ENTERO
            | FLOTANTE'''
    p[0] = ('NUM', eval(p[1]))


def p_expr_variable(p):
    '''expr : variable'''
    p[0] = ('VAR', p[1])


def p_expr_grupo(p):
    '''expr : IPAREN expr DPAREN'''
    p[0] = ('GRUPO', p[2])


def p_expr_unario(p):
    '''expr : MENOS expr %prec UMENOS'''
    p[0] = ('UNARIO', '-', p[2])

def p_comparacion(p):
    '''comparacion : expr MEQ expr
               | expr MEI expr
               | expr MAQ expr
               | expr MAI expr
               | expr II expr
               | expr IGUAL expr
               | expr DIF expr'''
    p[0] = ('COMP', p[2], p[1], p[3])

def p_variable(p):
    '''variable : PALABRA
              | PALABRA IPAREN expr DPAREN
              | PALABRA IPAREN expr COMA expr DPAREN'''
    if len(p) == 2:
        p[0] = (p[1], None, None)
    elif len(p) == 5:
        p[0] = (p[1], p[3], None)
    else:
        p[0] = (p[1], p[3], p[5])

def p_plista(p):
    '''plista   : plista COMA pelemento
               | pelemento'''
    if len(p) > 3:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]


def p_elemento_cadena(p):
    '''pelemento : CADENA'''
    p[0] = (p[1][1:-1], None)


def p_elemento_CADENA_expr(p):
    '''pelemento : CADENA expr'''
    p[0] = (p[1][1:-1], p[2])


def p_elemento_expr(p):
    '''pelemento : expr'''
    p[0] = ("", p[1])

    
def p_error(p):
    if not p:
        print("ERROR DE SINTAXIS, LINEA ", cont)

bparser = yacc.yacc()

def parse(data, debug=0):
    bparser.error = 0
    p = bparser.parse(data)
    if bparser.error:
        return None
    return p
