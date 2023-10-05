import math
from statistics import mean

my_arr1 = [1, 2, 3, 4, 5]
my_arr2 = [5, 4, 3, 2, 1]


def correl(arr1: list, arr2: list):
    avg1 = mean(arr1)
    avg2 = mean(arr2)

    def x_minus_mean(x):
        return x - avg1

    def y_minus_mean(y):
        return y - avg2

    x_chisl = list(map(x_minus_mean, arr1))
    y_chisl = list(map(y_minus_mean, arr2))

    def sum_chisl(x, y):
        return x * y

    def sum_znam_x(x):
        return x ** 2

    def sum_znam_y(y):
        return y ** 2

    chisl = sum(map(sum_chisl, x_chisl, y_chisl))
    znam = math.sqrt(sum(map(sum_znam_x, x_chisl)) * sum(map(sum_znam_y, y_chisl)))

    return chisl / znam


print(correl(my_arr1, my_arr2))

