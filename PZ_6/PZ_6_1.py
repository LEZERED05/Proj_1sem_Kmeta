"""
Дан целочисленный список размера 10. Вывести все содержащиеся в данном списе
четные числа в порядке убывания их индексов, а также их количество K.
"""


def program():
    try:
        a_list = []
        i = 0
        while i < 10:
            a_list.append(int(input('Введи значение списка: ')))
            i += 1
        var = [x for x in a_list if x % 2 == 0]
        var.reverse()
        print(var)
        print(len(var))

    except ValueError:
        print("Ошибка ввода")  # Оповещание об ошибке
        program()  # Повторный вызов функции из-за ошибки


program()
