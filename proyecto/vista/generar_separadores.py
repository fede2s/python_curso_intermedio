import flet as ft


def generar_separador(
        page,
        botones,
        tabla):
    """
    funcion copiada de repositorio oficial de flet
    https://github.com/flet-dev/examples/blob/main/python/apps/
    controls-gallery/examples/layout/divider/02_draggable_divider.py
    """
    def move_divider(e: ft.DragUpdateEvent):
        if (
                (e.delta_y > 0 and c.height < 300) or
                (e.delta_y < 0 and c.height > 100)):
            c.height += e.delta_y
        c.update()

    def show_draggable_cursor(e: ft.HoverEvent):
        e.control.mouse_cursor = ft.MouseCursor.RESIZE_UP_DOWN
        e.control.update()

    c = ft.Container(
        alignment=ft.alignment.center,
        height=150,
        content=botones
    )

    return ft.Column(
        [
            c,
            ft.GestureDetector(
                content=ft.Divider(),
                on_pan_update=move_divider,
                on_hover=show_draggable_cursor,
            ),
            ft.Container(
                alignment=ft.alignment.center_left,
                expand=1,
                content=tabla
            ),
        ],
        spacing=0,
        scroll=True
    )
