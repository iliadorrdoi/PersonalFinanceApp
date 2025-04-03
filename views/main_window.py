import tkinter as tk
from tkinter import messagebox
from controllers.account_controller import AccountController
from controllers.transaction_controller import TransactionController
from controllers.category_controller import CategoryController

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Personal Finance Manager")
        self.window.geometry("400x400")

        self.account_ctrl = AccountController()
        self.transaction_ctrl = TransactionController()
        self.category_ctrl = CategoryController()

        tk.Label(self.window, text="💰 Personal Finance Manager", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.window, text="➕ Добавить счёт", width=30, command=self.add_account).pack(pady=5)
        tk.Button(self.window, text="📋 Показать счета", width=30, command=self.show_accounts).pack(pady=5)
        tk.Button(self.window, text="➕ Добавить транзакцию", width=30, command=self.add_transaction).pack(pady=5)
        tk.Button(self.window, text="🚪 Выйти", width=30, command=self.window.quit).pack(pady=20)

        self.window.mainloop()

    def add_account(self):
        win = tk.Toplevel()
        win.title("Новый счёт")

        labels = ["ID", "User ID", "Название", "Баланс", "Валюта"]
        entries = []
        for i, label in enumerate(labels):
            tk.Label(win, text=label).grid(row=i, column=0)
            entry = tk.Entry(win)
            entry.grid(row=i, column=1)
            entries.append(entry)

        def submit():
            try:
                acc_id = int(entries[0].get())
                user_id = int(entries[1].get())
                name = entries[2].get()
                balance = float(entries[3].get())
                currency = entries[4].get()

                existing = self.account_ctrl.dao.get_account_by_id(acc_id)
                if existing:
                    messagebox.showerror("Ошибка", f"Счёт с ID {acc_id} уже существует.")
                    return

                self.account_ctrl.create_account(acc_id, user_id, name, balance, currency)
                messagebox.showinfo("Успех", "Счёт создан!")
                win.destroy()
            except ValueError:
                messagebox.showerror("Ошибка", "Проверьте правильность ввода!")

        tk.Button(win, text="Сохранить", command=submit).grid(row=5, column=0, columnspan=2, pady=10)

    def show_accounts(self):
        accounts = self.account_ctrl.dao.get_all_accounts()
        if not accounts:
            messagebox.showinfo("Счета", "Счета не найдены.")
            return
        msg = "\n".join([f"{a.account_name}: {a.balance} {a.currency}" for a in accounts])
        messagebox.showinfo("Счета", msg)

    def add_transaction(self):
        win = tk.Toplevel()
        win.title("Добавить транзакцию")

        labels = ["ID", "User ID", "Account ID", "Category ID", "Сумма", "Тип (income/expense)", "Валюта", "Описание"]
        entries = []
        for i, label in enumerate(labels):
            tk.Label(win, text=label).grid(row=i, column=0)
            entry = tk.Entry(win)
            entry.grid(row=i, column=1)
            entries.append(entry)

        def submit():
            try:
                tx_id = int(entries[0].get())
                user_id = int(entries[1].get())
                acc_id = int(entries[2].get())
                cat_id = int(entries[3].get())
                amount = float(entries[4].get())
                tx_type = entries[5].get().lower()
                if tx_type not in ("income", "expense"):
                    raise ValueError("Тип должен быть income или expense")
                currency = entries[6].get()
                desc = entries[7].get()

                self.transaction_ctrl.add_transaction(
                    tx_id, user_id, acc_id, cat_id, amount, tx_type, currency, desc
                )
                messagebox.showinfo("Успех", "Транзакция добавлена!")
                win.destroy()
            except ValueError as e:
                messagebox.showerror("Ошибка", f"Неверный ввод: {e}")

        tk.Button(win, text="Добавить", command=submit).grid(row=len(labels), column=0, columnspan=2, pady=10)
