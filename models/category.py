class Category:
    def __init__(self, category_id, user_id, name, tx_type):
        self.category_id = category_id
        self.user_id = user_id
        self.name = name
        self.tx_type = tx_type  # "income" или "expense"

    def create_category(self):
        print(f"Категория '{self.name}' ({self.tx_type}) создана.")

    def update_category(self, new_name=None, new_type=None):
        if new_name:
            self.name = new_name
        if new_type:
            self.tx_type = new_type
        print(f"Категория обновлена: {self.name} ({self.tx_type})")

    def delete_category(self):
        print(f"Категория '{self.name}' удалена.")

    def get_info(self):
        return f"Категория: {self.name} | Тип: {self.tx_type}"
