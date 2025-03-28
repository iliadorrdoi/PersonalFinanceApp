from models.category import Category

def main():
    category = Category(1, 1, "Продукты", "expense")
    category.create_category()
    print(category.get_info())
    category.update_category(new_name="Продукты и напитки")
    print(category.get_info())
    category.delete_category()

if __name__ == "__main__":
    main()
