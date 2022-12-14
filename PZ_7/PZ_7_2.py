"""
Дана строка-предложение с избыточными пробелами между словами.
Преобразовать ее так, чтобы между словами был ровно один пробел.
"""

def program():
    try:
        num = str(input("Введите строку с избыточными пробелами: ")) # Ввод сткроки
        print(" ".join(num.split()))  # ЗАнесли в массив и с помощью .join разделили на одиночные пробелы
    except ValueError:
        print("Ошибка ввода")  # Оповещание об ошибке
        program()  # Повторный вызов функции из-за ошибки


program()