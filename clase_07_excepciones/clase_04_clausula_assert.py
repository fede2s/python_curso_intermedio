"""##################################################################
la clausula assert me va a permitir evaluar la informacion que estoy
tomando de un modulo o de otra app o cualquier lado
Yo quiero saber si viene en el formato adecuado y poder hacer una
excepcion especifica

"""
#numero = 5
numero = int(input("Ingrese numero\n"))
print(numero)
assert numero >=0 , "El valor debe ser mayor o igual a cero"
print(numero**0.5)

"""Si ingreso 4 imprime:
Ingrese numero
-4
-4
Traceback (most recent call last):
  File "C:\Users\Fede\Desktop\python_curso_intermedio\clase_07_excepciones\clase_04_clausula_assert.py", line 11, in <module>
    assert numero >=0 , "El valor debe ser mayor o igual a cero"
           ^^^^^^^^^^
AssertionError: El valor debe ser mayor o igual a cero"""