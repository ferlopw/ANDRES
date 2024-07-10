import flet as ft

class GenerateSignalsView:
    def __init__(self, page):
        self.page = page
        self.signals_loaded = False

    def toggle_signals(self, e):
        self.signals_loaded = not self.signals_loaded
        self.page.views[-1].controls.clear()
        self.page.views[-1].controls.append(self.content)
        self.page.update()

    @property
    def content(self):
        columns = [
            ft.DataColumn(ft.Text("Hora")),
            ft.DataColumn(ft.Text("Par")),
            ft.DataColumn(ft.Text("Acción")),
            ft.DataColumn(ft.Text("Expiración")),
        ]

        rows = [
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("18:00")),
                ft.DataCell(ft.Text("EURJPY-OTC")),
                ft.DataCell(ft.Text("PUT")),
                ft.DataCell(ft.Text("1M")),
            ]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("18:03")),
                ft.DataCell(ft.Text("EURUSD-OTC")),
                ft.DataCell(ft.Text("PUT")),
                ft.DataCell(ft.Text("1M")),
            ]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("18:07")),
                ft.DataCell(ft.Text("EURUSD-OTC")),
                ft.DataCell(ft.Text("PUT")),
                ft.DataCell(ft.Text("1M")),
            ]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("18:09")),
                ft.DataCell(ft.Text("USDCHF-OTC")),
                ft.DataCell(ft.Text("PUT")),
                ft.DataCell(ft.Text("1M")),
            ]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("18:13")),
                ft.DataCell(ft.Text("NZDUSD-OTC")),
                ft.DataCell(ft.Text("PUT")),
                ft.DataCell(ft.Text("1M")),
            ]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("18:19")),
                ft.DataCell(ft.Text("EURJPY-OTC")),
                ft.DataCell(ft.Text("PUT")),
                ft.DataCell(ft.Text("1M")),
            ]),
        ] if self.signals_loaded else []

        table = ft.DataTable(
            columns=columns,
            rows=rows,
            width=700,  # Ajusta el ancho de la tabla para mejor apariencia
        )

        button = ft.ElevatedButton(
            text="DETENER" if self.signals_loaded else "INICIAR",
            bgcolor=ft.colors.RED if self.signals_loaded else ft.colors.BLUE,
            on_click=self.toggle_signals,
            width=150
        )

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Generar Señales", style="headlineMedium"),
                    table,
                    ft.Container(expand=True),  # Añade un contenedor expandible para empujar el botón hacia abajo
                    ft.Container(content=button, alignment=ft.alignment.center)  # Envuelve el botón en un contenedor para centrarlo
                    
                ],
                alignment="start",  # Alinea los elementos al principio del contenedor
                horizontal_alignment="center",
                spacing=20,
            ),
            alignment=ft.alignment.center,
            padding=20,
            expand=True
        )


