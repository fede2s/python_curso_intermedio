import flet as ft


def generar_tabla(columnas_txt, filas_lista_txt):
    """
    copiado de repositorio oficial de flet
    https://github.com/flet-dev/examples/blob/main/python/apps/
    controls-gallery/examples/layout/datatable/01_basic_datatable.py
    lo hice dinamico para que reciba una lista de titulos de columnas
    y una lista de filas, donde cada fila es una lista de celdas
    """
    columnas = []
    filas = []
    for columna in columnas_txt:
        columnas.append(ft.DataColumn(ft.Text(columna)))
    for fila in filas_lista_txt:
        celdas = []
        for celda in fila:
            celdas.append(ft.DataCell(ft.Text(celda)))
        filas.append(ft.DataRow(cells=celdas))
    return ft.DataTable(
            columns=columnas,
            rows=filas
        )
