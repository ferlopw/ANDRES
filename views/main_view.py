from .base_view import BaseView
import flet as ft

class MainView(BaseView):
    def __init__(self, page, navigate):
        super().__init__(page)
        self.navigate = navigate

    def display(self):
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
            bgcolor=ft.colors.BLUE_GREY_700
        )

        def toggle_menu(e):
            menu.content.visible = not menu.content.visible
            self.page.update()

        def hide_menu(e):
            if menu.content.visible:
                menu.content.visible = False
                self.page.update()

        self.page.on_click = hide_menu
        menu_button = ft.IconButton(icon=ft.icons.MENU, on_click=toggle_menu)
        welcome_text = ft.Text("Bienvenido a la página de inicio")

        self.clear_and_add([menu_button, welcome_text, menu])
