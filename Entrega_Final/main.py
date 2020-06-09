'''
Mauricio Peón García                    A01024162
Alexandro Francisco Marcelo González    A01021383
Andrés Campos Tams                      A01024385
12 Jun 2020
'''

import sys
sys.path.insert(0, "../..")

import Lex
import Yacc
import Interpreter

# Recibe un archivo como parámetro, ejemplo: input.espy (la terminación no importa)
if len(sys.argv) == 2:
    with open(sys.argv[1]) as f:
        data = f.read()
    prog = Yacc.parse(data)
    #print("PROG:",prog)
    if not prog:
        raise SystemExit
    compilador = Interpreter.Interpreter(prog)
    try:
        compilador.ejecutar()
        raise SystemExit
    except RuntimeError:
        pass

else:
    compilador = Interpreter.Interpreter({})
