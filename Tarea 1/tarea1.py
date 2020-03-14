"""
    Tarea 1
    Fecha de Entrega: 14 de Marzo de 2020

    Estudiantes:
    Mauricio Peón García                        A01024162
    Alexandro Francisco Marcelo González        A
    Andrés Campos Tams                          A
"""

def regex_to_NFA(string):
    print(string)


def menu():
    print('**************************** WELCOME TO COMPILATORS ****************************')
    string = 1
    pilas = []

    while string != 0:
        string = int(input('Enter your input: ') )
        regex = input('Enter your regex: ')
        print(regex)
       
        for i,e in enumerate(regex):
            #char2 = char
            if e is '(':
                pila = []
                for j in regex[i:]:
                    print(j)
                    if j is ')':
                        break
                    pila.append(j)
                print(pila)
                pilas.append(pila)

    print(pilas)



#regex(string)
menu()