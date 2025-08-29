""" 
super se utiliza para acceder a un método o constructor de la clase padre

tiene un problema, que si una clase no espera parámetros y la que sigue 
en el orden de busqueda sí entonces genera error porque ya no tengo los
parámetros
entonces uso el *argv y **kwars para esos casos
*tuplas
**diccionarios
"""
class AbueloPaterno(): pass
class Padre(AbueloPaterno): pass
class Madre(): pass

class Hijo(Padre,Madre):

    def __init__ (self, arg, *args, **kwars):
        print("Hijo", "arg = ", arg)
        super(Hijo,self).__init__(arg,*args,**kwars) 