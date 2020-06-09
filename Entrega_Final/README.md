# ESPY

Orientaciones para comprender la estructura del lenguaje de programación llamado ESPY. 
En este proyecto se encuentran los archivos necesarios para comprender los siguientes puntos del lenguaje.

1. Análisis Léxico
2. Análisis Sintáctico 
3. Validación de Tipado. 

Para la creación del *Lexer* y *Parser* se utilizó la librería `PLY.py` ya que provee una cantidad de herramientas muy útiles para poder trabajar con tokens y gramáticas de una forma mucho más entendible que creando desde cero los algoritmos.
Si te interesa saber más de la librería `PLY.py`, [haz click aquí](https://www.dabeaz.com/ply/)

## 0. Pre-requisitos

* Poder correr programas de Python3.
* Instalar dependencias `pip3 install -r requirements.txt`

## 1. Análisis Léxico 

El análisis léxico se encuentra en el documento `Lex.py`, en el se localizan los tokens utilizados y las palabras clave. La creación del lexer fue realizada por el módulo `lex` de la librería `PLY.py`
A continuación se presenta una tabla con cada palabra clave y su descripción:

| Palabra Clave | Descripción | Ejemplo
| --- | --- | --- |
| VAR | Indica que la palabra que viene después, será considerada como variable | |
| IMPRIMIR | Similar a 'print' en python, imprime el contenido que le mandes | |
| SI | Condicional para realizar una operación  | |
| ENTONCES | Define que operación se realizará si la condición del SI se cumple | |
| PARA | Ciclo funcional en la que se le puede indicar de antemano el número de iteraciones |
| SIG | Instrucción que indica el regreso a la primera línea del PARA |
| A | Indica hacia que iteración irá el ciclo PARA | |
| FIN | Define el final del programa | |
| FUNC | Declaración de funciones | |
| ARREGLO |  | |
| COMENTARIO | Está representado por un "#", todo lo que viene después de ese símbolo, no se procesará | |
| REGRESAR | Indica el fin de una función | |

A continuación se presenta una tabla con cada palabra clave y su descripción:
| Token | Descripción |
| --- | --- |
| IGUAL | Es la definición del símbolo "=" para poder hacer operaciones |
| MAS | Es la definición del símbolo "+" para poder hacer operaciones |
| MENOS | Es la definición del símbolo "-" para poder hacer operaciones |
| MULTIPLICACION | Es la definición del símbolo "*" para poder hacer operaciones |
| DIVISION | Es la definición del símbolo "/" para poder hacer operaciones |
| POTENCIA | Es la definición del símbolo "^" para poder hacer operaciones |
| IPAREN | Es la definición del símbolo "(" para poder agrupar expresiones |
| DPAREN | Es la definición del símbolo ")" para poder agruar expresiones |
| MEQ | Es la definición del símbolo "<" para poder hacer operaciones y comparaciones |
| MEI | Es la definición del símbolo "<=" para poder hacer operaciones y comparaciones|
| MAQ | Es la definición del símbolo ">" para poder hacer operaciones y comparaciones|
| MAI | Es la definición del símbolo ">=" para poder hacer operaciones y comparaciones|
| DIF | Es la definición del símbolo "!=" para poder hacer operaciones  y comparaciones|
| COMA | Es la definición del símbolo ","  |
| ENTERO | Es la definición de números enteros |
| FLOTANTE | Es la definición de números flotantes |
| CADENA | Es la definición cualquier cadena de caracteres |
| PALABRA | Es la definición de variables, va en conjunto con el token VAR |
| LINEA | Indica si hay un salto de línea |

## 2. Análisis Sintáctico 

En el análisis sintáctico se verifica si la estructura del lenguaje es correcta, para ello se usó el módulo `yacc` de la librería `PLY.py`. Es importante decir que el *parser* necesita del *lexer* para poder recibri todos los tokens de la gramática, así como las palabras clave.

Las reglas utilizadas en la gramática del lenguaje fueron las siguientes:
```
Rule 0     S' -> programa
Rule 1     programa -> programa declaracion
Rule 2     programa -> declaracion
Rule 3     programa -> error
Rule 4     declaracion -> ENTERO instruccion LINEA
Rule 5     declaracion -> ENTERO LINEA
Rule 6     declaracion -> ENTERO error LINEA
Rule 7     declaracion -> LINEA
Rule 8     instruccion -> VAR variable IGUAL expr
Rule 9     instruccion -> VAR variable IGUAL error
Rule 10    instruccion -> IMPRIMIR IPAREN plista DPAREN optend
Rule 11    optend -> COMA
Rule 12    optend -> <empty>
Rule 13    instruccion -> IMPRIMIR error
Rule 14    instruccion -> IMPRIMIR
Rule 15    instruccion -> SI IPAREN comparacion DPAREN ENTONCES ENTERO
Rule 16    instruccion -> SI error ENTONCES ENTERO
Rule 17    instruccion -> SI comparacion ENTONCES error
Rule 18    instruccion -> PARA PALABRA IGUAL expr A expr optstep
Rule 19    instruccion -> PARA PALABRA IGUAL error A expr optstep
Rule 20    instruccion -> PARA PALABRA IGUAL expr A error optstep
Rule 21    instruccion -> PARA PALABRA IGUAL expr A expr error
Rule 22    optstep -> expr
Rule 23    optstep -> vacio
Rule 24    instruccion -> SIG PALABRA
Rule 25    instruccion -> SIG error
Rule 26    instruccion -> FIN
Rule 27    instruccion -> COMENTARIO
Rule 28    instruccion -> FUNC PALABRA IPAREN PALABRA DPAREN IGUAL expr
Rule 29    instruccion -> FUNC PALABRA IPAREN PALABRA DPAREN IGUAL error
Rule 30    instruccion -> FUNC PALABRA IPAREN error DPAREN IGUAL expr
Rule 31    instruccion -> REGRESAR
Rule 32    instruccion -> ARREGLO arreglolista
Rule 33    instruccion -> ARREGLO error
Rule 34    arreglolista -> arreglolista COMA elementoarreglo
Rule 35    arreglolista -> elementoarreglo
Rule 36    elementoarreglo -> PALABRA IPAREN ENTERO DPAREN
Rule 37    elementoarreglo -> PALABRA IPAREN ENTERO COMA ENTERO DPAREN
Rule 38    expr -> expr MAS expr
Rule 39    expr -> expr MENOS expr
Rule 40    expr -> expr MULTIPLICACION expr
Rule 41    expr -> expr DIVISION expr
Rule 42    expr -> expr POTENCIA expr
Rule 43    expr -> ENTERO
Rule 44    expr -> FLOTANTE
Rule 45    expr -> variable
Rule 46    expr -> IPAREN expr DPAREN
Rule 47    expr -> MENOS expr
Rule 48    comparacion -> expr MEQ expr
Rule 49    comparacion -> expr MEI expr
Rule 50    comparacion -> expr MAQ expr
Rule 51    comparacion -> expr MAI expr
Rule 52    comparacion -> expr IGUAL expr
Rule 53    comparacion -> expr DIF expr
Rule 54    variable -> PALABRA
Rule 55    variable -> PALABRA IPAREN expr DPAREN
Rule 56    variable -> PALABRA IPAREN expr COMA expr DPAREN
Rule 57    varlista -> varlista COMA variable
Rule 58    varlista -> variable
Rule 59    numlista -> numlista COMA numero
Rule 60    numlista -> numero
Rule 61    numero -> ENTERO
Rule 62    numero -> FLOTANTE
Rule 63    numero -> MENOS ENTERO
Rule 64    numero -> MENOS FLOTANTE
Rule 65    plista -> plista COMA pelemento
Rule 66    plista -> pelemento
Rule 67    pelemento -> CADENA
Rule 68    pelemento -> CADENA expr
Rule 69    pelemento -> expr
Rule 70    vacio -> <empty>
```

Para más información sobre la gramática, favor de revisar el documento `parser.out` generado por `PLY`


## 3. Validación de Tipado

