"""Exact tiny cutoff-101 kernel, component and single-resource ledger."""

from fractions import Fraction as Q


def require(ok, label):
    if not ok:
        raise ValueError(label)


def price(pairs):
    return (23067643444721720934 + 1189 * 981205 * (pairs + 64)) // 1200 + 134944


def verify():
    budget = 2130706433**6 // 2**128
    require(12 * 67472 > 11 * 67483 and 12 * 1200 < 67473,
            "LOW floor and HIGH monotonicity")
    require(1224 * (67473 - 1122) - 1200 * 67473 == 246024 > 0,
            "HIGH Bernoulli certificate")
    for j in (8656, 8763, 8764):
        a, w, n = j + 67371, j - 1, 1048576 + j
        full = sum((i + 1) * (a - i * w) for i in range(9))
        mult = sum((i + 1) * (a - (i + 4) * w) for i in range(5))
        require(full - n - mult == 972694 - 111 * j, "new full-kernel surplus")
    require(972694 - 111 * 8763 == 1 and 972694 - 111 * 8764 == -110,
            "strict endpoint and next failure")
    require(67379 - 7 * 8763 == 6038, "positive monomial blocks")
    require(960724 - 111 * 8763 < 0, "old cutoff is not extrapolated")

    totals = []
    for d in range(12):
        if d in (7, 10):
            continue
        h = 0 if d in (0, 11) else 8762 // (10 // (11 - d))
        r = (d + 2) // 3
        ratio = Q(1048577 - h, 67372 - h)
        require(ratio >= 3, "weighted-lift ratio guard")
        cap = int(2**d * 3**(22 - d - r) * ratio**r)
        totals.append((price(cap), d))
    require(max(totals) == (274741711077757253, 11), "all nonexceptional kernel dimensions")
    low7 = int(2**7 * 3**12 * Q(1047977, 66772)**3)
    require(low7 == 262988722817, "d7 low-height pair cap")

    ell, u0, s0 = 2720, 67973, 2099558
    a, s = u0 + 3 * ell, s0 + 7 * ell
    den, num = a*a - s*ell, s*(a - ell)
    require((a, s, den, num) == (76133, 2118598, 33647129, 155532634974),
            "coupled component endpoint")
    require(6*u0 - s0 == -1691720 and -1691720 + 4*ell < 0,
            "component denominator monotonicity")
    require(1827666 - 5*ell > 0 and 1895038 - 2*ell + 601 > 0,
            "both coupled derivative signs")
    top, lower = num // den, int(2**7 * 3**13 * Q(1044196, 62991)**2)
    require(top == 4622 and lower == 56078104495, "top and entire lower complement")
    component = top * 3**16 + lower + 1
    require(component == 255040048958 and price(component) == 267175680601112099,
            "all component and singular contributions")
    require((67373 - 2*8656) // 3 == 16687 < 17580, "projection-height guard")

    cases = [value for value, _ in totals]
    cases += [price(low7), price(component), price(80530893115),
              price(163774741769), price(73222472421), price(6),
              price(3*696), price(127031877504 + 696), 255637083438792239]
    require(max(cases) == 274903465748372176, "exhaustive factor/source maximum")
    require(budget - max(cases) == 77262363022911, "strict finite reserve")
    require(max(cases) < 274979661292365251 < budget, "combined old and new strip")
    require(8763 - 8656 + 1 == 108, "new complete interval")
    print("PASS: every normalized 8656..8763 source pays by", max(cases))
    print("Reserve", budget-max(cases), "; combined coverage 4801..8763; prizes OPEN")
    print("Kernel, affine-offset geometry and universal incidence are hand proofs")


if __name__ == "__main__":
    verify()
