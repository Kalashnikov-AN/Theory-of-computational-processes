__author__ = "Калашников А.Н."

"""
Модуль для работы с массивами
"""


def input_array():
    """Функция ввода массива пользователем. Пользователь задаёт размер массива.
    Возвращает введённый пользователем массив."""
    n = int(input("Введите количество элементов в массиве: "))
    arr = [0] * n
    for i in range(n):
        arr[i] = float(input(f"Введите {i + 1}-й элемент массива: "))
    return arr


def sum_square_array(arr):
    """Функция суммирования всех элементов массива arr, возведённых в квадрат."""
    s = 0
    for i in range(len(arr)):
        s += arr[i] ** 2
    return s


def is_multiple_of_3_not_5(a):
    """Функция, проверяющая, что число делится на 3 и не делится на 5"""
    return ( (a % 3 == 0) and (a % 5 != 0))


def count_correct_elements(arr, func):
    """Возвращает кол-во элементов массива arr, подходящих под условие функции func"""
    count = 0
    for i in range(len(arr)):
        if func(arr[i]) == True:
            count += 1
    return count


def sum_334a(i, j):
    """Возвращает сумму из задачи 334 а)"""
    return ( 1/(i+j**2) )


def find_double_sum(n, k, sum_func):
    """Возвращает двойную сумму. Внешняя от 1 до n. Внутренняя от 1 до k. sum_func - суммирующая функция, работает на каждой итерации"""
    s = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            s += sum_func(i, j)
    return s


def input_matrix():
    n = int(input("Введите порядок матрицы: "))
    arr = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input(f"Введите a[{i}][{j}] элемент матрицы: ")))
        arr.append(row)
    return arr


def input_numbers(n):
    arr = [0] * n
    print(f"Введите {n} чисел!")
    for i in range(n):
        arr[i] = int(input(f"Введите {i+1}-е число: "))
    return arr


def replace_elements_in_matrix(matrix, arr):
    """Возвращает матрицу с заменёнными нулями элементами из matrix с чётной суммой индексов, для которых имеются равные в массиве arr"""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i + j) % 2 == 0:
                if matrix[i][j] in arr:
                    matrix[i][j] = 0
    return matrix