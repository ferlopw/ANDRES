import flet as ft

class LoadSignalsView:
    def __init__(self, page):
        self.page = page

    @property
    def content(self):
        return ft.Column([
            ft.Text("Cargar señales")
        ])
