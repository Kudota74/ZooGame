import tkinter as tk
from tkinter import scrolledtext
import sqlite3

def add_animal():
    # Получаем значения полей ввода
    art_value = art_text.get("1.0", tk.END).strip()
    place_value = place_entry.get()
    hint_value = hint_entry.get()
    name_value = name_entry.get()

    # Создаем подключение к базе данных
    conn = sqlite3.connect('zoo_game.db')
    cursor = conn.cursor()

    # Выполняем SQL-запрос для добавления данных в таблицу
    cursor.execute('''
        INSERT INTO animals (art, place, hint, name)
        VALUES (?, ?, ?, ?)
    ''', (art_value, place_value, hint_value, name_value))

    # Сохраняем изменения и закрываем подключение к базе данных
    conn.commit()
    conn.close()

    # Очищаем поля ввода
    art_text.delete("1.0", tk.END)
    place_entry.delete(0, tk.END)
    hint_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)

def on_copy(event):
    if event.widget == art_text:
        root.clipboard_clear()
        root.clipboard_append(art_text.get("sel.first", "sel.last"))

def on_paste(event):
    if event.widget == art_text:
        art_text.delete("1.0", tk.END)
        art_text.insert(tk.END, root.clipboard_get())

# Создаем главное окно
root = tk.Tk()
root.title("Добавление животного")

# Создаем метки и поля ввода для каждого поля таблицы
art_label = tk.Label(root, text="Арт:")
art_label.pack()
art_text = scrolledtext.ScrolledText(root, height=10, width=30)
art_text.pack()

place_label = tk.Label(root, text="Место:")
place_label.pack()
place_entry = tk.Entry(root)
place_entry.pack()

hint_label = tk.Label(root, text="Подсказка:")
hint_label.pack()
hint_entry = tk.Entry(root)
hint_entry.pack()

name_label = tk.Label(root, text="Имя:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Создаем кнопку "Добавить"
add_button = tk.Button(root, text="Добавить", command=add_animal)
add_button.pack()

# Привязываем обработчики событий для сочетаний клавиш Ctrl+C и Ctrl+V
root.bind("<Control-c>", on_copy)
root.bind("<Control-v>", on_paste)

# Запускаем главный цикл обработки событий
root.mainloop()
