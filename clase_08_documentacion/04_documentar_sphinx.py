"""
Parado en la carpeta archivos que cree previamente...
En consola poner:
    sphinx-build -b html docs/source/ docs/build/html

Va a generar dentro del directorio docs el html
en archivos/docs/builds se genero el html con un index
Ese html es un holamundo de sphinx. me falta agregar
paginas con la documentacion.

####################################################################
Vamos a customizar la pagina inicial de la documentacion
En archivos\docs\source\index.rst

copiamos algun markdown para ir
titulo
====

**titulo fuerte**
*titulo debil*
.. note::
    esto es una nota

####################################################################
Modificar el html con los cambios que hice:
    cd docs
    make html

Ver formatos de salida que podria tener:
    make help

"""