import numpy as np

"""Cuando se trabajan con arrays acceder a los elementos de este y extraer arrays
    a partir de uno ya existente son tareas que se realizan con frecuencia. Muchas
    de estas tareas se podrían realizar de ciertas formas que generan un tiempo 
    ejecucion mayor. A continuacion se mostrarán algunos ejemplos de las funcionalidades
    que ofrece el paquete de Numpy."""
    
"""RELLENAR CIERTO SECTOR DE UNA MATRIZ"""

np.random.seed(0)
Abase = np.random.randint(1, 11, size=(10,10))
A = Abase.copy()
"""Se obtiene: 
    
 [[ 6  1  4  4  8 10  4  6  3  5]
 [ 8  7  9  9  2  7  8  8  9  2]
 [ 6 10  9 10  5  4  1  4  6  1]
 [ 3  4  9  2  4  4  4  8  1  2]
 [10 10  1  5  8  4  3  8  3  1]
 [ 1  5  6  6  7  9  5  2  5 10]
 [ 9  2  2  8 10 10  4  7  8  3]
 [ 1  4  6 10  5  5  7  5  5  4]
 [ 5  5  9  5  4  8  6  6  1  2]
 [ 6 10  4  1  6  1  2  3  5  3]]
    
"""

B = Abase.copy()

print(A)
#ASIGNAR EL VALOR DE 0 A LOS VALORES MAYORES A 5

#Metodo 1
for i in range(10):
    for j in range(10):
        if A[i,j] >= 5:
            A[i, j] = 0

"""Durante la ejecucion del ciclo for se realiza la asignacion, elemento a elemento
    del valor que se desea en funcion de la condicion impuesta
"""

#Metodo 2 
B[B>=5] = 0

"""En la ejecucion de la anterior linea suceden dos cosas:
    1. Primero se genera una mascara, o array booleano, el cual 'le dice' al array 
    original en cuales posiciones debe realizar la accion que se especifica. Se emplea
    cualquier operador de comparacion: <, >, ==, !=, <=, >=; estos comparan cada elemento
    del array para verificar el cumplimiento de la condicion, y asi generar el array booleano.
    2. Luego, la máscara se emplea para determinar qué posiciones se les asignara el nuevo
    valor.

B>=5 -->Mascara: array booleano
[[ True False False False  True  True False  True False  True]
 [ True  True  True  True False  True  True  True  True False]
 [ True  True  True  True  True False False False  True False]
 [False False  True False False False False  True False False]
 [ True  True False  True  True False False  True False False]
 [False  True  True  True  True  True  True False  True  True]
 [ True False False  True  True  True False  True  True False]
 [False False  True  True  True  True  True  True  True False]
 [ True  True  True  True False  True  True  True False False]
 [ True  True False False  True False False False  True False]]

"""
"""Por medio de ambos metodos se obtiene:
    
 [[0 1 4 4 0 0 4 0 3 0]
 [0 0 0 0 2 0 0 0 0 2]
 [0 0 0 0 0 4 1 4 0 1]
 [3 4 0 2 4 4 4 0 1 2]
 [0 0 1 0 0 4 3 0 3 1]
 [1 0 0 0 0 0 0 2 0 0]
 [0 2 2 0 0 0 4 0 0 3]
 [1 4 0 0 0 0 0 0 0 4]
 [0 0 0 0 4 0 0 0 1 2]
 [0 0 4 1 0 1 2 3 0 3]]
 
 Sin embargo es recomendado usar el metodo 2, debido a su versatilidad y menos gasto computacional.
"""

"""CONDICIONES COMPUESTAS SOBRE UNA MATRIZ"""

"""Parte de la versatilidad ofrecida por los arrays booleanos se debe a que permiten
    realizar selecciones un poco mas especilizadas. Ya que es posible trabajar con estos
    junto a los operadores booleanos (and, or, not)."""
    
#Seleccionar valores mayores a 5 y menores a 10
C = Abase.copy()
print('Array con los elementos que cumplen la condicion: ',C[(C>5) & (C<10)])
print('Mascara de: (C>5) & (C<10): ')
print((C>5) & (C<10))

"""Cuando se emplean las mascaras con los operadores booleanos: &, | ; se debe tener en
    cuenta que la mascara debe ir entre parentesis. Estos operadores se ejecutan 
    elemento a elemento, por lo que cuando se empleen mascaras, la dimension de estas debe
    coincidir con la dimension de la matriz sobre la que se apliquen.
"""

"""CONTAR ELEMENTOS QUE CUMPLEN CON DETERMINADA CONDICION"""

cantidad = np.sum((C>6))
print('Cantidad de elementos en la matriz C mayores a 6: ',cantidad)

"""La funcion np.sum suma los elementos elementos en un array; si en este solo se
    ingresa el array sobre el que trabajar, la funcion retornara la suma de todos los
    elementos en este. Cuando se ingresa un array booleano, este tomara los elementos
    True como 1 y los False como 0."""

