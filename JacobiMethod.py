import numpy as np
EPS = 1e-6


def check_for_non_zeros(matrix: np.array) -> bool:
    n = len(matrix)
    for i in range(n):
        if matrix[i, i] == 0:
            return False
    return True


def is_diagonally_dominant(matrix: np.array) -> bool:
    n = len(matrix)
    for i in range(n):
        sum_of_row_elements = 0
        for j in range(n):
            if j != i:
                sum_of_row_elements += abs(matrix[i, j])
        if sum_of_row_elements <= abs(matrix[i, i]):
            continue
        else:
            return False
    return True


def jacobi_solution_for(matrix: np.array, b: np.array, x0: np.array, max_iter=10000, eps=EPS) -> np.array:
    # check for zero elements on the principal diagonal
    if check_for_non_zeros(matrix):
        # check for diagonal dominance
        if is_diagonally_dominant(matrix):
            n = len(matrix)
            x = x0.copy()
            x_prev_guess = x0.copy()
            k = 0
            while k < max_iter:
                for i in range(n):
                    sigma = 0
                    for j in range(n):
                        if j != i:
                            sigma += matrix[i, j] * x_prev_guess[j]
                    x[i] = (b[i] - sigma) / matrix[i, i]
                if np.linalg.norm(x - x_prev_guess) < eps:
                    break
                x_prev_guess = x.copy()
                k += 1
            return x
        raise Exception('Matrix is not diagonally dominant')
    raise Exception('Matrix has zeros on the principal diagonal')


if __name__ == '__main__':
    # my_matrix = np.array([[3, 2, -1],
    #                      [2, 5, 2],
    #                      [1, -2, 4]])
    # my_d = np.array([10, 5, 3])

    # my_matrix = np.array([[4, -1, 0, 0],
    #                       [-1, 4, -1, 0],
    #                       [0, -1, 4, -1],
    #                       [0, 0, -1, 3]])
    # my_d = np.array([5, 5, 0, 5])

    my_matrix = np.array([[3, 0, 0],
                         [0, 4, 0],
                          [0, 0, 5]])
    my_d = np.array([6, 8, 10])
    my_x0 = np.zeros_like(my_d)
    solution = jacobi_solution_for(my_matrix, my_d, my_x0)
    print(f'Roots: {solution}')

