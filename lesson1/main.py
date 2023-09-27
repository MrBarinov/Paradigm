def sort_arr_imp(array: list):
    length: int = len(array)
    for i in range(0, length-1):
        for j in range(0, length-1):
            if array[j] < array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])
    return array


def sort_arr_decl(array: list):
    array.sort(reverse=True)
    return array


myArr: list = [5, 8, 9, 3, 1, 7]

print(sort_arr_imp(myArr))

myArr: list = [5, 8, 9, 3, 1, 7]

print(sort_arr_decl(myArr))
