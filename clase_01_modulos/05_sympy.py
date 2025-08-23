"""
Módulo sympy: no viene instalado con python, lo tenemos que instalar
junto con este instalar jupyterlab

que pasa si en mi variable quiero guardar una ecuación matemática?
se hace con matemática simbólica, herramientas como FEniCS
"""
import math
print(math.sqrt(8)) # imprime 2.82...

import sympy
print(sympy.sqrt(8)) # imprime 2 sqrt(2)

a = sympy.sqrt(8)
print (a * 3) # imprime 6 sqrt(2)

from sympy import symbols, Eq, diff, cos
x = symbols ('x')

print(x+1) # imprime x + 1

x, y, z = symbols('x y z')
expresion = x + 2 * y
print (expresion)
print (expresion.subs({x:2, y:2}))

Eq( x + 1, 4) # genera X + 1 = 4

"""DERIVADAS"""
diff( cos(x), x)
# -sin (x)

"""Integrales también hay"""
"""Matrices/ series/ ...."""

"""Ver más en el archivo que nos compartió el profe"""