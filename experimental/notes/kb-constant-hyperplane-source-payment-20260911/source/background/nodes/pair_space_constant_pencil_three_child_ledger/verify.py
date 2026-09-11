"""Small exact controls for maximal constant three-pencils and degree credit."""
import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent/"pair_space_regular_projection_anchor/verify.py"
spec = importlib.util.spec_from_file_location("constant_child_linear_algebra", PATH)
linear = importlib.util.module_from_spec(spec)
spec.loader.exec_module(linear)
P = 97


def need(ok, why):
    if not ok:
        raise ValueError(why)


def value(a, x):
    out = 0
    for c in reversed(a):
        out = (out*x+c) % P
    return out


def product(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j]+x*y) % P
    return out


def field_rank_two(pairs):
    for i, (a, b) in enumerate(pairs):
        for c, d in pairs[:i]:
            if product(a, d) != product(b, c):
                return True
    return False


def child_pairs(pairs, x):
    matrix = [[value(pair[j], x) for pair in pairs] for j in (0, 1)]
    need(len(linear.rref(matrix, P)[1]) == 2, "joint rank two")
    kernel = linear.kernel(matrix, P)
    length = len(pairs[0][0])
    return [tuple(tuple(sum(v[k]*pairs[k][j][i] for k in range(len(pairs))) % P
                        for i in range(length)) for j in (0, 1)) for v in kernel]

def main():
    examples = [
        ([0, 2, -3, 1], [1], 3),
        ([0, 0, -1, 1], [1], 2),
        ([1], [0, 0, 0, 0, 0, 1], 0),
    ]
    checks = 0
    for g, complement, expected_roots in examples:
        scalar = [([0]*j)+g for j in range(3)]
        degree = max(len(complement)-1, len(g)+1)
        length = degree+1
        pad = lambda a: tuple((a[i] if i<len(a) else 0) % P for i in range(length))
        scalar = list(map(pad, scalar))
        g, complement, zero = pad(g), pad(complement), pad([])
        pairs = [(a, zero) for a in scalar]+[(complement, g), (zero, complement)]
        need(len(linear.rref([list(a) for a in scalar+[complement]], P)[1]) == 4,
             "full generic projection already visible at z0")
        roots = []
        for z in range(P):
            matrix = [[(a[i]-z*b[i]) % P for a, b in pairs] for i in range(length)]
            need(5-len(linear.rref(matrix, P)[1]) <= 2, "other constant directions have dimension at most2")
        for x in range(P):
            need(value(g, x) or value(complement, x), "generic kernel component complement-zG is nonzero")
            child = child_pairs(pairs, x)
            need(len(child) == 3, "regular child dimension")
            exceptional = value(g, x) == 0
            need(field_rank_two(child) != exceptional, "exact whole-constant/rank-two split")
            if exceptional:
                need(all(not any(b) for a, b in child), "whole constant direction")
                roots.append(x)
            else:
                evaluated = [[value(a, x) for a in scalar]]
                need(len(linear.kernel(evaluated, P)) == 2, "retained constant plane")
            checks += 1
        need(len(roots) == expected_roots and len(roots) <= degree-2, "distinct roots and primitive degree credit")
    zero = (0,)*4
    basis = [tuple(int(i==j) for i in range(4)) for j in range(4)]
    pairs = [(a, zero) for a in basis]+[(zero, basis[0])]
    for x in range(P):
        child = child_pairs(pairs, x)
        need(len(child)==3 and not field_rank_two(child), "constant4 can make every child constant3")
    print("PASS", checks, "constant3 regular anchors; simple/repeated roots and infinity slack")
    print("PASS 97 constant4 counter-controls; maximum-dimension guard cannot be omitted")
    print("Algebraic controls only; not official MCA sources or universal proofs by sampling")


if __name__ == "__main__":
    main()
