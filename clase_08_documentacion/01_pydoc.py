"""##################################################################
para tener una descripcion de random o math que son librerias de 
python podemos usar pydoc que ademas permite documentar.

Vamos a abrir cmd y ponemos:
    python -m pydoc

me muestra comandos de pydoc

para ver documentacion de random:
    python -m pydoc random
si doy enter sigo bajando en la documentacion
Ctrl + C para salir
cls para limpiar la pantalla

crear servidor en una ip deshabilitada para ver documentacion en html:
    python -m pydoc -p 54200
me devuelve:
    PS C:\Users\Fede\Desktop\python_curso_intermedio> python -m pydoc -p 54200
    Server ready at http://localhost:54200/
    Server commands: [b]rowser, [q]uit
    server>

crear documentacion en un html para archivo debug2.py:
    python -m pydoc -w debug2
"""