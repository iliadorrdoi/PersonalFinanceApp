from models.currency import Currency

def main():
    usd = Currency(1, "USD", 89.5)  # курс USD относительно KGS
    eur = Currency(2, "EUR", 96.0)

    usd.update_exchange_rate(90.0)
    usd.convert_amount(100, eur.exchange_rate)

if __name__ == "__main__":
    main()
