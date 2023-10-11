"""
Для разработки использованы процедурная парадигма, структурная, функциональная
"""


def search_in_sorted_array(arr: list, number: int) -> int:
    index: int = len(arr) // 2
    if arr[index] != number and len(arr) == 1:
        return -1
    if arr[index] == number:
        return index
    elif arr[index] > number:
        return search_in_sorted_array(arr[:index], number)
    else:
        result: int = search_in_sorted_array(arr[index:], number)
        return index + result if result != -1 else result


my_arr: list = [0, 1, 2, 5, 8, 9, 12, 15]

print(search_in_sorted_array(my_arr, 9))

