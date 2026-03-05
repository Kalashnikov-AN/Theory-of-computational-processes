"""
Задача 136 д): Найти сумму ( (a_1)**2 + .... + (a_n)**2 )
Версия с командным интерфейсом.
"""

import sys


def sum_square_array(arr: list[float | int]) -> float:
    """Функция суммирования всех элементов массива arr, возведённых в квадрат."""
    s = 0
    for i in range(len(arr)):
        s += arr[i] ** 2
    return s


def parse_args(args: list[str]) -> list[float]:
    """Разбирает аргументы командной строки и возвращает список чисел."""
    if not args:
        print("Ошибка: не передано ни одного числа.")
        print(f"Использование: python {sys.argv[0]} <число1> <число2> ...")
        sys.exit(1)

    numbers = []
    for arg in args:
        try:
            numbers.append(float(arg))
        except ValueError:
            print(f"Ошибка: '{arg}' не является числом.")
            sys.exit(1)

    return numbers


if __name__ == "__main__":
    arr = parse_args(sys.argv[1:])
    result = sum_square_array(arr)

    print(f"Массив:       {arr}")
    print(f"Сумма квадратов: {result}")