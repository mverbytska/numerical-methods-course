from sympy import *

x = symbols('x')


def newtons_solving(equation, initial_approx: float, eps: float) -> float:
    prime_equation = diff(equation, x)
    current_root = initial_approx
    for i in range(1000):
        func_value = equation.subs(x, current_root)
        if abs(func_value) < eps:
            return current_root
        prime_func_value = prime_equation.subs(x, current_root)
        if prime_func_value == 0:
            raise Exception('Method does not converge')
        current_root -= func_value / prime_func_value

    return current_root


if __name__ == '__main__':
    my_equation = x ** 2 - 2 * x - 1
    my_initial_approx = 0.5
    my_eps = 1e-6
    root = newtons_solving(my_equation, my_initial_approx, my_eps)
    print(f'Approximated root: {root}')







