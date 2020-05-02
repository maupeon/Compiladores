# Compiladores Tarea 2
## LEXER

Orientaciones para correr el programa que, a partir de un archivo de entrada, muestra los tokens válidos. 

## 0. Pre-requisitos
* Poder correr programas de Python3.

## 1. Instalar las dependencias
`pip3 install -r requirements.txt`

## 2. Introducir los tokens a evaluar (código)
* Un ejemplo se muestra en el archivo code.txt
* Para validar los tokens, se muestra de la siguiente manera:
  - `ent age = 17;`
  - `dec mau = 17.999842;`
  - `int 54hola`

* Definición de tokens:
  - "ent" definición de entero.
  - "dec" definición de decimal y notación científica.
  - "<, >, +, -, /, *, or, and, <=, >=, =" definición de operadores.
  - "Cualquier palabra que empiece con una letra" definición de variable.
  - "!!! o ¡¡¡" definición de comentario.
  - "Lo que no se encuentre en estas definiciones, son tokens inválidos."

## 3. Ejecutar en la consola
`python3 tarea2.py`

## 4. Explicación del archivo de salida.
En el archivo de salida: `output.txt` se encuentra la definición de los tokens en el mismo orden en el que fue leído, ejemplos:

code.txt
 - `ent age = 17;`
 - `dec mau = 17.999842;`

output.txt
 - `identifier variable operator int ;`
 - `identifier variable operator int operator int ;`


## 5. Eliminar proyecto.
Para dejar de usar el proyecto, solamente se rquiere eliminar el repositorio raíz.
 - `cd ..`
 - `rm -rf Compiladores`

