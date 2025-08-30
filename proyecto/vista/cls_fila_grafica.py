from flet import Row
# encontré como generar una fila de contenedores acá
# https://flet.dev/docs/controls/container/
class FilaGrafica(Row):
    def __init__(self, objetos):
        super().__init__(objetos)