"""
Дан список размера N. Заменить каждый элемент списка на среднее арифметическое
этого элемента и его соседей.
"""
import random

def program():
    try:
        lst = [random.randint(0, 1000) for el in range(int(input('Введите размер списка: ')))]
        print(lst)





    except ValueError:
        print("Ошибка ввода")  # Оповещание об ошибке
        program()  # Повторный вызов функции из-за ошибки


program()