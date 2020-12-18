import math


def quadratic_equation(a, b, c):
    t = math.sqrt(int(b * b - 4 * a * c))
    return (-b + t) / (2 * a), (-b + t) / (2 * a)


print(quadratic_equation(2, 9, 5))
