import flet as ft

class LoginView:
    def __init__(self, page, on_login_success):
        self.page = page
        self.on_login_success = on_login_success
        self.username = "admin"
        self.password = "admin"

    def authenticate(self, e=None):
        print("Autenticando...")  # Mensaje de depuración
        if self.username_input.value == self.username and self.password_input.value == self.password:
            print("Autenticación exitosa")  # Mensaje de depuración
            self.on_login_success()
        else:
            print("Autenticación fallida")  # Mensaje de depuración

    @property
    def content(self):
        self.username_input = ft.TextField(label="Usuario", width=200)
        self.password_input = ft.TextField(label="Contraseña", password=True, width=200)
        login_button = ft.ElevatedButton(text="Iniciar Sesión", on_click=self.authenticate)

        login_form = ft.Column(
            [
                ft.Container(content=ft.Image(src="assets/logo.png", width=100, height=100), alignment=ft.alignment.center),
                self.username_input,
                self.password_input,
                login_button,
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=10  # Ajusta el espaciado entre los elementos si es necesario
        )

        return ft.Container(
            content=login_form,
            alignment=ft.alignment.center,
            expand=True
        )


