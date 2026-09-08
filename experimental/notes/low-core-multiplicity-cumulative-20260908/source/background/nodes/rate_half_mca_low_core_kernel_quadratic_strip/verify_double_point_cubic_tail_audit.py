"""Independent integer/ceiling audit; does not import the primary checker."""

from math import lcm


def check(ok, label):
    if not ok:
        raise RuntimeError(label)


def up(n, d):
    return (n + d - 1) // d


def verify():
    c, near, labels, budget = 23067643444721720934, 134944, 981604, 274980728111395087
    # Literal product at the worst allowed M, with integer cross multiplication.
    for r in range(1, 501):
        numerator, denominator = 12 * r * (67483 - r), 67483
        for i in range(1, 11):
            numerator *= 67472 + i - r
            denominator *= 67472 + i
        check(numerator > 11 * r * denominator, "all exact LOW weights")
    check(67473 - 12 * 5500 > 0, "HIGH monotonicity interval")

    count_num = 2**7 * 3**12 * 1046977**3
    terms = [(c, 5500)]
    for t in (1, 499):
        terms.append((499 * (981104 + t) * count_num, 1000 * (65873 - t)**3))
    terms.append((499 * 256 * 981354, 500))
    denominator = lcm(*(d for _, d in terms))
    chord = sum(n * (denominator // d) for n, d in terms) // denominator + near
    check(chord == 274778805314695460, "independent chord fraction")

    # Separately sum 499 upward-rounded list counts; no convexity formula import.
    cumulative_labels = sum((981104 + t) * (up(count_num, (65873 - t)**3) + 256)
                            for t in range(1, 500))
    upper = up(c + 11 * cumulative_labels, 5500) + near
    check(upper <= chord < budget, "all nested LOW counts independently pay")
    raw_upper = up(c, 5500) + near + sum(
        up((981104 + t) * (up(count_num, (65873 - t)**3) + 256), t * (t + 1))
        for t in range(1, 500))
    check(raw_upper < upper, "retaining per-pair raw budgets is stronger at this profile")
    check(499 * (981104 + 250) == sum(981104 + t for t in range(1, 500)),
          "complete exception-label sum")

    # Direct Cauchy inequalities certify and exclude the next component integer.
    a, s, ell = 76793, 2122734, 2740
    den, num = a * a - s * ell, s * (a - ell)
    check(1943 * den <= num < 1944 * den and den > 0, "component 1943 boundary")
    lower = (2**7 * 3**13 * 1043667**2) // 62063**2
    top_pairs = 1943 * 43046721
    high_source = c // 5500 + near + labels * (top_pairs + lower + 257)
    check(high_source == 142942788280886491 < chord, "high-height cubic assembly")
    den, num = 55877**2 - 2946 * 1058397, 1058397 * (55877 - 2946)
    check(13333 * den <= num < 13334 * den and den > 0, "GP list boundary")
    gp_pairs = (1024 * 19683 * 1047595**3) // 65991**3
    check(c // 5500 + near + labels * (gp_pairs + 256) == 83344622367408351,
          "GP lower-dimensional payment")

    check(458576 * 100 < 57153 * 803 and 803**5 > 32768 * 100**5, "outside factors")
    remainder_num = labels * (2 * 803**11 + 256 * 100**11)
    large = 255637082864553899 + up(remainder_num, 100**11)
    check(large == 273209735302733347 < chord, "one resource in large-line branch")
    check(980 * 58297001 <= 57153932880 < 981 * 58297001, "small-line integer")

    # All kernel rows use the two actual monomial regimes on this tail.
    for j in range(9527, 9823):
        w, a = j - 1, j + 66972
        dimensions = [sum(max(2 * a - (shift + y + z) * w, 0)
                          for y in range(18) for z in range(18 - y))
                      for shift in (0, 4)]
        gap = dimensions[0] - dimensions[1] - 4 * (1048576 + j)
        check((gap > 0) == (j <= 9821), "whole tail and first failed kernel row")
    check(chord + 201922796699627 == budget, "final tail reserve")
    print("PASS: independent integer weights, 499 cumulative counts and both component boundaries")
    print("PASS: every tail kernel row, original labels and resource-once factor composition")


if __name__ == "__main__":
    verify()
