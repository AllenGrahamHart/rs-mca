"""Small exact controls for inside-extension coupling; no field-sized scan."""

from itertools import combinations
from math import comb, factorial, prod


def check(ok, message):
    if not ok:
        raise ValueError(message)


def rank(rows, p):
    if not rows:
        return 0
    a = [[v % p for v in row] for row in rows]
    pivot = 0
    for col in range(len(a[0])):
        target = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if target is None:
            continue
        a[pivot], a[target] = a[target], a[pivot]
        inv = pow(a[pivot][col], -1, p)
        a[pivot] = [x*inv % p for x in a[pivot]]
        for i in range(pivot+1, len(a)):
            mult = a[i][col]
            a[i] = [(x-mult*y) % p for x, y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def falling(n, k):
    return prod(n-i for i in range(k)) if n >= k else 0


def rising(c, k):
    return prod(c+i for i in range(k))


def derivative(c, k):
    return sum(prod(c+i for i in range(k) if i != omitted) for omitted in range(k))


def tail(c, k, y):
    return rising(c-y, k) if y < c or k == 0 else 0


def uniform():
    # F_29 degree-<11 evaluations: all eleven distinct points are a basis.
    s, M, c = 11, 22, 12
    exact = falling(M, s)
    for j in range(1, 5):
        for t in range(j+1):
            P = falling(M-t, s-j)
            full = sum(comb(s, b)*falling(t, b)*falling(M-t, s-b)
                       for b in range(j+1))
            check(full == exact, "uniform inside partition")
            constructed = sum(comb(s, b)*P*falling(t, b)*tail(c, j-b, t-b)
                              for b in range(min(j, t)+1))
            check(constructed == exact, "uniform injective construction")
            lower = P*(tail(c, j, t)+s*rising(c, j-1)*t)
            check(lower <= exact, "uniform coupled lower bound")
    # Two distinct defect coordinates 22,23 with (u,v)=(0,1),(-1,1)
    # give labels 0,1 over a common all-zero core. Independent completed
    # tuples identify their sole noncore coordinate, so they are disjoint.
    check(2*12*exact <= falling(24, 12), "original tuple budget")
    print("PASS: 14 uniform inside counts; completed tuples per label", 12*exact)


def deficient(p, s, K, j, a, zeros, inside, outside):
    ell, M, t = s-j, len(inside)+len(outside), len(inside)
    c = M-K+1
    def evaluate(x):
        G = prod(x-y for y in range(a)) % p
        H = prod(x-y for y in range(zeros)) % p
        return tuple([pow(x, i, p) for i in range(j-1)] + [H]
                     + [G*pow(x, i, p) % p for i in range(ell)])
    core = tuple(inside)+tuple(outside)
    vectors = {x: evaluate(x) for x in range(p)}
    degrees = list(range(j-1))+[zeros]+list(range(a, a+ell))
    check(len(set(degrees)) == s and max(degrees) < K, "actual polynomial carrier")
    check(rank([vectors[x] for x in range(a)], p) == j, "full flat rank")
    check(rank([vectors[x] for x in inside], p) == j-1, "deficient inside rank")
    actual = [0]*(j+1)
    for points in combinations(core, s):
        if rank([vectors[x] for x in points], p) == s:
            actual[sum(x in inside for x in points)] += factorial(s)
    E, Y, R = [], [], []
    for b in range(j+1):
        eb = yb = rb = 0
        for points in combinations(inside, b):
            rows = [vectors[x] for x in points]
            if rank(rows, p) != b:
                continue
            y = sum(rank(rows+[vectors[x]], p) > b for x in inside)
            eb += factorial(b)
            yb += factorial(b)*y
            rb += factorial(b)*tail(c, j-b, y)
        E.append(eb)
        Y.append(yb)
        R.append(rb)
    check(Y == E[1:]+[0], "exact extension-count identity")
    check(K-a == ell, "control has actual zero quotient excess")
    P = falling(len(outside), ell)
    for b in range(j+1):
        check(comb(s, b)*P*R[b] <= actual[b], "injective inside class")
    coupled = s*rising(c, j-1)*t
    for b in range(2, j+1):
        coeff = comb(s, b)*rising(c, j-b)-comb(s, b-1)*derivative(c, j-b+1)
        check(coeff >= 0, "control coefficient sign")
        coupled += coeff*E[b]
    tangent = sum(comb(s, b)*(rising(c, j-b)*E[b]-derivative(c, j-b)*Y[b])
                  for b in range(1, j+1))
    check(coupled == tangent, "coupling before dropping nonnegative terms")
    lower = P*(tail(c, j, t)+s*rising(c, j-1)*t)
    check(0 < lower <= sum(actual), "deficient inside still supplies bases")
    print("DEFICIENT", (p, s, K, j), "ordered classes", actual, "lower", lower)


def main():
    uniform()
    deficient(17, 5, 9, 2, 6, 4, tuple(range(4)), tuple(range(6, 13)))
    deficient(13, 7, 11, 3, 7, 5, tuple(range(5)), tuple(range(7, 13)))
    deficient(17, 9, 12, 4, 7, 6, tuple(range(6)), tuple(range(7, 15)))
    print("PASS: exact small geometry controls; lower-dimensional examples test coupling only")
    print("They do not certify maximum density or the full dimension-eleven theorem")


if __name__ == "__main__":
    main()
