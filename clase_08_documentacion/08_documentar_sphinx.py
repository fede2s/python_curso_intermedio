"""
en el mismo directorio donde cree la carpeta archivos creo un
proyecto, dentro pongo mis archivos py

Los comentarios que salen entre triple comilla doble son los que
permiten crear la documentacion
Ademas puedo poner estas variables en el main:
    __author__
    __maintainer__
    __email__
    __copyright__
    __version__

Vuelvo a C:\Users\PC\Desktop\ejemplo\para_sphinx\proyecto
Ejecuto el codigo:
    sphinx-apidoc -o docs . -f -F -H MiProyecto -A "Juan" -V 0.0.1 -R 0.0.1

en \docs\conf.py
    import os
    import sys
    sys.path.insert(0, os.path.abspath('../'))

en \docs
    make html

Si me sale el tema por defecto con la pagina blanca fea, repetir pasos del video 06
"""