'''
Mauricio Peón García                    A01024162
Alexandro Francisco Marcelo González    A01021383
Andrés Campos Tams                      A01024385
12 Jun 2020
'''

import sys
import math
import random


class Interpreter:

    # Inicializar el interprete
    def __init__(self, prog):
        self.prog = prog

        self.funciones = {           # Tabla de funciones matemáticas
            'SIN': lambda z: math.sin(self.eval(z)),
            'COS': lambda z: math.cos(self.eval(z)),
            'TAN': lambda z: math.tan(self.eval(z)),
            'ATN': lambda z: math.atan(self.eval(z)),
            'EXP': lambda z: math.exp(self.eval(z)),
            'ABS': lambda z: abs(self.eval(z)),
            'LOG': lambda z: math.log(self.eval(z)),
            'SQR': lambda z: math.sqrt(self.eval(z)),
            'INT': lambda z: int(self.eval(z)),
            'RND': lambda z: random.random()
        }

    # Checa si está la palabra FIN en el programa
    def checar_fin(self):
        tiene_fin = 0
        for num_linea in self.stat:
            if self.prog[num_linea][0] == 'FIN' and not tiene_fin:
                tiene_fin = num_linea
        if not tiene_fin:
            print("No hay una instrucción final para 'PARA'")
            self.error = 1
            return
        if tiene_fin != num_linea:
            print("FIN NO ESTÁ AL FINAL")
            self.error = 1

    # Checa la cantidad de ciclos que hay en el programa
    def checar_ciclos(self):
        for contador in range(len(self.stat)):
            num_linea = self.stat[contador]
            if self.prog[num_linea][0] == 'PARA':
                ciclo_i = self.prog[num_linea]
                ciclo_var = ciclo_i[1]
                for i in range(contador + 1, len(self.stat)):
                    if self.prog[self.stat[i]][0] == 'SIG':
                        sig_var = self.prog[self.stat[i]][1]
                        if sig_var != ciclo_var:
                            continue
                        self.fin_ciclo[contador] = i
                        break
                else:
                    print("PARA sin SIG linea %s" % self.stat[contador])
                    self.error = 1

    # Función para evaluar expresiones
    def eval(self, expr):
        tipo = expr[0]
        if tipo == 'NUM':
            return expr[1]
        elif tipo == 'GRUPO':
            return self.eval(expr[1])
        elif tipo == 'UNARIO':
            if expr[1] == '-':
                return -self.eval(expr[2])
        elif tipo == 'BINOP':
            if expr[1] == '+':
                return self.eval(expr[2]) + self.eval(expr[3])
            elif expr[1] == '-':
                return self.eval(expr[2]) - self.eval(expr[3])
            elif expr[1] == '*':
                return self.eval(expr[2]) * self.eval(expr[3])
            elif expr[1] == '/':
                return float(self.eval(expr[2])) / self.eval(expr[3])
            elif expr[1] == '^':
                return abs(self.eval(expr[2]))**self.eval(expr[3])
        elif tipo == 'VAR':
            var, dim1, dim2 = expr[1]
            if not dim1 and not dim2:
                if var in self.vars:
                    return self.vars[var]
                else:
                    print("VARIABLE NO DEFINIDA %s EN LA LINEA %s" %
                          (var, self.stat[self.contador]))
                    raise RuntimeError
            # Checar si hay funciones
            if dim1 and not dim2:
                if var in self.funciones:
                    # Una funcuión
                    return self.funciones[var](dim1)
                else:
                    # Lista de evluaciones
                    if var in self.listas:
                        dim1val = self.eval(dim1)
                        if dim1val < 1 or dim1val > len(self.listas[var]):
                            print("ÍNDICE DE LISTA FUERA DE RANGO %s" %
                                  self.stat[self.contador])
                            raise RuntimeError
                        return self.listas[var][dim1val - 1]
            if dim1 and dim2:
                if var in self.tablas:
                    dim1val = self.eval(dim1)
                    dim2val = self.eval(dim2)
                    if dim1val < 1 or dim1val > len(self.tablas[var]) or dim2val < 1 or dim2val > len(self.tablas[var][0]):
                        print("ÍNDICES FUERA DE RANGO %s" %
                              self.stat[self.contador])
                        raise RuntimeError
                    return self.tablas[var][dim1val - 1][dim2val - 1]
            print("VARIABLE NO DEFINIDA %s EN LA LINEA %s" %
                  (var, self.stat[self.contador]))
            raise RuntimeError

    # Evaluación de una expresión para comparación de variables
    def comparacion(self, expr):
        tipo = expr[1]
        izq = self.eval(expr[2])
        der = self.eval(expr[3])
        if tipo == '<':
            if izq < der:
                return 1
            else:
                return 0

        elif tipo == '<=':
            if izq <= der:
                return 1
            else:
                return 0

        elif tipo == '>':
            if izq > der:
                return 1
            else:
                return 0

        elif tipo == '>=':
            if izq >= der:
                return 1
            else:
                return 0

        elif tipo == '==':
            if izq == der:
                return 1
            else:
                return 0

        elif tipo == '=':
            if izq == der:
                return 1
            else:
                return 0

        elif tipo == '!=':
            if izq != der:
                return 1
            else:
                return 0

    # Asignación de variables
    def asignacion(self, objetivo, valor):
        var, dim1, dim2 = objetivo
        if not dim1 and not dim2:
            self.vars[var] = self.eval(valor)
        elif dim1 and not dim2:
            # Lista de asignaciones
            dim1val = self.eval(dim1)
            if not var in self.listas:
                self.listas[var] = [0] * 10

            if dim1val > len(self.listas[var]):
                print ("DIMENSIÓN MUY LARGA EN LINEA %s" % self.stat[self.contador])
                raise RuntimeError
            self.listas[var][dim1val - 1] = self.eval(valor)
        elif dim1 and dim2:
            dim1val = self.eval(dim1)
            dim2val = self.eval(dim2)
            if not var in self.tablas:
                temp = [0] * 10
                v = []
                for i in range(10):
                    v.append(temp[:])
                self.tablas[var] = v
            # Variable already exists
            if dim1val > len(self.tablas[var]) or dim2val > len(self.tablas[var][0]):
                print("DIMENSIÓN MUY LARGA EN LINEA %s" % self.stat[self.contador])
                raise RuntimeError
            self.tablas[var][dim1val - 1][dim2val - 1] = self.eval(valor)
#########################################################################################
    # Change the current line number
    def goto(self, linenum):
        if not linenum in self.prog:
            print("NUMERO DE LINEA NO DEFINIDA %d EN LA LINEA %d" %
                  (linenum, self.stat[self.contador]))
            raise RuntimeError
        self.contador = self.stat.index(linenum)
#########################################################################################
    # ejecutar it
    def ejecutar(self):
        self.vars = {}            # Todas las variables
        self.listas = {}            # Lista de variables
        self.tablas = {}            # Tablas
        self.ciclos = []            # Todos los ciclos
        self.fin_ciclo = {}        # Definir en donde terminan los ciclos
        self.gosub = None           # Gosub return point (if any)
        self.error = 0              # Error en programa

        self.stat = list(self.prog)  # Lista ordenada del programa
        self.stat.sort()
        self.contador = 0                  # Contador del programa

        # Funciones de ayuda
        self.checar_fin
        self.checar_ciclos()

        if self.error:
            raise RuntimeError

        while 1:
            linea = self.stat[self.contador]
            instr = self.prog[linea]

            op = instr[0]
            # DECLARACIÓN DE FIN
            if op == 'FIN':
                break           # Termina el programa

            # DECLARACIÓN DE GOTO 
            elif op == 'GOTO':
                nueva_linea = instr[1]
                self.goto(nueva_linea)
                continue

            # DECLARACIÓN DE IMPRIMIR
            elif op == 'IMPRIMIR':
                plista = instr[1]
                salida = ""
                for etiqueta, val in plista:
                    if salida:
                        salida += ' ' * (15 - (len(salida) % 15))
                    salida += etiqueta
                    if val:
                        if etiqueta:
                            salida += " "
                        eval = self.eval(val)
                        salida += str(eval)
                sys.stdout.write(salida)
                end = instr[2]
                if not (end == ',' or end == ';'):
                    sys.stdout.write("\n")
                if end == ',':
                    sys.stdout.write(" " * (15 - (len(salida) % 15)))
                if end == ';':
                    sys.stdout.write(" " * (3 - (len(salida) % 3)))

            # VAR statement
            elif op == 'VAR':
                objetivo = instr[1]
                valor = instr[2]
                self.asignacion(objetivo, valor)

            elif op == 'SI':
                comp = instr[1]
                nueva_linea = instr[2]
                if (self.comparacion(comp)):
                    if(type(nueva_linea) == dict):
                        print("ENTREO")
                        stat_aux = []
                        stat_aux = list(nueva_linea)  # Ordered list of all line numbers
                        stat_aux.sort()
                        contador_aux = stat_aux[0]                 # Current program counter
                        while 1:
                            # END and STOP statements
                            if contador_aux == stat_aux[len(stat_aux)-1]+1:
                                break           # We're done
                            line = contador_aux
                            instr = nueva_linea[contador_aux]
                            op = instr[0]

                            # PRINT statement
                            if op == 'IMPRIMIR':
                                plista = instr[1]
                                salida = ""
                                for etiqueta, val in plista:
                                    if salida:
                                        salida += ' ' * (15 - (len(salida) % 15))
                                    salida += etiqueta
                                    if val:
                                        if etiqueta:
                                            salida += " "
                                        eval = self.eval(val)
                                        salida += str(eval)
                                sys.stdout.write(salida)
                                fin = instr[2]
                                if not (fin == ',' or fin == ';'):
                                    sys.stdout.write("\n")
                                if fin == ',':
                                    sys.stdout.write(" " * (15 - (len(salida) % 15)))
                                if fin == ';':
                                    sys.stdout.write(" " * (3 - (len(salida) % 3)))

                            # VAR statement
                            elif op == 'VAR':
                                objetivo = instr[1]
                                valor = instr[2]
                                self.asignacion(objetivo, valor)

                            contador_aux += 1

                        self.contador+=1
                    else:
                        self.goto(nueva_linea)
                    continue

            elif op == 'PARA':
                ciclo_var = instr[1]
                valor_inicial = instr[2]
                valor_final = instr[3]
                sig_val = instr[4]

                # Checar si es un nuevo civlo
                if not self.ciclos or self.ciclos[-1][0] != self.contador:
                    # Nuevo ciclo
                    nuevo_valor = valor_inicial
                    self.asignacion((ciclo_var, None, None), valor_inicial)
                    if not sig_val:
                        sig_val = ('NUM', 1)
                    sig_val = self.eval(sig_val)    # Evaluar los valores siguientes
                    self.ciclos.append((self.contador, sig_val))
                else:
                    # Es el mismo ciclo anterior
                    sig_val = ('NUM', self.ciclos[-1][1])
                    nuevo_valor = (
                        'BINOP', '+', ('VAR', (ciclo_var, None, None)), sig_val)

                if self.ciclos[-1][1] < 0:
                    comp = '>='
                else:
                    comp = '<='
                if not self.comparacion(('COMP', comp, nuevo_valor, valor_final)):
                    # Termina el ciclo
                    self.contador = self.fin_ciclo[self.contador]
                    self.ciclos.pop()
                else:
                    self.asignacion((ciclo_var, None, None), nuevo_valor)

            elif op == 'SIG':
                if not self.ciclos:
                    print("SIG SIN PARA EN LA LINEA %s" % line)
                    return

                sig_var = instr[1]
                self.contador = self.ciclos[-1][0]
                loopinst = self.prog[self.stat[self.contador]]
                forvar = loopinst[1]
                if sig_var != forvar:
                    print("SIG NO TIENE SU PARA CORRESPONDIENTE%s" % line)
                    return
                continue
            

            elif op == 'REGRESAR':
                if not self.gosub:
                    print("REGRESAR sin a GOSUB en linea %s" % line)
                    return
                self.goto(self.gosub)
                self.gosub = None

            elif op == 'FUNC':
                f_nombre = instr[1]
                p_nombre = instr[2]
                expr = instr[3]

                def eval_func(pvalor, name=p_nombre, self=self, expr=expr):
                    self.asignacion((p_nombre, None, None), pvalor)
                    return self.eval(expr)
                self.funciones[f_nombre] = eval_func

            elif op == 'ARREGLO':
                for v_nombre, x, y in instr[1]:
                    if y == 0:
                        # Arreglo de una dimensión
                        self.listas[v_nombre] = [0] * x
                    else:
                        # Arreglo de dos dimensiones
                        temp = [0] * y
                        v = []
                        for i in range(x):
                            v.append(temp[:])
                        self.tablas[v_nombre] = v

            self.contador += 1
        #print("VARIABLES USADAS:", self.vars)