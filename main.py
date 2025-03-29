from controllers.category_controller import CategoryController

def main():
    controller = CategoryController()

    controller.create_category(1, 1, "Продукты", "expense")
    controller.get_category(1)
    controller.update_category(1, new_name="Еда и напитки")
    controller.list_categories()
    controller.delete_category(1)

if __name__ == "__main__":
    main()
