class Account:
    def __init__(self, account_id, user_id, account_name, balance, currency):
        self.account_id = account_id
        self.user_id = user_id
        self.account_name = account_name
        self.balance = balance
        self.currency = currency

    def create_account(self):
        print(f"Счёт '{self.account_name}' создан с балансом {self.balance} {self.currency}")

    def update_account(self, new_name=None, new_currency=None):
        if new_name:
            self.account_name = new_name
        if new_currency:
            self.currency = new_currency
        print(f"Счёт обновлен: {self.account_name}, {self.currency}")

    def delete_account(self):
        print(f"Счет '{self.account_name}' удален.")

    def get_account_balance(self):
        print(f"Баланс счета '{self.account_name}': {self.balance} {self.currency}")
        return self.balance
    
    