"""
raise me permite levantar una excepcion cuando estoy
esperando una excepcion
por ejemplo: 
    -si quiero recibir temperatura dentro de 
    un cierto rango y no viene dentro del rango
    -cuando tengo un monto negativo
   
"""
x = -1

if x<0:
    raise Exception("Valor no permitido")
"""
PS C:\Users\Fede\Desktop\python_curso_intermedio\clase_07_excepciones> python .\clase_02_raise.py
Traceback (most recent call last):
  File "C:\Users\Fede\Desktop\python_curso_intermedio\clase_07_excepciones\clase_02_raise.py", line 14, in <module>
    raise Exception("Valor no permitido")
"""

#####################################################################
import sys

try:
    frutas=["Peras","Manzanas"]
    print(frutas[7])
except IndexError as e:
    print("---:" , e)
    print(sys.exc_info()) #informacion especifica de la clase que estoy usando de error

"""
---: list index out of range
(<class 'IndexError'>, IndexError('list index out of range'), <traceback object at 0x0000023C1577B300>)
"""
#####################################################################
import sys

try:
    frutas=["Peras","Manzanas"]
    print(frutas[7])
except IndexError as e:
    print("---:" , e)
    print(sys.exc_info()) #informacion especifica de la clase que estoy usando de error
    mi_except = IndexError("Hay un error en el índice")
    raise mi_except