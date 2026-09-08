"""Exact rational certificate; analytic box coverage is proved in proof.md."""

import hashlib

from fractions import Fraction as F
from math import comb, prod

D, C, R, GAP, NEAR = 67466, 67467, 1048576, 67472, 134944
TARGET = 274977202549132026
EXPECTED_DIGEST = "aa67aff314740d5cebcbd03b85dec7e136cea67b009740ad1bdc28ee4dde05d7"


def need(ok, message):
    if not ok:
        raise ValueError(message)


def floor_check(numerator, denominator, candidate):
    need(denominator > 0 and denominator*candidate <= numerator
         < denominator*(candidate+1), "exact rational floor")


def cover_check(ranges):
    need(ranges and ranges[0][0] == 24538 and ranges[-1][1] == 29999,
         "degree endpoints")
    need(all(a <= b for a, b in ranges), "nonempty degree blocks")
    need(all(x[1]+1 == y[0] for x, y in zip(ranges, ranges[1:])),
         "exhaustive disjoint degree cover")


def blocks():
    for lo, hi, step in ((24538, 26998, 128), (26999, 27015, 1),
                         (27016, 27199, 16), (27200, 27999, 64),
                         (28000, 29999, 128)):
        for start in range(lo, hi+1, step):
            yield start, min(hi, start+step-1)


def product(rank, degree):
    return prod(F(D+degree)-F(i*(degree-1), rank-1) for i in range(rank))


def box(J0, J1, t, b0, b1):
    M, ell = J0+D, 11-t
    h1 = F(J1-3, 8)
    ds = [max(C+i, M-(10-i)*(J0-3)//8) for i in range(t)]
    if not all(x > b1 for x in ds):
        raise ValueError("positive factors")
    degree0, degree1 = J0-b1, J1-b0
    hq = min(degree1-ell+1, (t+1)*h1-b0)
    if not (ell <= degree0 <= degree1 and (ell*ell//4)*hq <= D+degree0):
        raise ValueError(("balanced quotient gate", J0, J1, t, b0, b1))
    outside = (M-b1)*prod(max(D+ell-i, M-(t+i)*(J0-3)//8)
                          for i in range(1, ell))
    quote = max(outside, product(ell, degree0))
    base = prod(x-b1 for x in ds)
    inner = F(base)
    for calibration in range(6):
        previous, coefficients = F(0), []
        for i in range(1, t+1):
            q = (max(b0-i*(J1-3)//8, 0) if calibration == 5
                 else F(calibration*b1, 4))
            vals = [x-q for x in ds[:t-i]]
            derivative = sum(prod(vals[k] for k in range(len(vals)) if k != v)
                             for v in range(len(vals)))
            coefficients.append(comb(11, i)*(prod(vals)+q*derivative)-previous)
            previous = comb(11, i)*derivative
        tail = coefficients[-1]
        for i in range(t-1, 0, -1):
            ratio = max(b0-i*(J1-3)//8, 0) if tail >= 0 else b1-i
            tail = coefficients[i-1]+ratio*tail
        inner = max(inner, base+tail*(b0 if tail >= 0 else b1))
    if not inner > 0:
        raise ValueError("positive inner count")
    return 12*quote*inner


def main():
    overall, count, floors = (0, None), 0, 0
    ranges = list(blocks())
    cover_check(ranges)
    digest = hashlib.sha256()
    for lo, hi in ranges:
        resource = prod(R+hi-i for i in range(12))
        costs = [12*product(11, lo),
                 F(10488, 125)*(GAP+lo)*prod(GAP+i for i in range(1, 11))]
        basic = F(resource)/min(costs)
        floor_check(basic.numerator, basic.denominator, int(basic))
        digest.update(f"B:{lo},{hi}:{basic.numerator}/{basic.denominator}\n".encode())
        worst = (int(basic)+NEAR, ("no-flag/HIGH",))
        for t in range(1, 8):
            onset = (8*D+8*(10-t)*(t-1)+3*t*(11-t))//(t*(11-t)-8)+1
            actual_lo = max(lo, onset)
            if actual_lo > hi:
                continue
            bmin = (actual_lo+D+(10-t)*(t-1))//(11-t)+1
            bmax = min(hi-11+t, t*(hi-3)//8)
            if bmin > bmax:
                continue
            step = max(1, (bmax-bmin+8)//8)
            for b0 in range(bmin, bmax+1, step):
                b1 = min(bmax, b0+step-1)
                cost = box(actual_lo, hi, t, b0, b1)
                quotient = F(resource)/cost
                cap = int(quotient)+NEAR
                floor_check(quotient.numerator, quotient.denominator, cap-NEAR)
                for wrong in (cap-NEAR-1, cap-NEAR+1):
                    try:
                        floor_check(quotient.numerator, quotient.denominator, wrong)
                    except ValueError:
                        floors += 1
                    else:
                        raise ValueError("accepted adjacent wrong floor")
                digest.update(f"C:{actual_lo},{hi},{t},{b0},{b1}:{cost.numerator}/{cost.denominator}:{cap}\n".encode())
                count += 1
                if cap > worst[0]:
                    worst = cap, (t, b0, b1)
        need(worst[0] <= TARGET, "every box below declared total")
        if worst[0] > overall[0]:
            overall = worst[0], (lo, hi, worst[1])
    need(count == 2038 and len(ranges) == 78 and floors == 4076, "complete certificate inventory")
    need(overall == (TARGET, (26999, 26999, (7, 23621, 23621))), "declared maximum")
    need(digest.hexdigest() == EXPECTED_DIGEST, "all exact box values")
    need(2130706433**6//2**128-TARGET == 3525562263061, "original budget reserve")
    need(30*(24537-3) <= 8*(24537+D), "old density covers earlier degrees")
    need(TARGET < 274979661975561635, "fits original assembly")
    bad_covers = (ranges[1:], ranges[:-1], ranges+[ranges[-1]],
                  [(24537, ranges[0][1])]+ranges[1:], ranges[:20]+ranges[21:])
    for bad in bad_covers:
        try:
            cover_check(bad)
        except ValueError:
            pass
        else:
            raise ValueError("accepted broken cover")
    print("PASS rational:", count, "flag boxes; 78 degree blocks; 4076 wrong floors; 5 cover mutations")
    print("MAX", overall, "DIGEST", digest.hexdigest(), flush=True)
    print("Original density-qualified source paid; no whole-degree or unrestricted closure")


if __name__ == "__main__":
    main()
