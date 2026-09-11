"""Exact polynomial identity and singular rational-curve scope controls."""
from fractions import Fraction as Q
from math import comb, gcd


def need(ok, why):
    if not ok:
        raise ValueError(why)


def coefficients(m, mu):
    d0 = m+2*mu
    return (d0*(mu-1)*(mu-2)+2*m*(d0-3),
            m**3+3*m*m*(mu-1)+m*(3*mu-1)*(mu-2)+3*mu*(mu-1)*(mu-2),
            mu*(m*(m-1)+(mu-2)*(m+mu-1)))


def main():
    # Both sides have separate degrees at most (3,3,2) in (m,mu,h).
    count = 0
    for m in range(4):
        for mu in range(4):
            for h in range(3):
                eta = h+2
                d = m+mu*eta
                lhs = (eta-1)*d*(m+mu-1)*(m+mu-2)-m*(d-2)*(d-3)
                c0,c1,c2 = coefficients(m,mu)
                need(lhs==c0+h*c1+h*h*c2, "polynomial identity")
                count += 1
    prices = 0
    for m in range(1,13):
        for mu in range(2,12):
            need(min(coefficients(m,mu))>=0, "nonnegative decomposition")
            for eta in range(2,10):
                d = m+mu*eta
                need(Q(m*comb(d-2,2),comb(m+mu-1,2))<=(eta-1)*d,
                     "multiplicity price")
                prices += 1
    for powers,expected in (((0,5,7,9),(5,2,2)),((0,1,3,7),(1,2,3))):
        need(gcd(*powers)==1 and max(powers)<97, "birational low-characteristic carrier")
        fixed = min(powers[1:])
        child = [e-fixed for e in powers[1:]]
        mu = gcd(*child)
        eta = max(child)//mu
        need((fixed,mu,eta)==expected and max(powers)==fixed+mu*eta,
             "actual inner divisor and image degree")
    need(Q(5*21,comb(5+2-1,2))==7<=9, "cusp multiplicity price")
    need(5*21//comb(1+2-1,2)==105>9, "branch-only price must fail")
    need(Q(comb(7-2,2),comb(1+2-1,2))==10>7, "eta-minus-one omission must fail")
    print("PASS",count,"tensor-grid identities, exact degrees(3,3,2);",prices,"price controls")
    print("PASS two F97 monomial inner maps; branch-only and eta-factor shortcuts fail")
    print("Multiplicity genus and geometric projection remain written universal proofs")


if __name__ == "__main__":
    main()
