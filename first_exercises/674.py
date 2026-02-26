__author__ = "Калашников А.Н."

from arrays import input_matrix, input_numbers, replace_elements_in_matrix
from test import test_674

"""
Задача 674: Даны целые числа a_1, ..., a_10, целочисленная квадратная матрица порядка n.
Заменить нулями в матрице те элементы с чётной суммой индексов, для которых имеются равные среди a_1, ..., a_10.
"""

test_674()

arr = input_numbers(10)

m = input_matrix()

result = replace_elements_in_matrix(m, arr)

print(result)