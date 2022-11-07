#  Постановка задачи: Начальный вклад в банке равен 1000 руб. Через каждый месяц размер вклада
# увеличивается на P процентов от имеющейся суммы (P — вещественное число, 0< P
# <25). По данному P определить, через сколько месяцев размер вклада превысит 1100
# руб., и вывести найденное количество месяцев K (целое число) и итоговый размер
# вклада S (вещественное число).
def program():  # Объявляем функцию
    try:  # Выполнится если всё верно
        duration = 0  # количество месяцев K
        contribution = 1000  # Начальный вклад в банке
        percent = float(input("Введите процент он 0 до 25: "))  # Ввод процента
        if (0 < percent < 25):  # Проверка значения percent на диапозон
            while (contribution <= 1100):  # Узнаём колво месяцев превышения вклада
                duration += 1
                contribution += contribution * percent / 100  # Находим итоговый размер вклада
            print("Number of months: ", duration)  # Вывод успешно выполненной программы
            print("Size contribution: ", contribution)  # Вывод успешно выполненной программы
        else:
            print("Неверное значение!!!")  # Вывод уведомления об ошибке
            program()  # повторный вызов функции при ошибке
    except ValueError:  # Выполнится если введено не верное значение
        print("Неверное значение!!!")  # Вывод уведомления об ошибке
        program()  # повторный вызов функции при ошибке


program()  # Запуск функции и программы
