"""Independent integer-scaled endpoint and polynomial-curvature audit."""

from math import gcd, lcm, prod


def check(ok, message):
    if not ok:
        raise ValueError(message)


def rational(n, d=1):
    g = gcd(n, d)
    return n//g, d//g


def le(a, b):
    return a[0]*b[1] <= b[0]*a[1]


def floor_certificate(n, d, proposed):
    check(d > 0 and proposed*d <= n < (proposed+1)*d, "floor certificate")


def endpoint(J, rank, a, t):
    scale = lcm(J[1], a[1]*rank, t[1])
    Jn, an, tn = (x[0]*(scale//x[1]) for x in (J, a, t))
    h, ell = an//rank, 11-rank
    x = Jn+67466*scale-tn
    excess = Jn-an-ell*scale
    prefix = x
    for i in range(1, ell):
        factor = x-min(excess+i*scale, i*h)
        check(factor > 0, "positive quotient factor")
        prefix *= factor
    tail = prod((67467+i)*scale-tn for i in range(rank)) if tn <= 67467*scale else 0
    inside = 11*prod(range(67467, 67467+rank-1))*tn*scale**(rank-1)
    numerator = prod(Jn+(1048576-i)*scale for i in range(12))
    denominator = 12*prefix*(tail+inside)*scale
    value = numerator//denominator
    floor_certificate(numerator, denominator, value)
    try:
        floor_certificate(numerator, denominator, value+1)
    except ValueError:
        pass
    else:
        raise ValueError("accepted off-by-one mutation")
    return value+134944


def polynomial_product(constants):
    coeff = [1]
    for v in constants:
        out = [0]*(len(coeff)+1)
        for i, value in enumerate(coeff):
            out[i] += v*value
            out[i+1] -= value
        coeff = out
    return coeff


def main():
    maxima, count = [], 0
    for rank in range(1, 5):
        values = []
        for profile in range(rank, 6):
            crossing = rational(11*rank+profile*(67467-rank), rank)
            js = {(65000, 1), (169999, 1)}
            if le((65000, 1), crossing) and le(crossing, (169999, 1)):
                js.add(crossing)
            for J in js:
                a = rational(rank*(J[0]+(profile-11)*J[1]), profile*J[1])
                ts = {(0, 1), a}
                if le((67467, 1), a):
                    ts.add((67467, 1))
                for t in ts:
                    values.append(endpoint(J, rank, a, t))
                    count += 1
        # Independently check which outer constant-a endpoints are admissible.
        for J in (65000, 169999):
            if rank*(J-6) <= 5*67467 and 67467 <= J-11+rank:
                check((rank, J) == (1, 169999), "constant-a outer boundary")
                for t in ((0, 1), (67467, 1)):
                    values.append(endpoint((J, 1), rank, (67467, 1), t))
                    count += 1
        maxima.append(max(values))
    expected = [266533517899145497, 244377164689337849,
                244401081788492566, 244417756062852746]
    check(count == 91 and maxima == expected, "complete endpoint table")

    # The low-density profile is scaled by five; numerator degree is twelve,
    # denominator degree eleven. No rational-arithmetic library is used.
    x = 5*(65000+67466)
    hybrid = x*prod(x-i*(65000-6) for i in range(1, 5))
    hybrid *= prod(5*(67466+11-i) for i in range(5, 11))
    numerator = prod(5*(1048576+65000-i) for i in range(12))
    floor_certificate(numerator, 60*hybrid, 253456757626524982-134944)

    l0 = 1113565
    check(14*l0 > 60*(67466+169999), "low-density derivative")
    check(7*l0 > 12*(169999+5*67466+50), "moving t=0 derivative")
    check(7*l0 > 12*(169999+50), "moving t=c derivative")
    check(l0*l0 > 12*(169999+67466)**2, "constant-a curvature")
    check(l0*l0 > 12*169999**2, "linear-g curvature")
    bounds = [(2207258, 1), (4048025, 2), (4048030, 3), (4048035, 4)]
    for j, n, (en, ed) in zip(range(1, 5), (99, 78, 57, 36), bounds):
        coefficients = polynomial_product(range(67467, 67467+j))
        previous = prod(range(67467, 67467+j-1))
        coefficients[1] += 11*previous
        second = 2*coefficients[2] if j > 1 else 0
        check(coefficients[1]**2-coefficients[0]*second >= n*previous**2,
              "independent polynomial curvature")
        check(n*l0*l0*ed*ed > 12*en*en, "whole-piece curvature")

    resource = 23067643444721720934
    for J, ceiling in ((65000, 14024864706947406176), (169999, resource)):
        num = prod(range(1048576+J-11, 1048576+J+1))
        den = (67472+J)*prod(range(67473, 67483))
        check((ceiling-1)*den < num <= ceiling*den, "resource ceiling")
    check(84*(67473-77)*125 > 10488*67473 and 12*84 < 67473, "HIGH proof")
    total = 274929007493481160
    floor_certificate(125*resource, 10488, total-134944)
    check(max(maxima) < total, "one-resource composition")
    check(2130706433**6//2**128-total == 51720617913927, "field reserve")
    print("PASS: 91 scaled-integer endpoints and 91 rejected mutations", maxima)
    print("PASS: polynomial curvature, derivative, resource and field certificates")
    print("Analytic completeness and universal geometry require the hand proofs")


if __name__ == "__main__":
    main()
