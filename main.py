import flet as ft
from controllers.main_controller import MainController

def main(page: ft.Page):
    page.title = "Mi Aplicación de Trading"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    controller = MainController(page)
    
    page.on_keyboard_event = controller.handle_key_down
    controller.show_login_view()

ft.app(target=main)



