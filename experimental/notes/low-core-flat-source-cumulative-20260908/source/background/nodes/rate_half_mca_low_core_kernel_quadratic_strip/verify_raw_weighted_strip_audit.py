"""Independent integer audit; no imports of the primary check."""

from math import comb, lcm, prod

TARGET = 274811931500367244
BUDGET = 274980728111395087
C = 13062473626374413737


def check(ok, message):
    if not ok:
        raise ValueError(message)


def up(n, d):
    return (n + d - 1) // d


def down(n, d):
    return n // d


def dim(d, w):
    if d <= 0:
        return 0
    return sum(max(d - (i + k) * w, 0)
               for i in range((d - 1) // w + 1)
               for k in range((d - 1) // w + 1 - i))


def main():
    for j, ceiling in ((9822, C), (9940, 13060022408459260015)):
        numerator = prod(range(1048576 + j - 11, 1048576 + j + 1))
        denominator = (67472 + j) * prod(range(67473, 67483))
        check((ceiling - 1) * denominator < numerator <= ceiling * denominator,
              "independent resource cross-products")
    for j in range(9822, 9941):
        a, w, n = j + 67347, j - 1, j + 1048576
        check(dim(2 * a, w) - dim(2 * a - 4 * w, w) - 4 * n > 0, "literal monomial gap")
        check(2 * a <= 16 * w, "pair degree <=15")
    check(dim(2 * (9941 + 67347), 9940) -
          dim(2 * (9941 + 67347) - 4 * 9940, 9940) -
          4 * (9941 + 1048576) == -100, "next gap")

    # Round each raw budget UP before independently adding its telescoping weight.
    common = lcm(*range(1, 126), 1375)
    total = C * (common // 1375)
    for t in range(1, 125):
        denominator = (65923 - t)**3
        numerator = (981104 + t) * (2**7 * 3**12 * 1047027**3 + 256 * denominator)
        raw_budget_ceiling = up(numerator, denominator)
        check(common % (t * (t + 1)) == 0, "integer weight denominator")
        total += raw_budget_ceiling * (common // (t * (t + 1)))
    actual_ceiling_bound = total // common + 134944
    check(actual_ceiling_bound <= TARGET < BUDGET, "124 separate raw budgets pay")
    check(BUDGET - TARGET == 168796611027843, "printed reserve")

    for raw in range(1, 126):
        num = 12 * raw * (67483 - raw) * prod(67472 + i - raw for i in range(1, 11))
        den = 67483 * prod(67472 + i for i in range(1, 11))
        check(num >= 11 * raw * den, "all used low weights")
    check(12 * (67473 - 5500) - 11 * 67473 > 0 and 12 * 5500 < 67473,
          "all-large-raw weight bridge")
    base, labels = C // 1375 + 134944, 981229

    top_n = 2122926 * (77286 - 2796)
    top_d = 77286**2 - 2122926 * 2796
    check(top_d == 37424700 and 4225 * top_d <= top_n < 4226 * top_d, "d7 top")
    low7 = down(2**7 * 3**13 * 1043608**2, 62379**2)
    check(low7 == 57119482443, "entire smaller-dimensional complement")
    check(base + labels * (4225 * 3**16 + low7 + 257) < TARGET, "d7 full count")
    gp_d = 56316**2 - 1058516 * 2979
    gp_n = 1058516 * (56316 - 2979)
    check(gp_d == 18172692 and 3106 * gp_d <= gp_n < 3107 * gp_d, "GP top")
    low10 = down(2**10 * 3**9 * 1047584**3, 66355**3)
    check(low10 == 79311626937 and base + labels * (low10 + 256) < TARGET, "GP complement")
    for d in (0, 1, 2, 3, 4, 5, 6, 8, 9, 11):
        h = 0 if d in (0, 11) else 9939 // (10 // (11 - d))
        r = (d + 2) // 3
        pairs = down(2**d * 3**(22 - d - r) * (1048577 - h)**r, (67348 - h)**r)
        check(base + labels * (pairs + 256) < TARGET, "other dimension")

    for h in (0, 1, 1550, 9939):
        check(77169**2 - (590000 + 16 * h) * (9939 - h) ==
              91044561 + 430976 * h + 16 * h**2 > 0, "line height polynomial")
        check(458576 - 16 * h < 8 * (57409 - h) and 57409 - h > 0, "outside ratio")
    check(57801433056 < 635 * 91044561, "line cap")
    check(2**16 * 8**6 <= 2 * 8**11, "conic and two-line cases")
    large = 255637082864553899 + labels * (2 * 8**11 + 256)
    check(large == 272494468975295659 < TARGET and large + base > BUDGET, "one resource")
    check(501 - 126 > 0 and 501 - 11 * 126 < 0, "omitted-medium-margin control")
    for count in (3 * 634, 127031877504 + 634, 163774741769, 223154201664, 6):
        check(base + labels * (count + 256) < TARGET, "remaining whole-source patterns")

    for j in (9981, 169999):
        a, w, n = j + 67471, j - 1, j + 1048576
        for r in range(1, 5):
            check(dim(r * a, w) - dim(r * a - 4 * w, w) < n * comb(r + 2, 3),
                  "independent small-r fence endpoints")
        check(10 * a * a + 4 * a * w < 7 * n * w, "all-r>=5 hand certificate")
    print("PASS: independent monomial, 124 raw-budget, component and factor audit")
    print("Independently rounded raw-budget total", actual_ceiling_bound, "; printed cap", TARGET)
    print("Universal geometry, convex extension and all-r monotonicity are hand proofs")


if __name__ == "__main__":
    main()
