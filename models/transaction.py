from datetime import datetime

class Transaction:
    def __init__(self, transaction_id, user_id, account_id, category_id, amount, tx_type, currency, date=None, description=""):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.account_id = account_id
        self.category_id = category_id
        self.amount = amount
        self.tx_type = tx_type  # "income" или "expense"
        self.currency = currency
        self.date = date or datetime.now()
        self.description = description

    def add_transaction(self):
        print(f"{self.tx_type.title()} на сумму {self.amount} {self.currency} добавлена.")

    def edit_transaction(self, new_amount=None, new_desc=None):
        if new_amount is not None:
            self.amount = new_amount
        if new_desc:
            self.description = new_desc
        print(f"Транзакция обновлена: {self.amount} {self.currency}, описание: {self.description}")

    def delete_transaction(self):
        print("Транзакция удалена.")

    def get_transaction_info(self):
        return f"{self.tx_type.title()} {self.amount} {self.currency} | {self.date.strftime('%d.%m.%Y')} | {self.description}"
