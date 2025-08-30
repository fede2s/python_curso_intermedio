"""
registro de log, genera un txt con los errores que la app va tomando
"""

import os
import datetime

class RegistroLogError(Exception): # clase administradora

    # quiero poner la ruta a donde voy a guardar el modulo log
    BASE_DIR = os.path.dirname((os.path.abspath((__file__))))
    ruta = os.path.join(BASE_DIR,'log.txt')

    def __init__(self, linea, archivo, fecha):
        self.linea = linea
        self.archivo = archivo
        self.fecha = fecha

    def registrar_error(self):
        log = open(self.ruta, "a")
        print("Se ha dado un error:", self.archivo, self.linea, self.fecha,file=log)

def registrar():
    # poner la fecha actual
    raise RegistroLogError(7,"archivo1.txt",datetime.datetime.now())

try:
    registrar()
except RegistroLogError as log:
    log.registrar_error()