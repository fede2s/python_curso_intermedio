"""
Que es patron MVC?
es un patron de diseño, un bloque grande que nos permite 
hacer tareas que ya estan establecidas, nos permite tener
estructuras para hacer algo más rápido.
No son exclusivos de python, están en todos los lenguajes
de programación modernos.

Una herramienta es la utilización de clases. Se suele usar
con UML (diagrama de fluojs)

Modelo: es como el que piensa
Controlador: es como el gerente/recepcionista
Vista: es como el sector de marketing

Como implementarlo?
podemos hacer 3 archivos: 
    controlador.py
    vista.py
    modelo.py

en modelo podría ir alta, baja, modificacion

en el controlador llamo a la aplicacion, además tengo que
ponerle if __name__ == '__main__':
lo que viene a continuacion, solamente se va a ver si abro el archivo
entonces las pruebas solamente se ven en ese archivo.

en vista tengo que ir haciendo los imports
y llamar al modelo
"""

### Controlador
from tkinter import Tk
import vista

if __name__ == "__main__":
    root_tk = Tk()
    vista.vista_principal(root_tk) #llamo la funcion vista
    root_tk.mainloop()

### Vista
# el uso de tkinter y llamadas al modelo

### Modelo
# llamadas a la base de datos