from controllers.base_controller import BaseController
from models.user_model import User
from views.login_view import LoginView
from controllers.main_controller import MainController

users_db = {
    "admin": User("admin", "admin")
}

class AuthController(BaseController):
    def __init__(self, page):
        super().__init__(page)
        self.login_view = LoginView(page, self.login)
        self.main_controller = MainController(page)

    def login(self, username, password):
        user = users_db.get(username)
        if user and user.check_password(password):
            self.main_controller.navigate("inicio")
        else:
            self.login_view.display()



