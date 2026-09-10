"""Small exact polynomial operations, coefficients in increasing degree."""

from fractions import Fraction as Q
from math import comb


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, factor):
    return trim([factor*x for x in a])


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    result = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return trim(result)


def at(a, x):
    value = 0
    for coefficient in reversed(a):
        value = value*x+coefficient
    return value


def derivative(a):
    return [i*a[i] for i in range(1, len(a))] or [Q(0)]


def compose(a, offset, slope):
    result, power = [Q(0)], [Q(1)]
    for coefficient in a:
        result = add(result, scale(power, coefficient))
        power = mul(power, [offset, slope])
    return result


def bernstein(a, low, high):
    coefficients = compose(a, low, high-low)
    degree = len(coefficients)-1
    return [sum(coefficients[j]*Q(comb(i, j), comb(degree, j)) for j in range(i+1))
            for i in range(degree+1)]
