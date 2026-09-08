"""Rank-five signed coefficient identities and small actual inside-rank controls."""

from itertools import combinations
from math import comb, factorial, prod
from verify import check, rank, rising, derivative


def main():
    p, t = 127, 8
    for inside_rank in range(1, 6):
        a = t+5-inside_rank
        degrees = list(range(inside_rank))+list(range(t, t+5-inside_rank))+list(range(a, a+6))
        check(len(set(degrees)) == 11 and max(degrees) < a+6, "actual polynomial carrier degrees")
        def row(x):
            z = prod(x-v for v in range(t)) % p
            whole = prod(x-v for v in range(a)) % p
            return tuple([pow(x, i, p) for i in range(inside_rank)]
                         +[z*pow(x, i, p) % p for i in range(5-inside_rank)]
                         +[whole*pow(x, i, p) % p for i in range(6)])
        check(rank([row(x) for x in range(a)], p) == 5, "full flat rank five")
        inside = [row(x) for x in range(t)]
        check(rank(inside, p) == inside_rank, "actual deficient inside rank")
        e = [1]+[factorial(b)*sum(rank(list(xs), p) == b for xs in combinations(inside, b))
                 for b in range(1, 6)]
        check(e[3] <= t*e[2] and e[4] <= t*t*e[2], "actual extension inequalities")
        for c in (100, 67467):
            coefficients = [comb(11, b)*rising(c, 5-b)-comb(11, b-1)*derivative(c, 6-b)
                            for b in range(2, 6)]
            printed = [11*(c**3-3*c*c-12*c-6), -165*c-110, -165, 132]
            check(coefficients == printed, "signed rank-five identities")
            check(coefficients[1] < 0 and coefficients[2] < 0, "termwise positivity is false")
            check(sum(coef*e[b] for b, coef in enumerate(coefficients, 2)) >= 0, "coupled remainder")
            absorbed = coefficients[0]-(165*c+110)*c-165*c*c
            check(absorbed == 11*(c**3-33*c*c-22*c-6) > 0, "uniform absorption")
        print("PASS: actual inside rank", inside_rank, "ordered counts", e)
    check(29**2*25 > 20*26**2, "rank-five log-concavity seed bound")
    check(34**2 > 22*34+6, "universal c>=34 absorption base")
    # Both sides have degree at most four; five distinct values certify the identities.
    for c in range(1, 6):
        coefficients = [comb(11, b)*rising(c, 6-b)-comb(11, b-1)*derivative(c, 7-b)
                        for b in range(2, 7)]
        printed = [-110*c**3-550*c*c-770*c-264,
                   -55*c**3-495*c*c-880*c-330,
                   -165*c*c-660*c-330, -198*c-330, 0]
        check(coefficients == printed, "rank-six linear-tangent coefficient identities")
        check(all(x < 0 for x in printed[:-1]) and printed[-1] == 0, "rank-six sign obstruction")
    print("PASS: two negative coefficients absorbed, not discarded; c>=100,a<=c scope")
    print("PASS: rank-six signed remainder is negative when E2>0; proof-step boundary only")
    print("Inside-geometry controls do not assert maximum density of these particular test flats")


if __name__ == "__main__":
    main()
