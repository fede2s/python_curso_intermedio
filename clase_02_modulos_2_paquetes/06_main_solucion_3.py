import sys
import os

"""
voy a pararme en el directorio en el que me encuentro y tomar una 
ruta relativa
"""
BASE_DIR = os.path.dirname((os.path.abspath(__file__))) #dir actual
BASE_DIR = os.path.dirname(BASE_DIR) # subi un nivel
sys.path.append(BASE_DIR)
print(">>>>>> ", BASE_DIR)

from juan1 import ver # desde fuera de juan importo juan1 el mod ver

ver.imprimir("".join(sys.argv[1:]))