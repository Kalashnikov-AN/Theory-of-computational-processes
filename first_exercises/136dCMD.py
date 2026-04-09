"""
Задача 136 д): Найти сумму ( (a_1)**2 + .... + (a_n)**2 )
Версия с командным интерфейсом.
"""

__author__ = "Калашников А.Н."

import sys

from arrays import parse_args, sum_square_array

if __name__ == "__main__":
    arr = parse_args(sys.argv[1:])
    result = sum_square_array(arr)

    print(f"Массив:       {arr}")
    print(f"Сумма квадратов: {result}")