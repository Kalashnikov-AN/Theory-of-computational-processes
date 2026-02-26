__author__ = "Калашников А.Н."

from arrays import  find_double_sum, sum_334a
from test import test_334a

"""
Задача 334 а): Найти сумму i = 1,100 для вложенной суммы j = 1,50 ( 1/(i+j**2) )
"""

test_334a()

n,k = int(input("Введите n: ")), int(input("Введите k: "))

result = find_double_sum(n, k, sum_334a)

print(result)