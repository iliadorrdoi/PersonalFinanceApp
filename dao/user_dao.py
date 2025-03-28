import sqlite3
from models.user import User

class UserDAO:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            email TEXT,
            created_at TEXT
        )
        """)
        self.conn.commit()

    def create_user(self, user: User):
        self.cursor.execute("""
            INSERT INTO users (user_id, username, password, email, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (user.user_id, user.username, user.password, user.email, user.created_at))
        self.conn.commit()

    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        row = self.cursor.fetchone()
        if row:
            return User(*row)
        return None

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        return [User(*row) for row in rows]

    def update_user(self, user: User):
        self.cursor.execute("""
            UPDATE users SET username = ?, password = ?, email = ? WHERE user_id = ?
        """, (user.username, user.password, user.email, user.user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
        self.conn.commit()
