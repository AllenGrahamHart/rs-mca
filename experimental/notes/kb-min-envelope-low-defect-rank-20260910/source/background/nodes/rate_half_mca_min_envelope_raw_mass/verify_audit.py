"""Independent unshifted-degree branch reconstruction; no primary/helper imports."""

from fractions import Fraction as Q
from math import comb, prod

R, GAP, LOW, END = 1048576, 67472, 9941, 21499
FLOORS = {
    9: (578501226347492453, 577632198670483716, 469162745598573006, 360134884494564694),
    44: (581590844909990298, 580716689867229534, 471656010466926030, 362042867686781386),
    150: (591058329359405303, 590168445222317677, 479295814582433859, 367889195256820383),
}


def need(ok, message):
    if not ok:
        raise ValueError(message)


def linear_change(coefficients, a, b):
    return [sum(coefficients[j]*comb(j, i)*a**(j-i)*b**i
                for j in range(i, len(coefficients))) for i in range(len(coefficients))]


def value(coefficients, x):
    return sum(c*x**i for i, c in enumerate(coefficients))


def slope(coefficients):
    return [i*coefficients[i] for i in range(1, len(coefficients))] or [Q(0)]


def difference(first, second, weight=1):
    n = max(len(first), len(second))
    return [(first[i] if i < len(first) else 0)
            - weight*(second[i] if i < len(second) else 0) for i in range(n)]


def positive_on(coefficients, low, high):
    power = linear_change(coefficients, low, high-low)
    degree = len(power)-1
    controls = [sum(power[j]*Q(comb(i, j), comb(degree, j)) for j in range(i+1))
                for i in range(degree+1)]
    return min(controls) >= 0


def tree(cutoff):
    d = GAP-cutoff
    need(11 <= LOW < END <= d, "entire core-degree corridor")
    branches = [[Q(d*(2*d+1), 2*(d+2)), Q(3*d+1, 2*(d+2)), Q(1, 2*(d+2))]]
    count = 0
    for rank in range(4, 12):
        next_level = []
        for q in branches:
            need(value(q, rank-1) == d+rank-1, "common child endpoint")
            first, second = slope(q), slope(slope(q))
            need(positive_on(first, rank-1, END) and positive_on(second, rank-1, END),
                 "branch increasing and convex")
            need(positive_on(difference([2*c for c in first], second, END), rank-1, END),
                 "weighted-fiber concavity gate")
            need(positive_on(difference([2*(rank-2)*c for c in first], second, d+END), rank-1, END),
                 "mixed-branch concavity gate")
            spike = linear_change(q, -1, 1)
            spike[0] -= rank-1
            spike[1] += 1
            transformed = linear_change(q, Q(1, rank-1), Q(rank-2, rank-1))
            equal = [Q(0)]*(len(q)+1)
            for i, c in enumerate(transformed):
                equal[i] += d*c/(d+rank-1)
                equal[i+1] += c/(d+rank-1)
            next_level.extend((spike, equal))
            count += 1
        branches = next_level
    need(count == 255 and len(branches) == 256, "complete unpruned endpoint tree")
    shifted = [linear_change(q, 11, 1) for q in branches]
    for q in shifted:
        need(q[0] == d+11 and min(q) >= 0, "positive final shifted coefficients")
        need(value(slope(q), LOW-11)*(R+LOW-11) > 12*value(q, END-11),
             "each universe/basis quotient decreases throughout J")
        need((GAP+11)*q[1] >= q[0], "each basis/m quotient increases")
    return branches, shifted


def main():
    families, factors = {}, {}
    for cutoff, expected in FLOORS.items():
        original, shifted = tree(cutoff)
        families[cutoff] = shifted
        factor = factors[cutoff] = 12*prod(range(GAP-cutoff+1, GAP-cutoff+11))
        for j, floor in zip((9941, 9965, 14000, 21499), expected):
            unshifted = min(value(q, j) for q in original)
            need(unshifted == min(value(q, j-11) for q in shifted), "degree-coordinate equivalence")
            ratio = Q(prod(R+j-i for i in range(12)), factor)/unshifted
            need(floor <= ratio < floor+1, "independent endpoint floor")
            need(not floor-1 <= ratio < floor and not floor+1 <= ratio < floor+2,
                 "both adjacent wrong floors rejected")
        print("PASS independent core", cutoff, "all four endpoint floors", expected)
    high = 11*151*(GAP+END)*prod(range(GAP+1, GAP+11))
    beta_end = factors[150]*min(value(q, END-11) for q in families[150])
    need(47*beta_end <= high < 48*beta_end, "completed HIGH endpoint gate")
    for cutoff in (9, 44):
        for small, large in zip(families[cutoff], families[150]):
            residual = difference([(cutoff+1)*factors[150]*c for c in large],
                                  small, cutoff*factors[cutoff])
            need(min(residual) >= 0, "coefficientwise paired-branch transfer")
        need(cutoff+1 <= 47, "HIGH covers transferred truncation")
    need(not positive_on([0, 1, -1], 0, 2), "negative-endpoint shape control")
    need(positive_on([1, -2, 1], 0, Q(1, 2)), "nonnegative Bernstein control")
    need(2130706433**6//2**128 == 274980728111395087, "original field budget")
    print("PASS independent 765 input-branch gates and 512 coefficient transfers")
    print("24 adjacent wrong floors rejected; all raw cases need the printed ownership proof")


if __name__ == "__main__":
    main()
