def generate_range(n: int) -> list[int]:
    """
    Генерирует список чисел от 0 до n включительно.

    Аргументы:
        n: Целое число, до которого генерируется список.

    Возвращает:
        Список чисел от 0 до n.
    """
    return list(range(n + 1))

# Примеры использования
print(generate_range(5))  # [0, 1, 2, 3, 4, 5]
print(generate_range(0))  # [0]