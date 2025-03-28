class Budget:
    def __init__(self, budget_id, user_id, category_id, amount, period):
        self.budget_id = budget_id
        self.user_id = user_id
        self.category_id = category_id
        self.amount = amount
        self.period = period  # Например: "monthly", "yearly"

    def create_budget(self):
        print(f"Бюджет {self.amount} на период {self.period} создан.")

    def update_budget(self, new_amount=None, new_period=None):
        if new_amount is not None:
            self.amount = new_amount
        if new_period:
            self.period = new_period
        print(f"Бюджет обновлён: {self.amount} на {self.period}")

    def delete_budget(self):
        print("Бюджет удалён.")

    def check_budget_status(self, total_spent):
        remaining = self.amount - total_spent
        print(f"Остаток бюджета: {remaining}")
        return remaining
