"""Seven exact certificates and tiny actual-support transport controls."""

from fractions import Fraction
from itertools import product
from math import isqrt, prod
from pathlib import Path


R, D = 1048576, 67472
CAPS = (0, 4070947, 63264449, 983145945, 15278131113,
        231038329409, 3424826154478, 50371450079970,
        737012707696078, 10755802499540570,
        156765527508668296, 2283382040940633027)


def ceiling_root(num, den):
    root = isqrt(num // den)
    result = root + (den*root*root < num)
    assert den*(result-1)**2 < num <= den*result**2
    return result


def check_certificates():
    text = Path(__file__).with_name("certificates.md").read_text()
    counts = [0, 0]
    for line in text.splitlines():
        cells = [s.strip() for s in line.split("|")]
        if len(cells) not in (6, 9) or not cells[1].isdigit():
            continue
        values = list(map(int, cells[1:-1]))
        if len(values) == 7:
            s, k, t, x, y, z, j = values
            n, a, degree, sigma = R+k, D+k, k-1, 2*t+1
            assert 4*t*t*a*a >= sigma*sigma*n*degree
            assert x == ceiling_root(sigma*sigma*n*degree, 4)
            assert y == ceiling_root(sigma*sigma*n, 4*degree)
            assert z == max(y, (sigma*sigma*n+12*degree-1)//(12*degree))
            assert j == 2*x*y*y*z+(n-a+1)*y+z
            endpoint = (R+k+1)*CAPS[s-1]//(D+k+1)
            assert endpoint >= max(j, CAPS[s-1])
            assert CAPS[s] == endpoint+R-k
            counts[0] += 1
        else:
            s, endpoint, allowance, cap = values
            k = R-allowance
            assert endpoint == (R+k+1)*CAPS[s-1]//(D+k+1)
            assert endpoint+allowance == cap == CAPS[s]
            counts[1] += 1
    assert counts == [7, 7]
    for s in (2, 3, 4):
        assert CAPS[s] == (R+s)*CAPS[s-1]//(D+s)
    assert all(x <= y for x, y in zip(CAPS, CAPS[1:]))


def evaluate(poly, x, p):
    value = 0
    for c in reversed(poly):
        value = (value*x+c) % p
    return value


def contained(domain, values, k, p):
    if len(domain) <= k:
        return True
    for x, value in zip(domain[k:], values[k:]):
        interpolated = 0
        for i, xi in enumerate(domain[:k]):
            term = values[i]
            for j, xj in enumerate(domain[:k]):
                if i != j:
                    term = term*(x-xj)*pow(xi-xj, -1, p) % p
            interpolated += term
        if interpolated % p != value:
            return False
    return True


def bad_record(domain, k, threshold, u, v, gamma, poly, p):
    support = tuple(i for i, x in enumerate(domain)
                    if (u[i]+gamma*v[i]-evaluate(poly, x, p)) % p == 0)
    if len(support) < threshold:
        return None
    points = tuple(domain[i] for i in support)
    if all(contained(points, tuple(w[i] for i in support), k, p) for w in (u, v)):
        return None
    return support


def records(domain, k, threshold, u, v, polynomials, p):
    out = {}
    for gamma in range(p):
        for poly in polynomials:
            support = bad_record(domain, k, threshold, u, v, gamma, poly, p)
            if support is not None:
                out[gamma] = (poly, support)
                break
    return out


def controls():
    p = 7
    domain = (0, 1, 2, 3)
    u, v = (0, 0, 1, 1), (0, 1, 2, 4)
    original = records(domain, 1, 2, u, v, [(c,) for c in range(p)], p)
    assert original
    added = (4, 5)
    weights = [prod(x-t for t in added) % p for x in domain]
    padded_u = tuple(w*x % p for w, x in zip(weights, u))+(0, 0)
    padded_v = tuple(w*x % p for w, x in zip(weights, v))+(0, 0)
    for gamma, (poly, support) in original.items():
        c = poly[0]
        lifted = (20*c % p, -9*c % p, c)
        new_support = bad_record(domain+added, 3, 4, padded_u, padded_v,
                                 gamma, lifted, p)
        assert new_support is not None
        assert set(new_support) == set(support) | {4, 5}
        assert [padded_u[i]*pow(weights[i], -1, p) % p for i in range(4)] == list(u)
        assert [padded_v[i]*pow(weights[i], -1, p) % p for i in range(4)] == list(v)

    # A common zero can contribute a genuinely lost bad slope.
    domain = tuple(range(6))
    u, v = (0, 0, 0, 0, 4, 3), (1, 1, 2, 3, 4, 5)
    polys = [(0, a, b) for a, b in product(range(p), repeat=2)]
    original = records(domain, 3, 4, u, v, polys, p)
    assert set(original) == {0}
    child_u = tuple(u[x]*pow(x, -1, p) % p for x in domain[1:])
    child_v = tuple(v[x]*pow(x, -1, p) % p for x in domain[1:])
    child = records(domain[1:], 2, 3, child_u, child_v,
                    list(product(range(p), repeat=2)), p)
    assert not child and child_v == (1,)*5
    return len(original)


def consumers():
    budget = 2130706433**6//2**128
    assert CAPS[10]+2*D == 156765527508803240 < budget
    assert budget-CAPS[10]-2*D == 118215200602591847
    assert CAPS[11] > budget
    k, s = 255000, 11
    n, m, h = R+k, D+k, k-s+2
    balanced = Fraction(n*(2*n-h), m*(2*m-h))
    spike = Fraction(R+s-1, D+s-1) + Fraction((R+s-1)*(R-D), m*(m-1))
    assert balanced == Fraction(383277578467, 15718615477)
    assert spike == Fraction(11153988094749115, 438581833089399) > balanced
    exact = spike*CAPS[9]
    main = exact.numerator//exact.denominator
    assert main == 273540953997732057
    total = main+R+2*D
    assert total == 273540953998915577 < budget
    assert budget-total == 1439774112479510
    assert R-k == 793576 and 424999-254999 == 170000
    assert 70921548248995035 < 10**17


if __name__ == "__main__":
    check_certificates()
    controls()
    consumers()
    print("PASS: seven fixed Johnson gates and all endpoint/exception constants")
    print("PASS: actual padding and universal-zero return; nonuniversal loss-one counterexample")
    print("PASS: stronger rank-eleven payment and 170000-value rank-twelve interval reduction")
