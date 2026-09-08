"""Exact anchor and all-interval endpoint certificate; no source search."""

from math import isqrt, prod


def check(ok,why):
    if not ok:
        raise ValueError(why)


def ceil_root(n,d):
    k = isqrt(n//d)
    return k+(d*k*k < n)


def main():
    R,d,H,near = 1048576,67472,52999,134944
    N,M,k,sigma = R+4700,d+4700,4699,41
    check(4*20**2*M*M >= sigma*sigma*N*k and 36*k <= sigma*sigma*N,"Johnson gates")
    x,y = ceil_root(sigma*sigma*N*k,4),ceil_root(sigma*sigma*N,4*k)
    z = max(y,(sigma*sigma*N+12*k-1)//(12*k))
    child = 2*x*y*y*z+(N-M+1)*y+z
    check((x,y,z,child)==(1442208,307,31400,8536194661768235),"full child anchor")
    check(2130706433**6 >= 2*R,"same-field padding room")
    J,D = 23000,d-6
    numerator = prod(R+J-i for i in range(12))
    denominator = 12*(D+J)*(D+1)*prod(D+J-4690-i for i in range(1,10))
    low = numerator//denominator
    check(10*(R+J-11)>12*(D+H),"whole-interval derivative")
    check(low <= 161394160592554522,"LOW dominated by proved HIGH quotient")
    for wrong in (low-1,low+1):
        check(not wrong*denominator <= numerator < (wrong+1)*denominator,"wrong floor")
    total = 10*(child+H)+161394160592554522+near
    check(total==246756107210901806 and 2130706433**6//2**128-total==28224620900493281,
          "whole-source total and reserve")
    print("PASS child",child,"LOW",low,"TOTAL",total)
    print("Uniform source class, full children and one near; not every carrier")


if __name__ == "__main__":
    main()
