import sqlite3
from models.category import Category

class CategoryDAO:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            name TEXT,
            tx_type TEXT
        )
        """)
        self.conn.commit()

    def create_category(self, category: Category):
        self.cursor.execute("""
            INSERT INTO categories (category_id, user_id, name, tx_type)
            VALUES (?, ?, ?, ?)
        """, (category.category_id, category.user_id, category.name, category.tx_type))
        self.conn.commit()

    def get_category_by_id(self, category_id):
        self.cursor.execute("SELECT * FROM categories WHERE category_id = ?", (category_id,))
        row = self.cursor.fetchone()
        if row:
            return Category(*row)
        return None

    def get_all_categories(self):
        self.cursor.execute("SELECT * FROM categories")
        rows = self.cursor.fetchall()
        return [Category(*row) for row in rows]

    def update_category(self, category: Category):
        self.cursor.execute("""
            UPDATE categories
            SET name = ?, tx_type = ?
            WHERE category_id = ?
        """, (category.name, category.tx_type, category.category_id))
        self.conn.commit()

    def delete_category(self, category_id):
        self.cursor.execute("DELETE FROM categories WHERE category_id = ?", (category_id,))
        self.conn.commit()
