__author__ = "Калашников А.Н."

from arrays import input_or_random_array, get_matrix_order, input_or_random_matrix, apply_replacement

"""
Задача 674: Даны целые числа a_1, ..., a_10, целочисленная квадратная матрица порядка n.
Заменить нулями в матрице те элементы с чётной суммой индексов, для которых имеются равные среди a_1, ..., a_10.
"""


if __name__ == "__main__":
    a = input_or_random_array(10)
    n = get_matrix_order()
    matrix = input_or_random_matrix(n)

    print("\nИсходная матрица:")
    print(matrix)

    result = apply_replacement(matrix, a)

    print("\nМатрица после замены:")
    print(result)