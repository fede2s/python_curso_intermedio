"""
si yo mi programa principal le pongo __main__.py

yo en vez de ejecutar:
    python mi_proyecto/main.py

puedo ejecutar:
    python mi_proyecto
    
porque python por defecto busca el archivo __main__.py
inclusive si el main recibia varibles por consola, al ejecutar
el archivo ejecutando el directorio me los toma.
"""

"""
recordemos que print(sys.path) me muestra donde busca los imports
en el orden en que se buscan
"""

"""
La bandera -m busca los modulos en el directorio que está agregado 
al path"""