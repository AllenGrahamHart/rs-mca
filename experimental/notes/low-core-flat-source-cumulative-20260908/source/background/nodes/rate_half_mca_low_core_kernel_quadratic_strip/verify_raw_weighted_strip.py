"""Exact small-memory resource and factor prices at raw cutoff 125."""

from fractions import Fraction as Q
from math import prod

C = 13062473626374413737
B = 2130706433**6 // 2**128
NEAR = 134944
LABELS = 981229
BASE = C // 1375 + NEAR
TARGET = 274811931500367244


def require(ok, message):
    if not ok:
        raise ValueError(message)


def ceil(q):
    return -(-q.numerator // q.denominator)


def phi(d, w):
    if d <= 0:
        return 0
    ell = (d - 1) // w
    return d * (ell + 1) * (ell + 2) // 2 - w * ell * (ell + 1) * (ell + 2) // 3


def resource(j):
    return Q(prod(1048576 + j - i for i in range(12)),
             (67472 + j) * prod(67472 + i for i in range(1, 11)))


def main():
    require(ceil(resource(9822)) == C, "first resource endpoint")
    require(ceil(resource(9940)) == 13060022408459260015 < C, "second resource endpoint")
    require(BASE == 9499980819316335, "single HIGH/near base")
    for j in range(9822, 9941):
        a, w, n = j + 67347, j - 1, j + 1048576
        require((2 * a - 1) // w == 15 and (2 * a - 4 * w - 1) // w == 11,
                "both monomial regimes")
        gap = phi(2 * a, w) - phi(2 * a - 4 * w, w) - 4 * n
        require(gap == 3618424 - 364 * j > 0, "full-kernel degree <=3")
        require(resource(j) <= C, "actual resource interval")
        require((134696 - j) // 3 <= 41624 < 51391, "actual doubled factor height")
    require(3618424 - 364 * 9941 == -100, "first failed fixed-cutoff row")
    require(15**2 <= 256, "conservative full off-gcd allowance")

    harmonic = sum((Q(1, t) for t in range(1, 125)), Q(0))
    for m in (2, 4, 8, 16, 32, 64):
        exact = sum((Q(1, t) for t in range(m, 2 * m)), Q(0))
        chord = m * (Q(1, m) + Q(1, 2 * m - 1)) / 2
        require(exact <= chord <= Q(5, 6), "dyadic harmonic hand certificate")
    require(harmonic <= 6, "H124 bound")
    f = lambda t: (981104 + t) * (2**7 * 3**12 * Q(1047027, 65923 - t)**3 + 256)
    raw_chord = Q(124, 125) * f(1) + Q(502, 15375) * (f(124) - f(1))
    require(int(Q(C, 1375) + raw_chord) + NEAR == TARGET, "weighted chord price")
    require(B - TARGET == 168796611027843, "reserve")
    old_resource = 23067643444721720934
    require(int(Q(old_resource, 1375) + raw_chord) + NEAR > B,
            "coarse whole-interval resource cannot pay this profile")
    direct_raw = sum((f(t) / (t * (t + 1)) for t in range(1, 125)), Q(0))
    require(direct_raw <= raw_chord, "exact nested sum below hand chord")

    ell, h = 2796, 1550
    a, slots = 67348 + h + 3 * ell, 2097154 + 4 * h + 7 * ell
    denominator = a * a - slots * ell
    top = slots * (a - ell) // denominator
    lower = int(2**7 * 3**13 * Q(1043608, 62379)**2)
    require((a, slots, denominator, top, lower) ==
            (77286, 2122926, 37424700, 4225, 57119482443), "high-height d7 envelope")
    require(BASE + LABELS * (top * 3**16 + lower + 257) == 244005743185015160 < TARGET,
            "all components, singular pair and exceptions")
    n, a1, collision = 1058516, 56316, 2979
    den = a1 * a1 - collision * n
    gp_top = n * (a1 - collision) // den
    gp_low = int(2**10 * 3**9 * Q(1047584, 66355)**3)
    require((den, gp_top, gp_low) == (18172692, 3106, 79311626937), "d10 envelope")
    require(BASE + LABELS * (max(gp_top + 1, gp_low) + 256) == 87322849458276532 < TARGET,
            "all d10 coefficient dimensions")

    ordinary = []
    for d in range(12):
        if d in (7, 10):
            continue
        h = 0 if d in (0, 11) else 9939 // (10 // (11 - d))
        r = (d + 2) // 3
        m = int(2**d * 3**(22 - d - r) * Q(1048577 - h, 67348 - h)**r)
        ordinary.append(BASE + LABELS * (m + 256))
    require(max(ordinary) == 267756687104005804 < TARGET, "every other kernel dimension")

    require(77169**2 - 590000 * 9939 == 91044561, "small-line denominator")
    require(749024 * 77169 == 57801433056 and 57801433056 // 91044561 == 634,
            "small-line numerator and count")
    require(590000 - 16 * 9939 == 430976 > 0, "line denominator increases with height")
    require(Q(458576, 57409) < 8 and 458576 - 16 * 57409 < 0, "outside-domain ratio")
    require(57409 - 9939 > 0 and 2**16 * 8**6 == 2 * 8**11, "all complement factors")
    require(11 * 126 > 501 and 126 < 501, "medium margins need completed weights")
    large = 255637082864553899 + LABELS * (2 * 8**11 + 256)
    require(large == 272494468975295659 < TARGET, "large-line source")
    require(large + BASE > B, "extra resource fails the budget")
    for pairs in (3 * 634, 127031877504 + 634, 163774741769, 223154201664, 6):
        require(BASE + LABELS * (pairs + 256) < TARGET, "other complete factor alternatives")
    require(9940 - 9822 + 1 == 119, "new interval length")
    print("PASS: every canonical normalized 9822..9940 source paid by the hand composition")
    print("Bound", TARGET, "reserve", B - TARGET, "; combined coverage 4801..9940")
    print("Original-source/owner transport, higher ranks, LIST and both prizes remain open")


if __name__ == "__main__":
    main()
