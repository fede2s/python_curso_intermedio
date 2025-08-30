"""##################################################################
que pasa si se da un anidamiento de excepciones?
si yo lanzo una excepcion y esa lanza a otra que pasa?
se ejecuta la que esta mas adentro primero
"""
def evento2():
    print(1+"pera")

def evento1():
    try:
        evento2()
    except TypeError:
        print("Try interno")

try:
    evento1()
except TypeError:
    print("Try externo")