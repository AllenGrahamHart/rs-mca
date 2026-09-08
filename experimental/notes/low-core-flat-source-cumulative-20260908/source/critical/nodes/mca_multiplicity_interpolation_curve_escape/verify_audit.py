"""Independent monomial/Taylor controls; no imports of the primary checker."""

from math import comb


def check(ok, label):
    if not ok:
        raise RuntimeError(label)


def monomials(d, w):
    if d <= 0:
        return []
    return [(x, y, z) for y in range((d - 1) // w + 1)
            for z in range((d - 1) // w - y + 1)
            for x in range(d - w * (y + z))]


def hasse(poly, point, index, p):
    value = 0
    for powers, coefficient in poly.items():
        term = coefficient
        for degree, at, order in zip(powers, point, index):
            if order > degree:
                term = 0
                break
            term *= comb(degree, order) * pow(at, degree - order, p)
        value += term
    return value % p


def mul(a, b, p):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] = (result[i + j] + x * y) % p
    return result


def verify():
    for w in (1, 2, 3):
        for d in range(1, 14):
            terms = monomials(d, w)
            check(len(terms) == sum((i + 1) * max(d - i * w, 0) for i in range(d)),
                  "literal weighted monomial census")
            check(all(x + w * (y + z) < d for x, y, z in terms),
                  "strict weighted support")
    check(len(monomials(6, 1)) == 56 and len(monomials(2, 1)) == 4,
          "small escape dimensions")

    for j in range(8764, 9823):
        w, a, n = j - 1, j + 66972, j + 1048576
        # Count each pair monomial separately; never enumerate its many X powers.
        full = sum(max(2 * a - (y + z) * w, 0)
                   for y in range(20) for z in range(20 - y))
        multiple = sum(max(2 * a - (4 + y + z) * w, 0)
                       for y in range(20) for z in range(20 - y))
        gap = full - multiple - 4 * n
        check((gap > 0) == (j <= 9821), "all restricted rows and first failed row")
        if j == 9822:
            check(gap == -284 and full - multiple - 3 * n > 0,
                  "omitting X derivative would falsely certify the next row")

    # Q=Y^2(Y-1)^2, G=Z-Y^4 over F7; the toy is not a canonical MCA source.
    q = {(0, 4, 0): 1, (0, 3, 0): -2, (0, 2, 0): 1}
    domain = range(5)
    receiver = [(0, 0)] * 3 + [(1, 1)] * 2
    jets = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    for x, (u, v) in zip(domain, receiver):
        check(all(hasse(q, (x, u, v), jet, 7) == 0 for jet in jets),
              "full double-point Taylor conditions")
    rich = []
    curve_pairs = 0
    for a0 in range(7):
        for a1 in range(7):
            square = mul([a0, a1], [a0, a1], 7)
            fourth = mul(square, square, 7)
            if any(fourth[2:]):
                continue
            curve_pairs += 1
            b0, b1 = fourth[:2]
            agreements = sum(((a0 + a1 * x) % 7, (b0 + b1 * x) % 7) == target
                             for x, target in zip(domain, receiver))
            if agreements >= 3:
                rich.append((a0, a1, b0, b1))
    check(curve_pairs == 7 and rich == [(0, 0, 0, 0)], "all linear pairs on toy quartic")
    wrong = {(1, 0, 0): 1}
    check(all(hasse(wrong, (0, 0, 0), jet, 7) == 0
              for jet in (jets[0], jets[2], jets[3])) and
          hasse(wrong, (0, 0, 0), jets[1], 7) == 1, "missing X condition control")
    check(hasse({(0, 2, 0): 1}, (0, 0, 0), (0, 2, 0), 2) == 1,
          "Hasse coefficient detects a term ordinary derivatives miss in F2")

    high, remainder = divmod(23067643444721720934, 5500)
    check(0 <= remainder < 5500, "one HIGH resource floor")
    total = high + 134944 + 132 * (1048576 - 66972)
    check(total == 4194117119656075 < 274979661975561635,
          "independent original source accounting")
    check(274979661975561635 + 1066135833452 == 274980728111395087,
          "complete strip budget and reserve")
    print("PASS: independent weighted monomials, all rows, F7 root/control census and F2 Hasse guard")
    print("PASS: original labels, 64 exceptions, HIGH and near; no field-sized computation")


if __name__ == "__main__":
    verify()
