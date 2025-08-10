"""hay 3 tipos de modulos
-los que vienen en el nucleo de python: sys, os, etc
-realizados por terceros (librerias): 
    django (framework para paginas web)
    kivy(apps de escritorio)
    pyqt(interfaz grafica)
-un modulo es un script .py

los de terceros se ubican en un directorio python/lib/site-packages/
se instalan con pip install ...

nuestros modulos se van a ubicar en principio en el directorio que 
estemos trabajando hasta que aprendamos a crear paquetes
nos sirven para quitar logica del programa principal

"""
"""Ejercicio a"""
import modulo1
import sys
print(sys.path)

# modulo importado + punto + funcion imprimir definida dentro del modulo
modulo1.imprimir('Mensjae a imprimir')
print(sys.modules)

"""Ejercicio b"""
import modulo2
# modulo + punto + variable
print(modulo2.color) # imprime el valor original
modulo2.color = 'verde'
print(modulo2.color) #imprime verde
import modulo2
print(modulo2.color)# imprime verde porque solamente se importa la primera vez
# lo que se puede hacer es un prolog, relectura de modulo, pero lo vamos a ver
# mas adelante
"""esa importacion es como importar un diccionario que solo se importa una vez
por lo tanto la clave color no se sobreescribe"""

"""Ejercicio c
modulo3 tiene x =1 e y=[1,2]
x es inmutable pero y es mutable
"""
x=42
y[0] = 84
print(x)
print(y[0])
print(y)
from modulo3 import x,y
print(x)
print(y[0])
print(y)
""" x se reasigna a 42 y el primer valor de la lista tambien
imprime 
42
84
[84,2]
1
84
[84,2]

aca tenemos modulo3.x= 1 y tenemos x=42 que no es lo mismo 
porque no es la misma x. La lista al ser inmutable sigue siendo la misma
pero el valor de la primera posicion se cambia

"""