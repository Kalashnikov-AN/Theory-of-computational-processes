__author__ = "Калашников А.Н."

import sys
from typing import Callable
import numpy as np

"""
Модуль для работы с массивами
"""

HELP_TEXT = f"""\
Использование: python {{prog}} <число1> <число2> ...

Задача 136 д): вычисляет сумму квадратов переданных чисел
    Результат: (a_1)^2 + (a_2)^2 + ... + (a_n)^2

Аргументы:
    <число1> <число2> ...  Набор чисел (целых или дробных)

Параметры:
    --help                 Показать эту справку и выйти

Примеры:
    python {{prog}} 1 2 3 4 5
    python {{prog}} -3.5 2.1 0 7\
"""

def input_array() -> list[float]:
    """Функция ввода массива пользователем. Пользователь задаёт размер массива.
    Возвращает введённый пользователем массив."""
    n = int(input("Введите количество элементов в массиве: "))
    arr = [0] * n
    for i in range(n):
        arr[i] = float(input(f"Введите {i + 1}-й элемент массива: "))
    return arr


def sum_square_array(arr: list[float | int]) -> float:
    """Функция суммирования всех элементов массива arr, возведённых в квадрат."""
    s = 0
    for i in range(len(arr)):
        s += arr[i] ** 2
    return s


def is_multiple_of_3_not_5(a: int):
    """Функция, проверяющая, что число делится на 3 и не делится на 5"""
    return ((a % 3 == 0) and (a % 5 != 0))


def count_correct_elements(arr: list, func: Callable[[int], bool]):
    """Возвращает кол-во элементов массива arr, подходящих под условие функции func"""
    count = 0
    for i in range(len(arr)):
        if func(arr[i]) == True:
            count += 1
    return count


def sum_334a(i, j):
    """Возвращает сумму из задачи 334 а)"""
    return (1 / (i + j ** 2))


def find_double_sum(n, k, sum_func):
    """Возвращает двойную сумму. Внешняя от 1 до n. Внутренняя от 1 до k. sum_func - суммирующая функция, работает на каждой итерации"""
    s = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            s += sum_func(i, j)
    return s


def input_matrix():
    """Возвращает матрицу, заполненную пользователем"""
    n = int(input("Введите порядок матрицы: "))
    arr = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input(f"Введите a[{i}][{j}] элемент матрицы: ")))
        arr.append(row)
    return arr


def input_numbers(n):
    """Заполняет и возвращает массив размера n введёнными пользователем элементами"""
    arr = [0] * n
    print(f"Введите {n} чисел!")
    for i in range(n):
        arr[i] = int(input(f"Введите {i + 1}-е число: "))
    return arr


def replace_elements_in_matrix(matrix, arr):
    """Возвращает матрицу с заменёнными нулями элементами из matrix с чётной суммой индексов, для которых имеются равные в массиве arr"""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i + j) % 2 == 0:
                if matrix[i][j] in arr:
                    matrix[i][j] = 0
    return matrix


def input_or_random_array(size):
    """
    Запрашивает у пользователя ввод одномерного массива целых чисел
    размера size или генерирует его случайным образом.

    Возвращает:
        np.ndarray массив целых чисел длиной size.
    """
    print(f"\nВведите массив ({size} целых чисел):")
    print("  1 - ввести вручную")
    print("  2 - сгенерировать случайно")
    choice = input("Выбор: ").strip()

    if choice == "2":
        arr = np.random.randint(-20, 21, size=size)
        print(f"Сгенерировано: {arr}")
        return arr
    else:
        while True:
            try:
                values = np.fromiter(
                    map(int, input(f"Введите {size} целых чисел через пробел: ").split()),
                    dtype=int
                )
                if values.shape != (size,):
                    print(f"Ошибка: нужно ровно {size} чисел.")
                    continue
                return values
            except ValueError:
                print("Ошибка: вводите только целые числа.")


def input_or_random_matrix(n):
    print(f"\nМатрица {n}x{n}:")
    print("  1 - ввести вручную")
    print("  2 - сгенерировать случайно")
    choice = input("Выбор: ").strip()

    if choice == "2":
        matrix = np.random.randint(-20, 21, size=(n, n))
        print("Сгенерированная матрица:")
        print(matrix)
        return matrix
    else:
        matrix = np.empty((n, n), dtype=int)
        print(f"Вводите матрицу построчно ({n} чисел на строку):")
        for i in range(n):
            while True:
                try:
                    row = np.fromiter(
                        map(int, input(f"  Строка {i+1}: ").split()),
                        dtype=int
                    )
                    if row.shape != (n,):
                        print(f"  Ошибка: нужно ровно {n} чисел.")
                        continue
                    matrix[i] = row
                    break
                except ValueError:
                    print("  Ошибка: вводите только целые числа.")
        return matrix


def get_matrix_order():
    """
    Запрашивает у пользователя порядок матрицы

    Возвращает:
        int число n, где n >= 1
    """
    while True:
        try:
            n = int(input("\nВведите порядок матрицы n (n >= 1): "))
            if n < 1:
                print("Ошибка: n должно быть не меньше 1.")
                continue
            return n
        except ValueError:
            print("Ошибка: введите целое число.")


def replace_elements_in_matrixNP(matrix, a):
    """Возвращает матрицу с заменёнными нулями элементами из matrix с чётной суммой индексов, для которых имеются равные в массиве a"""
    matrix = matrix.copy()
    rows_idx, cols_idx = np.indices(matrix.shape)
    even_sum_mask = (rows_idx + cols_idx) % 2 == 0
    in_a_mask = np.isin(matrix, a)
    matrix[even_sum_mask & in_a_mask] = 0
    return matrix


def sum_square_array(arr: list[float | int]) -> float:
    """Функция суммирования всех элементов массива arr, возведённых в квадрат."""
    s = 0
    for i in range(len(arr)):
        s += arr[i] ** 2
    return s


def parse_args(args: list[str]) -> list[float]:
    """Разбирает аргументы командной строки и возвращает список чисел."""
    prog = sys.argv[0]

    if not args or "--help" in args:
        print(HELP_TEXT.format(prog=prog))
        sys.exit(0 if "--help" in args else 1)

    numbers = []
    for arg in args:
        try:
            numbers.append(float(arg))
        except ValueError:
            print(f"Ошибка: '{arg}' не является числом.")
            print(f"Подсказка: запустите 'python {prog} --help' для справки.")
            sys.exit(1)

    return numbers
