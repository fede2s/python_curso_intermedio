import controlador.cls_abmc_de_tablas as abmc
import flet


def main(page:flet.Page):
    controlador = abmc.ControladorDeTablas(page)
    print(page)
flet.app(target=main)