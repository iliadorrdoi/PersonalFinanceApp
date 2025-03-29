from dao.transaction_dao import TransactionDAO
from models.transaction import Transaction
from datetime import datetime

def main():
    dao = TransactionDAO()
    tx = Transaction(
        transaction_id=1,
        user_id=1,
        account_id=1,
        category_id=1,
        amount=200.0,
        tx_type="expense",
        currency="KGS",
        date=datetime.now(),
        description="Кафе"
    )

    dao.create_transaction(tx)

    found = dao.get_transaction_by_id(1)
    if found:
        print("Найдена транзакция:", found.description, found.amount)

    tx.amount = 250.0
    tx.description = "Кафе и напитки"
    dao.update_transaction(tx)

    for t in dao.get_all_transactions():
        print(t.tx_type, t.amount, t.currency, t.description)

    dao.delete_transaction(1)

if __name__ == "__main__":
    main()
