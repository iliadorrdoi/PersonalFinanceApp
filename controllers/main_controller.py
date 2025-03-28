from models.user import User

class MainController:
    def __init__(self):
        self.current_user = None

    def register_user(self, user_id, username, password, email):
        user = User(user_id, username, password, email)
        user.register()
        return user
    
    def login_user(self, user, username, password):
        if user.login(username, password):
            self.current_user = user
            print(f"Пользователь {username} вошел в систему.")
        else:
            print("Ошибка авторизации.")