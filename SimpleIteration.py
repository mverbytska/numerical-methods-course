from sympy import *


def simple_iteration(equation, initial_approx: float, eps: float) -> float:
    x = symbols('x')
    g_func = solve(equation, x)[0]

    if abs(g_func.diff(x).subs(x, initial_approx)) >= 1:
        raise Exception('Cannot does not converge with this initial approximation')

    current_root = initial_approx
    for i in range(1000):
        next_root = g_func.subs(x, current_root)
        if re(Abs(next_root - current_root).evalf()) < eps:
            return next_root

        current_root = next_root

    return current_root


if __name__ == '__main__':
    x = symbols('x')
    my_equation = x**2 - 2*x - 5
    my_initial_approx = 3
    my_eps = 1e-5
    my_root = simple_iteration(my_equation, my_initial_approx, my_eps)
    print(f'Approximated root: {my_root}')



