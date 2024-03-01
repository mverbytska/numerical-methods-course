import numpy as np


def is_three_diagonal(matrix: np.array) -> bool:
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if abs(i - j) > 1 and matrix[i, j] != 0:
                return False
            if i - j == 1 and matrix[i, j] == 0:
                return False
            if j - i == 1 and matrix[i, j] == 0:
                return False
    return True


def run_thomas(matrix: np.array, d: list) -> np.array:
    if is_three_diagonal(matrix):
        n = len(d)
        a = np.zeros(n)  # lower sub-diagonal
        b = np.zeros(n)  # principal diagonal
        c = np.zeros(n)  # upper sub-diagonal

        x = np.zeros(n)  # Xs we are looking for

        a[1:] = matrix.diagonal(offset=-1)
        b[:] = matrix.diagonal()
        c[:-1] = matrix.diagonal(offset=1)

        for j in range(1, n):
            w = a[j] / b[j - 1]
            b[j] = b[j] - c[j - 1] * w
            d[j] = d[j] - d[j - 1] * w

        x[-1] = d[-1] / b[-1]
        for j in range(n-2, -1, -1):
            x[j] = (d[j] - c[j] * x[j + 1]) / b[j]

        return x


if __name__ == '__main__':
    # my_matrix = np.array([[2.04, -1, 0, 0],
    #                       [-1, 2.04, -1, 0],
    #                       [0, -1, 2.04, -1],
    #                       [0, 0, -1, 2.04]])
    # my_d = [40.8, 0.8, 0.8, 200.8]
    my_matrix = np.array([[1, 1, 0],
                          [2, 7, 8],
                          [0, 3, 5]])
    my_d = [6, 9, 6]
    my_roots = run_thomas(my_matrix, my_d)
    print(f'System roots: {my_roots}')
