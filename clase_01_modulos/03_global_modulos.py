print('Hola')
nombre = 'Juan'

def funcion1(): pass

class Clase1(): pass

print('Chau')


"""
tenemos el main (este programa si se llamara main.py), una funcion, una clase

lo que permite __dict__ me da informacion de los namespaces que tengo
(el archivo que estoy trabajando)
.keys() me da el listado de las claves
me da la info que se esta guardando en memoria al traer esos namespaces
"""
import modulo5
print(list(modulo5.__dict__.keys()))

print( modulo5.__dict__['__file__']) #me da la ruta en donde esta el modulo
print( modulo5.__dict__['__name__']) # me da el nombre del modulo sin .py
"""ESTO ES UTIL PARA CONOCER LO QUE ESTAMOS TRAYENDO DE UN MODULO"""

"""el primer lugar donde busca el archivo es dentro de mi directorio
si yo creo un modulo sys y hago un import sys va a importar el mio, no el de python
Eso me puede llevar a tener errores si en otra parte estaba importando sys

"""

"""
El modulo 6 tiene x e y =88
tiene 2 funciones

llamando x o y hago referencia a la variable de este programa
llamando modulo6.x o modulo6.y llamo a la definida en el modulo
si llamo a una funcion del modulo que modifica la variable del modulo
entonces si modifica la variable global definida en ese modulo
"""
x=11
y=11
import modulo6
modulo6.f()
print(x,modulo6.x)
modulo6.g(1)
print(y.modulo6.y)