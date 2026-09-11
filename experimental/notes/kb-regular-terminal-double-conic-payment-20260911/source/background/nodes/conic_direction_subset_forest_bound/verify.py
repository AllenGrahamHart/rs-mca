"""Small actual null-line fixtures and exact subset expectation checks."""
from fractions import Fraction as Q
from itertools import combinations

from bounds import averaging_cost, edge_bound, phi, psi


def need(ok, why):
    if not ok:
        raise ValueError(why)


def main():
    p = 101
    points = [(0,0,0),(0,0,1),(0,0,2),(1,-2,1),
              (2,-4,2),(1,0,0),(2,0,0),(1,-2,2)]
    points = [tuple(x % p for x in a) for a in points]
    m = len(points)

    def difference(i, j):
        return tuple((a-b) % p for a,b in zip(points[i], points[j]))

    def null(v):
        a,b,c = v
        return (b*b-4*a*c) % p == 0

    groups = set()
    for i,j in combinations(range(m), 2):
        v = difference(i,j)
        if not null(v):
            continue
        group = []
        for k in range(m):
            w = difference(k,j)
            if all((v[a]*w[b]-v[b]*w[a]) % p == 0 for a,b in combinations(range(3),2)):
                group.append(k)
        groups.add(tuple(group))
    need(any(len(g) >= 3 for g in groups) and len(groups) > 3, "nontrivial line fixture")
    total_subsets = 0
    for s in range(2,m+1):
        edge_sum = 0
        for subset in combinations(range(m),s):
            vertices = set(subset)
            adjacency = {v:set() for v in vertices}
            edges = set()
            for group in groups:
                selected = sorted(vertices.intersection(group))
                for u,v in zip(selected, selected[1:]):
                    need((u,v) not in edges, "line trees share an edge")
                    edges.add((u,v))
                    adjacency[u].add(v)
                    adjacency[v].add(u)
            for u,v,w in combinations(subset,3):
                need(not (v in adjacency[u] and w in adjacency[u] and w in adjacency[v]),
                     "null forest triangle")
                need(len(adjacency[u] & adjacency[v] & adjacency[w]) <= 2,
                     "three-common-neighbour bound")
            need(len(edges) <= edge_bound(s), "actual subset forest bound")
            edge_sum += len(edges)
            total_subsets += 1
        expected = sum(averaging_cost(m,s,len(g)) for g in groups)
        need(Q(edge_sum, len(list(combinations(range(m),s)))) == expected <= edge_bound(s),
             "exact all-subset averaging")
        for r in range(m+1):
            group = set(range(r))
            samples = [max(0,len(group.intersection(a))-1) for a in combinations(range(m),s)]
            need(Q(sum(samples),len(samples)) == averaging_cost(m,s,r), "hypergeometric formula")
    for s in range(6,58):
        need(all(psi(s,Q(d)) <= phi(s,d) for d in range(s)), "convex minorant at integers")
        slopes = [psi(s,Q(d+1))-psi(s,Q(d)) for d in range(s-1)]
        need(slopes == sorted(slopes), "convex slopes")
    expected = {19:61,20:67,22:79,24:92,26:106,27:114,32:153,33:161,40:225,43:256,57:417}
    need(all(edge_bound(s)==k for s,k in expected.items()), "sufficient graph bounds")
    need(averaging_cost(8,3,0)==averaging_cost(8,3,1)==0, "zero-cost singleton cases")
    need(averaging_cost(8,3,4) != Q(3,8)*3, "linear thinning shortcut rejected")
    # A clique on three collinear null points is a triangle, not a line tree.
    clique = set(combinations(range(3),2))
    need(len(clique)==3 > 2, "clique-as-forest countercontrol")
    print("PASS",len(groups),"actual null lines;",total_subsets,"exact subset forests")
    print("PASS hypergeometric expectations, convex minorants and sufficient K_s;",expected)
    print("No official source census; universal null geometry remains a written proof")


if __name__ == "__main__":
    main()
