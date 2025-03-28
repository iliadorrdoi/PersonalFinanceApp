import sqlite3
from models.account import Account

class AccountDAO:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            account_name TEXT,
            balance REAL,
            currency TEXT
        )
        """)
        self.conn.commit()

    def create_account(self, account: Account):
        self.cursor.execute("""
            INSERT INTO accounts (account_id, user_id, account_name, balance, currency)
            VALUES (?, ?, ?, ?, ?)
        """, (account.account_id, account.user_id, account.account_name, account.balance, account.currency))
        self.conn.commit()

    def get_account_by_id(self, account_id):
        self.cursor.execute("SELECT * FROM accounts WHERE account_id = ?", (account_id,))
        row = self.cursor.fetchone()
        if row:
            return Account(*row)
        return None

    def get_all_accounts(self):
        self.cursor.execute("SELECT * FROM accounts")
        rows = self.cursor.fetchall()
        return [Account(*row) for row in rows]

    def update_account(self, account: Account):
        self.cursor.execute("""
            UPDATE accounts
            SET account_name = ?, balance = ?, currency = ?
            WHERE account_id = ?
        """, (account.account_name, account.balance, account.currency, account.account_id))
        self.conn.commit()

    def delete_account(self, account_id):
        self.cursor.execute("DELETE FROM accounts WHERE account_id = ?", (account_id,))
        self.conn.commit()
