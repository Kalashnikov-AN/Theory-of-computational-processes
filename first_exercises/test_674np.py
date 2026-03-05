import numpy as np
from unittest.mock import patch
from arrays import input_or_random_array, input_or_random_matrix, get_matrix_order, apply_replacement


def test_input_or_random_array():
    # Случай 1: случайная генерация — правильный размер и тип
    with patch("builtins.input", return_value="2"):
        result = input_or_random_array(10)
    assert result.shape == (10,)
    assert isinstance(result, np.ndarray)

    # Случай 2: случайные значения в диапазоне [-20, 20]
    with patch("builtins.input", return_value="2"):
        result = input_or_random_array(10)
    assert np.all(result >= -20) and np.all(result <= 20)

    # Случай 3: ручной ввод корректных чисел
    inputs = iter(["1", "1 2 3 4 5 6 7 8 9 10"])
    with patch("builtins.input", side_effect=inputs):
        result = input_or_random_array(10)
    assert np.array_equal(result, np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    # Случай 4: ручной ввод отрицательных чисел
    inputs = iter(["1", "-5 -4 -3 -2 -1 0 1 2 3 4"])
    with patch("builtins.input", side_effect=inputs):
        result = input_or_random_array(10)
    assert np.array_equal(result, np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]))

    # Случай 5: неверное количество чисел — запрашивается повтор
    inputs = iter(["1", "1 2 3", "1 2 3 4 5 6 7 8 9 10"])
    with patch("builtins.input", side_effect=inputs):
        result = input_or_random_array(10)
    assert result.shape == (10,)

    # Случай 6: нечисловой ввод — запрашивается повтор
    inputs = iter(["1", "a b c d e f g h i j", "1 2 3 4 5 6 7 8 9 10"])
    with patch("builtins.input", side_effect=inputs):
        result = input_or_random_array(10)
    assert result.shape == (10,)

    # Случай 7: крайний случай — размер 1, случайная генерация
    with patch("builtins.input", return_value="2"):
        result = input_or_random_array(1)
    assert result.shape == (1,)

    # Случай 8: крайний случай — размер 1, ручной ввод одного числа
    inputs = iter(["1", "42"])
    with patch("builtins.input", side_effect=inputs):
        result = input_or_random_array(1)
    assert np.array_equal(result, np.array([42]))

    # Случай 9: неизвестный выбор режима воспринимается как ручной ввод
    inputs = iter(["xyz", "0 0 0 0 0 0 0 0 0 0"])
    with patch("builtins.input", side_effect=inputs):
        result = input_or_random_array(10)
    assert np.array_equal(result, np.zeros(10, dtype=int))


def test_input_or_random_matrix():
    # Случай 1: случайная генерация — правильная форма и тип
    with patch("builtins.input", return_value="2"):
        result = input_or_random_matrix(4)
    assert result.shape == (4, 4)
    assert isinstance(result, np.ndarray)

    # Случай 2: случайные значения в диапазоне [-20, 20]
    with patch("builtins.input", return_value="2"):
        result = input_or_random_matrix(5)
    assert np.all(result >= -20) and np.all(result <= 20)

    # Случай 3: крайний случай — матрица 1x1
    with patch("builtins.input", return_value="2"):
        result = input_or_random_matrix(1)
    assert result.shape == (1, 1)

    # Случай 4: крайний случай — матрица большого размера
    with patch("builtins.input", return_value="2"):
        result = input_or_random_matrix(20)
    assert result.shape == (20, 20)

    # Случай 5: ручной ввод матрицы 2x2
    inputs = iter(["1", "1 2", "3 4"])
    with patch("builtins.input", side_effect=inputs):
        result = input_or_random_matrix(2)
    assert np.array_equal(result, np.array([[1, 2], [3, 4]]))

    # Случай 6: ручной ввод матрицы 3x3
    inputs = iter(["1", "1 2 3", "4 5 6", "7 8 9"])
    with patch("builtins.input", side_effect=inputs):
        result = input_or_random_matrix(3)
    assert np.array_equal(result, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    # Случай 7: неверная длина строки — запрашивается повтор
    inputs = iter(["1", "1 2", "1 2 3", "4 5 6", "7 8 9"])
    with patch("builtins.input", side_effect=inputs):
        result = input_or_random_matrix(3)
    assert result.shape == (3, 3)

    # Случай 8: нечисловой ввод строки — запрашивается повтор
    inputs = iter(["1", "a b c", "1 2 3", "4 5 6", "7 8 9"])
    with patch("builtins.input", side_effect=inputs):
        result = input_or_random_matrix(3)
    assert result.shape == (3, 3)

    # Случай 9: ручной ввод отрицательных значений
    inputs = iter(["1", "-1 -2", "-3 -4"])
    with patch("builtins.input", side_effect=inputs):
        result = input_or_random_matrix(2)
    assert np.array_equal(result, np.array([[-1, -2], [-3, -4]]))


def test_get_matrix_order():
    # Случай 1: корректный ввод возвращает правильное значение и тип int
    with patch("builtins.input", return_value="4"):
        result = get_matrix_order()
    assert result == 4
    assert isinstance(result, int)

    # Случай 2: крайний случай — минимально допустимое значение n=1
    with patch("builtins.input", return_value="1"):
        result = get_matrix_order()
    assert result == 1

    # Случай 3: крайний случай — большое значение n
    with patch("builtins.input", return_value="100"):
        result = get_matrix_order()
    assert result == 100

    # Случай 4: крайний случай — ввод 0 (недопустимо) → повтор
    inputs = iter(["0", "3"])
    with patch("builtins.input", side_effect=inputs):
        result = get_matrix_order()
    assert result == 3

    # Случай 5: отрицательное число → повтор
    inputs = iter(["-5", "2"])
    with patch("builtins.input", side_effect=inputs):
        result = get_matrix_order()
    assert result == 2

    # Случай 6: число с плавающей точкой → повтор
    inputs = iter(["3.5", "3"])
    with patch("builtins.input", side_effect=inputs):
        result = get_matrix_order()
    assert result == 3

    # Случай 7: буквы → повтор
    inputs = iter(["abc", "5"])
    with patch("builtins.input", side_effect=inputs):
        result = get_matrix_order()
    assert result == 5

    # Случай 8: пустая строка → повтор
    inputs = iter(["", "2"])
    with patch("builtins.input", side_effect=inputs):
        result = get_matrix_order()
    assert result == 2

    # Случай 9: несколько некорректных вводов подряд, затем верный
    inputs = iter(["-1", "0", "abc", "4"])
    with patch("builtins.input", side_effect=inputs):
        result = get_matrix_order()
    assert result == 4


def test_apply_replacement():
    # Случай 1: элементы с чётной суммой индексов, входящие в a, заменяются нулём
    # (0,0) сумма=0, (1,1) сумма=2 — оба чётные, значение 5 есть в a → 0
    # (0,1) сумма=1, (1,0) сумма=1 — нечётные → без изменений
    matrix = np.array([[5, 1], [1, 5]])
    a = np.array([5, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    result = apply_replacement(matrix, a)
    assert np.array_equal(result, np.array([[0, 1], [1, 0]]))

    # Случай 2: элементы с нечётной суммой индексов не заменяются
    matrix = np.array([[0, 7], [7, 0]])
    a = np.array([7, 7, 7, 7, 7, 7, 7, 7, 7, 7])
    result = apply_replacement(matrix, a)
    assert result[0, 1] == 7
    assert result[1, 0] == 7

    # Случай 3: элементы с чётной суммой, не входящие в a, не заменяются
    matrix = np.array([[9, 1], [1, 9]])
    a = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
    result = apply_replacement(matrix, a)
    assert np.array_equal(result, matrix)

    # Случай 4: a состоит из нулей — заменяются только нулевые элементы с чётной суммой
    matrix = np.array([[0, 1], [2, 0]])
    a = np.zeros(10, dtype=int)
    result = apply_replacement(matrix, a)
    assert result[0, 0] == 0
    assert result[1, 1] == 0
    assert result[0, 1] == 1
    assert result[1, 0] == 2

    # Случай 5: крайний случай — матрица 1x1, элемент есть в a → замена
    matrix = np.array([[3]])
    a = np.array([3, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    result = apply_replacement(matrix, a)
    assert result[0, 0] == 0

    # Случай 6: крайний случай — матрица 1x1, элемента нет в a → без изменений
    matrix = np.array([[7]])
    a = np.array([3, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    result = apply_replacement(matrix, a)
    assert result[0, 0] == 7

    # Случай 7: функция не изменяет исходную матрицу (работает с копией)
    matrix = np.array([[5, 5], [5, 5]])
    original = matrix.copy()
    a = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
    apply_replacement(matrix, a)
    assert np.array_equal(matrix, original)

    # Случай 8: крайний случай — матрица большого размера
    matrix = np.ones((10, 10), dtype=int) * 3
    a = np.array([3, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    result = apply_replacement(matrix, a)
    rows_idx, cols_idx = np.indices(matrix.shape)
    even_mask = (rows_idx + cols_idx) % 2 == 0
    assert np.all(result[even_mask] == 0)
    assert np.all(result[~even_mask] == 3)

    # Случай 9: отрицательные значения обрабатываются корректно
    matrix = np.array([[-5, -5], [-5, -5]])
    a = np.array([-5, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    result = apply_replacement(matrix, a)
    assert result[0, 0] == 0
    assert result[1, 1] == 0
    assert result[0, 1] == -5
    assert result[1, 0] == -5

    # Случай 10: смешанная матрица — заменяются только подходящие элементы
    # Чётные суммы индексов: (0,0)=1, (0,2)=3, (1,1)=5, (2,0)=7, (2,2)=9
    # В a есть: 1, 3, 9 → они заменяются; 5 и 7 — нет
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    a = np.array([1, 3, 9, 0, 0, 0, 0, 0, 0, 0])
    result = apply_replacement(matrix, a)
    assert result[0, 0] == 0
    assert result[0, 2] == 0
    assert result[2, 2] == 0
    assert result[1, 1] == 5
    assert result[2, 0] == 7
    assert result[0, 1] == 2