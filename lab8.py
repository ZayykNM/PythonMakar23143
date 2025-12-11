from PIL import Image
import os
"""
Лабораторная работа №8
Вариант 2

Задание:
Написать функцию, которая принимает путь к изображению и конвертирует его в формат .ICO,
сохраняя её по тому же пути, что и исходное изображение.

Описание работы:
Скрипт использует библиотеку Pillow (PIL). Реализована функция, которая принимает
путь к файлу, формирует новое имя с расширением .ico и сохраняет конвертированную
копию изображения в той же директории.
"""
def convert_to_ico(filename):
    # Проверяем, есть ли файл
    if not os.path.exists(filename):
        print(f"ОШИБКА: Файл '{filename}' не найден в папке!")
        print("Проверь, что картинка лежит рядом с файлом main.py")
        return

    try:
        # Открываем изображение
        with Image.open(filename) as img:
            # Создаем имя для нового файла (старое имя + .ico)
            # splitext разделяет имя и расширение
            name = os.path.splitext(filename)[0]
            new_filename = name + ".ico"
            
            # Сохраняем
            img.save(new_filename, format='ICO')
            print(f"Готово! Файл сохранен как: {new_filename}")
            
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# --- ЗАПУСК ---
# В кавычках напиши ТОЧНОЕ имя твоего файла с картинкой
my_image = "cat.jpg" 

convert_to_ico(my_image)