"""Fixed whole-box weighted-collision certificate, with exact streaming digest."""

from fractions import Fraction as F
import hashlib
import importlib.util
from math import prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
D, R, GAP, NEAR = 67466, 1048576, 67472, 134944
LO, HI, TOTAL = 21800, 22499, 274954262108377832
TRIGGER = 274960000000000000
EXPECTED = "b0d340b813df77e827f49d3b4d273c8de17c42214f12e4823ee1d87edc8aaafb"


def load(name, node):
    spec = importlib.util.spec_from_file_location(name, ROOT/node/"verify.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


w = load("weighted_credit", "mca_coordinate_weighted_collision_resource")
root = load("weighted_split_moment", "mca_flat_split_root_moment_basis")
old = load("weighted_old_completion", "rate_half_mca_first_excess_core_interval")
p = w.p


def need(ok, why):
    if not ok:
        raise ValueError(why)


def cover(rows, low, high):
    need(rows and rows[0][0] == low and rows[-1][1] == high
         and all(a <= b for a, b in rows)
         and all(x[1]+1 == y[0] for x, y in zip(rows, rows[1:])),
         "exact disjoint interval cover")


def old_cost(J0, J1, t, a0, a1):
    M, h, ell = D+J0, F(a1, t), 11-t
    k0, k1 = max(ell, J0-a1), J1-a0
    ds = [max(D+1+i, M-(10-i)*a1//t) for i in range(t)]
    caps = {i: i*a1//t for i in range(1, t+1)}
    inner = old.inside(ds, a0, a1, caps)
    if ell == 1:
        quotient = F(D+k0)
    else:
        greedy = (D+k0)*prod(max(D+ell-i, D+k0-i*a1//t) for i in range(1, ell))
        quotient = max(old.quotient(ell, k0, k1, greedy),
                       p.bound(D, k0, k1, ell, min(F(k1-ell+1), h)))
    hybrid = M*prod(max(D+11-r, M-r*a1//t) for r in range(1, 11))
    return max(quotient*inner, hybrid, p.bound(D, J0, J1, 11, h))


def data(J0, J1):
    n0, n1 = R+J0, R+J1
    A = J1-6001
    need(n0 >= 10*(J1-10), "whole-box first branch of source moment cap")
    Tmax = n1*(J1-11)//10
    need(Tmax == w.source_cap(n1, J1, 11), "exact source collision cap")
    credit = w.credit(n0, n1, 12, A, Tmax)
    need(credit > 0, "strictly positive common source weight")
    resource = w.c.falling(n1, 12)
    high = F(10488, 125)*(GAP+J0)*prod(GAP+i for i in range(1, 11))
    return credit, Tmax, resource, high, J1-11+Tmax//2+NEAR


def root_terms(J0, J1, t, a0, a1, credit, Tmax):
    M0, M1, h, ell, k1 = D+J0, D+J1, F(a1, t), 11-t, J1-a0
    mu = p.profile(D, J0, J1, 11, h)
    cmin = F(a0*(a0-1) if t == 1 else 0)
    cmax = min(M1*(h-1), M1*((J1-1)*mu[11]-1), F(Tmax),
               a1*h+min((D+k1)*h, root.moment(D+k1, k1, ell))-M0)
    need(cmin <= cmax, "this certificate excludes no parameter boxes")
    need(J0-h >= 1 and J0-1-cmax/M0 >= 1, "whole convex domain")
    G = p.product(D, J0-h, 10, mu)
    slopes = [prod(1-mu[r] for r in range(i+1, 11)) for i in range(2, 11)]
    lower = F(0)
    for i in range(5):
        point = cmin+F(i, 4)*(cmax-cmin)
        x = J0-1-point/M0
        value, derivative = F(D+1), F(0)
        for slope in slopes:
            factor = D+1+(x-1)*slope
            value, derivative = value*factor, derivative*factor+value*slope
        coefficient = 11*credit*G-derivative
        lower = max(lower, M0*value+point*derivative
                    +coefficient*(cmin if coefficient >= 0 else cmax))
    need(lower > 0, "positive tangent cost")
    return lower, 11*credit*cmin*G, cmin, cmax


def main():
    rows = [(left, min(left+15, HI)) for left in range(LO, HI+1, 16)]
    cover(rows, LO, HI)
    bad = (rows[1:], rows[:-1], rows+[rows[-1]], rows[:7]+rows[8:])
    for broken in bad:
        try:
            cover(broken, LO, HI)
        except ValueError:
            pass
        else:
            raise ValueError("accepted broken degree cover")
    need(84*125*(GAP+1-77) > 10488*(GAP+1) and 22*84 < GAP+1,
         "all-HIGH raw margins retained")
    need(21000 <= LO <= HI <= 52999 and 266180883463176443 < TOTAL
         < TRIGGER < 2130706433**6//2**128, "source alternatives and row budget")
    digest = hashlib.sha256()
    count, used, floors, peak = 0, 0, 0, (0, None)
    ranks = {t: 0 for t in range(1, 11)}
    for J0, J1 in rows:
        credit, Tmax, resource, high, add = data(J0, J1)
        digest.update(f"R:{J0},{J1}:{credit}:{Tmax}:{resource}:{add}\n".encode())
        for t in range(1, 11):
            top = min(J1-11+t, J1-6001 if t == 1 else J1)
            bins = list(old.bins(t, top, 128))
            cover(bins, t, top)
            for a0, a1 in bins:
                lower, bonus, cmin, cmax = root_terms(J0, J1, t, a0, a1, credit, Tmax)
                cost = 12*lower
                if resource//min(cost, high)+add > TRIGGER:
                    cost = max(cost, 12*(old_cost(J0, J1, t, a0, a1)+bonus))
                    used += 1
                cost = min(cost, high)
                ratio = resource/cost
                integer = ratio.numerator//ratio.denominator
                need(integer <= ratio < integer+1, "exact resource floor")
                for wrong in (integer-1, integer+1):
                    need(not wrong <= ratio < wrong+1, "reject adjacent wrong floor")
                    floors += 1
                cap = integer+add
                need(cap <= TOTAL, "all cores in the entire degree box paid")
                digest.update(f"B:{J0},{J1},{t},{a0},{a1}:{cmin}:{cmax}:{lower}:{bonus}:{cost}:{cap}\n".encode())
                if cap > peak[0]:
                    peak = cap, (J0, J1, t, a0, a1)
                count += 1
                ranks[t] += 1
        print("BLOCK", J0, J1, "boxes", count, "running maximum", peak[0], flush=True)
    need(len(rows) == 44 and count == 56320 and floors == 112640
         and set(ranks.values()) == {5632} and used == 12990, "whole finite inventory")
    need(peak == (TOTAL, (22056, 22071, 5, 19554, 19726)), "exact certificate maximum")
    print("CERTIFICATE", peak, "old-used", used, "DIGEST", digest.hexdigest(), flush=True)
    need(digest.hexdigest() == EXPECTED, "frozen every-box digest")
    print("PASS all56320 boxes; no exclusions; common source credit; four broken covers")


if __name__ == "__main__":
    main()
