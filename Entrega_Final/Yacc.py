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
        print("%s %s %s" % (p[1], "AT LINEA", cont))
        p[0] = None
        p.parser.error = 1
    else:
        p[0] = (p[1])


def p_declaracion_blanca(p):
    '''declaracion : LINEA'''
    p[0] = (0, ('BLANCA', p[1]))


def p_declaracion_mala(p):
    '''declaracion : error LINEA'''
    print("Declaracion errónea en linea %s" % p[1])
    p[0] = None
    p.parser.error = 1


def p_instruccion_var(p):
    '''instruccion : VAR variable IGUAL expr'''
    p[0] = ('VAR', p[2], p[4])


def p_instruccion_mal_var(p):
    '''instruccion : VAR variable IGUAL error'''
    p[0] = "EXPRESION INCORRECTA EN VAR"


def p_instruccion_imprimir(p):
    '''instruccion : IMPRIMIR IPAREN plista DPAREN optend'''
    p[0] = ('IMPRIMIR', p[3], p[5])

def p_optend(p):
    '''optend : COMA 
              |'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = None
        
def p_instruccion_imprimir_mal(p):
    '''instruccion : IMPRIMIR error'''
    p[0] = "MALPARAMED IMPRIMIR declaracion"


def p_instruccion_imprimir_vacio(p):
    '''instruccion : IMPRIMIR'''
    p[0] = ('IMPRIMIR', [], None)


def p_instruccion_si(p):
    '''instruccion : SI IPAREN comparacion DPAREN ENTONCES ENTERO
                    | SI IPAREN comparacion DPAREN ENTONCES LINEA programa FINSI'''
    if len(p) == 7:
        p[0] = ('SI', p[3], int(p[6]))
    else:
        p[0] = ('SI', p[3], p[7])

def p_instruccion_si_mal(p):
    '''instruccion : SI error ENTONCES ENTERO'''
    p[0] = "EXPRESION MAL RELACIONADA"


def p_instruccion_si_mal2(p):
    '''instruccion : SI comparacion ENTONCES error'''
    p[0] = "ERROR EN LA LINEA POR EL NUMERO"


def p_instruccion_para(p):
    '''instruccion : PARA PALABRA IGUAL expr A expr optstep'''
    p[0] = ('PARA', p[2], p[4], p[6], p[7])


def p_instruccion_para_mal_initial(p):
    '''instruccion : PARA PALABRA IGUAL error A expr optstep'''
    p[0] = "mal INITIAL VALUE IN PARA declaracion"


def p_instruccion_para_mal_final(p):
    '''instruccion : PARA PALABRA IGUAL expr A error optstep'''
    p[0] = "mal FINAL VALUE IN PARA declaracion"


def p_instruccion_para_mal_step(p):
    '''instruccion : PARA PALABRA IGUAL expr A expr error'''
    p[0] = "MALPARAMED STEP IN PARA declaracion"

def p_optstep(p):
    '''optstep : expr
               | vacio'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None

def p_instruccion_sig(p):
    '''instruccion : SIG PALABRA'''

    p[0] = ('SIG', p[2])


def p_instruccion_sig_mal(p):
    '''instruccion : SIG error'''
    p[0] = "MALPARAMED SIG"


def p_instruccion_FIN(p):
    '''instruccion : FIN'''
    p[0] = ('FIN',)


def p_instruccion_rem(p):
    '''instruccion : COMENTARIO'''
    p[0] = ('COMENTARIO', p[1])


def p_instruccion_def(p):
    '''instruccion : FUNC PALABRA IPAREN PALABRA DPAREN IGUAL expr'''
    p[0] = ('FUNC', p[2], p[4], p[7])


def p_instruccion_def_mal_rhs(p):
    '''instruccion : FUNC PALABRA IPAREN PALABRA DPAREN IGUAL error'''
    p[0] = "mal EXPRESION IN DEF declaracion"


def p_instruccion_def_mal_arg(p):
    '''instruccion : FUNC PALABRA IPAREN error DPAREN IGUAL expr'''
    p[0] = "mal ARGUMENT IN DEF declaracion"

def p_instruccion_regresar(p):
    '''instruccion : REGRESAR'''
    p[0] = ('REGRESAR',)

def p_instruccion_arreglo(p):
    '''instruccion : ARREGLO arreglolista'''
    p[0] = ('ARREGLO', p[2])


def p_instruccion_arreglo_mal(p):
    '''instruccion : ARREGLO error'''
    p[0] = "MALPARAMED VARIABLE LIST IN ARREGLO"

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


def p_expr_groupo(p):
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

def p_varlista(p):
    '''varlista : varlista COMA variable
               | variable'''
    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]

def p_numlista(p):
    '''numlista : numlista COMA numero
               | numero'''

    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]

def p_numero(p):
    '''numero  : ENTERO
               | FLOTANTE'''
    p[0] = eval(p[1])

def p_numero_signo(p):
    '''numero  : MENOS ENTERO
               | MENOS FLOTANTE'''
    p[0] = eval("-" + p[2])

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

def p_vacio(p):
    '''vacio : '''
    
def p_error(p):
    if not p:
        print("ERROR DE SINTAXIS")

bparser = yacc.yacc()

def parse(data, debug=0):
    bparser.error = 0
    p = bparser.parse(data, debug=debug)
    if bparser.error:
        return None
    return p
