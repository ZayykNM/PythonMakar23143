import random

def generate_random_list(n: int) -> list[int]:
    """
    Генерирует список случайных чисел длиной n.

    Аргументы:
        n: Целое число, определяющее длину списка.

    Возвращает:
        Список из n случайных чисел в диапазоне [0, 100).
    """
    return [random.randint(0, 100) for _ in range(n)]

# Примеры использования
print(generate_random_list(5))  # Например: [34, 7, 92, 15, 56]
print(generate_random_list(3))  # Например: [88, 23, 5]
