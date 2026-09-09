"""Independent integer endpoint and common-denominator check."""


def need(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    numerators, denominators, separate = [], [], []
    for t in (1, 2):
        pnum, pden = 798577, 67474-t
        hnum, hden = 1027079, 45975-t
        cnum, cden = 548576, 67473-t
        need(cnum >= cden > 0 and cnum*pden <= pnum*cden, "constant pencil envelope")
        need(hnum*pden*pden <= hden*pnum*pnum, "rank-two step fits two pencil powers")
        pair_num, pair_den = hnum*pnum**9, hden*pden**9
        separate.append(pair_num//pair_den)
        numerators.append((981104+t)*pair_num)
        denominators.append(t*(t+1)*pair_den)
    a, b = denominators
    denominator = 3*a*b
    numerator = 613022127444579907*a*b+3*numerators[0]*b+3*numerators[1]*a
    branch = numerator//denominator+134944
    need(separate == [101805808190, 101821603501] and branch == 270931433891625928,
         "independent pair and branch floors")
    total = max(branch, 274136923022229951, 274138707278280353)
    need(total == 274138707278280353 and 274980728111395087-total == 842020833114734,
         "previous source alternatives are retained")
    need(total > branch, "strong branch is not the universal source cap")
    print("PASS independent integer pencil gates and exact pair-to-slope denominator")
    print("PASS whole-source maximum", total, "rather than overclaiming branch", branch)
    print("No primary imports; hereditary sections and source normalization require their hand proofs")


if __name__ == "__main__":
    main()
