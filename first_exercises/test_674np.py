import numpy as np
from unittest.mock import patch
from arrays import input_or_random_array, input_or_random_matrix, get_matrix_order, replace_elements_in_matrixNP

__author__ = "Калашников А.Н."


def test_input_or_random_array():
    # правильный размер и тип
    with patch("builtins.input", return_value="2"):
        result = input_or_random_array(10)
    assert result.shape == (10,)
    assert isinstance(result, np.ndarray)

    # значения в диапазоне [-20, 20]
    with patch("builtins.input", return_value="2"):
        result = input_or_random_array(10)
    assert np.all(result >= -20) and np.all(result <= 20)

    # ручной ввод корректных чисел
    inputs = iter(["1", "1 2 3 4 5 6 7 8 9 10"])
    with patch("builtins.input", side_effect=inputs):
        result = input_or_random_array(10)
    assert np.array_equal(result, np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    # ручной ввод отрицательных чисел
    inputs = iter(["1", "-5 -4 -3 -2 -1 0 1 2 3 4"])
    with patch("builtins.input", side_effect=inputs):
        result = input_or_random_array(10)
    assert np.array_equal(result, np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]))

    # неверное количество чисел — запрашивается повтор
    inputs = iter(["1", "1 2 3", "1 2 3 4 5 6 7 8 9 10"])
    with patch("builtins.input", side_effect=inputs):
        result = input_or_random_array(10)
    assert result.shape == (10,)


def test_input_or_random_matrix():
    #  правильная форма и тип
    with patch("builtins.input", return_value="2"):
        result = input_or_random_matrix(4)
    assert result.shape == (4, 4)
    assert isinstance(result, np.ndarray)

    #  значения в диапазоне [-20, 20]
    with patch("builtins.input", return_value="2"):
        result = input_or_random_matrix(5)
    assert np.all(result >= -20) and np.all(result <= 20)

    #  матрица 1x1
    with patch("builtins.input", return_value="2"):
        result = input_or_random_matrix(1)
    assert result.shape == (1, 1)

    # матрица большого размера
    with patch("builtins.input", return_value="2"):
        result = input_or_random_matrix(20)
    assert result.shape == (20, 20)

    # ручной ввод матрицы 2x2
    inputs = iter(["1", "1 2", "3 4"])
    with patch("builtins.input", side_effect=inputs):
        result = input_or_random_matrix(2)
    assert np.array_equal(result, np.array([[1, 2], [3, 4]]))



def test_get_matrix_order():
    # корректный ввод возвращает правильное значение и тип int
    with patch("builtins.input", return_value="4"):
        result = get_matrix_order()
    assert result == 4
    assert isinstance(result, int)

    #  минимально допустимое значение n=1
    with patch("builtins.input", return_value="1"):
        result = get_matrix_order()
    assert result == 1

    #  большое значение n
    with patch("builtins.input", return_value="100"):
        result = get_matrix_order()
    assert result == 100

    #  ввод 0 (недопустимо)
    inputs = iter(["0", "3"])
    with patch("builtins.input", side_effect=inputs):
        result = get_matrix_order()
    assert result == 3

    # отрицательное число
    inputs = iter(["-5", "2"])
    with patch("builtins.input", side_effect=inputs):
        result = get_matrix_order()
    assert result == 2



def test_replace_elements_in_matrixNP():
    #  элементы с чётной суммой индексов, входящие в a, заменяются нулём
    matrix = np.array([[5, 1], [1, 5]])
    a = np.array([5, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    result = replace_elements_in_matrixNP(matrix, a)
    assert np.array_equal(result, np.array([[0, 1], [1, 0]]))

    #  элементы с нечётной суммой индексов не заменяются
    matrix = np.array([[0, 7], [7, 0]])
    a = np.array([7, 7, 7, 7, 7, 7, 7, 7, 7, 7])
    result = replace_elements_in_matrixNP(matrix, a)
    assert result[0, 1] == 7
    assert result[1, 0] == 7

    #  элементы с чётной суммой, не входящие в a, не заменяются
    matrix = np.array([[9, 1], [1, 9]])
    a = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
    result = replace_elements_in_matrixNP(matrix, a)
    assert np.array_equal(result, matrix)

    #  a состоит из нулей — заменяются только нулевые элементы с чётной суммой
    matrix = np.array([[0, 1], [2, 0]])
    a = np.zeros(10, dtype=int)
    result = replace_elements_in_matrixNP(matrix, a)
    assert result[0, 0] == 0
    assert result[1, 1] == 0
    assert result[0, 1] == 1
    assert result[1, 0] == 2

    #  матрица 1x1, элемент есть в a -> замена
    matrix = np.array([[3]])
    a = np.array([3, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    result = replace_elements_in_matrixNP(matrix, a)
    assert result[0, 0] == 0

