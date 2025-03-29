from controllers.financial_goal_controller import FinancialGoalController

def main():
    controller = FinancialGoalController()
    controller.create_goal(1, 1, "Новый ноутбук", 50000.0, 10000.0, "2025-06-01")
    controller.get_goal(1)
    controller.update_goal(1, added_amount=5000.0)
    controller.list_goals()
    controller.delete_goal(1)

if __name__ == "__main__":
    main()
