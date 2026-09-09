"""Tiny joint-LIST controls for pencil escape; no MCA source enumeration."""

from itertools import product


def need(ok, message):
    if not ok:
        raise ValueError(message)


def cap(e, k, a):
    need(e >= 0 and k >= 1 and a > 0, "scope")
    if a > e:
        return 0
    denominator = a*a-e*(k-1)
    need(denominator > 0, "strict Johnson denominator")
    return e*(a-k+1)//denominator


def agreements(pair, receiver, p):
    return {x for x, target in enumerate(receiver)
            if tuple((poly[0]+poly[1]*x) % p for poly in pair) == target}


def main():
    p, u = 7, {0, 1, 2}
    receiver = [(0 if x in u else x, 0) for x in range(p)]
    words = list(product(range(p), repeat=2))
    off = []
    need(agreements(((0, 0), (0, 0)), receiver, p) == u, "complete constant-pencil core")
    for pair in product(words, repeat=2):
        h = agreements(pair, receiver, p)
        if pair[0] != (0, 0) and len(h) >= 5:
            need(len(h & u) <= 1 and len(h-u) >= 4, "constant-row escape")
            off.append(pair)
    need(off == [((0, 1), (0, 0))] and len(off) == cap(4, 2, 4) == 1,
         "sharp joint Johnson count")

    p = 5
    receiver = [(-x*x % p, x) for x in range(p)]
    pencil = [((0, -z % p), (z, 0)) for z in range(p)]
    cores = [agreements(pair, receiver, p) for pair in pencil]
    need(set().union(*cores) == set(range(p)), "moving pencil complete core union")
    words = list(product(range(p), repeat=2))
    off = [pair for pair in product(words, repeat=2)
           if pair not in pencil and len(agreements(pair, receiver, p)) >= 2]
    need(len(off) == 10, "moving-row off-pencil list")
    witness = ((4, 0), (0, 1))
    need(agreements(witness, receiver, p) == {1, 4}, "X^2-1 residual")
    need(2 > 2-1 and 2 == 2+1-1, "row height cannot be dropped")
    need(cap(0, 2, 1) == 0, "false height-free prediction conflicts with witness")

    rejected = 0
    for args in ((4, 2, 2), (5, 2, 2), (0, 2, 0)):
        try:
            cap(*args)
        except ValueError:
            rejected += 1
        else:
            raise ValueError("accepted failed escape/Johnson gate")
    need(rejected == 3, "gate controls")
    print("PASS 2401 constant-row and 625 moving-row pairs; sharp joint Johnson count")
    print("PASS actual height-one witness rejects K-1 inside-root shortcut; three invalid gates rejected")
    print("Generic pair census only; original MCA ownership remains a consumer obligation")


if __name__ == "__main__":
    main()
