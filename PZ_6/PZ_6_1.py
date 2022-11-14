"""
Дан целочисленный список размера 10. Вывести все содержащиеся в данном списе
четные числа в порядке убывания их индексов, а также их количество K.
"""


def program():
    try:
        a_list = []  # Создаём список

        for i in range(10):
            a_list.append(int(input('Введи значение списка: ')))  # Заполняем список 10 числами
            i += 1
        var = [x for x in a_list if x % 2 == 0]  # Поиск чётных значений списка
        var.reverse()  # Переварачиваем список
        print("писок чётных чисел в порядке убывания: ", var)
        print("Кол-во чётных чисел: ", len(var))  # Выводим длину списка чётных значений

    except ValueError:
        print("Ошибка ввода")  # Оповещание об ошибке
        program()  # Повторный вызов функции из-за ошибки


program()
