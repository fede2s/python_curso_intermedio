"""
Un constructor es una de las formas de ingreso a la clase
Es para cuando trabajamos en equipo
necesito un constructor para pasarle info a la clase? No, puedo tener clases sin constructor
es conveniente para trabajo en equipo? si, porque voy a declarar los parametros que usa la clase
Podria definir una clase sin constructor

Constructores:
    __init__
    __new__
"""

class OperacionesM():
    def __init__(self, ): #init es el constructor
        pass

    def sumar(self, a, b):
        c = a + b
        return c
    
obj=OperacionesM()
print(obj.sumar(2,3))

#############################
class Persona():
    def __init__(self, nombre ):
        self.nombre = nombre
    
    def comer_arroz(self):
        pass

anna = Persona("Anna Karen")
juan = Persona("Juan Marcelo")

print(anna.nombre)
print(juan.nombre)