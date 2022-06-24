#a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
#b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda r: '   '.join(map(str, r)), self.matrix)) + '\n'

    def __add__(self, other):
        return Matrix(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))


matrix_1 = Matrix([[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]])
matrix_2 = Matrix([[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]])
matrix_new = matrix_1 + matrix_2
print(matrix_1)
print(matrix_2)
print(matrix_new)
