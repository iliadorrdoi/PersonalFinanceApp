from dao.financial_goal_dao import FinancialGoalDAO
from models.financial_goal import FinancialGoal
from datetime import datetime

class FinancialGoalController:
    def __init__(self):
        self.dao = FinancialGoalDAO()

    def create_goal(self, goal_id, user_id, name, target_amount, current_amount, deadline_str):
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
        goal = FinancialGoal(goal_id, user_id, name, target_amount, current_amount, deadline)
        self.dao.create_goal(goal)
        print(f"Цель '{name}' создана: {current_amount}/{target_amount} до {deadline.date()}")

    def get_goal(self, goal_id):
        goal = self.dao.get_goal_by_id(goal_id)
        if goal:
            print(f"Цель: {goal.goal_name} | {goal.current_amount}/{goal.target_amount} до {goal.deadline.date()}")
        else:
            print("Цель не найдена.")

    def update_goal(self, goal_id, added_amount=0, new_target=None):
        goal = self.dao.get_goal_by_id(goal_id)
        if goal:
            goal.current_amount += added_amount
            if new_target:
                goal.target_amount = new_target
            self.dao.update_goal(goal)
            print("Цель обновлена.")
        else:
            print("Цель не найдена.")

    def delete_goal(self, goal_id):
        self.dao.delete_goal(goal_id)
        print(f"Цель с ID {goal_id} удалена.")

    def list_goals(self):
        goals = self.dao.get_all_goals()
        for g in goals:
            print(f"[{g.goal_id}] {g.goal_name}: {g.current_amount}/{g.target_amount} до {g.deadline.date()}")
