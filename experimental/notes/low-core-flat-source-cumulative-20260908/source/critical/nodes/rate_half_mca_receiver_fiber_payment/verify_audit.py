"""Independent scaled-integer floors and source-class composition audit."""

from math import prod


def check(ok, message):
    if not ok:
        raise ValueError(message)


def exact_floor(num, den, answer):
    check(den > 0 and answer*den <= num < (answer+1)*den, "exact floor")


def exact_ceil(num, den, answer):
    check(den > 0 and (answer-1)*den < num <= answer*den, "exact ceiling")


def main():
    r, slack, hi, near = 1048576, 67472, 52999, 134944
    n, degree, agreement = 1050576, 1999, 69472
    for num, den, root in ((9*n*degree, 4, 68741), (9*n, 4*degree, 35)):
        check((root-1)**2*den < num <= root**2*den, "ceil square root")
    exact_ceil(9*n, 12*degree, 395)
    check(4*agreement**2 >= 9*n*degree and 4*degree <= n, "Johnson gates")
    child = 66558441820
    check(child == 2*68741*35**2*395+(n-agreement+1)*35+395, "whole child bound")
    numer = lambda j: prod(r+j-i for i in range(12))
    den_resource = lambda j: (slack+j)*prod(slack+i for i in range(1, 11))
    cap = 13541615650357694642
    exact_ceil(numer(hi), den_resource(hi), cap)
    check(numer(14000) <= cap*den_resource(14000), "other convex endpoint")
    exact_floor(125*cap, 10488, 161394160592554522)
    exact_floor(cap, 143, 94696612939564298)
    check(84*(slack+1-77)*125 > 10488*(slack+1), "seven weight")
    check(144*(slack+1-132) > 143*(slack+1), "twelve weight")
    cases = []
    j, gap = 14000, slack-6
    denominator = 12*(gap+j)*(gap+1)*prod(gap+j-1990-i for i in range(1, 10))
    cases.append((numer(j), denominator, 248408193733124448))
    check(10*(r+j-11) > 12*(gap+hi), "near-full whole interval")
    j, gap = 45000, slack-11
    cases.extend((
        (numer(j)*2**9, 12*(gap+j)*(gap+1)*prod(2*gap+j+20-2*i for i in range(1, 10)),
         83217244759090589),
        (numer(j)*2*4**10, 12*(4*gap+3*j)*(2*gap+2+5*j)
         *prod(4*gap+j+40-4*i for i in range(1, 10)), 115346523791651123),
        (numer(j)*2**10, 12*(2*gap+j+10)*(gap+1+5*j-50)
         *prod(2*gap+j+10-2*i for i in range(1, 10)), 24011435147053027),
    ))
    # Check the termwise logarithmic derivative bound at the upper endpoint.
    profiles = (
        [(gap, 1, 1)]+[(2*gap+20-2*i, 1, 2) for i in range(1, 10)],
        [(4*gap, 3, 4)]+[(4*gap+40-4*i, 1, 4) for i in range(1, 10)],
        [(2*gap+10, 1, 2)]+[(2*gap+10-2*i, 1, 2) for i in range(1, 10)],
    )
    for profile in profiles:
        for intercept, slope, denominator in profile:
            check(intercept+slope*j > 0 and denominator > 0, "positive affine factor")
            check(slope*(4*gap+3*hi) >= intercept+slope*hi, "uniform log derivative floor")
    check(10*(r+j-11) > 12*(4*gap+3*hi), "half-size whole interval")
    check(hi-10 < 2*(gap+1), "no light-occupancy kink")
    for num, den, answer in cases:
        exact_floor(num, den, answer)
        for wrong in (answer-1, answer+1):
            try:
                exact_floor(num, den, wrong)
            except ValueError:
                continue
            raise ValueError("accepted incorrect endpoint floor")
    check(10*(child+hi)+cases[0][2]+near == 248408859318207582, "ten disjoint heavy classes")
    check(156765527508668296+hi+cases[2][2]+near == 272112051300507362, "one heavy class")
    check(cases[0][2] > 161394160592554522 and cases[2][2] > 94696612939564298,
          "max of LOW/HIGH, not sum")
    check(52999-9941+1 == 43059, "numerical degree interval is not removed")
    print("PASS: independent integer Johnson, resource, four LOW floors and all-J derivative gates")
    print("PASS: eight endpoint mutations rejected; disjoint heavy/light composition and one near")
    print("Scoped classes only; no original rank bound or unrestricted endpoint")


if __name__ == "__main__":
    main()
