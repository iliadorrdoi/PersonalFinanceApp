from dao.category_dao import CategoryDAO
from models.category import Category

class CategoryController:
    def __init__(self):
        self.dao = CategoryDAO()

    def create_category(self, category_id, user_id, name, tx_type):
        category = Category(category_id, user_id, name, tx_type)
        self.dao.create_category(category)
        print(f"Категория '{name}' ({tx_type}) добавлена.")

    def get_category(self, category_id):
        category = self.dao.get_category_by_id(category_id)
        if category:
            print(f"Категория: {category.name}, Тип: {category.tx_type}")
        else:
            print("Категория не найдена.")

    def update_category(self, category_id, new_name=None, new_type=None):
        category = self.dao.get_category_by_id(category_id)
        if category:
            if new_name:
                category.name = new_name
            if new_type:
                category.tx_type = new_type
            self.dao.update_category(category)
            print("Категория обновлена.")
        else:
            print("Категория не найдена.")

    def delete_category(self, category_id):
        self.dao.delete_category(category_id)
        print(f"Категория с ID {category_id} удалена.")

    def list_categories(self):
        categories = self.dao.get_all_categories()
        for c in categories:
            print(f"[{c.category_id}] {c.name} - {c.tx_type}")
