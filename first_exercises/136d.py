__author__ = "Калашников А.Н."

from arrays import input_array, sum_square_array
from test import test_136d

"""
Задача 136 д): Найтиу сумму ( (a_1)**2 + .... + (a_n)**2 )
"""

test_136d()

arr = input_array()

result = sum_square_array(arr)

print(result)