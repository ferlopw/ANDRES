from .base_view import BaseView
import flet as ft

class LoginView(BaseView):
    def __init__(self, page, on_login):
        super().__init__(page)
        self.on_login = on_login

    def display(self):
        def handle_login(e):
            username = username_input.value
            password = password_input.value
            self.on_login(username, password)
        
        username_input = ft.TextField(label="Usuario", width=300)
        password_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
        login_button = ft.ElevatedButton(text="Iniciar Sesión", on_click=handle_login)
        
        # Contenedor Column para centrar verticalmente
        column = ft.Column(
            [username_input, password_input, login_button],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar horizontalmente
        )

        # Contenedor Row para centrar horizontalmente
        row = ft.Row(
            [column],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.clear_and_add([row])   # Agregar el Row directamente
