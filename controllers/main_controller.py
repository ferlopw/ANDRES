from controllers.base_controller import BaseController
from views.main_view import MainView
from views.operador_automatico_view import OperadorAutomaticoView
from views.operar_senales_view import OperarSenalesView
from views.generar_senales_view import GenerateSignalsView
from views.cargar_senales_view import CargarSenalesView
from views.configuracion_view import ConfiguracionView

class MainController(BaseController):
    def __init__(self, page):
        super().__init__(page)
        self.main_view = MainView(page, self.navigate)
        self.operador_automatico_view = OperadorAutomaticoView(page, self.navigate)
        self.operar_senales_view = OperarSenalesView(page, self.navigate)
        self.generar_senales_view = GenerateSignalsView(page, self.navigate)
        self.cargar_senales_view = CargarSenalesView(page, self.navigate)
        self.configuracion_view = ConfiguracionView(page, self.navigate)
        
    def navigate(self, view_name):
        print(f"Navegando a la vista: {view_name}")
        if view_name == "inicio":
            self.main_view.display()
        elif view_name == "operar_automatico":
            self.operador_automatico_view.display()
        elif view_name == "operar_senales":
            self.operar_senales_view.display()
        elif view_name == "generar_senales":
            self.generar_senales_view.display()
        elif view_name == "cargar_senales":
            self.cargar_senales_view.display()
        elif view_name == "configuracion":
            self.configuracion_view.display()
        elif view_name == "login":
            from controllers.auth_controller import AuthController
            auth_controller = AuthController(self.page)
            auth_controller.login_view.display()
