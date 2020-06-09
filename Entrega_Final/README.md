# ESPY
Orientaciones para comprender la estructura del lenguaje de programación llamado ESPY. 
En este proyecto se encuentran los archivos necesarios para comprender los siguientes puntos del lenguaje.

1. Análisis Léxico
2. Análisis Sintáctico 
3. Validación de Tipado. 

Para la creación del *Lexer* y *Parser* se utilizó la librería `PLY.py` ya que provee una cantidad de herramientas muy útiles para poder trabajar con tokens y gramáticas de una forma mucho más entendible que creando desde cero los algoritmos.
Si te interesa saber más de la librería `PLY.py`, [Haz click aquí](https://www.dabeaz.com/ply/)

## 0. Pre-requisitos
* Poder correr programas de Python3.
* Instalar dependencias `pip3 install -r requirements.txt`

## 1. Análisis Léxico 
El análisis léxico se encuentra en el documento `Lex.py`, en el se localizan los tokens utilizados y las palabras clave.
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
| IGUAL |  |
| MAS |  |
| MENOS |  |
| MULTIPLICACION |  |
| DIVISION |  |
| POTENCIA |  |
| IPAREN |  |
| DPAREN |  |
| MEQ |  |
| MEI |  |
| MAQ |  |
| MAI |  |
| DIF |  |
| COMA |  |
| ENTERO |  |
| FLOTANTE |  |
| CADENA |  |
| PALABRA |  |
| LINEA |  |



## 2. Análisis Sintáctico 

## 3. Validación de Tipado

