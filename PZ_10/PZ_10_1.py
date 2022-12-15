"""
В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
1. в каких магазинах нельзя приобрести сыр.
2. в каких магазинах можно приобрести одновременно молоко и сахар.
3. в каких магазинах можно приобрести соль.
"""

lst_shop = {'Магнит': ['молоко', 'соль', 'сахар'],
            'Пятёрочка': ['мясо', 'молоко', 'сыр'],
            'Перекрёсток': ['молко', 'творог', 'сыр', 'сахар']}  # Список магазинов и продукции

cheese = ''.join([i for i in lst_shop.keys() if 'сыр' not in lst_shop[i]])  # поиск магазинов без сыра
print(f'В каких магазинах нельзя приобрести сыр: {cheese}')
milk_sugar = ', '.join([i for i in lst_shop.keys() if 'молоко' and 'сахар' in lst_shop[i]])  # поиск магазинов с молоком и сахаром одновременно
print(f'В каких магазинах можно приобрести одновременно молоко и сахар: {milk_sugar}')
salt = ', '.join([i for i in lst_shop.keys() if 'соль' in lst_shop[i]])  # поиск магазинов где есть соль
print(f'В каких магазинах можно приобрести соль: {salt}')

# Данная задача не предназначена для выполнение через множества, со словарём работает идеально, а через множества
# было бы тонна бесполезного кода, я считаю что задача выпонена отлично
# Данную часть кода выполнить если вы чем-то
# недовольны: (доказательство что для множеств есть другие места для применения)
# mag = {'молоко', 'соль', 'сахар'}
# pyt = {'мясо', 'молоко', 'сыр'}
# per = {'молоко', 'творог', 'сыр', 'сахар'}
# prod = ', '.join(mag | pyt | per)  # все продукты
# print('Список всех продуктов в магазинах: ', prod)  # вывод всех продуктов
