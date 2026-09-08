"""Independent integer-scaled envelope and elementary-symmetric recurrence."""

from math import factorial, prod


def check(ok,why):
    if not ok:
        raise ValueError(why)


def symmetric(weights,degree):
    coefficients = [1]+[0]*degree
    for w in weights:
        for i in range(degree,0,-1):
            coefficients[i] += w*coefficients[i-1]
    return coefficients[degree]


def main():
    r,d,lo,hi,h,N = 1048576,67472,20481,22999,2048,560
    basis = lambda j: 12*prod(range(d+j-1-10*h,d+j,h))
    # The recurrence reconstructs the uniform-slot symmetric count without comb.
    numerator = factorial(12)*symmetric((1 for _ in range(N)),12)*(r+lo)**12
    denominator = N**12*basis(lo)
    quotient,remainder = divmod(numerator,denominator)
    exceptions,remainder_e = divmod((r+hi)*(h-1),2)
    total = quotient+exceptions+2*d
    check(total == 274545534639685994 and exceptions == 1096757012,
          "independent exact total")
    check(0<=remainder<denominator and remainder_e in (0,1), "both exact floors")
    for wrong in (quotient-1,quotient+1):
        check(not wrong*denominator<=numerator<(wrong+1)*denominator,
              "wrong rational floor")
    check(11*(r+lo)>12*(d+hi-1) and 12*500<d+lo-10*h,
          "whole interval and whole margin guards")
    check(5500*(d+lo)*prod(range(d+1,d+11))>basis(hi), "all HIGH records covered")
    check(2130706433**6//2**128-total == 435193471709093, "reserve")
    weights = [h]*522+[1]
    exact = factorial(12)*symmetric(weights,12)
    cost = basis(lo)
    exceptions = sum(w*(w-1)//2 for w in weights)
    point = exact//cost+exceptions+2*d
    check(point == 272166503326104174, "independent compressed histogram")
    check(sum(weights) == r+lo and len(weights) == 523, "source has no hidden coordinates")
    check(exact*N**12 <= factorial(12)*symmetric((1 for _ in range(N)),12)*(r+lo)**12,
          "concrete source below the relaxed resource")
    check(total<274979661975561635, "original assembly maximum unchanged")
    print("PASS independent total",total,"example",point,"reserve",435193471709093)
    print("Integer products and 13-entry symmetric recurrence; no primary/Fraction import")


if __name__ == "__main__":
    main()
