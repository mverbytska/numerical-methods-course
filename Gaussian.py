import numpy as np


def partial_pivoting(matrix: np.array, n: int) -> np.array:
    for i in range(n):
        pivot_row = i
        for j in range(i + 1, n):
            if abs(matrix[j, i]) > abs(matrix[pivot_row, i]):
                pivot_row = j
        if pivot_row != i:
            matrix[[i, pivot_row]] = matrix[[pivot_row, i]]

        for j in range(i + 1, n):
            factor = matrix[j, i] / matrix[i, i]
            matrix[j] -= factor * matrix[i]

        # singularity check-up (if there is zero-element at the principal diagonal => rows are not linearly independent
        if not matrix[i][i]:
            raise Exception('Matrix is singular => it is unsolvable by using Gaussian elimination')
    return matrix


def solution_extraction(matrix: np.array, n: int) -> np.array:
    ref_matrix = partial_pivoting(matrix, n)
    y_list = np.zeros(n)
    for i in range(n - 1, -1, -1):
        partial_sum = sum(ref_matrix[i, j] * y_list[j] for j in range(i + 1, n))
        y_list[i] = (ref_matrix[i][n] - partial_sum) / ref_matrix[i][i]
    return y_list


if __name__ == '__main__':
    # solvable
    test_mat = np.array([[2.0, -1.0, 3.0, 4.0],
                         [1.0, 2.0, -1.0, 1.0],
                         [3.0, 1.0, 1.0, 6.0]])
    print(f'Matrix:\n{test_mat}')
    test_mat_2_solution = solution_extraction(test_mat, 3)
    print(f'Solution: {test_mat_2_solution}')
