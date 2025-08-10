"""
ejercicio d
nuestra salida nos da siempre el mismo valor
estamos llamando al valor de esa variable 
poniendo la ruta (especificando el namespace)
por mas que haga importaciones posteriores, cada vez
que haga esa x es la definida ahi
"""
import modulo4

modulo4.x = 42
print(modulo4.x)

import modulo4
print(modulo4.x)
from modulo4 import x
print(x)

"""
namespace es un espacio de nombre

Explicacion: si 2 personas trabajan en cosas distintas
pero definen algo con el mismo nombre voy a tener
problemas al importar ambas cosas.

Ejemplo: En la web cada vez que subimos a un repositorio,
lo hacemos con el dominio de la persona. 
Ej  pepe sube a https://pepe.com/popup
    y ana sube a https://ana.com/carrouselle
entonces de su app realizan un contenedor y a ese 
contenedor le dan un nombre especifico
pepe llama a su funcion popup.pepe.com/miFuncion()
ana llama a su funcion popup.ana.com/miFuncion()
Ahora no se van a pisar al usar la funcion miFuncion()

___________________________________________________________
CONCLUSION:

cuando importamos no conviene el from
conviene hacer import

entonces puedo usar el namespace asi no cometo errores
en cuanto a importacion de modulos
"""
