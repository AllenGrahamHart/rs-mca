"""Exact, small-memory cubic-tail resource, factor and source checks."""

from fractions import Fraction as Q
from math import prod

C = 23067643444721720934
NEAR = 134944
LABELS = 981604
BUDGET = 2130706433**6 // 2**128
BASE = C // 5500 + NEAR


def require(ok, message):
    if not ok:
        raise ValueError(message)


def ceil(x):
    return (x.numerator + x.denominator - 1) // x.denominator


def cumulative(h, exceptions=256):
    def f(t):
        return (981104 + t) * 2**7 * 3**12 * Q(1048577 - h, 67473 - t - h)**3
    return int(Q(C, 5500) + Q(499, 1000) * (f(1) + f(499))
               + Q(499, 500) * exceptions * 981354) + NEAR


def phi(d, w):
    return sum((i + 1) * max(d - i * w, 0) for i in range(20))


def verify():
    require(12 * (67473 - 5500) - 11 * 67473 == 1473, "linear LOW weight")
    require(12 * 5500 < 67473, "monotone completed weights through 5500")
    for raw in (1, 11, 499, 500, 501, 5500):
        exact = 12 * raw * Q(67483 - raw, 67483) * prod(
            Q(67472 + i - raw, 67472 + i) for i in range(1, 11))
        require(max(min(67473, raw), exact) >= 11 * min(raw, 500),
                "pointwise completed weight")
    raws = [1, 2, 3, 17, 499, 500, 501, 700]
    for t in (1, 7, 101, 500):
        lhs = sum(min(r, t) for r in raws)
        rhs = t * len(raws) - sum(sum(r <= v for r in raws) for v in range(1, t))
        require(lhs == rhs, "cumulative count identity on one fixed label set")
        labels_form = Q(sum(sum(r <= v for r in raws) for v in range(1, t)), t)
        raw_form = sum((Q(sum(r for r in raws if r <= v), v * (v + 1))
                        for v in range(1, t)), Q(0))
        require(labels_form == raw_form, "equivalent raw-weighted cumulative identity")
    target = cumulative(1600)
    require(target == 274778805314695460 and BUDGET - target == 201922796699627,
            "d7 cumulative LOW source price")
    naive = BASE + LABELS * (int(2**7 * 3**12 * Q(1046977, 65373)**3) + 256)
    require(naive > BUDGET, "discarding the cumulative information does not pay")

    for j in range(9527, 9822):
        a, w, n = j + 66972, j - 1, j + 1048576
        require(phi(2 * a, w) - phi(2 * a - 4 * w, w) - 4 * n > 0,
                "full double-point gcd degree <=3")
        require(((2 * a - 1) // w)**2 <= 256, "all off-gcd pairs")
        require((133946 - j) // 3 <= 41473 < 51391, "new cubic graph height")
    require(phi(2 * (9822 + 66972), 9821) -
            phi(2 * (9822 + 66972) - 4 * 9821, 9821) -
            4 * (9822 + 1048576) == -284, "first unproved tail row")

    ordinary = []
    for d in range(12):
        if d in (7, 10):
            continue
        h = 0 if d in (0, 11) else 9820 // (10 // (11 - d))
        r = (d + 2) // 3
        count = int(2**d * 3**(22 - d - r) * Q(1048577 - h, 66973 - h)**r)
        total = BASE + LABELS * (count + 256)
        ordinary.append(total)
        require(total < target, "all other projection-kernel dimensions")
    require(max(ordinary) == 268384711456990155, "ordinary d11 maximum")

    ell, h = 2740, 1600
    a, slots = 66973 + h + 3 * ell, 2097154 + 4 * h + 7 * ell
    denominator = a * a - slots * ell
    top = slots * (a - ell) // denominator
    low = int(2**7 * 3**13 * Q(1043667, 62063)**2)
    require((a, slots, denominator, top, low) ==
            (76793, 2122734, 80873689, 1943, 57709146976), "d7 high-height components")
    c7 = BASE + LABELS * (1943 * 3**16 + low + 257)
    require(c7 == 142942788280886491 < target, "whole lower complement and exceptions")

    n, a1, collision = 1058397, 55877, 2946
    den = a1 * a1 - collision * n
    gp_top = n * (a1 - collision) // den
    gp_low = int(2**10 * 3**9 * Q(1047595, 65991)**3)
    require((den, gp_top, gp_low) == (4201567, 13333, 80633845345), "GP actual envelope")
    gp = BASE + LABELS * (max(gp_top + 1, gp_low) + 256)
    require(gp == 83344622367408351 < target, "GP all coefficient dimensions")

    a1 = 76499
    den = a1 * a1 - 590000 * 9820
    num = 747120 * a1
    require((den, num, num // den) == (58297001, 57153932880, 980), "small factor lines")
    for h in (0, 1, 9820):
        require(a1 * a1 - (590000 + 16 * h) * (9820 - h) ==
                58297001 + 432880 * h + 16 * h * h, "height-aware line denominator")
    q0 = Q(803, 100)
    require(Q(458576, 57153) < q0 and 458576 - 16 * 57153 < 0, "outside LIST ratio")
    require(2**16 * q0**6 <= 2 * q0**11, "one conic or two remaining lines")
    large = 255637082864553899 + ceil(LABELS * (2 * q0**11 + 256))
    require(large == 273209735302733347 < target, "large-line whole-source partition")
    require(large + BASE > BUDGET, "an extra resource base would not pay")
    for pairs in (3 * 980, 127031877504 + 980, 163774741769, 223154201664, 6):
        require(BASE + LABELS * (pairs + 256) < target, "remaining factor patterns")

    require(9821 - 9527 + 1 == 295, "new complete tail length")
    require(max(target, 274979661975561635) == 274979661975561635,
            "combine earlier complete intervals by maximum")
    print("PASS: cumulative LOW accounting closes all normalized 9527..9821 sources")
    print("Tail total", target, "reserve", BUDGET - target, "; combined coverage 4801..9821")
    print("Cover, geometry and canonical-source bridges are hand proofs; both prizes remain open")


if __name__ == "__main__":
    verify()
