# Телефонный справочник
Консольное приложение "телефонный справочник" с внешним хранилищем в файле формата JSON.


Программа имеет следующий функционал: Просмотр контактов, Добавление контактов, Поиск контактов, Удаление контактов, Обновление контактов, Импорт данных из файла.  
Для удобного восприятия кода, основаня функция программы (**main.py**) отделена от вспомогательных функций (**functions.py**). Хранилище записей (**phone_book.json**) создается в текущей папке программы. Импорт из внешнего хранилища в формате JSON производится из той же папке с указанием имени импортируемого файла.

#### Основное меню программы и пример добавления записи
![Основное меню программы и пример добавления записи](https://github.com/ArtRadchenko/Python_Phone_book/blob/master/Screenshots/001.jpg?raw=true)

#### Просмотр телефонного справочника
![Просмотр телефонного справочника](https://github.com/ArtRadchenko/Python_Phone_book/blob/master/Screenshots/002.jpg?raw=true)

# Структура репозитория
*Screenshots* - папка со скриншотами.  
*.gitignore* - исключения для GIT.  
*functions.py* - вспомогательные функции программы.  
*main.py* - основная функция программы.  
*phone_book.json* - пример созданного хранилища записей.  
*readme.md* - файл описания в формате markdown.  