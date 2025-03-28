class Currency:
    def __init__(self, currency_id, currency_code, exchange_rate):
        self.currency_id = currency_id
        self.currency_code = currency_code  # "KGS", "USD", "EUR"
        self.exchange_rate = exchange_rate  # Относительно базовой валюты (например, KGS)

    def update_exchange_rate(self, new_rate):
        self.exchange_rate = new_rate
        print(f"Курс {self.currency_code} обновлён: {self.exchange_rate}")

    def convert_amount(self, amount, to_rate):
        converted = (amount / self.exchange_rate) * to_rate
        print(f"{amount} {self.currency_code} = {converted:.2f} по новому курсу")
        return converted
