"""
для решения задачи была выбрана процедурная парадигма,
чтобы удобнее было подставлять разные числа
для печати таблицы умножения.
С другой стороны, можно было бы использовать и структурную парадигму,
т.к. задача решается в одно действие
"""


def mult_table(number: int):
    for i in range(1, 10):
        print(f'{number} * {i} = {number * i}')


mult_table(8)
