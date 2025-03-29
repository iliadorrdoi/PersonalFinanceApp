from controllers.budget_controller import BudgetController

def main():
    controller = BudgetController()
    controller.create_budget(1, 1, 1, 15000.0, "monthly")
    controller.get_budget(1)
    controller.update_budget(1, new_amount=17000.0)
    controller.list_budgets()
    controller.delete_budget(1)

if __name__ == "__main__":
    main()
