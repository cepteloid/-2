import numpy as np
from math import *

def make_matrix(n, a, b):
    """Инициализация квадратной матрицы размером NxN псевдослучайными величинами в диапазоне [a, b)"""
    matrix = (b - a) * np.random.random(size=(n, n)) + a
    return matrix

def calculate_mean_and_variance(matrix):
    """Вычисление среднего значения и дисперсии"""
    total_sum = 0
    (num_rows, num_cols) = matrix.shape  # Размеры матрицы
    for row in range(num_rows):
        for col in range(num_cols):
            total_sum += matrix[row][col]
    mean = total_sum / matrix.size  # Среднее
    variance = 0
    for row in range(num_rows):
        for col in range(num_cols):
            variance += (matrix[row][col] - mean) ** 2
    return (mean, variance / (matrix.size - 1))  # Кортеж

def correct_matrix(matrix, mean, std_deviation):
    """Замена "отскочивших" значений"""
    (num_rows, num_cols) = matrix.shape  # Размеры матрицы
    for row in range(num_rows):
        for col in range(num_cols):
            if abs(abs(matrix[row][col]) - mean) > std_deviation:
                matrix[row][col] = mean
    return matrix

def print_matrix(matrix):
    """Печать матрицы"""
    (num_rows, num_cols) = matrix.shape
    for row in range(num_rows):
        for col in range(num_cols):
            print(f"{matrix[row][col]:7.3f}", end=" ")
        print()
    print()

def main():
    n = int(input("Введите размер матрицы (NxN): "))
    my_matrix = make_matrix(n, -5, 5)  # Изготовление матрицы
    print_matrix(my_matrix)
    (mean, variance) = calculate_mean_and_variance(my_matrix)  # Среднее и дисперсия
    print(f"Midl = {mean:7.3f}")
    standard_deviation = sqrt(variance)
    print(f"Disp = {variance:7.3f} Sig = {standard_deviation:7.3f}")
    # Корректировка
    new_matrix = correct_matrix(my_matrix, mean, standard_deviation)
    print_matrix(new_matrix)

if __name__ == "__main__":
    main()
