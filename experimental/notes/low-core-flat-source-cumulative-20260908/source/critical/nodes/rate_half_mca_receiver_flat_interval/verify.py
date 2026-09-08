"""Exact factor-form proof certificate for all 80 receiver-flat profiles."""

import importlib.util
from fractions import Fraction as F
from math import prod
from pathlib import Path


R, GAP, LO, HI, NEAR = 1048576, 67472, 45000, 52999, 134944
D, C = GAP-6, GAP-5
CAP, OLD_CAP = 272429083415036159, 274929007493481160
LOW_CAP, HIGH_CAP = 259673779829962642, 244960029415389035
CHILD = (0, 10755802499540570, 737012707696078, 50371450079970, 3424826154478, 231038329409)
W = F(10488, 125)


def need(ok, message):
    if not ok:
        raise ValueError(message)


def numerator(j):
    return prod(R+j-i for i in range(12))


def basis_and_log_derivative(J, j, r, lam):
    alpha, beta = F(j, r), j*(1-F(11, r))
    a, ell = alpha*J+beta, 11-j
    t, x = lam*a, J+D-lam*a
    values, slopes = [x], [1-lam*alpha]
    for i in range(1, ell):
        if j+i < r:
            values.append(x-i*a/j)
            slopes.append(1-lam*alpha-i*alpha/j)
        else:
            values.append(D+(1-lam)*a+ell-i)
            slopes.append((1-lam)*alpha)
    need(all(v > 0 for v in values) and all(v > 0 for v in slopes), "positive affine profile")
    rising = prod(C+i for i in range(j-1))
    g = prod(C+i-t for i in range(j))+11*rising*t
    gp = 11*rising-sum(prod(C+i-t for i in range(j) if i != v) for v in range(j))
    need(0 <= t <= a < C and gp > 0 and g > 0, "coupled inside regime")
    derivative = sum(b/v for b, v in zip(slopes, values))+lam*alpha*gp/g
    return prod(values)*g, derivative


def main():
    path = Path(__file__).resolve().parents[1]/"rate_half_mca_fiber_contraction_interval"/"verify.py"
    spec = importlib.util.spec_from_file_location("contraction_certificate", path)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    a, b, c = old.ladder()
    p, pd = prod(D+i for i in range(1, 11)), prod(GAP+i for i in range(1, 11))
    need(b*GAP >= a and c >= 0, "monotone quadratic/degree ratio")
    need(24*p*(a+b*LO+c*LO*LO) >= (GAP+LO)*pd*W, "every record half-HIGH charge")
    need(HI <= 65000 <= D and LO >= 11, "universal quadratic scope")
    resource = 13541615650357694642
    for J in (LO, HI):
        need(numerator(J) <= resource*(GAP+J)*pd, "convex resource endpoints")
    need(F(numerator(HI), (GAP+HI)*pd) > resource-1, "exact resource ceiling")
    need(84*(1-F(77, GAP+1)) > W and GAP+1 > 12*84, "all HIGH margins")
    h = F(LO-5, 6)
    hybrid = (LO+D)*prod(LO+D-i*h for i in range(1, 6))*prod(D+11-i for i in range(6, 11))
    low_density = F(numerator(LO), 12*hybrid)+NEAR
    need(low_density.__floor__() == CAP, "exact low-density floor")
    need(F(7, 2*(D+HI)) > F(12, R+LO-11), "low-density whole interval")
    need(HI < C and C >= 100 and R+HI > 2*(GAP+HI), "rank-five and convex child gates")
    qmax = F((R+10)*CHILD[1], GAP+10)
    need(all(F((R+11-j)*CHILD[j], GAP+11-j) <= qmax for j in range(1, 6)), "uniform HIGH child cap")
    high = F(resource)/W+qmax/2+F(HI, 2)+NEAR
    need(high.__floor__() == HIGH_CAP, "exact HIGH total")
    records = []
    for j in range(1, 6):
        for r in range(j, 7):
            alpha, beta = F(j, r), j*(1-F(11, r))
            for kappa in (1-F(1, 2*j), F(1)):
                for lam in (F(0), 2-F(1, j)-kappa):
                    basis, _ = basis_and_log_derivative(LO, j, r, lam)
                    _, deriv = basis_and_log_derivative(HI, j, r, lam)
                    need(deriv > F(12, R+LO-11), "whole-J decreasing LOW profile")
                    need((1-alpha)*GAP-(1-kappa*alpha)*R+beta*(1-kappa) <= 0, "decreasing child ratio")
                    size = alpha*LO+beta
                    child = F((R+LO-size)*CHILD[j], GAP+LO-kappa*size)
                    total = F(numerator(LO), 12*basis)+child/2+F(HI, 2)+NEAR
                    need(total < LOW_CAP+1, "uniform low-profile integer bound")
                    records.append((total.__floor__(), j, r, kappa, lam))
    need(len(records) == 80 and max(x[0] for x in records) == LOW_CAP, "80 indexed exact profiles")
    need((LOW_CAP, 1, 4, F(1, 2), F(1, 2)) in records, "attained LOW floor")
    need(max(LOW_CAP, HIGH_CAP) < CAP < OLD_CAP, "max of whole-source alternatives and old union")
    need(2130706433**6//2**128-CAP == 2551644696358928, "original field reserve")
    print("PASS: half-HIGH tuple charge; 80 exact profiles and whole-J derivative gates")
    print("PASS: per-rank LOW maxima", [max(x[0] for x in records if x[1] == j) for j in range(1, 6)])
    print("PASS: LOW-density", CAP, "projected LOW", LOW_CAP, "HIGH", HIGH_CAP)
    print("EVERY normalized J=45000..169999 paid; original transport is downstream")


if __name__ == "__main__":
    main()
