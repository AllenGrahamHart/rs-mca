"""Exact cubic source-class prices and finite-characteristic controls."""

from fractions import Fraction as F
from itertools import product
from math import prod

R, D, LO, E, NEAR = 1048576, 67472, 9965, 21499, 134944
W, B = 624373932788019251, 274980728111395087
CASES = (
    (8, 227325639596777196, 12776402205892, 271476187024062739, 3942608723248893),
    (43, 228493023165539663, 12849534849046, 237527989066104848, 38323732976576059),
)


def need(ok, message):
    if not ok:
        raise ValueError(message)


def low(t, j):
    return F(3*prod(R+j-i for i in range(11)),
             11*(D+j-t)*prod(D-t+i for i in range(1, 10)))


def main():
    need(R+E-10-11*(D+E-1) == 91395 > 0, "entire J,T monotonicity gate")
    need(B == 2130706433**6//2**128 and NEAR == 2*D, "original row and denominator")
    degree_four_floor = int(4*low(1, LO)/3)
    need(degree_four_floor == 302790601542847445 < W,
         "smallest degree-at-least-four mass cap in this recipe")
    need(degree_four_floor+NEAR > B, "raising degree alone cannot pay this uniform recipe")
    for t, expected_mass, expected_pairs, expected_price, expected_outside in CASES:
        for j in (LO, E-1):
            need(low(t, j+1)/low(t, j) == F(R+j+1, R+j-10)*F(D+j-t, D+j+1-t) <= 1,
                 "exact decreasing ratio")
        mass = int(low(t, LO))
        pairs = int(prod(F(R+i, D-t+i) for i in range(1, 12)))
        exceptions = E-8+3*pairs
        amount = W+t*(mass+exceptions)
        price = amount//(t+1)+NEAR
        outside = ((t+1)*(B-NEAR+1)-amount+t-1)//t
        need((mass, pairs, price, outside) == (expected_mass, expected_pairs, expected_price, expected_outside),
             "exact cubic source price")
        need((amount+t*(outside-1))//(t+1)+NEAR == B, "last paid exception envelope")
        need((amount+t*outside)//(t+1)+NEAR == B+1, "adjacent envelope, not an unsafe source")
        print("PASS T", t, "MASS", mass, "PAIRS", pairs, "EXCEPTIONS", exceptions,
              "TOTAL", price, "RESERVE", B-price, "OUTSIDE_MIN", outside)
    controls = 0
    for p in (2, 3, 5):
        for coefficients in product(range(p), repeat=4):
            roots = [z for z in range(p) if sum(c*pow(z, i, p) for i, c in enumerate(coefficients)) % p == 0]
            need(len(roots) == p if not any(coefficients) else len(roots) <= 3,
                 "formal zero versus at-most-three distinct roots")
            controls += 1
    need(all((z**3-z) % 3 == 0 for z in range(3)) and any((0, 2, 0, 1)),
         "pointwise zero is not the polynomial identity")
    print("PASS", controls, "small cubic restrictions; W0 remains a proved-source input")
    print("PASS degree>=4 recipe lower envelope", degree_four_floor+NEAR, "exceeds budget")
    print("No whole J, arbitrary cubic cover, higher original rank or Prize closure")


if __name__ == "__main__":
    main()
