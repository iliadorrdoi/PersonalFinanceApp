from dao.account_dao import AccountDAO
from models.account import Account

class AccountController:
    def __init__(self):
        self.dao = AccountDAO()

    def create_account(self, account_id, user_id, name, balance, currency):
        account = Account(account_id, user_id, name, balance, currency)
        self.dao.create_account(account)
        print(f"Счёт '{name}' создан.")

    def get_account(self, account_id):
        account = self.dao.get_account_by_id(account_id)
        if account:
            print(f"Счёт: {account.account_name}, Баланс: {account.balance} {account.currency}")
        else:
            print("Счёт не найден.")

    def update_account(self, account_id, new_name=None, new_balance=None, new_currency=None):
        account = self.dao.get_account_by_id(account_id)
        if account:
            if new_name:
                account.account_name = new_name
            if new_balance is not None:
                account.balance = new_balance
            if new_currency:
                account.currency = new_currency
            self.dao.update_account(account)
            print("Счёт обновлён.")
        else:
            print("Счёт не найден.")

    def delete_account(self, account_id):
        self.dao.delete_account(account_id)
        print(f"Счёт с ID {account_id} удалён.")

    def list_accounts(self):
        accounts = self.dao.get_all_accounts()
        for acc in accounts:
            print(f"[{acc.account_id}] {acc.account_name} - {acc.balance} {acc.currency}")
