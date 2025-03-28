from datetime import datetime

class FinancialGoal:
    def __init__(self, goal_id, user_id, goal_name, target_amount, current_amount, deadline):
        self.goal_id = goal_id
        self.user_id = user_id
        self.goal_name = goal_name
        self.target_amount = target_amount
        self.current_amount = current_amount
        self.deadline = deadline  # datetime объект

    def create_goal(self):
        print(f"Финансовая цель '{self.goal_name}' создана. Цель: {self.target_amount}")

    def update_goal_progress(self, added_amount):
        self.current_amount += added_amount
        print(f"Добавлено {added_amount}. Текущий прогресс: {self.current_amount}/{self.target_amount}")

    def delete_goal(self):
        print(f"Цель '{self.goal_name}' удалена.")

    def get_goal_progress(self):
        percentage = (self.current_amount / self.target_amount) * 100
        print(f"Прогресс: {percentage:.2f}%")
        return percentage
