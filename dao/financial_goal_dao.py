import sqlite3
from models.financial_goal import FinancialGoal
from datetime import datetime

class FinancialGoalDAO:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS financial_goals (
            goal_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            goal_name TEXT,
            target_amount REAL,
            current_amount REAL,
            deadline TEXT
        )
        """)
        self.conn.commit()

    def create_goal(self, goal: FinancialGoal):
        self.cursor.execute("""
            INSERT INTO financial_goals (goal_id, user_id, goal_name, target_amount, current_amount, deadline)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            goal.goal_id, goal.user_id, goal.goal_name,
            goal.target_amount, goal.current_amount,
            goal.deadline.isoformat()
        ))
        self.conn.commit()

    def get_goal_by_id(self, goal_id):
        self.cursor.execute("SELECT * FROM financial_goals WHERE goal_id = ?", (goal_id,))
        row = self.cursor.fetchone()
        if row:
            row = list(row)
            row[5] = datetime.fromisoformat(row[5])
            return FinancialGoal(*row)
        return None

    def get_all_goals(self):
        self.cursor.execute("SELECT * FROM financial_goals")
        rows = self.cursor.fetchall()
        goals = []
        for row in rows:
            row = list(row)
            row[5] = datetime.fromisoformat(row[5])
            goals.append(FinancialGoal(*row))
        return goals

    def update_goal(self, goal: FinancialGoal):
        self.cursor.execute("""
            UPDATE financial_goals
            SET current_amount = ?, target_amount = ?
            WHERE goal_id = ?
        """, (goal.current_amount, goal.target_amount, goal.goal_id))
        self.conn.commit()

    def delete_goal(self, goal_id):
        self.cursor.execute("DELETE FROM financial_goals WHERE goal_id = ?", (goal_id,))
        self.conn.commit()
