"""Independent tiny arithmetic/evaluation audit; imports no primary verifier."""

from fractions import Fraction


def check(ok, label):
    if not ok:
        raise RuntimeError(label)


def choose(n, k):
    row = [1]
    for _ in range(n):
        row = [1] + [row[i - 1] + row[i] for i in range(1, len(row))] + [1]
    return row[k]


def hilbert_degree(a, b, exponent):
    values = [choose(t + a, a) * choose(exponent * t + b, b)
              for t in range(a + b + 1)]
    while len(values) > 1:
        values = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    return values[0]


def verify():
    for a, b, exponent in ((0, 0, 1), (0, 2, 3), (2, 0, 3),
                            (1, 1, 3), (3, 2, 2), (10, 10, 3), (11, 11, 3)):
        check(hilbert_degree(a, b, exponent) == choose(a + b, a) * exponent**b,
              "Hilbert leading coefficient by finite differences")
    q_floor = int(Fraction(1048577, 66973))
    classes00 = choose(20, 10) * 3**10
    cases = (choose(22, 11) * 3**11, choose(21, 10) * 3**11,
             3 * choose(21, 11) * 3**10, q_floor * classes00)
    check(classes00 == 10909657044 and max(cases) == 163644855660,
          "all offset/projective degree costs")
    high = int(Fraction(23067643444721720934, 5500))
    low = (1048576 - 67472 + 500) * (max(cases) + 64)
    total = high + low + 2 * 67472
    check(total == 164828561948185643, "independent full source composition")
    check(int(Fraction(2130706433**6, 2**128)) - total == 110152166163209444,
          "independent reserve")

    solutions = {}
    for c, d in ((0, 0), (1, 0), (0, 1), (1, 1)):
        # Degree <=4; equality at all seven points is a polynomial identity.
        solutions[c, d] = [(a, b) for a in range(7) for b in range(7)
                           if all(((c + a*t) * (d + b*t)**3 -
                                   (c + t) * (d + t)**3) % 7 == 0
                                  for t in range(7))]
    check([len(solutions[key]) for key in ((0, 0), (1, 0), (0, 1), (1, 1))]
          == [6, 3, 1, 1], "independent four-coset identities")
    rich_count = 0
    for a, b in solutions[0, 0]:
        hits = sum(a*t % 7 == t and b*t % 7 == (t if t <= 3 else 2*t) % 7
                   for t in range(7))
        rich_count += hits >= 4
    check(rich_count == 2, "independent common-zero saturation")
    pole_count = sum(all(((1 + a*t*t) * (b*t)**3 - t**5 - t**3) % 7 == 0
                         for t in range(7)) for a in range(7) for b in range(7))
    check(pole_count == 3, "degree-five cleared rational-offset identity")
    print("PASS: independent Pascal/Hilbert, four-case ledger and F7 evaluations")
    print("No universal geometric statement is inferred from these finite controls")


if __name__ == "__main__":
    verify()
