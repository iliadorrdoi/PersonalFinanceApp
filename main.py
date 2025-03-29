from dao.financial_goal_dao import FinancialGoalDAO
from models.financial_goal import FinancialGoal
from datetime import datetime

def main():
    dao = FinancialGoalDAO()
    goal = FinancialGoal(1, 1, "Ноутбук", 50000.0, 15000.0, datetime(2025, 6, 1))

    dao.create_goal(goal)

    found = dao.get_goal_by_id(1)
    if found:
        print("Найдена цель:", found.goal_name)

    goal.current_amount = 25000.0
    goal.target_amount = 55000.0
    dao.update_goal(goal)

    for g in dao.get_all_goals():
        print(g.goal_name, g.current_amount, g.deadline)

    dao.delete_goal(1)

if __name__ == "__main__":
    main()
