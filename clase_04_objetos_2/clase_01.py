#para testear un programa
if __name__=="__main__":
    """acá pongo mis test
    Ej: instancio objetos de la clase que tengo en este archivo y los pruebo"""

"""
puedo trabajar con una base de datos shelve guardando objetos
"""
import shelve
class Persona:pass

juan = Persona()
tom = Persona()

base_personas = [juan, tom]

db=shelve.open("personas")
db["juan"] = juan
db["tom"] = tom
db.close()