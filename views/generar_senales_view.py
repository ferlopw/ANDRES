from .base_view import BaseView
import flet as ft

class GenerateSignalsView(BaseView):
    def __init__(self, page, navigate):
        super().__init__(page)
        self.navigate = navigate
        self.signals_loaded = False

    def toggle_signals(self, e):
        self.signals_loaded = not self.signals_loaded
        self.display()

    def display(self):
        print("Mostrando GenerateSignalsView")

        # Crear el menú desplegable
        menu_items = [
            ft.TextButton("Inicio", on_click=lambda e: self.navigate("inicio")),
            ft.TextButton("Operar Automático", on_click=lambda e: self.navigate("operar_automatico")),
            ft.TextButton("Operar con señales", on_click=lambda e: self.navigate("operar_senales")),
            ft.TextButton("Generar señales", on_click=lambda e: self.navigate("generar_senales")),
            ft.TextButton("Cargar señales", on_click=lambda e: self.navigate("cargar_senales")),
            ft.TextButton("Configuración", on_click=lambda e: self.navigate("configuracion")),
            ft.TextButton("Cerrar sesión", on_click=lambda e: self.navigate("login"))
        ]

        menu = ft.Container(
            content=ft.Column(menu_items, visible=False),
            bgcolor=ft.colors.BLUE_GREY_700,
            padding=10,
            width=200
        )

        def toggle_menu(e):
            menu.content.visible = not menu.content.visible
            self.page.update()

        def hide_menu(e):
            if menu.content.visible and not (e.target == menu_button or menu_button in e.target):
                menu.content.visible = False
                self.page.update()

        self.page.on_click = hide_menu
        menu_button = ft.IconButton(icon=ft.icons.MENU, on_click=toggle_menu)

        # Botón para alternar señales
        button = ft.ElevatedButton(
            text="DETENER" if self.signals_loaded else "INICIAR",
            bgcolor=ft.colors.RED if self.signals_loaded else ft.colors.BLUE,
            on_click=self.toggle_signals,
            width=150
        )

        # Tabla de señales
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
            width=700  # Ajusta el ancho de la tabla para mejor apariencia
        )

        # Contenido completo con tabla y botón
        content = ft.Column(
            [
                ft.Text("Generar Señales", style="headlineMedium"),
                table,
                ft.Container(expand=True),  # Añade un contenedor expandible para empujar el botón hacia abajo
                ft.Container(content=button, alignment=ft.alignment.center)  # Envuelve el botón en un contenedor para centrarlo
            ],
            alignment="start",  # Alinea los elementos al principio del contenedor
            horizontal_alignment="center",
            spacing=20,
        )

        main_content = ft.Row(
            [
                ft.Column(
                    [
                        menu_button,
                        menu
                    ]
                ),
                ft.VerticalDivider(width=1),
                content
            ],
            expand=True
        )

        self.page.controls.clear()
        self.page.add(main_content)
        self.page.update()
        print("Menú desplegable y contenido completo agregados y página actualizada")
from .base_view import BaseView
import flet as ft

class GenerateSignalsView(BaseView):
    def __init__(self, page, navigate):
        super().__init__(page)
        self.navigate = navigate
        self.signals_loaded = False

    def toggle_signals(self, e):
        self.signals_loaded = not self.signals_loaded
        self.display()

    def display(self):
        print("Mostrando GenerateSignalsView")

        # Crear el menú desplegable
        menu_items = [
            ft.TextButton("Inicio", on_click=lambda e: self.navigate("inicio")),
            ft.TextButton("Operar Automático", on_click=lambda e: self.navigate("operar_automatico")),
            ft.TextButton("Operar con señales", on_click=lambda e: self.navigate("operar_senales")),
            ft.TextButton("Generar señales", on_click=lambda e: self.navigate("generar_senales")),
            ft.TextButton("Cargar señales", on_click=lambda e: self.navigate("cargar_senales")),
            ft.TextButton("Configuración", on_click=lambda e: self.navigate("configuracion")),
            ft.TextButton("Cerrar sesión", on_click=lambda e: self.navigate("login"))
        ]

        menu = ft.Container(
            content=ft.Column(menu_items, visible=False),
            bgcolor=ft.colors.BLUE_GREY_700,
            padding=10,
            width=200
        )

        def toggle_menu(e):
            menu.content.visible = not menu.content.visible
            self.page.update()

        def hide_menu(e):
            if menu.content.visible and not (e.target == menu_button or menu_button in e.target):
                menu.content.visible = False
                self.page.update()

        self.page.on_click = hide_menu
        menu_button = ft.IconButton(icon=ft.icons.MENU, on_click=toggle_menu)

        # Botón para alternar señales
        button = ft.ElevatedButton(
            text="DETENER" if self.signals_loaded else "INICIAR",
            bgcolor=ft.colors.RED if self.signals_loaded else ft.colors.BLUE,
            on_click=self.toggle_signals,
            width=150
        )

        # Tabla de señales
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
            width=700  # Ajusta el ancho de la tabla para mejor apariencia
        )

        # Contenido completo con tabla y botón
        content = ft.Column(
            [
                ft.Text("Generar Señales", style="headlineMedium"),
                table,
                ft.Container(expand=True),  # Añade un contenedor expandible para empujar el botón hacia abajo
                ft.Container(content=button, alignment=ft.alignment.center)  # Envuelve el botón en un contenedor para centrarlo
            ],
            alignment="start",  # Alinea los elementos al principio del contenedor
            horizontal_alignment="center",
            spacing=20,
        )

        main_content = ft.Row(
            [
                ft.Column(
                    [
                        menu_button,
                        menu
                    ]
                ),
                ft.VerticalDivider(width=1),
                content
            ],
            expand=True
        )

        self.page.controls.clear()
        self.page.add(main_content)
        self.page.update()
        print("Menú desplegable y contenido completo agregados y página actualizada")
