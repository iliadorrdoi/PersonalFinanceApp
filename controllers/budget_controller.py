from dao.budget_dao import BudgetDAO
from models.budget import Budget

class BudgetController:
    def __init__(self):
        self.dao = BudgetDAO()

    def create_budget(self, budget_id, user_id, category_id, amount, period):
        budget = Budget(budget_id, user_id, category_id, amount, period)
        self.dao.create_budget(budget)
        print(f"Бюджет {amount} для категории {category_id} на период '{period}' создан.")

    def get_budget(self, budget_id):
        budget = self.dao.get_budget_by_id(budget_id)
        if budget:
            print(f"Бюджет: {budget.amount}, Период: {budget.period}")
        else:
            print("Бюджет не найден.")

    def update_budget(self, budget_id, new_amount=None, new_period=None):
        budget = self.dao.get_budget_by_id(budget_id)
        if budget:
            if new_amount:
                budget.amount = new_amount
            if new_period:
                budget.period = new_period
            self.dao.update_budget(budget)
            print("Бюджет обновлён.")
        else:
            print("Бюджет не найден.")

    def delete_budget(self, budget_id):
        self.dao.delete_budget(budget_id)
        print(f"Бюджет с ID {budget_id} удалён.")

    def list_budgets(self):
        budgets = self.dao.get_all_budgets()
        for b in budgets:
            print(f"[{b.budget_id}] {b.amount} на {b.period} (категория: {b.category_id})")
