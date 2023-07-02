import sqlite3
import random
import os
import time


def fetch_animals_from_db():
    # Создаем подключение к базе данных
    conn = sqlite3.connect('zoo_game.db')
    cursor = conn.cursor()

    # Выполняем запрос SELECT для получения данных из таблицы animals
    cursor.execute('SELECT art, place, hint FROM animals')
    animals_data = cursor.fetchall()

    # Закрываем подключение к базе данных
    conn.close()

    return animals_data


def play_game(animals):
    print(
        "Привет! Сегодня мы сыграем в игру зоопарк! По месту вы должны отгадать животное, но у вас есть возможность взять подсказку.")
    time.sleep(3)
    os.system("cls")

    images = [animal[0] for animal in animals]
    places = [animal[1] for animal in animals]
    hints = [animal[2] for animal in animals]

    for i in range(len(images)):
        random_index = random.choice(range(len(images)))

        print("Скажите где живёт?!\n")
        print(images[random_index])

        choice = int(input("Вы можете выбрать: 1 - Отгадать сразу; 2 - Взять подсказку. Но учтите подсказок всего 3. "))

        hint_amount = 0
        answer = ""

        while answer != places[random_index]:
            if choice == 1:
                print(f"Варианты: {places}")
                answer = input("Ваш ответ: ")
                os.system("cls")
            else:
                if hint_amount != 3:
                    print(hints[random_index])
                    hint_amount += 1
                    choice = int(input(
                        "Вы можете выбрать: 1 - Отгадать сразу; 2 - Взять подсказку. Но учтите подсказок всего 3. "))
                else:
                    print("Подсказки кончились")
                    choice = 1
        print("Правильно!")
        del images[random_index]
        del places[random_index]
        del hints[random_index]


def main():
    animals_data = fetch_animals_from_db()
    play_game(animals_data)


if __name__ == "__main__":
    main()
