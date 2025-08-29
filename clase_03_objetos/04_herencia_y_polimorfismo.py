"""
herencia
si tengo clase bicicletas
puedo heredarle a:
    bicicletas traccion delantera
    bicicletas traccion trasera

cada una de esas clases es un nodo

ademas podria tener
clase 1 hereda a clase 2a y clase2b
clase2a y clase2b heredan a clase3
o sea puedo tener una clase que hereda de 2 clases

en estos casos en python 3 se busca primero en clase3, despues clase2a y clase2b y despues clase1
en python 2 en ese caso se busca clase3, clase2a y clase1 ; despues clase3, clase2b y clase1
"""

class Persona():
    def __init__(self,nombre):
        self.nombre = nombre

    def comer_arroz(self):
        print("Comer arroz desde Persona")

"""
puedo usar los atributos o metodos de la clase de arriba
"""
class Cultura(): pass

class Argentinos(Persona, Cultura):
    def __init__(self, nombre):
        self.nombre = nombre

    def comer_arroz(self): 
        print("como arroz con tenedor")

class Chinos(Persona):
    def __init__(self, nombre):
        self.nombre = nombre

    def comer_arroz(self): 
        print("como arroz con palillos")

anna = Persona("Anna")
juan = Persona("Juan")
pepe = Argentinos("pepe")
chino = Chinos("chinchon")

anna.comer_arroz()
juan.comer_arroz()
pepe.comer_arroz()
chino.comer_arroz()

"""
Polimorfismo: pisar la funcionalidad de una clase de la cual heredo
los argentinos comen arroz con tenedor
los chinos comen arroz con palillos
y desde persona se comia arroz desde persona

clase.__mro__ me devuelve la estructura que python encuentra de las clases
"""
print(Chinos.__mro__)
"""
me devuelve:
    (<class '__main__.Chinos'>, <class '__main__.Persona'>, <class 'object'>)

"""

print(Argentinos.__mro__)
"""
me devuelve
    (<class '__main__.Argentinos'>, <class '__main__.Persona'>, <class '__main__.Cultura'>, <class 'object'>)
    
"""

"""Conclusion: el metodo __mro__ de una clase me permite entender facilmente la arquitectura de la clase"""