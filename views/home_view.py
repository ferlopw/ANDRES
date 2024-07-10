import flet as ft

class HomeView:
    
    def __init__(self, page: ft.Page, controller):
        self.page = page
        self.controller = controller
        self.menu_open = False
        self.menu_container = self.create_menu_container()
        # Añadir un contenedor transparente para detectar clics fuera del menú
        self.overlay = ft.Container(
            expand=True, 
            on_click=self.handle_click_outside,
            visible=False  # inicialmente no visible
        )

    def handle_click_outside(self, e):
        if self.menu_open:
            self.menu_open = False
            self.menu_container.visible = self.menu_open
            self.overlay.visible = self.menu_open
            self.page.update()

    def toggle_menu(self, e=None):
        self.menu_open = not self.menu_open
        self.menu_container.visible = self.menu_open
        self.overlay.visible = self.menu_open
        self.page.update()

    def navigate_to(self, destination):
        if destination == "Inicio":
            self.controller.show_home_view()
        elif destination == "Operar Automático":
            self.controller.show_automatic_trading_view()
        elif destination == "Operar con señales":
            self.controller.show_signal_trading_view()
        elif destination == "Generar señales":
            self.controller.show_generate_signals_view()
        elif destination == "Cargar señales":
            self.controller.show_load_signals_view()
        elif destination == "Configuración":
            self.controller.show_settings_view()
        self.toggle_menu()

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
                ft.Container(expand=True),
                ft.ListTile(
                    title=ft.Text("Configuración"),
                    on_click=lambda _: self.navigate_to("Configuración")
                ),
                ft.ListTile(
                    title=ft.Text("Cerrar sesión"),
                    on_click=lambda _: self.navigate_to("Cerrar sesión")
                ),
            ], expand=True),
            width=200,
            bgcolor=ft.colors.BLUE_GREY,
            padding=10,
            visible=self.menu_open
        )

    @property
    def content(self):
        menu_button = ft.IconButton(icon=ft.icons.MENU, on_click=self.toggle_menu)
        return ft.Stack([
            self.overlay,  # Contenedor para detectar clics fuera del menú
            ft.Column([
                ft.Row([menu_button, ft.Text("Inicio")], alignment="start"),
                ft.Container(content=ft.Text("Bienvenido a la página de inicio"), expand=True)
            ], expand=True),
            self.menu_container
        ], expand=True)

