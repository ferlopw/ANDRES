import flet as ft

class MenuView:
    def __init__(self, page, controller):
        self.page = page
        self.controller = controller
        self.menu_open = False
        self.menu_container = self.create_menu_container()

    def toggle_menu(self, e=None):
        self.menu_open = not self.menu_open
        self.menu_container.visible = self.menu_open
        self.page.update()

    def navigate_to(self, destination):
        self.menu_open = False
        self.menu_container.visible = self.menu_open
        self.page.update()
        self.controller.navigate(destination)

    def create_menu_container(self):
        return ft.Container(
            content=ft.Column([
                ft.ListTile(
                    title=ft.Text("Inicio"),
                    on_click=lambda _: self.navigate_to("Inicio")
                ),
                ft.ListTile(
                    title=ft.Text("Operar Automático"),
                    on_click=lambda _: self.navigate_to("Operar Automático")
                ),
                ft.ListTile(
                    title=ft.Text("Operar con señales"),
                    on_click=lambda _: self.navigate_to("Operar con señales")
                ),
                ft.ListTile(
                    title=ft.Text("Generar señales"),
                    on_click=lambda _: self.navigate_to("Generar señales")
                ),
                ft.ListTile(
                    title=ft.Text("Cargar señales"),
                    on_click=lambda _: self.navigate_to("Cargar señales")
                ),
                ft.Container(expand=True),  # Contenedor vacío para empujar los elementos hacia abajo
                ft.ListTile(
                    title=ft.Text("Configuración"),
                    on_click=lambda _: self.navigate_to("Configuración")
                ),
                ft.ListTile(
                    title=ft.Text("Cerrar sesión"),
                    on_click=lambda _: self.navigate_to("Cerrar sesión")
                ),
            ],
            expand=True),  # Asegúrate de que el contenedor de la columna se expanda
            width=200,
            bgcolor=ft.colors.BLUE_GREY,
            padding=10,
            visible=self.menu_open
        )

    @property
    def content(self):
        menu_button = ft.IconButton(icon=ft.icons.MENU, on_click=self.toggle_menu)
        return ft.Column([
            ft.Container(content=menu_button, alignment=ft.alignment.center),
            self.menu_container
        ])
