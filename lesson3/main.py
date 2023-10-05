"""
Для разработки игры крестики нолики использовались следующие парадигмы:
1. Объектно-ориентированная, для удобства создания элементов игры
2. Императивная для описания методов классов и самой игры
3. Структурная для описания логики игры
"""
from table import Table
from circle import Circle
from cross import Cross


new_table = Table()

play: bool = True
turn: str = 'Крестики'
while play:
    print(new_table)
    print(f'Ходят {turn}. Введите координаты клетки через пробел (строка столбец). Для выхода введите "exit":')
    coord = input().split(' ')
    if coord[0] == 'exit':
        play = False
    else:
        try:
            x = int(coord[0])
            y = int(coord[1])
            if turn == 'Крестики':
                sign = Cross()
            elif turn == 'Нолики':
                sign = Circle()
            if new_table.set_sign(x, y, sign):
                if new_table.check_is_winner():
                    print(new_table)
                    print(f'Победили {turn}! Поздравляем!')
                    new_game = input('Начать новую игру? (y/n): ')
                    if new_game == 'y':
                        new_table = Table()
                    else:
                        play = False
                if 'new_game' not in locals():
                    if turn == 'Крестики':
                        turn = 'Нолики'
                    elif turn == 'Нолики':
                        turn = 'Крестики'
        except ValueError:
            print('Значения координат должны быть числовыми от 1 до 3')

