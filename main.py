from models.financial_goal import FinancialGoal
from datetime import datetime

def main():
    goal = FinancialGoal(
        goal_id=1,
        user_id=1,
        goal_name="Купить ноутбук",
        target_amount=50000.0,
        current_amount=15000.0,
        deadline=datetime(2025, 6, 1)
    )

    goal.create_goal()
    goal.get_goal_progress()
    goal.update_goal_progress(5000.0)
    goal.get_goal_progress()
    goal.delete_goal()

if __name__ == "__main__":
    main()
