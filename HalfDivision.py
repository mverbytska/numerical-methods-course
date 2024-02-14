from sympy import *

x = symbols('x')


def half_division(equation, interval: tuple, eps: float) -> float:
    # x = symbols('x')
    a, b = interval

    if equation.subs(x, a) * equation.subs(x, b) >= 0:
        raise Exception('Cannot be solved within this range [a; b]')

    while abs(b - a) >= eps:
        new_x = (a + b) / 2
        func_new_x = equation.subs(x, new_x)
        if func_new_x == 0:
            return new_x
        func_a = equation.subs(x, a)

        if func_new_x * func_a < 0:
            b = new_x
        else:
            a = new_x

    return (a + b) / 2


if __name__ == '__main__':
    my_equation = x ** 3 - 6 * x ** 2 + 11 * x - 6
    my_interval = (0, 5)
    my_eps = 1e-6
    my_root = half_division(my_equation, my_interval, my_eps)
    print(f'Approximated root: {my_root}')
