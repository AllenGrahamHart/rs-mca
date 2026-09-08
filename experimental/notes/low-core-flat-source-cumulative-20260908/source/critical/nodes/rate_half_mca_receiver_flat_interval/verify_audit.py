"""Independent expanded-polynomial and integer-scaled endpoint audit."""

from fractions import Fraction as Q
from math import lcm, prod


R, D, GAP, LO, HI, NEAR = 1048576, 67466, 67472, 45000, 52999, 134944
C = D+1
CHILD = (0, 10755802499540570, 737012707696078, 50371450079970,
         3424826154478, 231038329409)
RANK_MAX = (259673779829962642, 192193469600729520, 198675278016199881,
            214134334318091303, 218501759775600252)


def need(ok, message):
    if not ok:
        raise ValueError(message)


def add(a, b):
    return [(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))]


def mul(a, b):
    result = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def scale(a, x):
    return [x*y for y in a]


def value(a, x):
    result = Q(0)
    for y in reversed(a):
        result = result*x+y
    return result


def derivative(a):
    return [i*a[i] for i in range(1, len(a))]


def compose(a, b):
    result = [Q(0)]
    for y in reversed(a):
        result = add(mul(result, b), [y])
    return result


def same(a, b):
    return not any(add(a, scale(b, -1)))


def exact_floor(num, den, expected):
    need(den > 0 and expected*den <= num < (expected+1)*den, "floor cross products")


def quadratic_basis():
    # Reconstruct the unnormalized basis polynomial, without the supplier's ladder API.
    f = scale(mul([D, 1], [Q(2*D+1, 2), Q(1, 2)]), D+1)
    anchor, end = 5000, 65000
    for rank in range(4, 12):
        need(f[1] >= D*f[2] >= 0, "contraction concavity")
        spike = add(scale([1-rank, 1], value(f, rank-1)),
                    scale(compose(f, [-1, 1]), D+rank-1))
        equal = mul([D, 1], compose(f, [Q(1, rank-1), Q(rank-2, rank-1)]))
        curvature = (D+rank-1)*f[2]
        residual = add(equal, [0, 0, -curvature])
        need(residual[2] >= 0 and residual[3] >= 0, "convex residual")
        slope = value(derivative(residual), anchor)
        intercept = value(residual, anchor)-anchor*slope
        raw = [intercept, slope, curvature]
        shift = max(Q(0), *(value(raw, k)-value(spike, k) for k in (rank, end)))
        following = [intercept-shift, slope, curvature]
        remainder = add([shift], mul(mul([-anchor, 1], [-anchor, 1]),
                                    [residual[2]+2*anchor*residual[3], residual[3]]))
        need(same(add(equal, scale(following, -1)), remainder), "global tangent identity")
        difference = add(spike, scale(following, -1))
        need(difference[2] == 0 and all(value(difference, k) >= 0 for k in (rank, end)),
             "whole affine spike profile")
        need(following[1] >= D*following[2] >= 0, "next contraction gate")
        f = following
    pd = prod(GAP+i for i in range(1, 11))
    need(24*125*value(f, LO) >= (GAP+LO)*pd*10488, "half-HIGH charge")
    need(GAP*f[1] >= f[0] and f[2] >= 0, "whole-J charge monotonicity")


def profile_polynomial(j, r, lam):
    alpha, beta, ell = Q(j, r), j*(1-Q(11, r)), 11-j
    factors = [[D-lam*beta, 1-lam*alpha]]
    for i in range(1, ell):
        if j+i < r:
            factors.append([D-lam*beta-i*beta/j, 1-lam*alpha-i*alpha/j])
        else:
            factors.append([D+(1-lam)*beta+ell-i, (1-lam)*alpha])
    outside = [Q(1)]
    for factor in factors:
        need(factor[1] > 0 and value(factor, LO) > 0, "positive all-J outside factor")
        outside = mul(outside, factor)
    inside = [Q(1)]
    for i in range(j):
        inside = mul(inside, [C+i-lam*beta, -lam*alpha])
    inside = add(inside, scale([lam*beta, lam*alpha], 11*prod(C+i for i in range(j-1))))
    return mul(outside, inside)


def scaled_basis(j, r, kappa, lam):
    a = Q(j*(LO+r-11), r)
    s = lcm((a/j).denominator, a.denominator,
            (kappa*a).denominator, (lam*a).denominator)
    an, tn, zn = int(a*s), int(kappa*a*s), int(lam*a*s)
    need(an % j == 0, "integral scaled density")
    ell = 11-j
    x, e = (LO+D)*s-zn, LO*s-an-ell*s
    outside = x*prod(x-min(e+i*s, i*(an//j)) for i in range(1, ell))
    inside = (prod((C+i)*s-zn for i in range(j))
              +11*prod(C+i for i in range(j-1))*zn*s**(j-1))
    need(outside > 0 and inside > 0 and 0 <= zn <= an < C*s, "positive scaled basis")
    return s, an, tn, outside*inside


def main():
    quadratic_basis()
    need(C >= 100 and HI < C and R+HI > 2*(GAP+HI), "rank-five and child convexity")
    need(29**2*25 > 20*26**2 and C**3-33*C*C-22*C-6 > 0, "signed coupling/log-concavity")
    pd = prod(GAP+i for i in range(1, 11))
    numerator = lambda J: prod(R+J-i for i in range(12))
    resource = 13541615650357694642
    for J in (LO, HI):
        need(numerator(J) <= resource*(GAP+J)*pd, "convex resource endpoints")
    need((resource-1)*(GAP+HI)*pd < numerator(HI), "exact resource ceiling")
    low_num = numerator(LO)*6**5
    low_den = 12*(LO+D)*prod(6*(LO+D)-i*(LO-5) for i in range(1, 6))
    low_den *= prod(D+11-i for i in range(6, 11))
    low_num += NEAR*low_den
    exact_floor(low_num, low_den, 272429083415036159)
    need(7*(R+LO-11) > 24*(D+HI), "whole-J low-density derivative")
    qmax = Q((R+10)*CHILD[1], GAP+10)
    for j in range(1, 6):
        need((R+11-j)*CHILD[j]*qmax.denominator <= (GAP+11-j)*qmax.numerator,
             "maximum uniform child cap")
    high = Q(125*resource, 10488)+qmax/2+Q(HI, 2)+NEAR
    exact_floor(high.numerator, high.denominator, 244960029415389035)
    maxima, count, mutations = [], 0, 0
    for j in range(1, 6):
        answers = []
        for r in range(j, 7):
            alpha, beta = Q(j, r), j*(1-Q(11, r))
            for kappa in (Q(2*j-1, 2*j), Q(1)):
                for lam in (Q(0), 2-Q(1, j)-kappa):
                    p = profile_polynomial(j, r, lam)
                    need(value(derivative(p), HI)*(R+LO-11) > 12*value(p, HI) > 0,
                         "whole-J endpoint log-derivative")
                    need((1-alpha)*GAP-(1-kappa*alpha)*R+beta*(1-kappa) <= 0,
                         "decreasing child profile")
                    s, an, tn, basis_num = scaled_basis(j, r, kappa, lam)
                    need(value(p, LO)*s**11 == basis_num, "independent polynomial/scaled equality")
                    num, den = numerator(LO)*s**11, 12*basis_num
                    cn, cd = ((R+LO)*s-an)*CHILD[j], 2*((GAP+LO)*s-tn)
                    need(cd > 0, "child denominator")
                    total_num = 2*(num*cd+cn*den)+(HI+2*NEAR)*den*cd
                    total_den = 2*den*cd
                    answer = total_num//total_den
                    exact_floor(total_num, total_den, answer)
                    for wrong in (answer-1, answer+1):
                        try:
                            exact_floor(total_num, total_den, wrong)
                        except ValueError:
                            mutations += 1
                        else:
                            raise ValueError("accepted mutated endpoint floor")
                    answers.append(answer)
                    count += 1
        maxima.append(max(answers))
    need(tuple(maxima) == RANK_MAX and count == 80 and mutations == 160, "complete profile inventory")
    need(max(maxima) < 272429083415036159 < 274929007493481160, "whole-source union maximum")
    need(2130706433**6//2**128-272429083415036159 == 2551644696358928, "field reserve")
    print("PASS: independent unnormalized quadratic, expanded polynomials and scaled integer products")
    print("PASS: 80 all-J derivative certificates; 160 off-by-one endpoint mutations rejected")
    print("PASS: per-rank maxima", maxima)
    print("PASS: every-carrier new total 272429083415036159; union total 274929007493481160")
    print("Analytic completeness and universal hand proofs are not certified by finite controls")


if __name__ == "__main__":
    main()
