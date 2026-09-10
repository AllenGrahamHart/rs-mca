"""Actual F11 sources include a tuple owned by two different bad labels."""

from collections import defaultdict
from itertools import combinations, permutations, product

P = 11


def need(ok, message):
    if not ok:
        raise ValueError(message)


def det(rows):
    (a, b, c), (d, e, f), (g, h, i) = rows
    return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)) % P


def evaluate(poly, x):
    return sum(a*pow(x, i, P) for i, a in enumerate(poly)) % P


def main():
    # V=span(1,X,X^2), U=span(X), v1=1, v2=X^2; K=3,m=6,T=2.
    u, v = {x: 3 for x in range(P)}, {x: 4 for x in range(P)}
    for x in (2, 6, 7, 8):
        u[x], v[x] = 0, 0
    for x in (0, 2, 5, 9):
        u[x], v[x] = (x*x-2*x) % P, (1-6*x) % P
    u[4], v[4] = 0, 7
    records = ((0, 0, 0, 0, (2, 6, 7, 8, 0, 4)),
               (1, -2, -6, 1, (0, 2, 5, 9, 6, 4)))
    owners, actual_bases, mass, inserted = defaultdict(set), [], 0, 0
    for gamma, A, B, t, support in records:
        c = (A+gamma*B) % P
        need(all((u[x]+gamma*v[x]-c*x-t*(x*x+gamma)) % P == 0 for x in support),
             "original scalar agreement")
        defects = [x for x in support if (v[x]-B*x-t) % P]
        core = [x for x in support if x not in defects]
        need(len(core) == 4 and len(defects) == 2, "actual selected defect multiplicity")
        minimum = min(sum(evaluate(poly, x) != v[x] for x in support)
                      for poly in product(range(P), repeat=3))
        need(minimum == 2, "minimizer in the full degree-<3 code")
        need(all(x or (x*x+gamma) % P for x in core), "no moving zero on retained core")
        bases = [xs for xs in permutations(core, 2)
                 if (xs[0]*(xs[1]*xs[1]+gamma)-xs[1]*(xs[0]*xs[0]+gamma)) % P]
        need(len(bases) >= 4*2, "root-flat greedy basis lower bound")
        actual_bases.append(len(bases))
        local = set()
        for basis in bases:
            for defect in defects:
                for position in range(3):
                    xs = basis[:position]+(defect,)+basis[position:]
                    need(xs not in local, "recoverable defect and ordered core basis")
                    local.add(xs)
                    need(det([(v[x]-t, -x, -x*x-gamma) for x in xs]) != 0,
                         "invertible cone-restricted Jacobian")
                    owners[xs].add(gamma)
        need(len(local) == len(defects)*3*len(bases), "all weighted insertions")
        mass += len(defects)
        inserted += len(local)
    need(actual_bases == [12, 10], "nontrivial moving-carrier degeneracy control")
    need(max(map(len, owners.values())) == 2 and owners[(0, 2, 6)] == {0, 1},
         "one-owner shortcut is false")
    unordered = {tuple(sorted(xs)) for xs in owners}
    two_roots = 0
    for xs in unordered:
        roots = [(g, c, t) for g, c, t in product(range(P), repeat=3)
                 if all((g*v[x]-c*x-t*x*x-g*t+u[x]) % P == 0 for x in xs)]
        need(1 <= len(roots) <= 2, "all actual roots of the fixed ambient section")
        two_roots += len(roots) == 2
    need(mass*3*8 <= inserted <= 2*P*(P-1)*(P-2), "common two-label tuple resource")
    # A separate valid record has a moving zero at a genuine joint-core point.
    support = tuple(range(6))
    ve = {x: (0 if x < 4 else x-3) for x in support}
    core = [x for x in support if ve[x] == 0]
    bad_labels = {g for g in range(P) if any(x == 0 and (x*x+g) % P == 0 for x in core)}
    need(bad_labels == {0} and len(bad_labels) <= 3-3+2, "real moving-zero label exception")
    minimum = min(sum(evaluate(poly, x) != ve[x] for x in support)
                  for poly in product(range(P), repeat=3))
    need(minimum == 2, "exceptional record is also full-code bad")
    print("PASS two actual retained F11 records; bases", actual_bases,
          "owned tuples", inserted, "distinct", len(owners), "two-root sections", two_roots)
    print("PASS full polynomial minima; genuine two-owner tuple; one moving-zero exceptional label")
    print("Arbitrary-field line-section and source-accounting proofs remain hand arguments")


if __name__ == "__main__":
    main()
