# Основная функция программы
from functions import add_contact, view_contacts, search_contact, delete_contact, update_contact, import_phone_book

def main():
    while True:
        print("\nМеню Телефонного справочника:")
        print("1. Просмотр контактов")
        print("2. Добавить контакт")
        print("3. Поиск контакта")
        print("4. Удалить контакт")
        print("5. Обновить контакт")
        print("6. Импорт данных из файла")
        print("7. Выход")

        choice = input("Введите ваш выбор: ")

        if choice == '1':
            view_contacts()
        elif choice == '2':
            name = input("Введите имя: ")
            number = input("Введите номер: ")
            email = input("Введите email: ")
            add_contact(name, number, email)
        elif choice == '3':
            name = input("Введите имя для поиска: ")
            search_contact(name)
        elif choice == '4':
            name = input("Введите имя для удаления: ")
            delete_contact(name)
        elif choice == '5':
            name = input("Введите имя для обновления: ")
            number = input("Введите новый номер: ")
            email = input("Введите новый email: ")
            update_contact(name, number, email)
        elif choice == '6':
            file_name = input("Введите имя файла для импорта: ")
            import_phone_book(file_name)
        elif choice == '7':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()