from flet import Column


class ColumnaGrafica(Column):
    """ simplificado de ejemplo en
    https://flet.dev/docs/controls/column
    """
    def __init__(self, objetos):
        super().__init__(expand=False, spacing=50, controls=objetos)
