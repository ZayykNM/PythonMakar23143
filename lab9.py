import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk, ImageGrab, ImageEnhance, ImageFilter
import time
"""
Лабораторная работа №9
Вариант 3

Задание:
Написать GUI приложение с кнопкой «Сделать скриншот». Скриншот должен вставляться
в окно приложения. Добавить возможности настройки яркости, фильтры, поворот изображения
и кнопку сохранения результата.

Описание работы:
Приложение разработано с использованием библиотеки Tkinter (интерфейс) и Pillow (захват
и обработка изображений). Реализован класс ScreenshotApp, который скрывает окно, делает
снимок экрана через ImageGrab, а затем позволяет применять эффекты (яркость, фильтры,
поворот) и сохранять итоговый файл.
"""
class ScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторная №9 - Скриншот Мастер")
        self.root.geometry("800x600")

        # Переменные для хранения изображений
        self.original_image = None  # Исходный скриншот
        self.current_image = None   # Обработанное изображение
        self.display_image = None   # Картинка для показа в окне (уменьшенная)

        # Переменные настроек
        self.brightness_val = tk.DoubleVar(value=1.0)
        self.rotation_val = tk.IntVar(value=0)
        self.filter_val = tk.StringVar(value="Нет")

        # --- Интерфейс (GUI) ---
        
        # 1. Верхняя панель с кнопкой скриншота
        top_frame = tk.Frame(root, pady=10)
        top_frame.pack()
        
        self.btn_snap = tk.Button(top_frame, text="📸 Сделать скриншот", command=self.take_screenshot, bg="#dddddd", font=("Arial", 12))
        self.btn_snap.pack()

        # 2. Область для картинки
        self.canvas_frame = tk.Frame(root, bg="gray")
        self.canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.label_image = tk.Label(self.canvas_frame, text="Здесь появится скриншот", bg="lightgray")
        self.label_image.pack(expand=True)

        # 3. Панель настроек (скрыта, пока нет скриншота)
        self.controls_frame = tk.Frame(root, pady=10)
        # Мы её покажем (pack) только после создания скриншота

        # Элементы управления:
        # Яркость
        tk.Label(self.controls_frame, text="Яркость:").pack(side=tk.LEFT, padx=5)
        self.scale_bright = tk.Scale(self.controls_frame, from_=0.1, to=2.0, resolution=0.1, 
                                     orient=tk.HORIZONTAL, variable=self.brightness_val, command=self.apply_effects)
        self.scale_bright.pack(side=tk.LEFT, padx=5)

        # Поворот
        tk.Button(self.controls_frame, text="↺ -90°", command=lambda: self.rotate_image(-90)).pack(side=tk.LEFT, padx=5)
        tk.Button(self.controls_frame, text="↻ +90°", command=lambda: self.rotate_image(90)).pack(side=tk.LEFT, padx=5)

        # Фильтры
        tk.Label(self.controls_frame, text="Фильтр:").pack(side=tk.LEFT, padx=5)
        filters = ["Нет", "Размытие", "Контур", "Рельеф"]
        self.combo_filter = ttk.Combobox(self.controls_frame, values=filters, state="readonly", textvariable=self.filter_val)
        self.combo_filter.pack(side=tk.LEFT, padx=5)
        self.combo_filter.bind("<<ComboboxSelected>>", self.apply_effects)

        # Кнопка Сохранить
        self.btn_save = tk.Button(self.controls_frame, text="💾 Сохранить", command=self.save_image, bg="lightblue")
        self.btn_save.pack(side=tk.LEFT, padx=20)

    def take_screenshot(self):
        """Скрывает окно, делает скриншот, возвращает окно."""
        self.root.withdraw()  # Спрятать окно программы
        time.sleep(0.5)       # Дать системе время отрисовать изменения (чтобы окна не было видно)
        
        try:
            # Делаем скриншот всего экрана
            self.original_image = ImageGrab.grab()
            self.current_image = self.original_image.copy()
            
            # Сбрасываем настройки
            self.brightness_val.set(1.0)
            self.rotation_val.set(0)
            self.filter_val.set("Нет")
            self.combo_filter.current(0)

            self.show_image()
            
            # Показываем панель управления
            self.controls_frame.pack(side=tk.BOTTOM, fill=tk.X)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сделать скриншот: {e}")
        finally:
            self.root.deiconify() # Вернуть окно программы

    def rotate_image(self, angle):
        """Меняет угол поворота и перерисовывает."""
        current_angle = self.rotation_val.get()
        new_angle = (current_angle + angle) % 360
        self.rotation_val.set(new_angle)
        self.apply_effects()

    def apply_effects(self, event=None):
        """Применяет все текущие настройки к исходному изображению."""
        if not self.original_image:
            return

        # 1. Берем оригинал
        img = self.original_image.copy()

        # 2. Применяем поворот
        angle = self.rotation_val.get()
        if angle != 0:
            img = img.rotate(-angle, expand=True) # expand=True чтобы углы не обрезались

        # 3. Применяем яркость
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(self.brightness_val.get())

        # 4. Применяем фильтр
        filter_name = self.filter_val.get()
        if filter_name == "Размытие":
            img = img.filter(ImageFilter.BLUR)
        elif filter_name == "Контур":
            img = img.filter(ImageFilter.CONTOUR)
        elif filter_name == "Рельеф":
            img = img.filter(ImageFilter.EMBOSS)

        self.current_image = img
        self.show_image()

    def show_image(self):
        """Отображает self.current_image в окне, уменьшая его для предпросмотра."""
        if not self.current_image:
            return
            
        # Создаем копию для отображения (thumbnail), чтобы не тормозило и влезало в окно
        display_img = self.current_image.copy()
        
        # Получаем размеры окна для картинки (или ставим дефолтные, если окно еще не отрисовано)
        w = self.canvas_frame.winfo_width()
        h = self.canvas_frame.winfo_height()
        if w < 100: w = 700
        if h < 100: h = 400
        
        display_img.thumbnail((w, h))
        
        # Конвертируем для Tkinter
        self.tk_image = ImageTk.PhotoImage(display_img)
        self.label_image.config(image=self.tk_image, text="")

    def save_image(self):
        """Открывает диалог сохранения."""
        if not self.current_image:
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                self.current_image.save(file_path)
                messagebox.showinfo("Успех", f"Изображение сохранено:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()