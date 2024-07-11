import flet as ft
from controllers.auth_controller import AuthController

def main(page: ft.Page):
    page.title = "Login App"
    auth_controller = AuthController(page)
    auth_controller.login_view.display()

ft.app(target=main)

