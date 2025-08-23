"""
Comandos para ejecutar en cmd como administrador en 
c:\windows\system32

py -m pip install --upgrade pip
pip install --upgrade setuptools --user
pip install --upgrade build

dentro OTRO directorio voy a generar un par de archivitos
ver.py con funcion imprimir
principal.py
"""
#####################################################################
### principal.py

import sys
import ver

ver.imprimir(" ".join(sys.argv[1:]))

#####################################################################

"""
ejecuto python principal.py hola clase
imprime hola clase

"""