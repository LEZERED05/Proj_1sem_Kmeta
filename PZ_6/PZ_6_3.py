"""

Дан список размера N. Заменить каждый элемент списка на среднее арифметическое
этого элемента и его соседей.

"""
import random  # Импортируем библиотеку random


def program():
    try:
        count = []
        lst = [random.randint(0, 10) for el in range(int(input('Введите размер списка: ')))]
        # Заполняем список размера N, рандомными значениями
        print(f'Массив: {lst}')  # Выводим созданный список на экран
        for j in range(len(lst) - 1): # Перебираем массив с помощью цикла
            var = (lst[j - 1] + lst[j] + lst[j + 1]) / 3  # Находи среднее арифметическое
            count.append(int(var))  # Записываем в новый массив
        print(f'Результат: {count}')  # Выводим результат
    except ValueError:
        print("Ошибка ввода")  # Оповещание об ошибке
        program()  # Повторный вызов функции из-за ошибки


program()
