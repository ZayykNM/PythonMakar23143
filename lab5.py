import json

def json_to_dict(json_string: str) -> dict:
    """
    Конвертирует JSON-строку в словарь Python.

    Аргументы:
        json_string: Строка в формате JSON.

    Возвращает:
        Словарь, полученный из JSON-строки.
    """
    return json.loads(json_string)

# Пример использования
json_string = '{"name": "Alice", "age": 30, "city": "Moscow"}'
result = json_to_dict(json_string)
print(result)  # {'name': 'Alice', 'age': 30, 'city': 'Moscow'}