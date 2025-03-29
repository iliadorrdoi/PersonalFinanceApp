from controllers.account_controller import AccountController

def main():
    controller = AccountController()
    controller.create_account(1, 1, "Бюджет Эльдияра", 7624, "KGS")
    controller.get_account(1)
    controller.update_account(1, new_name="Домашний счёт", new_balance=3000.0)
    controller.list_accounts()
    controller.delete_account(1)

if __name__ == "__main__":
    main()
