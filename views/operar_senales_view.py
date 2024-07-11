from .base_view import BaseView
import flet as ft

class OperarSenalesView(BaseView):
    def __init__(self, page, navigate):
        super().__init__(page)
        self.navigate = navigate

    def display(self):
        menu_items = [
            ft.Text("Inicio", on_click=lambda e: self.navigate("inicio")),
            ft.Text("Operar Automático", on_click=lambda e: self.navigate("operar_automatico")),
            ft.Text("Operar con señales", on_click=lambda e: self.navigate("operar_senales")),
            ft.Text("Generar señales", on_click=lambda e: self.navigate("generar_senales")),
            ft.Text("Cargar señales", on_click=lambda e: self.navigate("cargar_senales")),
            ft.Text("Configuración", on_click=lambda e: self.navigate("configuracion")),
            ft.Text("Cerrar sesión", on_click=lambda e: self.navigate("login"))
        ]

        menu = ft.Column(menu_items, visible=False, bgcolor=ft.colors.BLUE_GREY_700)

        def toggle_menu(e):
            menu.visible = not menu.visible
            self.page.update()

        def hide_menu(e):
            if menu.visible:
                menu.visible = False
                self.page.update()

        self.page.on_click = hide_menu
        menu_button = ft.IconButton(icon=ft.icons.MENU, on_click=toggle_menu)
        content = ft.Text("Operar con Señales")

        self.clear_and_add([menu_button, content, menu])
