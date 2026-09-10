"""Exact scope/exhaustion arithmetic; the structural dichotomy is hand-proved."""


def need(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    budget, near, W = 274980728111395087, 134944, 624373932788019251
    cases = (W//8+near, 274138707278280353, 256541462574529459, 272889015800964850)
    need(max(cases) == 274138707278280353 < budget, "maximum of whole-source alternatives")
    need(budget-max(cases) == 842020833114734, "exact inherited maximum reserve")
    degrees = {}
    for rank in range(16, 23):
        codim = 22-rank
        options = [degree for degree in range(2, 12) if degree+1 <= codim]
        need(all(2 <= degree <= 5 for degree in options), "all deficient full-shared degrees are paid")
        need((not options) == (codim <= 2), "deficient case impossible in codimension<=2")
        need(0 <= codim <= 6, "remaining finite rank-drop allowance")
        degrees[rank] = options
    need(degrees[16] == [2, 3, 4, 5] and degrees[19] == [2], "degree endpoints")
    print("PASS exhaustive deficient-branch degree table", degrees)
    print("PASS whole-source max", max(cases), "reserve", budget-max(cases))
    print("Full affine-hull projection is not a bad-label census; the regular branch stays open")


if __name__ == "__main__":
    main()
