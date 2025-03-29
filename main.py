from controllers.account_controller import AccountController
from controllers.transaction_controller import TransactionController
from controllers.category_controller import CategoryController
from controllers.financial_goal_controller import FinancialGoalController

def print_menu():
    print("\n=== Personal Finance Menu ===")
    print("1. Создать счёт")
    print("2. Добавить транзакцию")
    print("3. Добавить категорию")
    print("4. Добавить финансовую цель")
    print("5. Показать все счета")
    print("6. Показать все транзакции")
    print("7. Показать все категории")
    print("8. Показать все цели")
    print("0. Выйти")

def safe_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("❌ Ошибка: нужно ввести целое число.")
        return None

def safe_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("❌ Ошибка: нужно ввести число.")
        return None

def main():
    account_ctrl = AccountController()
    transaction_ctrl = TransactionController()
    category_ctrl = CategoryController()
    goal_ctrl = FinancialGoalController()

    while True:
        print_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            id = safe_int("ID счёта: ")
            uid = safe_int("ID пользователя: ")
            if id is None or uid is None:
                continue
            name = input("Название счёта: ")
            bal = safe_float("Баланс: ")
            if bal is None:
                continue
            cur = input("Валюта: ")
            account_ctrl.create_account(id, uid, name, bal, cur)

        elif choice == "2":
            id = safe_int("ID транзакции: ")
            uid = safe_int("ID пользователя: ")
            acc_id = safe_int("ID счёта: ")
            cat_id = safe_int("ID категории: ")
            if None in (id, uid, acc_id, cat_id):
                continue
            amt = safe_float("Сумма: ")
            if amt is None:
                continue
            typ = input("Тип (income/expense): ").lower()
            if typ not in ("income", "expense"):
                print("❌ Ошибка: тип должен быть 'income' или 'expense'")
                continue
            cur = input("Валюта: ")
            desc = input("Описание: ")
            transaction_ctrl.add_transaction(id, uid, acc_id, cat_id, amt, typ, cur, desc)

        elif choice == "3":
            id = safe_int("ID категории: ")
            uid = safe_int("ID пользователя: ")
            if id is None or uid is None:
                continue
            name = input("Название категории: ")
            typ = input("Тип (income/expense): ").lower()
            if typ not in ("income", "expense"):
                print("❌ Ошибка: тип должен быть 'income' или 'expense'")
                continue
            category_ctrl.create_category(id, uid, name, typ)

        elif choice == "4":
            id = safe_int("ID цели: ")
            uid = safe_int("ID пользователя: ")
            if id is None or uid is None:
                continue
            name = input("Название цели: ")
            target = safe_float("Целевая сумма: ")
            current = safe_float("Начальная сумма: ")
            if None in (target, current):
                continue
            deadline = input("Дедлайн (в формате YYYY-MM-DD): ")
            goal_ctrl.create_goal(id, uid, name, target, current, deadline)

        elif choice == "5":
            account_ctrl.list_accounts()

        elif choice == "6":
            transaction_ctrl.list_transactions()

        elif choice == "7":
            category_ctrl.list_categories()

        elif choice == "8":
            goal_ctrl.list_goals()

        elif choice == "0":
            print("👋 До свидания!")
            break

        else:
            print("❌ Ошибка: такого пункта меню нет. Попробуйте снова.")

if __name__ == "__main__":
    main()
