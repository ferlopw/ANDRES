import flet as ft


class SettingsView:
    def __init__(self, page):
        self.page = page

    @property
    def content(self):
        return ft.Column([
            ft.Text("Configuración"),
        ])
