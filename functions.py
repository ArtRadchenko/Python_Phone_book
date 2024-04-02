# Функции телефонного справочника
import json

# Функция для загрузки данных из файла
def load_data(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

# Функция для сохранения данных в файл
def save_data(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

