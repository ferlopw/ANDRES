import flet as ft

class BaseView:
    def __init__(self, page):
        self.page = page

    def clear_and_add(self, controls):
        self.page.clean()
        self.page.add(*controls)



