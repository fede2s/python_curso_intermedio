"""
usamos anteriormente
try:
    codigo a probar
except:
    mostrar error
"""

def sumar(a,b):
    return a+b

try:
    print(sumar(3,"Pera"))
except:
    print("Error")    

"""
en docs.python.org hay una parte de excepciones donde puedo ver que puedo tener
errores en los atributos, errores en una funcion,
error por dividir por 0, etc
uno puede esperar el tipo de error o varios tipos de error en el except
NamError: espero una variable y ese nombre de variable no existe

"""
"""
try:
    print(sumar(3,variable_sin_declarar))
except(NameError,):
    print("Error", NameError)    
"""