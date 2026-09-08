"""Tiny all-candidate joint-list checks and an MCA ownership counterexample."""

from fractions import Fraction
from itertools import product

from compiler import compile_cap


def verify():
    p, domain = 5, tuple(range(5))
    tested, candidates = 0, 0
    for arity in (1, 2, 3):
        for basis in ((lambda x: 1, lambda x: x), (lambda x: x,), ()):
            s = len(basis)
            bound = compile_cap(3, 1, 2, s)[0]
            sources = [
                tuple(tuple(0 for _ in domain) for _ in range(arity)),
                tuple(tuple((x * (j + 1) if x < 3 else j + 1) % p for x in domain) for j in range(arity)),
                tuple(tuple((x*x+j*x+int(x == 0)) % p for x in domain) for j in range(arity)),
            ]
            for source in sources:
                count = 0
                for coefficients in product(range(p), repeat=arity*s):
                    candidates += 1
                    agreement = sum(all(sum(coefficients[j*s+i] * basis[i](x) for i in range(s)) % p == source[j][x]
                                        for j in range(arity)) for x in domain)
                    count += agreement >= 3
                assert count <= bound, (arity, s, count, bound)
                tested += 1
    # The actual two-pair F_17 family defeats using e=n-|U| without a relation charge.
    n, k, m, t = 12, 3, 7, 3
    u = [0]*6 + list(range(6, 12))
    v = [0]*6 + [16]*6
    union, labels = set(), set()
    for gamma in range(12):
        support = list(range(6, 12)) + [gamma] if gamma < 6 else list(range(6)) + [gamma]
        h = lambda x: (x-gamma) % 17 if gamma < 6 else 0
        assert all((u[x]+gamma*v[x]) % 17 == h(x) for x in support)
        scores = [(sum(v[x] != (b0+b1*x) % 17 for x in support), (b0, b1))
                  for b0, b1 in product(range(17), repeat=2)]
        raw = min(value for value, _ in scores)
        choices = [b for value, b in scores if value == raw]
        assert raw == 1 and len(choices) == 1
        b0, b1 = choices[0]
        core = {x for x in range(n) if v[x] == (b0+b1*x) % 17
                and u[x] == (h(x)-gamma*(b0+b1*x)) % 17}
        assert len(core) == 6 and set(support)-core == {gamma}
        union |= core
        labels.add(gamma)
    resource = Fraction(n*(n-1)*(n-2), m*(m-k+1))
    assert len(union) == n and len(labels) == 12 > resource/(t+1) == Fraction(66, 7)
    # Correct per-pair multiplicity is (n-a_f)/t_f=6, not e/t_f=0.
    assert 2*(n-6) == len(labels)
    print("PASS:", tested, "joint-list sources;", candidates, "tuples exhaustively counted")
    print("Actual MCA cross-core ownership obstruction: 12 > 66/7 despite e=0")


if __name__ == "__main__":
    verify()
