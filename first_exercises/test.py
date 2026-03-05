__author__ = "Калашников А.Н."

"""
Модуль для тестирования функций, решающих задачи 5-8
"""

from arrays import input_array, sum_square_array, is_multiple_of_3_not_5, count_correct_elements, sum_334a, \
    find_double_sum, replace_elements_in_matrix


def test_136d():
    """Тестирующая функция для функций, решающих задачу 136 д)"""
    if __name__ == "__main__":
        arr = input_array()
        print(arr)
    assert sum_square_array([1, -2, 3]) == 14       # разные числа
    assert sum_square_array([]) == 0                # пустой массив
    assert sum_square_array([5]) == 25              # один элемент
    assert sum_square_array([-1, -2, -3]) == 14     # только отрицательные
    assert sum_square_array([0, 0, 0]) == 0         # все нули
    print("Все тесты для задачи 136 д) успешно пройдены!")


def test_178b():
    """Тестирующая функция для функций, решающих задачу 178 б)"""
    # Положительные числа, кратные 3, но не 5
    assert is_multiple_of_3_not_5(3) == True
    assert is_multiple_of_3_not_5(6) == True
    assert is_multiple_of_3_not_5(9) == True
    assert is_multiple_of_3_not_5(303) == True

    # Отрицательные числа, кратные 3, но не 5
    assert is_multiple_of_3_not_5(-3) == True
    assert is_multiple_of_3_not_5(-6) == True
    assert is_multiple_of_3_not_5(-9) == True

    # Числа, кратные и 3, и 5
    assert is_multiple_of_3_not_5(15) == False
    assert is_multiple_of_3_not_5(30) == False
    assert is_multiple_of_3_not_5(45) == False
    assert is_multiple_of_3_not_5(-15) == False
    assert is_multiple_of_3_not_5(-30) == False

    # Числа, не кратные 3
    assert is_multiple_of_3_not_5(5) == False
    assert is_multiple_of_3_not_5(10) == False
    assert is_multiple_of_3_not_5(1) == False
    assert is_multiple_of_3_not_5(-5) == False
    assert is_multiple_of_3_not_5(-10) == False

    # Крайний случай: 0 (кратно любому ненулевому числу, в том числе 3 и 5)
    assert is_multiple_of_3_not_5(0) == False


    # Пустой массив
    assert count_correct_elements([], is_multiple_of_3_not_5) == 0

    # Различные массивы
    assert count_correct_elements([3, 6, 9, 12], is_multiple_of_3_not_5) == 4
    assert count_correct_elements([15, 30, 45], is_multiple_of_3_not_5) == 0
    assert count_correct_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], is_multiple_of_3_not_5) == 3  # подходят 3, 6 и 9
    assert count_correct_elements([-3, -6, -9], is_multiple_of_3_not_5) == 3
    assert count_correct_elements([-15, -30], is_multiple_of_3_not_5) == 0
    assert count_correct_elements([0], is_multiple_of_3_not_5) == 0

    print("Все тесты пройдены успешно!")


def test_334a():
    """Тестирующая функция для функций, решающих задачу 334 а)"""
    # Проверка отдельных значений
    assert abs(sum_334a(1, 1) - 0.5) < 1e-9
    assert abs(sum_334a(1, 2) - 0.2) < 1e-9
    assert abs(sum_334a(2, 1) - 1 / 3) < 1e-9
    assert abs(sum_334a(2, 2) - 1 / 6) < 1e-9

    # Крайние случаи: нулевые границы
    assert abs(find_double_sum(0, 0, sum_334a) - 0.0) < 1e-9
    assert abs(find_double_sum(0, 5, sum_334a) - 0.0) < 1e-9
    assert abs(find_double_sum(5, 0, sum_334a) - 0.0) < 1e-9

    # Отрицательные границы (циклы не выполняются)
    assert abs(find_double_sum(-3, 2, sum_334a) - 0.0) < 1e-9
    assert abs(find_double_sum(2, -3, sum_334a) - 0.0) < 1e-9

    # Малые значения (n, k от 1 до 2)
    assert abs(find_double_sum(1, 1, sum_334a) - 0.5) < 1e-9
    assert abs(find_double_sum(1, 2, sum_334a) - (0.7)) < 1e-9
    assert abs(find_double_sum(2, 1, sum_334a) - (0.833333)) < 1e-6
    assert abs(find_double_sum(2, 2, sum_334a) - (1.2)) < 1e-9

    # Другие комбинации (n=3, k=1 и n=1, k=3)
    assert abs(find_double_sum(3, 1, sum_334a) - (1.08333)) < 1e-5
    assert abs(find_double_sum(1, 3, sum_334a) - (0.8)) < 1e-9

    print("Все тесты пройдены успешно!")

def test_674():
    """Тестирующая функция для функций, решающих задачу 674"""
    # квадратная матрица 2x2 
    matrix1 = [[1, 2], [3, 4]]
    arr1 = [1, 2]
    expected1 = [[0, 2], [3, 4]]
    result1 = replace_elements_in_matrix(matrix1, arr1)
    assert result1 == expected1

    # матрица 2x3
    matrix2 = [[1, 2, 3], [4, 5, 6]]
    arr2 = [2, 4, 6]
    expected2 = [[1, 2, 3], [4, 5, 6]]
    result2 = replace_elements_in_matrix(matrix2, arr2)
    assert result2 == expected2

    #  матрица из одной строки (1x3)
    matrix3 = [[10, 20, 30]]
    arr3 = [10, 30]
    expected3 = [[0, 20, 0]]
    result3 = replace_elements_in_matrix(matrix3, arr3)
    assert result3 == expected3

    #  матрица из одного столбца (3x1)
    matrix4 = [[1], [2], [3]]
    arr4 = [2]
    expected4 = [[1], [2], [3]]  # ни один элемент с чётной суммой не подходит
    result4 = replace_elements_in_matrix(matrix4, arr4)
    assert result4 == expected4

    #  пустая матрица
    matrix5 = []
    arr5 = [1, 2, 3]
    expected5 = []
    result5 = replace_elements_in_matrix(matrix5, arr5)
    assert result5 == expected5

    #  все чётные элементы заменяются
    matrix6 = [[1, 2], [3, 4]]
    arr6 = [1, 2, 3, 4]
    expected6 = [[0, 2], [3, 0]]
    result6 = replace_elements_in_matrix(matrix6, arr6)
    assert result6 == expected6

    #  повторяющиеся элементы
    matrix7 = [[5, 5], [5, 5]]
    arr7 = [5]
    expected7 = [[0, 5], [5, 0]]
    result7 = replace_elements_in_matrix(matrix7, arr7)
    assert result7 == expected7

    #  пустой массив
    matrix8 = [[1, 2], [3, 4]]
    arr8 = []
    expected8 = [[1, 2], [3, 4]]
    result8 = replace_elements_in_matrix(matrix8, arr8)
    assert result8 == expected8

    #  элементы не совпадают
    matrix9 = [[10, 20], [30, 40]]
    arr9 = [5, 6, 7]
    expected9 = [[10, 20], [30, 40]]
    result9 = replace_elements_in_matrix(matrix9, arr9)
    assert result9 == expected9

    #  матрица с отрицательными числами
    matrix10 = [[-1, -2], [-3, -4]]
    arr10 = [-1, -4]
    expected10 = [[0, -2], [-3, 0]]
    result10 = replace_elements_in_matrix(matrix10, arr10)
    assert result10 == expected10

    print("Все тесты успешно пройдены!")


if __name__ == "__main__":
    test_136d()