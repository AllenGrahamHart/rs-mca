"""Tiny actual sources test affine offsets, omitted core points and ownership."""

from itertools import combinations, permutations, product
from math import prod


def need(ok, message):
    if not ok:
        raise ValueError(message)


def det(rows, p):
    (a, b, c), (d, e, f), (g, h, i) = rows
    return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)) % p


def main():
    p, K, s, d, T, m = 11, 3, 2, 2, 2, 5
    domain = list(range(p))
    groups = ((list(range(1, 4)), 0, 0),
              (list(range(4, 7)), 1, 1),
              (list(range(7, 11)), 2, 3))
    u, v = {0: 2}, {0: 1}
    for points, A, B in groups:
        for x in points:
            u[x], v[x] = (2+A*x) % p, (1+B*x) % p
    # U=span(X,X^2), a0=2, b0=1; both offsets are outside U.
    Z = [x for x in domain if x == x*x % p == 0 and u[x] == 2 and v[x] == 1]
    need(Z == [0] and len(Z) == K-s, "full auxiliary core and root bound")
    remaining = [x for x in domain if x not in Z]
    up = {x: (u[x]-2)*pow(x, -1, p) % p for x in remaining}
    vp = {x: (v[x]-1)*pow(x, -1, p) % p for x in remaining}
    L, beta = m-len(Z)-T, (s+1)*(m-len(Z)-T)*(d-T+1)
    count, owned_total, omitted, multiplicities = 0, 0, 0, set()
    group_pairs = list(combinations(range(3), 2))
    for flags in product((False, True), repeat=3):
        owners, slopes, mass = {}, set(), 0
        for include_zero, (left, right) in zip(flags, group_pairs):
            core, A, B = groups[left]
            other, C, E = groups[right]
            gamma = (A-C)*pow((E-B) % p, -1, p) % p
            alpha = (A+gamma*B) % p
            need(gamma not in slopes, "original distinct finite labels")
            slopes.add(gamma)
            support = core[:3]+other[:1 if include_zero else 2]+([0] if include_zero else [])
            need(len(support) == m, "original support size")
            need(all((u[x]+gamma*v[x]-2-gamma-alpha*x) % p == 0
                     for x in support), "original scalar agreement")
            defects = [x for x in support if (v[x]-1-B*x) % p]
            tau = len(defects)
            actual = min(sum((v[x]-1-c*x-e*x*x) % p != 0 for x in support)
                         for c, e in product(range(p), repeat=2))
            need(actual == tau and 1 <= tau <= T, "actual full-carrier minimum")
            multiplicities.add(tau)
            mass += tau
            omitted += not include_zero
            need(not set(defects).intersection(Z), "no deleted defect")
            chosen = [x for x in support if x not in Z and x not in defects][:L]
            need(len(chosen) == L and all(vp[x] == B and up[x] == A for x in chosen),
                 "enough divided joint points even when support omitted Z")
            local = set()
            for basis in permutations(chosen, s):
                need((basis[1]-basis[0]) % p != 0, "independent divided core evaluations")
                for defect in defects:
                    for position in range(s+1):
                        xs = basis[:position]+(defect,)+basis[position:]
                        need(xs not in local, "recoverable inserted defect")
                        local.add(xs)
                        need(det([(vp[x], 1, x) for x in xs], p) != 0, "independent incidence tuple")
                        need(all((up[x]+gamma*vp[x]-alpha) % p == 0 for x in xs),
                             "same original label satisfies divided equations")
                        need(xs not in owners, "different labels cannot own one independent tuple")
                        owners[xs] = gamma
            need(len(local) == tau*beta, "all weighted insertions retained")
        need(len(owners) == mass*beta <= prod(range(len(remaining)-s, len(remaining)+1)),
             "one common tuple resource")
        owned_total += len(owners)
        count += 1
    need(multiplicities == {1, 2} and omitted == 12, "both multiplicities and omitted-core cases")
    need(det([(0, 0, 0), (0, 1, 1), (1, 4, 5)], p) == 0,
         "an uncancelled zero evaluation is not a first basis vector")
    print("PASS", count, "actual affine F11 selections;", omitted, "supports omit Z;",
          owned_total, "independent owned tuples; both defect multiplicities")
    print("Original offsets outside U, all defects preserved; universal proof remains a hand argument")


if __name__ == "__main__":
    main()
