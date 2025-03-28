from datetime import datetime

class User:
    def __init__(self, user_id, username, password, email, created_at=None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.created_at = created_at or datetime.now()

    def register(self):
        print(f"Пользователь {self.username} успешно зарегистрирован!")

    def login(self, username, password):
        if self.username == username and self.password == password:
            print(f"Пользователь {self.username} успешно вошел в систему.")
            return True
        else:
            print("Неверный логин или пароль.")
            return False