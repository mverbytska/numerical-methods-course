import sympy as sp
import numpy as np

x = sp.Symbol('x')


# given function
func = sp.sin(x)


def func_prime_within(a, b):
    return sp.integrate(func, (x, a, b))


def rectangular_integration(a: float, b: float, n: int):
    h = (b-a) / n
    res = 0.0
    func_second_derivative = sp.diff(func, x, 2)
    max_second_derivative = max(abs(func_second_derivative.evalf(subs={x: xi})) for xi in np.linspace(float(a),
                                                                                                      float(b),
                                                                                                      n+1))

    for i in range(1, n+1):
        x_i = a + (i-0.5) * h
        res += func.subs(x, x_i)
    res *= h

    error_bound = max_second_derivative * h**2 * (b-a) / 24
    real_error = abs(func_prime_within(a, b) - res.evalf())
    return res.evalf(), error_bound.evalf(), real_error


def trapezoidal_integration(a: float, b: float, n: int):
    h = (b-a) / n
    res = 0.5*(func.subs(x, a) + func.subs(x, b))
    func_second_derivative = sp.diff(func, x, 2)
    max_second_derivative = max(abs(func_second_derivative.evalf(subs={x: xi})) for xi in np.linspace(float(a),
                                                                                                      float(b),
                                                                                                      n+1))
    for i in range(1, n):
        x_i = a + i*h
        res += func.subs(x, x_i)
    res *= h
    error_bound = max_second_derivative * h**2 * (b-a) / 12
    real_error = abs(func_prime_within(a, b) - res.evalf())
    return res.evalf(), error_bound.evalf(), real_error


def simpson_integration(a: float, b: float, n: int):
    h = (b-a) / n
    x_s = [0] * (n+1)
    x_s[0] = a
    res = 0

    func_fourth_derivative = sp.diff(func, x, 4)
    max_fourth_derivative = max(abs(func_fourth_derivative.evalf(subs={x: xi})) for xi in np.linspace(float(a),
                                                                                                      float(b),
                                                                                                      n+1))
    for i in range(1, n+1):
        x_s[i] = a + h*i

    for i in range(1, n//2 + 1):
        res += func.subs(x, (x_s[2*i - 2])) + 4*func.subs(x, (x_s[2*i-1])) + func.subs(x, (x_s[2*i]))

    res *= h/3

    error_bound = max_fourth_derivative * h**4 * (b-a) / 2880
    real_error = abs(func_prime_within(a, b) - res.evalf())
    return res.evalf(), error_bound.evalf(), real_error



if __name__ == '__main__':
    n = 20
    a = 0
    b = sp.pi
    rectangular_res, rectangular_error_bound, rec_method_real_error = rectangular_integration(a, b, n)
    print(f'Rectangular approximation: {rectangular_res}')
    print(f'Real error: {rec_method_real_error}, maximum theoretical error bound: {rectangular_error_bound}')
    print(f'Does found value lay within the limits: {rec_method_real_error < rectangular_error_bound}\n')

    trapezoidal_res, trapezoidal_error_bound, trap_method_real_error = trapezoidal_integration(a, b, n)
    print(f'Trapezoidal approximation: {trapezoidal_res}')
    print(f'Real error: {trap_method_real_error}, maximum theoretical error bound: {trapezoidal_error_bound}')
    print(f'Does found value lay within the limits: {trap_method_real_error < trapezoidal_error_bound}\n')

    simpson_res, simpson_error_bound, simpson_method_real_error = simpson_integration(a, b, n)
    print(f'Simpson\'s approximation: {simpson_res}')
    print(f'Real error: {simpson_method_real_error}, maximum theoretical error bound: {simpson_error_bound}')
    print(f'Does found value lay within the limits: {simpson_method_real_error < simpson_error_bound}\n')


