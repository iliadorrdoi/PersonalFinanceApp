from dao.user_dao import UserDAO
from models.user import User
from datetime import datetime

def main():
    user_dao = UserDAO()

    user = User(1, "eldiyar", "pass123", "eldiyar@example.com", datetime.now())
    user_dao.create_user(user)

    fetched_user = user_dao.get_user_by_id(1)
    if fetched_user:
        print("Найден пользователь:", fetched_user.username)

    user.username = "eldiyar_updated"
    user_dao.update_user(user)

    for u in user_dao.get_all_users():
        print(u.username, u.email)

    user_dao.delete_user(1)

if __name__ == "__main__":
    main()

