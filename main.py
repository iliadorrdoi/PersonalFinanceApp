from models.account import Account

def main():
    account = Account(1, 1, "Основной счёт", 1000.0, "KGS")
    account.create_account()
    account.get_account_balance()
    account.update_account(new_name="Новый счёт", new_currency="USD")
    account.get_account_balance()
    account.delete_account()

if __name__ == "__main__":
    main()

