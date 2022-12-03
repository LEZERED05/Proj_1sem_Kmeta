"""
Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
отражающая продажи продукции по дням в кг. Преобразовать информацию из
строки в словари, с использованием функции найти среднее значение продаж по
каждому виду продукции, результаты вывести на экран
"""


def program():
    lst = {}
    inf = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
    print(inf)  # Вывод строки
    inf = inf.split()  # Преобразуем строку в список
    lst['Продукт 1'] = inf[0]  # Создаём ключи и их значения
    lst['продажи продукта 1'] = []
    for i in inf[1:5]:  # Заполняем значения ключей
        lst['продажи продукта 1'].append(int(i))
    lst['Продукт 2'] = inf[6]  # Создаём ключи и их значения
    lst['продажи продукта 2'] = []
    for i in inf[7:11]:  # Заполняем значения ключей
        lst['продажи продукта 2'].append(int(i))
    print(lst)  # Вывод словаря
    # Нахождение средних значений продаж
    sum_lst1 = sum(lst['продажи продукта 1'])  # Сумма значений массива
    sum_lst2 = sum(lst['продажи продукта 2'])
    list_avg1 = sum_lst1/len(lst['продажи продукта 1'])  # делим результат суммы на длину списка
    list_avg2 = sum_lst2 / len(lst['продажи продукта 2'])
    print(f"Среднее значение продаж апельсинов: {list_avg1}")  # Вывод результата
    print(f"Среднее значение продаж яблок: {list_avg2}")


program()
