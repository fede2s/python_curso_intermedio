"""
una clase engloba rutinas y engloba atributos
las rutinas son funciones: comer, saltar, bailar
dentro de las clases se llaman métodos
atributos: color de ojos, color de pelo, etc, son variables

VAMOS A VER UN MÉTODO DE INSTANCIA
"""
#antes las funciones eran de este formato
def sumar(a,b):
    c = a + b
    return c

sumar(2,3)

# ahora tenemos las clases
class OperacionesM():

    #las funciones en una clase son métodos
    # de instancia
    # tambien hay de objeto o fijos 
    # los metodos de instancia tienen self, en otros lenguajes es this
    def sumar(self,a,b):
        c = a + b
        print("1: ", self) #self referencia al objeto
        return c
    
# instanciacion de objeto
obj = OperacionesM()

# utilizo el método
obj.sumar(2,3)

print("1: ", obj) # me imprime lo mismo que self desde dentro de la clase

