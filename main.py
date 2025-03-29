from dao.report_queries import ReportQueries

def main():
    reports = ReportQueries()

    user_id = 1

    print("\n📊 Расходы:")
    print("Всего расходов:", reports.total_expenses_by_user(user_id))

    print("\n📈 Доходы:")
    print("Всего доходов:", reports.total_income_by_user(user_id))

    print("\n🧾 Расходы по категориям:")
    for row in reports.expenses_by_category(user_id):
        print(row[0], "-", row[1])

    print("\n💼 Балансы по счетам:")
    for row in reports.account_balances(user_id):
        print(f"{row[0]}: {row[1]} {row[2]}")

    print("\n🎯 Цели, которые ещё не достигнуты:")
    for row in reports.incomplete_goals(user_id):
        print(f"{row[0]}: {row[1]}/{row[2]}, до {row[3]}")
