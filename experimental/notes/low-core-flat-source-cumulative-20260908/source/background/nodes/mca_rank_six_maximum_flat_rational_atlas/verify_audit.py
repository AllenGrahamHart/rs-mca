"""Independent integer envelope and small set-system packing controls."""

from itertools import combinations


def check(ok, why):
    if not ok:
        raise ValueError(why)


def main():
    gap, end = 67466, 22999
    for start, floor in ((20481, 25), (22500, 17)):
        numerator = 35*(gap+start)
        denominator = 29*start-7*gap-144
        q, rem = divmod(numerator, denominator)
        check(q == floor and 0 < rem < denominator, "independent exact floor")
        # The upper-bound inequality is affine in J, so its two endpoints suffice.
        for J in (start, end):
            den = 29*J-7*gap-144
            check(den > 0 and (floor+1)*den > 35*(gap+J), "entire affine envelope")
            check(16*(J-4) > 7*(2*J-2), "strict root-count margin")
            check(J+24 <= 7*3289, "strict degree upper bound")
        for wrong in (q-1, q+1):
            check(not wrong*denominator <= numerator < (wrong+1)*denominator,
                  "wrong floor rejection")
        print("INTEGER ENVELOPE", start, end, floor, "quotient/remainder", q, rem)

    tested = 0
    for n, size, overlap in ((6, 3, 1), (7, 3, 1), (8, 4, 1)):
        sets = tuple(map(frozenset, combinations(range(n), size)))
        for family in combinations(sets, 3):
            if any(len(A & B) > overlap for A, B in combinations(family, 2)):
                continue
            counts = [sum(x in A for A in family) for x in range(n)]
            L = len(family)
            check(sum(counts) == L*size, "same-domain incidence sum")
            check(sum(c*c for c in counts) <= L*size+L*(L-1)*overlap,
                  "pairwise intersections upper second moment")
            check((L*size)**2 <= n*sum(c*c for c in counts), "integer Cauchy")
            check(size*size > n*overlap, "positive packing denominator")
            check(L*(size*size-n*overlap) <= n*(size-overlap), "packing conclusion")
            tested += 1
    check(tested > 0, "nonvacuous packing controls")
    # The domain guard cannot be omitted, even though its formal quotient exists.
    check(3*3-10*1 < 0, "negative denominator must not be divided as positive")
    # One point in the actual J22500 core calibration, not a whole-row payment.
    K, M, h, b = 22500, 89966, 3250, 19374
    check(6 <= b <= 6*h and 2*b-5*h > K-4, "near-maximum band premise")
    check(3*b-2*h > 2*K-2 and b*b > M*h, "both strict band gates")
    numerator, denominator = M*(b-h), b*b-M*h
    floor, remainder = divmod(numerator, denominator)
    check(floor == 17 and 0 < remainder < denominator, "point band packing cap")
    print("POINT near-maximum band", K, M, h, b, "flat cap", floor)
    print("PASS", tested, "small admissible families; no primary/Fraction import")
    print("This is a per-core flat atlas, not a bad-slope census")


if __name__ == "__main__":
    main()
