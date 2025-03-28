from models.budget import Budget

def main():
    budget = Budget(1, 1, 1, 10000.0, "monthly")
    budget.create_budget()
    budget.check_budget_status(total_spent=3200.0)
    budget.update_budget(new_amount=12000.0)
    budget.check_budget_status(total_spent=5000.0)
    budget.delete_budget()

if __name__ == "__main__":
    main()
