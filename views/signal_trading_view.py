import flet as ft

class SignalTradingView:
    def __init__(self, page):
        self.page = page

    @property
    def content(self):
        return ft.Column([
            ft.Text("Operar con señales")
        ])
