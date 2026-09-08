"""Independent determinant census and integer-only finite audit."""

from itertools import combinations, permutations
from math import factorial, prod


def check(ok, message):
    if not ok:
        raise ValueError(message)


def det(rows):
    n = len(rows)
    value = 0
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        value += (-1)**inversions * prod(rows[i][perm[i]] for i in range(n))
    return value % 13


def basis_count(core, evaluate):
    return factorial(3) * sum(det([evaluate(x) for x in triple]) != 0
                              for triple in combinations(core, 3))


def floor_check(num, den, floor):
    check(den > 0 and den*floor <= num < den*(floor+1), "integer floor certificate")


def main():
    g = lambda x: x*(x-1)*(x-2)
    v = lambda x: (1, g(x), x*g(x))
    core = (0, 1, 2, 3, 4, 5)
    check(basis_count(core, v) == 60, "saturated original core bases")
    check(4*basis_count(core, v) == 240, "one-defect insertion")
    full = lambda x: tuple((x-12)*a for a in v(x))
    check(basis_count(core, full) == 60, "zero outside core preserves basis count")
    check(basis_count((0, 1, 2, 3, 4, 12), full) == 18 < 24, "universal zero invalidates g=0 count")

    g2 = lambda x: x*(x-1)
    v2 = lambda x: (1, g2(x), x*x*g2(x))
    h = (0, 2, 3, 4, 9, 10)
    check(basis_count(h, v2) == 108, "nonsaturated core determinant census")
    outside = (2, 3, 4, 9, 10)
    prefix = 2*sum(det([(1,x*x),(1,y*y)]) != 0 for x,y in combinations(outside, 2))
    check(prefix == 16 and 5*(5-2) <= prefix < 5*(5-1), "cannot drop e=1")
    inside = 6*sum(det([v2(0),v2(x),v2(y)]) != 0 for x,y in combinations(outside, 2))
    check(inside == 48 and inside+60 == basis_count(h,v2), "zero/one-inside classes disjoint")

    d, near, c = 67466, 134944, 23067643444721720934
    p = prod(range(d+1,d+10))
    values = (
        (65000, (34003655554524123,266514954058742090,216764665972142342,216763564029644353)),
        (169999,(1252453225033902,220398387206020840,244346006891976872,244365664452173214)),
    )
    for j, totals in values:
        u = prod(range(1048576+j-11,1048576+j+1))
        numerators = (u*2**9, 2*u, u, u)
        denominators = (12*(j+d)*(d+1)*(2*d+j+2)**9,
                        12*p*(2*d+j)*(d+1+5*j),
                        132*(j-10)*(d+10)*p,
                        132*(d+1)*(j-1)*p)
        for num, den, target in zip(numerators,denominators,totals):
            floor_check(num, den, target-near)
            try:
                floor_check(num, den, target-near+1)
            except ValueError:
                pass
            else:
                raise ValueError("accepted off-by-one finite floor")
    low, high = 1113565, 304931
    check(9*low-12*(high+2) > 0, "whole-interval decreasing certificate")
    check(low**2-12*high**2 > 0, "whole-interval convexity certificate")
    check(84*(67473-77)*125 > 10488*67473, "rational-free HIGH proof")
    total = 274929007493481160
    floor_check(125*c,10488,total-near)
    check(2130706433**6//2**128-total == 51720617913927, "original field budget")
    check(266514954058742090 < total, "LOW not added to HIGH")
    check(10*(169998//10) < 169998, "old integer-h rank-ten rounding artifact")
    print("PASS: independent determinants, disjoint inside counts, zero/excess controls")
    print("PASS: eight exact floors and eight rejected mutations; source cap",total)
    print("Hand geometry and source transport are not certified by this arithmetic audit")


if __name__ == "__main__":
    main()
