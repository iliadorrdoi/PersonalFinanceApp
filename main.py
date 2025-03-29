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

def main():
    account_ctrl = AccountController()
    transaction_ctrl = TransactionController()
    category_ctrl = CategoryController()
    goal_ctrl = FinancialGoalController()

    while True:
        print_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            id = int(input("ID счёта: "))
            uid = int(input("ID пользователя: "))
            name = input("Название счёта: ")
            bal = float(input("Баланс: "))
            cur = input("Валюта: ")
            account_ctrl.create_account(id, uid, name, bal, cur)

        elif choice == "2":
            id = int(input("ID транзакции: "))
            uid = int(input("ID пользователя: "))
            acc_id = int(input("ID счёта: "))
            cat_id = int(input("ID категории: "))
            amt = float(input("Сумма: "))
            typ = input("Тип (income/expense): ")
            cur = input("Валюта: ")
            desc = input("Описание: ")
            transaction_ctrl.add_transaction(id, uid, acc_id, cat_id, amt, typ, cur, desc)

        elif choice == "3":
            id = int(input("ID категории: "))
            uid = int(input("ID пользователя: "))
            name = input("Название категории: ")
            typ = input("Тип (income/expense): ")
            category_ctrl.create_category(id, uid, name, typ)

        elif choice == "4":
            id = int(input("ID цели: "))
            uid = int(input("ID пользователя: "))
            name = input("Название цели: ")
            target = float(input("Целевая сумма: "))
            current = float(input("Начальная сумма: "))
            deadline = input("Дедлайн (YYYY-MM-DD): ")
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
            print("До свидания 👋")
            break

        else:
            print("Неверный выбор. Повторите попытку.")

if __name__ == "__main__":
    main()
