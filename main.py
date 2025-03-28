from models.transaction import Transaction

def main():
    tx = Transaction(
        transaction_id=1,
        user_id=1,
        account_id=1,
        category_id=2,
        amount=500.0,
        tx_type="expense",
        currency="KGS",
        description="Кафе"
    )

    tx.add_transaction()
    print(tx.get_transaction_info())
    tx.edit_transaction(new_amount=600.0, new_desc="Обед в кафе")
    print(tx.get_transaction_info())
    tx.delete_transaction()

if __name__ == "__main__":
    main()
