import sqlite3

class ReportQueries:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def total_expenses_by_user(self, user_id):
        self.cursor.execute("""
            SELECT SUM(amount) FROM transactions
            WHERE user_id = ? AND tx_type = 'expense'
        """, (user_id,))
        result = self.cursor.fetchone()[0]
        return result or 0.0

    def total_income_by_user(self, user_id):
        self.cursor.execute("""
            SELECT SUM(amount) FROM transactions
            WHERE user_id = ? AND tx_type = 'income'
        """, (user_id,))
        result = self.cursor.fetchone()[0]
        return result or 0.0

    def expenses_by_category(self, user_id):
        self.cursor.execute("""
            SELECT c.name, SUM(t.amount) 
            FROM transactions t
            JOIN categories c ON t.category_id = c.category_id
            WHERE t.user_id = ? AND t.tx_type = 'expense'
            GROUP BY c.name
        """, (user_id,))
        return self.cursor.fetchall()

    def account_balances(self, user_id):
        self.cursor.execute("""
            SELECT account_name, balance, currency FROM accounts
            WHERE user_id = ?
        """, (user_id,))
        return self.cursor.fetchall()

    def incomplete_goals(self, user_id):
        self.cursor.execute("""
            SELECT goal_name, current_amount, target_amount, deadline 
            FROM financial_goals
            WHERE user_id = ? AND current_amount < target_amount
        """, (user_id,))
        return self.cursor.fetchall()
