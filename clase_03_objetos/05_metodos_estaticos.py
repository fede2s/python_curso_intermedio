"""
ya habiamos visto los metodos de instancia que tenian la palabra self
los metodos estaticos o de clase

tenemos que usar descriptores: es una palabra que se agrega antes de 
método/rutina/funcion precedido de un arroba, que hace algo sobre el 
método antes de que sea retornado
Descriptores:
    @classmethod
    @staticmethod

Al declarar un método como de clase, ya no puedo usar self,
no puedo usar atributos de instancia en un método de clase, solamente
puedo utilizar atributos de clase
metodos y atributos de clase son para todas las instancias, es global
"""
class OperacionesM():

    variable = "atributo de clase" # es un atributo de clase

    @classmethod
    def sumar(cls, a, b):
        c = a + b
        print(cls.variable)

        return c
    
obj = OperacionesM()
print(obj.sumar(2,3))

"""
el nombre de una inmobiliaria es el mismo para todos los inmuebles,
entonces es atributo de clase porque es más global
"""
#Los metodos de clase los puedo llamar directo de la clase
print(OperacionesM.sumar(2,3))

"""
El static method no es de clase ni de instancia, por tanto no puedo
utilizar atributos de instancia ni atributos de clase
"""

class OperacionesM():

    variable = "atributo de clase" # es un atributo de clase

    @staticmethod
    def sumar(a, b):
        c = a + b
        return c
    
obj = OperacionesM()
print(obj.sumar(2,3))