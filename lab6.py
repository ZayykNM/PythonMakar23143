import sqlite3

def init_db():
    """Создаёт таблицу users и заполняет её тестовыми данными, сбрасывая счётчик id."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Удаляем таблицу users, если она существует
    cursor.execute('DROP TABLE IF EXISTS users')

    # Создаём таблицу users заново
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # Заполняем таблицу тестовыми данными
    test_users = [
        ('admin', 'admin@example.com'),
        ('user1', 'user1@example.com'),
        ('user2', 'user2@example.com')
    ]
    cursor.executemany('INSERT INTO users (username, email) VALUES (?, ?)', test_users)

    conn.commit()
    conn.close()

def get_record_id(table_name: str, field: str, value) -> int | None:
    """
    Возвращает идентификатор записи в таблице, где значение указанного поля совпадает с переданным значением.
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT id FROM {table_name} WHERE {field} = ?"
    cursor.execute(query, (value,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None

# Инициализируем базу данных
init_db()

# Пример использования
print(get_record_id('users', 'username', 'admin'))  # вернёт 1
print(get_record_id('users', 'username', 'user2'))  # вернёт 3