__author__ = "Калашников А.Н."

from arrays import input_array, is_multiple_of_3_not_5, count_correct_elements
from test import test_178b

"""
Задача 178 б): Даны натуральные числа n, a_1...a_n. Определить количество членов a_k последовательности a_1,...,a_n:
б) кратных 3 и не кратных 5;
"""

test_178b()

arr = input_array()

result = count_correct_elements(arr, is_multiple_of_3_not_5)

print(result)