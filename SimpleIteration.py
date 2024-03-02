import math


def simple_iteration(eq, initial_approx: float, eps: float, max_iterations=10000) -> (float, int):
    x_prev = initial_approx
    iterations = 0
    for _ in range(max_iterations):
        x_next = eq(x_prev)
        iterations += 1
        difference = abs(x_next - x_prev)
        if difference < eps:
            return x_next, iterations
        x_prev = x_next
    raise Exception(f'Method failed to converge in {max_iterations} iterations ')


def equation(x):
    # return x + 5
    return math.atan(math.sqrt(x + 1))


if __name__ == '__main__':
    my_eps = 1e-6
    my_approx = 2
    my_root, iterations_number = simple_iteration(equation, my_approx, my_eps)
    print(f'Approximated root: {my_root}\nNumber of iterations: {iterations_number}')
