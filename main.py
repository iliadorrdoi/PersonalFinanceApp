from dao.account_dao import AccountDAO
from models.account import Account

def main():
    dao = AccountDAO()
    acc = Account(1, 1, "Кошелёк", 2500.0, "KGS")

    dao.create_account(acc)

    found = dao.get_account_by_id(1)
    if found:
        print("Найден счёт:", found.account_name, found.balance)

    acc.balance = 3000.0
    dao.update_account(acc)

    all_accounts = dao.get_all_accounts()
    for a in all_accounts:
        print(a.account_name, a.balance, a.currency)

    dao.delete_account(1)

if __name__ == "__main__":
    main()
