"""
Cuando nos descargamos una libreria/una app, no es comun 
que esté en un único archivo. Django por ejemplo no tiene
un único directorio, y cada directorio tiene sus directorios
propios.

Cuando trabajamos con módulos y comienzan a crecer es normal
que se ordenen en grupos de directorios anidados.

En este caso tenemos dir0/dir1/dir2/__init__.py

Cada módulo que tenemos tiene que tener un archivo __init__.py
guarda informacion de la ruta hacia los elementos que queremos
ubicar.

Cuando yo importo import dir1.dir2.mod aun cuando yo no importe
los archivos __init__.py sino otros, igualmente se importan y 
se ejecutan. Aunque estén vacíos tienen que estar porque python
los utiliza para armar las rutas, los namespaces.

El profe no aclaró pero pone los archivos en carpetas __pycache__
"""

import dir1.dir2.mod
print(dir1.x) # en el __init__ de dir1 tenía definido una x
print(dir1.dir2.y) # en el __init__ de dir2 tenia una var y
print(dir1.dir2.mod.z) # en el dir2 tenía un mod.py con una var z

"""
Si yo defino una variable con 2 guiones bajos estoy definiendo
una variable privada
Tengo algunas que son palabras serservadas como __all__ que me
permite declarar variables en una lista que puedo llamarlas 
desde afuera solo si las llamo explicitamente, pero no son accesibles
si las llamo con from modulo import *

En __all__ listo lo que quiero compartir, el resto definido no
se comparte cuando hago import * from modulo. Es para que no
modifique por error una variable mientras programo.
"""
#####################################################################
#### Archivo /privado__all__/privadoall.py
__all__ = ['var_publica','funcion_publica']
var_privada = 5 # esta no se comparte porque no está en __all__
var_publica = 4

def funcion_publica():
    return 'Hola mundo'

#####################################################################
#### Archivo /privado__all__/recuperarall.py
from privadoall import * # se importa var_publica y funcion_publica
from privadoall import var_privada # se importa variable privada