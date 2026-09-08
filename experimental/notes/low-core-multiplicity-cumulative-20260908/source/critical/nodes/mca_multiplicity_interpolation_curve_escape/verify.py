"""Small exact checks of the multiplicity escape criterion and finite price."""

from math import comb


def require(ok, label):
    if not ok:
        raise ValueError(label)


def dimension(d, w):
    if d <= 0:
        return 0
    ell = (d - 1) // w
    return (ell + 1) * (ell + 2) * d // 2 - w * ell * (ell + 1) * (ell + 2) // 3


def escape_gap(n, a, w, r, g):
    return dimension(r * a, w) - dimension(r * a - g * w, w) - n * comb(r + 2, 3)


def verify():
    for w in range(1, 5):
        for d in range(-2, 24):
            direct = sum((i + 1) * max(d - i * w, 0) for i in range(max(d, 0) + 1))
            require(dimension(d, w) == direct, "strict weighted dimension formula")
    for r in range(1, 9):
        jets = sum(1 for x in range(r) for y in range(r - x)
                   for z in range(r - x - y))
        require(jets == comb(r + 2, 3), "all three-variable Hasse jets")

    for j in range(8764, 9822):
        a, w, n = j + 66972, j - 1, j + 1048576
        gap = escape_gap(n, a, w, 2, 4)
        expected = (4646608 - 480 * j if j <= 8930 else
                    4110764 - 420 * j if j <= 9568 else 3574924 - 364 * j)
        require(gap == expected > 0, "quartic escape at every certified J")
        require((2 * a - 1) // w == (17 if j <= 8930 else 16 if j <= 9568 else 15),
                "actual relation pair degree")
        if j >= 9527:
            require(((2 * a - 1) // w)**2 <= 256, "full-kernel tail exceptions")
    require(escape_gap(1048576 + 9526, 66972 + 9526, 9525, 2, 4) == 109844,
            "positive gap at exhaustive strip endpoint")
    require(escape_gap(1048576 + 9821, 66972 + 9821, 9820, 2, 4) == 80,
            "last restricted quartic row")
    require(escape_gap(1048576 + 9822, 66972 + 9822, 9821, 2, 4) == -284,
            "next row is not certified")
    require(escape_gap(1, 1, 1, 1, 1) == 0, "strictness equality control")
    require(escape_gap(5, 3, 1, 2, 4) == 32, "F7 toy dimension gap")

    resource = 23067643444721720934
    base = resource // 5500 + 134944
    total = base + 981604 * (4 * 17 + 64)
    budget = 2130706433**6 // 2**128
    require(total == 4194117119656075, "all 68 curve and 64 off-curve pairs")
    require(budget - total == 270786610991739012, "restricted source reserve")
    strip = max(274979661975561635, total)
    require(strip == 274979661975561635 and budget - strip == 1066135833452,
            "whole-source alternatives combine by maximum")
    require(9526 - 8764 + 1 == 763, "new complete interval length")
    print("PASS: full multiplicity dimensions and 1058 restricted quartic rows")
    print("PASS: quartic total", total, "; every normalized 4801..9526 source pays by", strip)
    print("Universal escape/coverage are hand proofs; higher J, transport and prizes remain open")


if __name__ == "__main__":
    verify()
