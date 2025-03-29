from dao.transaction_dao import TransactionDAO
from models.transaction import Transaction
from datetime import datetime

class TransactionController:
    def __init__(self):
        self.dao = TransactionDAO()

    def add_transaction(self, tx_id, user_id, account_id, category_id, amount, tx_type, currency, description=""):
        tx = Transaction(
            transaction_id=tx_id,
            user_id=user_id,
            account_id=account_id,
            category_id=category_id,
            amount=amount,
            tx_type=tx_type,
            currency=currency,
            date=datetime.now(),
            description=description
        )
        self.dao.create_transaction(tx)
        print("Транзакция добавлена.")

    def get_transaction(self, tx_id):
        tx = self.dao.get_transaction_by_id(tx_id)
        if tx:
            print(f"{tx.tx_type.title()}: {tx.amount} {tx.currency} | {tx.description}")
        else:
            print("Транзакция не найдена.")

    def update_transaction(self, tx_id, new_amount=None, new_description=None):
        tx = self.dao.get_transaction_by_id(tx_id)
        if tx:
            if new_amount:
                tx.amount = new_amount
            if new_description:
                tx.description = new_description
            self.dao.update_transaction(tx)
            print("Транзакция обновлена.")
        else:
            print("Транзакция не найдена.")

    def delete_transaction(self, tx_id):
        self.dao.delete_transaction(tx_id)
        print(f"Транзакция с ID {tx_id} удалена.")

    def list_transactions(self):
        txs = self.dao.get_all_transactions()
        for t in txs:
            print(f"[{t.transaction_id}] {t.tx_type} - {t.amount} {t.currency} ({t.description})")
