"""An actual cubic-carrier record and exact line-section/root controls."""

from itertools import permutations, product

P = 11


def need(ok, message):
    if not ok:
        raise ValueError(message)


def evaluate(poly, x):
    return sum(c*pow(x, i, P) for i, c in enumerate(poly)) % P


def rank(rows):
    a = [[v % P for v in row] for row in rows]
    r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = pow(a[r][col], -1, P)
        a[r] = [v*scale % P for v in a[r]]
        for i in range(len(a)):
            if i != r:
                scale = a[i][col]
                a[i] = [(v-scale*w) % P for v, w in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def interpolate(xs, values):
    result = [0]*len(xs)
    for x, value in zip(xs, values):
        poly, denominator = [1], 1
        for y in xs:
            if y != x:
                out = [0]*(len(poly)+1)
                for i, c in enumerate(poly):
                    out[i] = (out[i]-y*c) % P
                    out[i+1] = (out[i+1]+c) % P
                poly, denominator = out, denominator*(x-y) % P
        scale = value*pow(denominator, -1, P)
        result = [(a+scale*b) % P for a, b in zip(result, poly)]
    return result


def main():
    # V=degree<4, L_z(y)=y0+z*y1+z^2*y2, U=span(X^3).
    a, b, gamma = (0, 1, 2, 0), (-1, -2, 0, 0), 1
    support, core, defects = tuple(range(1, 9)), tuple(range(1, 7)), (7, 8)
    u = {x: (evaluate(a, x)-(x in defects)) % P for x in support}
    v = {x: (evaluate(b, x)+(x in defects)) % P for x in support}
    h = [(x+gamma*y) % P for x, y in zip(a, b)]
    need([a[0], a[1]+b[0], a[2]+b[1], b[2]] == [0]*4, "entire pair-line identity")
    need(all((u[x]+gamma*v[x]-evaluate(h, x)) % P == 0 for x in support), "scalar agreements")
    minimum = min(sum(evaluate(c, x) != v[x] for x in support)
                  for c in product(range(P), repeat=4))
    need(minimum == 2, "actual full-degree polynomial minimum")
    moving = lambda x: (x**3, x-gamma, x*x-gamma*gamma)
    bases = [xs for xs in permutations(core, 3) if rank([moving(x) for x in xs]) == 3]
    need(len(bases) >= 6*3*4, "nonzero core greedy lower bound")
    tuples = set()
    for basis in bases:
        for defect in defects:
            for position in range(4):
                xs = basis[:position]+(defect,)+basis[position:]
                need(xs not in tuples, "recoverable defect insertion")
                tuples.add(xs)
                need(rank([(v[x]+3, *(-c for c in moving(x))) for x in xs]) == 4,
                     "invertible moving-hyperplane restricted Jacobian")
    three_roots = 0
    sections = {tuple(sorted(xs)) for xs in tuples}
    for xs in sections:
        ua, vb = interpolate(xs, [u[x] for x in xs]), interpolate(xs, [v[x] for x in xs])
        coefficients = [ua[0], ua[1]+vb[0], ua[2]+vb[1], vb[2]]
        need(any(c % P for c in coefficients), "ambient incidence line is not contained")
        roots = [z for z in range(P) if evaluate(coefficients, z) == 0]
        need(gamma in roots and len(roots) <= 3, "all candidate section roots")
        three_roots += len(roots) == 3
    need(len(tuples) == 2*4*len(bases), "same-resource weighted tuple count")
    need(three_roots > 0, "cubic sections really can have three candidate roots")
    for p in (2, 3, 5, 11):
        exceptions = {(x, g) for x in range(p) for g in range(p)
                      if x**3 % p == (x-g) % p == (x*x-g*g) % p == 0}
        need(exceptions == {(0, 0)}, "unique label at each moving-zero coordinate")
    print("PASS actual F11 raw2 record;", len(bases), "core bases;", len(tuples), "owned tuples")
    print("PASS", len(sections), "sections;", three_roots, "have three candidate roots, not three proved owners")
    print("PASS moving-zero uniqueness in characteristics2,3,5,11; universal proof remains a hand argument")


if __name__ == "__main__":
    main()
