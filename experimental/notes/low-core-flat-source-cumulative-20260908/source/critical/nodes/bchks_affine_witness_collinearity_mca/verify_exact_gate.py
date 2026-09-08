"""Small exact checks of interpolation counts and the new load inequalities."""

from fractions import Fraction
from math import isqrt


def ceil_sqrt_ratio(num, den):
    assert num >= 0 and den > 0
    value = isqrt(num // den)
    value += den * value * value < num
    assert den * value * value >= num
    assert not value or den * (value-1)**2 < num
    return value


def main():
    cases = 0
    small_maximum_cases = 0
    for n in range(3, 81):
        for d in range(1, n-1):
            for m in range(1, 9):
                s = 2*m+1
                a = ceil_sqrt_ratio(s*s*n*d, 4*m*m)
                if a > n:
                    continue
                length = ceil_sqrt_ratio(s*s*n*d, 4)
                yceil = ceil_sqrt_ratio(s*s*n, 4*d)
                zceil = max(yceil, (s*s*n+12*d-1) // (12*d))
                variables = sum((length-d*j)*(zceil-j) for j in range(yceil))
                equations = n * sum((m-j)*(zceil-j) for j in range(m))
                assert variables > equations
                assert (a-d)*(2*length-1) > (2*d+1)*(n-d)
                if m >= 2:
                    assert 36*d <= s*s*n
                elif 4*d > n:
                    small_maximum_cases += 1
                x_upper = Fraction(m, 1) / Fraction(s, 2)
                if m == 1:
                    margin = Fraction(13, 10)*(3*d-x_upper)-(2*d+1)
                    assert margin >= Fraction(1, 30)
                elif m == 2:
                    assert 5*d-x_upper > 2*d+1
                cases += 1
    assert small_maximum_cases > 0
    # Floor(X) would lose the strict coordinate-load inequality here.
    n, d, m, a, length = 3, 1, 1, 3, 3
    assert (a-d)*(2*length-1) > (2*d+1)*(n-d)
    assert (a-d)*(2*(length-1)-1) == (2*d+1)*(n-d)
    print(f'PASS: {cases} exact interpolation/load cases; '
          f'{small_maximum_cases} small-m maximum-Z cases; rounding guard')


if __name__ == '__main__':
    main()
