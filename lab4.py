from datetime import datetime

def is_leap_year(dt: datetime) -> bool:
    """
    Проверяет, является ли год в объекте datetime високосным.

    Аргументы:
        dt: Объект datetime, из которого извлекается год.

    Возвращает:
        True, если год високосный, иначе False.
    """
    year = dt.year
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

# Примеры использования
print(is_leap_year(datetime(2024, 1, 1)))  # True
print(is_leap_year(datetime(2023, 1, 1)))  # False