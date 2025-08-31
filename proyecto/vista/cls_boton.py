from flet import OutlinedButton


class Boton(OutlinedButton):
    def __init__(self, texto, funcion):
        super().__init__()
        self.text = texto
        self.on_click = funcion
