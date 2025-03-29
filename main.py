from dao.budget_dao import BudgetDAO
from models.budget import Budget

def main():
    dao = BudgetDAO()
    budget = Budget(1, 1, 1, 10000.0, "monthly")

    dao.create_budget(budget)

    found = dao.get_budget_by_id(1)
    if found:
        print("Найден бюджет:", found.amount, found.period)

    budget.amount = 12000.0
    budget.period = "quarterly"
    dao.update_budget(budget)

    for b in dao.get_all_budgets():
        print(b.amount, b.period)

    dao.delete_budget(1)

if __name__ == "__main__":
    main()
