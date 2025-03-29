import tkinter as tk
from tkinter import messagebox
from controllers.account_controller import AccountController

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Personal Finance Manager")
        self.window.geometry("400x300")

        self.account_ctrl = AccountController()

        tk.Label(self.window, text="💰 Personal Finance Manager", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.window, text="➕ Добавить счёт", width=25, command=self.add_account).pack(pady=5)
        tk.Button(self.window, text="📋 Показать все счета", width=25, command=self.show_accounts).pack(pady=5)
        tk.Button(self.window, text="🚪 Выйти", width=25, command=self.window.quit).pack(pady=20)

        self.window.mainloop()

    def add_account(self):
        win = tk.Toplevel()
        win.title("Новый счёт")

        tk.Label(win, text="ID").grid(row=0, column=0)
        tk.Label(win, text="User ID").grid(row=1, column=0)
        tk.Label(win, text="Название").grid(row=2, column=0)
        tk.Label(win, text="Баланс").grid(row=3, column=0)
        tk.Label(win, text="Валюта").grid(row=4, column=0)

        id_entry = tk.Entry(win)
        uid_entry = tk.Entry(win)
        name_entry = tk.Entry(win)
        bal_entry = tk.Entry(win)
        cur_entry = tk.Entry(win)

        id_entry.grid(row=0, column=1)
        uid_entry.grid(row=1, column=1)
        name_entry.grid(row=2, column=1)
        bal_entry.grid(row=3, column=1)
        cur_entry.grid(row=4, column=1)

        def submit():
            try:
                id = int(id_entry.get())
                uid = int(uid_entry.get())
                name = name_entry.get()
                bal = float(bal_entry.get())
                cur = cur_entry.get()
                self.account_ctrl.create_account(id, uid, name, bal, cur)
                messagebox.showinfo("Успех", "Счёт создан!")
                win.destroy()
            except ValueError:
                messagebox.showerror("Ошибка", "Неверный ввод данных!")

        tk.Button(win, text="Сохранить", command=submit).grid(row=5, column=0, columnspan=2, pady=10)

    def show_accounts(self):
        accounts = self.account_ctrl.dao.get_all_accounts()
        msg = "\n".join([f"{a.account_name}: {a.balance} {a.currency}" for a in accounts])
        if not msg:
            msg = "Нет доступных счетов."
        messagebox.showinfo("Счета", msg)

