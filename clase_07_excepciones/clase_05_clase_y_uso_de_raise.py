"""##################################################################

Tenemos distintos tipos de excepciones y vimos como usarlas, pero
vamos a ver como crear mis propias clases para manejar errores.

Toda clase que yo quiero que sea excepcion, necesito que herede de 
exception
"""

class B(Exception):
    color="rojo" # atributo de clase

class C(B):
    color="verde"

class D(C):
    color="azul"

"""
cls se le suele llamar a las clases de la misma forma que self se
suele utilizar para llamar a las instancias de clase
"""
for cls in [B,C,D]: 
    try:
        raise cls()
    except D:
        print("D")
        print(D.color)
        print(cls.color)
    except C:
        print("C")
        print(C.color)
    except B:
        print("B")
        print(B.color)

""" el for instancia una por una las clases y evalua si salta alguna
es decir, podria tener una para saber si son enteros, otra para saber
si son strings, etc."""