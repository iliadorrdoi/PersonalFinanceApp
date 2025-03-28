from controllers.main_controller import MainController

def main():
    controller = MainController()

    # Регистрация нового пользователя
    user = controller.register_user(1, "eldiyar", "password123", "eldiyar@example.com")

    # Проверка логина с правильными данными
    controller.login_user(user, "eldiyar", "password123")

    # Проверка логина с неправильными данными
    controller.login_user(user, "eldiyar", "wrongpassword")

if __name__ == "__main__":
    main()
