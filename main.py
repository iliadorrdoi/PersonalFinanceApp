from dao.category_dao import CategoryDAO
from models.category import Category

def main():
    dao = CategoryDAO()
    cat = Category(1, 1, "Продукты", "expense")

    dao.create_category(cat)

    found = dao.get_category_by_id(1)
    if found:
        print("Найдена категория:", found.name)

    cat.name = "Продукты и напитки"
    dao.update_category(cat)

    for c in dao.get_all_categories():
        print(c.name, c.tx_type)

    dao.delete_category(1)

if __name__ == "__main__":
    main()
