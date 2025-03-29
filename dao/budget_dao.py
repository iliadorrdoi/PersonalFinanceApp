import sqlite3
from models.budget import Budget

class BudgetDAO:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            budget_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            category_id INTEGER,
            amount REAL,
            period TEXT
        )
        """)
        self.conn.commit()

    def create_budget(self, budget: Budget):
        self.cursor.execute("""
            INSERT INTO budgets (budget_id, user_id, category_id, amount, period)
            VALUES (?, ?, ?, ?, ?)
        """, (budget.budget_id, budget.user_id, budget.category_id, budget.amount, budget.period))
        self.conn.commit()

    def get_budget_by_id(self, budget_id):
        self.cursor.execute("SELECT * FROM budgets WHERE budget_id = ?", (budget_id,))
        row = self.cursor.fetchone()
        if row:
            return Budget(*row)
        return None

    def get_all_budgets(self):
        self.cursor.execute("SELECT * FROM budgets")
        rows = self.cursor.fetchall()
        return [Budget(*row) for row in rows]

    def update_budget(self, budget: Budget):
        self.cursor.execute("""
            UPDATE budgets
            SET amount = ?, period = ?
            WHERE budget_id = ?
        """, (budget.amount, budget.period, budget.budget_id))
        self.conn.commit()

    def delete_budget(self, budget_id):
        self.cursor.execute("DELETE FROM budgets WHERE budget_id = ?", (budget_id,))
        self.conn.commit()
