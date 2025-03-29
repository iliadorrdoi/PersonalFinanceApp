import sqlite3
from models.transaction import Transaction
from datetime import datetime

class TransactionDAO:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            account_id INTEGER,
            category_id INTEGER,
            amount REAL,
            tx_type TEXT,
            currency TEXT,
            date TEXT,
            description TEXT
        )
        """)
        self.conn.commit()

    def create_transaction(self, tx: Transaction):
        self.cursor.execute("""
            INSERT INTO transactions (transaction_id, user_id, account_id, category_id,
                                      amount, tx_type, currency, date, description)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            tx.transaction_id, tx.user_id, tx.account_id, tx.category_id,
            tx.amount, tx.tx_type, tx.currency, tx.date.isoformat(), tx.description
        ))
        self.conn.commit()

    def get_transaction_by_id(self, tx_id):
        self.cursor.execute("SELECT * FROM transactions WHERE transaction_id = ?", (tx_id,))
        row = self.cursor.fetchone()
        if row:
            row = list(row)
            row[7] = datetime.fromisoformat(row[7])  # Преобразуем дату обратно
            return Transaction(*row)
        return None

    def get_all_transactions(self):
        self.cursor.execute("SELECT * FROM transactions")
        rows = self.cursor.fetchall()
        tx_list = []
        for row in rows:
            row = list(row)
            row[7] = datetime.fromisoformat(row[7])
            tx_list.append(Transaction(*row))
        return tx_list

    def update_transaction(self, tx: Transaction):
        self.cursor.execute("""
            UPDATE transactions
            SET amount = ?, description = ?
            WHERE transaction_id = ?
        """, (tx.amount, tx.description, tx.transaction_id))
        self.conn.commit()

    def delete_transaction(self, tx_id):
        self.cursor.execute("DELETE FROM transactions WHERE transaction_id = ?", (tx_id,))
        self.conn.commit()
