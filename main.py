# Основная функция программы
from functions import *

def main():
    file_name = 'phone_book.json'
    data = load_data(file_name)

    while True:
        print('\nМеню Телефонного справочника:')
        print('1. Просмотр всех записей')
        print('2. Добавить новую запись')
        print('3. Поиск записи')
        print('4. Удаление записи')
        print('5. Обновление записи')
        print('6. Импорт данных')
        print('7. Выход')

        choice = input('Введите ваш выбор: ')

        if choice == '1':
            view_records(data)
        elif choice == '2':
            name = input('Введите имя: ')
            number = input('Введите номер: ')
            add_record(data, name, number)
        elif choice == '3':
            name = input('Введите имя для поиска: ')
            search_record(data, name)
        elif choice == '4':
            name = input('Введите имя для удаления: ')
            delete_record(data, name)
        elif choice == '5':
            name = input('Введите имя для обновления: ')
            new_number = input('Введите новый номер: ')
            update_record(data, name, new_number)
        elif choice == '6':
            file_to_import = input('Введите имя файла для импорта: ')
            imported_data = import_data(file_to_import)
            if imported_data:
                data.extend(imported_data)
                save_data(file_name, data)
                print('Данные успешно импортированы.')
        elif choice == '7':
            print('Выход из Телефонного справочника.')
            break
        else:
            print('Неверный выбор. Пожалуйста, попробуйте снова.')

if __name__ == "__main__":
    main()