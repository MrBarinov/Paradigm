from circle import Circle
from cross import Cross


class Table:
    __table: list

    def __init__(self):
        self.__table = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def set_sign(self, x: int, y: int, sign: Circle | Cross):
        if x < 1 or x > 3 or y < 1 or y > 3:
            print('Значения координат поля могут быть в промежутке от 1 до 3')
            return False
        x -= 1
        y -= 1
        if type(self.__table[x][y]) == Circle or type(self.__table[x][y]) == Cross:
            print('Клетка уже занята, попробуйте другую')
            return False
        self.__table[x][y] = sign
        return True

    def __str__(self):
        res: str = ''
        delim = '+-+-+-+\n'
        for i in range(3):
            res += delim
            res += '|'
            for j in range(3):
                res += f'{self.__table[i][j]}|'
            res += '\n'
        res += delim

        return res

    def check_is_winner(self):
        is_winner = self.__check_winner_in_line()
        if not is_winner:
            is_winner = self.__check_winner_in_column()
            if not is_winner:
                is_winner = self.__check_winner_in_cross()
        return is_winner

    def __check_winner_in_line(self):
        for i in range(3):
            circles_in_line: int = 0
            crosses_in_line: int = 0
            for j in range(3):
                if type(self.__table[i][j]) == Circle:
                    circles_in_line += 1
                elif type(self.__table[i][j]) == Cross:
                    crosses_in_line += 1
            if circles_in_line == 3 or crosses_in_line == 3:
                return True
        return False

    def __check_winner_in_column(self):
        for i in range(3):
            circles_in_col: int = 0
            crosses_in_col: int = 0
            for j in range(3):
                if type(self.__table[j][i]) == Circle:
                    circles_in_col += 1
                elif type(self.__table[j][i]) == Cross:
                    crosses_in_col += 1
            if circles_in_col == 3 or crosses_in_col == 3:
                return True
        return False

    def __check_winner_in_cross(self):
        circles_in_cross: int = 0
        crosses_in_cross: int = 0
        for i in range(3):
            if type(self.__table[i][i]) == Circle:
                circles_in_cross += 1
            elif type(self.__table[i][i]) == Cross:
                crosses_in_cross += 1
        if circles_in_cross == 3 or crosses_in_cross == 3:
            return True
        circles_in_cross = 0
        crosses_in_cross = 0
        for i in range(3):
            if type(self.__table[i][-i-1]) == Circle:
                circles_in_cross += 1
            elif type(self.__table[i][-i-1]) == Cross:
                crosses_in_cross += 1
        if circles_in_cross == 3 or crosses_in_cross == 3:
            return True
        return False
