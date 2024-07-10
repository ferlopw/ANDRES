import flet as ft
from views.login_view import LoginView
from views.home_view import HomeView
from views.automatic_trading_view import AutomaticTradingView
from views.signal_trading_view import SignalTradingView
from views.generate_signals_view import GenerateSignalsView
from views.load_signals_view import LoadSignalsView
from views.settings_view import SettingsView

class MainController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.login_view = LoginView(self.page, self.show_home_view)
        

    def handle_key_down(self, e: ft.KeyboardEvent):
        if e.key == "Enter" and self.login_view:
            self.login_view.authenticate(e)

    def show_login_view(self):
        self.page.views.clear()
        self.page.views.append(ft.View('/login', [self.login_view.content]))
        self.page.update()

    def show_home_view(self):
        home_view = HomeView(self.page, self)
        self.page.views.clear()
        self.page.views.append(ft.View('/home', [home_view.content]))
        self.page.update()

    def show_automatic_trading_view(self):
        automatic_trading_view = AutomaticTradingView(self.page)
        self.page.views.clear()
        self.page.views.append(ft.View('/automatic_trading', [automatic_trading_view.content]))
        self.page.update()

    def show_generate_signals_view(self):
        generate_signals_view = GenerateSignalsView(self.page)
        self.page.views.clear()
        self.page.views.append(ft.View('/generate_signals', [generate_signals_view.content]))
        self.page.update()


   
