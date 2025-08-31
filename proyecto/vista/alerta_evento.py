import flet as ft

""" copié código del repositorio oficial de flet
https://github.com/flet-dev/examples/blob/main/python/apps/
controls-gallery/examples/dialogs/alertdialog/01_basic_and_
modal_dialogs.py
"""


def generar_alerta(texto):
    dlg = ft.AlertDialog(
        title=ft.Text(texto), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def open_dlg(e):
        e.control.page.overlay.append(dlg)
        dlg.open = True
        e.control.page.update()

    return ft.Column(
        [
            ft.ElevatedButton(texto, on_click=open_dlg)
        ]
    )
