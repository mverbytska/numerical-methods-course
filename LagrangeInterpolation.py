from sympy import symbols, expand

x = symbols('x')
y = symbols('y')


def find_interpolation(given_points: list):
    """
    Find Lagrange's interpolating polynomial with a given set of points

    Args:
        :param given_points: list of tuples in a form of (x, y) where x is a function's argument and y is a value
    Returns:
        :return: sympy polynomial expression

    :raises:
        ValueError() if given list is empty
    """
    if given_points:
        result = 0
        n = len(given_points)
        for i in range(n):
            term = given_points[i][1]
            for j in range(n):
                if j != i:
                    term = term * (x - given_points[j][0]) / (given_points[i][0] - given_points[j][0])
            result += term
        return expand(result)
    else:
        raise ValueError('No points have been set')


if __name__ == '__main__':
    f = [(-1, -1.1071487177940905030),
         (-0.75, -0.98279372324732906799),
         (-0.5, -0.78539816339744830962),
         (-0.25, -0.46364760900080611621),
         (0, 0),
         (0.25, 0.46364760900080611621),
         (0.5, 0.78539816339744830962),
         (0.75, 0.98279372324732906799),
         (1, 1.1071487177940905030)]

    polynomial = find_interpolation(f)
    print(f'Lagrange\'s polynomial: {polynomial}')

    value_1 = polynomial.subs(x, -0.9)
    value_2 = polynomial.subs(x, -0.3)
    value_3 = polynomial.subs(x, 0.3)
    value_4 = polynomial.subs(x, 0.9)
    print(f'Polynom value in -0.9: {value_1}')
    print(f'Polynom value in -0.3: {value_2}')
    print(f'Polynom value in 0.3: {value_3}')
    print(f'Polynom value in 0.9: {value_4}')
