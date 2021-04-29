from __future__ import annotations
from random import randint


def make_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(randint(-10, 10))
    return matrix


class Matrix:
    def __init__(self, rows: int, cols: int, matrix):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix
        self.s = ""

    def matrix_in_str(self):
        for i in range(self.rows):
            for j in range(self.cols):
                c = str(self.matrix[i][j]) + ' '
                self.s = self.s + c
            self.s += '\n'

    def __str__(self):
        self.matrix_in_str()
        return self.s

    def __add__(self, other: Matrix):
        if isinstance(other, Matrix) and other.rows == self.rows and other.cols == self.cols:
            result_matrix = make_matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(self.rows, self.cols, result_matrix)

        else:
            raise ValueError("Для сложения двух матриц их размеры должны быть одинаковыми")

    def __iadd__(self, other: Matrix):
        if isinstance(other, Matrix) and other.rows == self.rows and other.cols == self.cols:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] += other.matrix[i][j]
            return self
        else:
            raise ValueError("Для сложения двух матриц их размеры должны быть одинаковыми")

    def __sub__(self, other):
        if isinstance(other, Matrix) and other.rows == self.rows and other.cols == self.cols:
            result_matrix = make_matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result_matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return Matrix(self.rows, self.cols, result_matrix)
        else:
            raise ValueError("Для вычитания двух матриц их размеры должны быть одинаковыми")

    def __isub__(self, other):
        if isinstance(other, Matrix) and other.rows == self.rows and other.cols == self.cols:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] -= other.matrix[i][j]
            return self
        else:
            raise ValueError("Для вычитания двух матриц их размеры должны быть одинаковыми")

    def __matmul__(self, other):
        if isinstance(other, Matrix) and self.cols == other.rows:
            result_matrix = make_matrix(self.rows, other.cols)
            c = 0
            for i in range(self.rows):
                for j in range(other.cols):
                    for z in range(self.cols):
                        c += self.matrix[i][z] * other.matrix[z][j]
                    result_matrix[i][j] = c
                    c = 0
            return Matrix(self.rows, other.cols, result_matrix)
        else:
            raise ValueError(
                "Для умножения двух матриц кол-во колонок первой матрицы и кол-во рядов второй должны быть одинаковыми")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result_matrix = make_matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result_matrix[i][j] = self.matrix[i][j] * other
            return Matrix(self.rows, self.cols, result_matrix)
        else:
            raise ValueError(
                "Введите число")

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            result_matrix = make_matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result_matrix[i][j] = self.matrix[i][j] * other
            return Matrix(self.rows, self.cols, result_matrix)
        else:
            raise ValueError(
                "Введите число")

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] *= other
            return self
        else:
            raise ValueError(
                "Введите число")


if __name__ == "__main__":
    rows1, cols1 = map(int, input().split())
    matrix = make_matrix(rows1, cols1)
    matrix1 = Matrix(rows1, cols1, matrix)
    rows2, cols2 = map(int, input().split())
    matrix = make_matrix(rows2, cols2)
    matrix2 = Matrix(rows2, cols2, matrix)
    print(matrix1)
    print(matrix2)
    c = matrix1 + matrix2
    print(c)
