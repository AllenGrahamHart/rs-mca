"""Exact rational certificate for a density-restricted source class, not all rows."""

from fractions import Fraction as Q
from math import prod


def need(ok, message):
    if not ok:
        raise ValueError(message)


def verify(low=268913508505087358, high=166836445768446334):
    d, D, R, L, E, near = 67472, 67466, 1048576, 23000, 29999, 134944
    budget = 2130706433**6//2**128
    basis = lambda k: prod(D+k-Q(i*(k-1),10) for i in range(11))
    resource = lambda k: prod(R+k-i for i in range(12))
    lo = Q(resource(L),12)/basis(L)+near
    hi = Q(125*resource(E),(d+L)*prod(d+i for i in range(1,11))*10488)+near
    need(low <= lo < low+1 and high <= hi < high+1, "exact directed floors")
    need(11*(R+L-11) > 24*(D+E), "LOW quotient decreasing over whole interval")
    need(22*84 < d+1 and 84*(d+1-77)*125 > 10488*(d+1), "HIGH weight gate")
    need(11*11//4 == 30 and D==d-6 and near==2*d, "density and one original near")
    need(high < low < 274979661975561635 < budget, "one shared resource, maximum not sum")
    need(budget-low==6067219606307729, "reserve")
    for j,last in ((8,24537),(9,28916),(10,33734)):
        rhs = j*D+330-30*j
        need((30-j)*last <= rhs < (30-j)*(last+1), "exact maximizing-rank boundary")
    spike = (D+11*(25000-10))*prod(D+i for i in range(1,11))
    need(spike < basis(25000), "unguarded full product is false on actual large-fiber space")
    need(30*(25000-10) > D+25000, "counterexample violates density hypothesis")
    print("PASS LOW",low,"HIGH",high,"reserve",budget-low)
    print("PASS whole-interval derivative, HIGH weight, three rank boundaries and guard counterexample")


def main():
    verify()
    for low,high in ((268913508505087357,166836445768446334),
                     (268913508505087359,166836445768446334),
                     (268913508505087358,166836445768446333),
                     (268913508505087358,166836445768446335)):
        try:
            verify(low,high)
        except ValueError:
            continue
        raise ValueError("accepted an adjacent incorrect floor")
    print("PASS four wrong-floor mutations; density is a hypothesis, not a sampled conclusion")


if __name__ == "__main__":
    main()
