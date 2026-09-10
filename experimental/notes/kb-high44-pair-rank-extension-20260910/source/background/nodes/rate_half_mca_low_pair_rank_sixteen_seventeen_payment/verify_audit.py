"""Independent integer-ratio reconstruction of both finite rank payments."""

from math import prod


def need(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    cases = ((7, 16, 5, 6, 192166560782635999, 261996525491320703),
             (23, 17, 6, 5, 270933399088173359, 270933399088173359))
    for t, rank, steps, terminal, branch, whole in cases:
        cn, cd = 481076, 67473-t
        pn, pd = (9, 1) if t == 7 else (607203, 67474-t)
        hn, hd = 1027079, 45975-t
        need(cn >= cd > 0 and pn*cd >= cn*pd, "scalar envelopes")
        need(hn*pd*pd <= hd*pn*pn, "hereditary induction gate")
        one_n, one_d = cn**terminal, cd**terminal
        two_n, two_d = hn*pn**(terminal-2), hd*pd**(terminal-2)
        use_two = two_n*one_d > one_n*two_d
        need(use_two == (t == 7), "price BOTH terminal direction ranks")
        numerator, denominator = (two_n, two_d) if use_two else (one_n, one_d)
        for i in range(steps):
            r, s = rank-2*i, 11-i
            need(0 < r-s and r <= 2*s, "joint rank guard")
            c = r-s
            numerator *= 1048576+c
            denominator *= 67472-t+c
        need((rank-2*steps, 11-steps) == (terminal, terminal), "complete anchor chain")
        total_n = 624373932788019251*denominator+t*(981104+t)*numerator
        total_d = (t+1)*denominator
        need(total_n//total_d+134944 == branch, "independent source floor")
        need(max(branch, 261996525491320703) == whole < 274980728111395087, "whole-source maximum")
        need((branch-134944)*total_d <= total_n < (branch-134944+1)*total_d, "adjacent floor gate")
        print("PASS independent P", t, "rank", rank, "source cap", whole)
    # Low pairs are nested, not equal: a P7-rank premise is not a P2-rank premise.
    need(7 < 23 < 44 and 16 < 17 and 22-17 == 5 and 22-18 == 4, "nested surviving ranks")
    print("No primary imports; universal pencil/anchor/source claims remain hand-proof inputs")


if __name__ == "__main__":
    main()
