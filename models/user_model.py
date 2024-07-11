class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password

class AdvancedUser(User):
    def __init__(self, username, password, role):
        super().__init__(username, password)
        self.role = role

    def has_role(self, role):
        return self.role == role

