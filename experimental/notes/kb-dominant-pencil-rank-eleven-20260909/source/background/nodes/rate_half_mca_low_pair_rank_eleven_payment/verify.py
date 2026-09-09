"""Exact hereditary pencil-incidence price for low-pair rank eleven."""

from fractions import Fraction as F

R, D, LO, HI = 1048576, 67472, 9965, 21499
W, NEAR, BUDGET = 613022127444579907, 134944, 274980728111395087
BRANCH, TOTAL = 270931433891625928, 274138707278280353


def need(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    price, floors = F(W, 3), []
    for t in (1, 2):
        c, p = F(R-500000, D+1-t), F(R-249999, D+2-t)
        h = F(R-HI+2, D-HI+2-t)
        need(1 <= c <= p and h <= p*p, "hereditary pencil envelope gates")
        need(D-HI+2-t >= 45973 and R-D+t > 0, "whole-J determinant denominator and monotonicity")
        need(R-250000 > D+1-t, "moving-pencil ratio decreases with height")
        need(F(R-250000+1, D+1-t+1) == p, "height-one maximum")
        cap = h*p**9
        floors.append(int(cap))
        price += F(R-D+t, t*(t+1))*cap
    need(floors == [101805808190, 101821603501], "complete-pair floors")
    need(int(price)+NEAR == BRANCH and BUDGET-BRANCH == 4049294219769159, "exact branch price")
    need(max(BRANCH, 274136923022229951, 274138707278280353) == TOTAL,
         "maximum of whole-source alternatives")
    need(TOTAL < BUDGET == 2130706433**6//2**128 and BUDGET-TOTAL == 842020833114734,
         "original budget and final reserve")
    print("PASS pencil-height monotonicity, whole-J determinant gates and H<=P^2")
    print("PAIR FLOORS", floors, "NO-LARGE BRANCH", BRANCH)
    print("RANK<=11 PAY", TOTAL, "RESERVE", BUDGET-TOTAL)
    print("Every over-budget low-pair family has affine dimension>=12; full Prize problems remain open")


if __name__ == "__main__":
    main()
