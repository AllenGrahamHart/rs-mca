#!/usr/bin/env python3
r"""
verify_b2b_concentration_scan.py
================================

Balance-point concentration scan / verifier for DAG node b2_modp_giant_extras.
Design + pre-registration: experimental/notes/roadmaps/b2b_balance_concentration_scan.md

QUESTION (B2b, no-concentration form).  At official prize-max rows the count of
NON-coset-union t-null blocks (the finite-field-only "extras"; the char-0 count
is exactly the coset unions -- node b1) is <= n^3 = 2^123 above the balanced
first-moment mean.  Prize-max sits within ~2% of the counting threshold
(t*log2 q ~ n), so counting alone cannot close it.  FALSIFIER: a scaled toy row
near its OWN balance point at which the non-coset count spikes >= 2^20 above the
balanced mean (and >= 2^20 absolute).

FRAME (exact, char q>t; n=2^s, n|q-1).  mu_n={zeta^s}; p_r(S)=sum_{s in S}
zeta^{rs}; t-null <=> p_1=..=p_t=0 mod q.  M0 = least 2-power > t; stride=R=n/M0.
Coset class (= char-0 class, q-independent): supports invariant under +stride;
exactly 2^R - 1 nonempty.  Everything else t-null = a NON-COSET EXTRA (the B2b
quantity).  Balanced mean: E[#non-coset t-null] ~ 2^n/q^t (total), C(n,b)/q^t
(fixed weight).  Balance point: n = t*log2 q.

TIERS
  A  FULL exhaustive census at n=32 (half=16 => full-subset MITM enumerates
     EVERY t-null block; exact, complete), t in {2,3,4}, each swept through its
     own balance point.  <-- the flagship; non-coset counts are EXACT.
  B  fixed-weight exhaustive MITM window at n=64,t=4 (b in [5,16]); 64-bit mixed
     key + exact re-verification of every collision.  Certifies the
     sub-coset-weight window (b in {5,6,7} < M0=8) is empty (or emits a hit).
  C  n=256,t=16 and n=512,t=32 (the prompt's scaled analogues): EXACT coset /
     mean / QA.25-boundary arithmetic + a positive-control coset check.  A
     sampled MITM probe at the minimal weight is included but is falsifier-ONLY
     (coverage ~2^-77; can only catch astronomically large concentration) and
     labeled as such.

Every reported t-null hit is re-verified by direct power-sum recomputation
(power_sums()); the full-subset census key is the EXACT reduced (p_1..p_t)
vector, so a match is exactly t-null (no lossy hash) -- an independent sample is
still re-verified as a guard.  Deterministic (seed below).  Single process,
<~2 GB.  PASS = no >=2^20 non-coset spike above the balanced mean at any q.

Usage:
  python3 verify_b2b_concentration_scan.py --selfcheck
  python3 verify_b2b_concentration_scan.py --tier A
  python3 verify_b2b_concentration_scan.py --tier B
  python3 verify_b2b_concentration_scan.py --tier C
  python3 verify_b2b_concentration_scan.py --tier all
"""
import argparse, itertools, math, sys
from collections import defaultdict
import numpy as np
import sympy

SEED = 20260704
MIX_C1 = np.uint64(0x9E3779B97F4A7C15)
MIX_C2 = np.uint64(0xC2B2AE3D27D4EB4F)

# pre-registered thresholds
SPIKE_FACTOR = 2 ** 20      # non-coset must exceed (mean+1)*this AND ...
SPIKE_ABS = 2 ** 20         # ... this absolute count, to count as a falsifier
def poly_pass_bound(n, mean):   # "small polynomial factor of mean+known"
    return (mean + 1.0) * (n ** 2) + (n ** 3)

# ----------------------------------------------------------- exact primitives
def least_2power_above(t):
    M = 1
    while M <= t:
        M *= 2
    return M

def prime_1modn_near(n, k):
    """Smallest prime q >= 2^k with q % n == 1 (deterministic)."""
    q = 1 << k
    while True:
        if q % n == 1 and sympy.isprime(q):
            return q
        q += 1

def get_zeta(q, n):
    """Deterministic primitive n-th root: least primitive root ^ ((q-1)/n)."""
    g = int(sympy.primitive_root(q))
    zeta = pow(g, (q - 1) // n, q)
    assert pow(zeta, n, q) == 1 and pow(zeta, n // 2, q) != 1
    return g, int(zeta)

def power_sums(S, n, q, zeta, t):
    """GROUND TRUTH p_r(B)=sum_{s in S} zeta^{rs} mod q, r=1..t."""
    out = []
    for r in range(1, t + 1):
        acc = 0
        for s in S:
            acc += pow(zeta, (r * s) % n, q)
        out.append(acc % q)
    return out

def is_coset_union(S, n, stride):
    Sset = set(int(x) % n for x in S)
    return all(((s + stride) % n) in Sset for s in Sset)

def classify(S, n, t):
    M0 = least_2power_above(t)
    return 'coset' if is_coset_union(S, n, n // M0) else 'noncoset'

def verify_hit(S, n, q, zeta, t):
    ps = power_sums(S, n, q, zeta, t)
    return dict(support=sorted(int(x) % n for x in S),
                b=len(set(int(x) % n for x in S)),
                power_sums=ps, tnull=all(v == 0 for v in ps),
                cls=classify(S, n, t))

# bit helpers over Z/n masks
def popcount(x):
    return int(x).bit_count() if hasattr(int, 'bit_count') else bin(x).count('1')

def rot(mask, s, n):
    """cyclic rotation of an n-bit mask by +s (bit i -> bit i+s mod n)."""
    full = (1 << n) - 1
    s %= n
    return ((mask << s) | (mask >> (n - s))) & full

def quotient_profile(mask, n, M0):
    """occupancy of each of the R=n/M0 cosets of mu_M0 (residue mod stride)."""
    stride = n // M0
    prof = [0] * stride
    for i in range(n):
        if (mask >> i) & 1:
            prof[i % stride] += 1
    return tuple(prof)

# ------------------------------------------------------ Tier A: full census
def half_tables(H, n, q, zeta, t):
    """All 2^len(H) subsets of half H: exact (p_1..p_t) tuples V and Z/n masks SM,
       in lockstep mask order.  Built by doubling."""
    V = [(0,) * t]
    SM = [0]
    for s in H:
        c = tuple(pow(zeta, (r * s) % n, q) for r in range(1, t + 1))
        bit = 1 << s
        V = V + [tuple((a + b) % q for a, b in zip(v, c)) for v in V]
        SM = SM + [m | bit for m in SM]
    return V, SM

def census_full(n, t, q, zeta, log, store_cap=64, verify_sample=64):
    """FULL exhaustive t-null census of mu_n via full-subset MITM (n<=~36)."""
    M0 = least_2power_above(t); stride = n // M0; R = n // M0
    half = n // 2
    H1 = list(range(0, half)); H2 = list(range(half, n))
    V1, SM1 = half_tables(H1, n, q, zeta, t)
    V2, SM2 = half_tables(H2, n, q, zeta, t)
    d1 = defaultdict(list)
    for key, sm in zip(V1, SM1):
        d1[key].append(sm)

    total = coset = noncoset = 0
    sig_tally = defaultdict(int)      # (b, antipodal, coset-profile-shape) -> count
    stored = []                        # capped sample of non-coset supports
    fullmask_all = (1 << n) - 1
    rot_s = None
    for v2, sm2 in zip(V2, SM2):
        key = tuple((-x) % q for x in v2)
        lst = d1.get(key)
        if not lst:
            continue
        for sm1 in lst:
            fm = sm1 | sm2
            if fm == 0:
                continue                # exclude empty set
            total += 1
            is_cos = (rot(fm, stride, n) == fm)
            if is_cos:
                coset += 1
            else:
                noncoset += 1
                b = popcount(fm)
                anti = 1 if rot(fm, half, n) == fm else 0
                prof = quotient_profile(fm, n, M0)
                # shape signature: sorted partial-occupancy multiset (0<occ<M0)
                partial = tuple(sorted(x for x in prof if 0 < x < M0))
                sig_tally[(b, anti, partial)] += 1
                if len(stored) < store_cap:
                    stored.append(dict(
                        support=[i for i in range(n) if (fm >> i) & 1],
                        b=b, antipodal=bool(anti), profile=prof))

    # independent re-verification of a deterministic sample of hits
    rng = np.random.default_rng(SEED ^ q)
    checked = badpc = 0
    sample_pool = stored[:]
    # also re-verify some coset positive controls
    for r0 in range(min(stride, verify_sample)):
        S = list(range(r0, n, stride))
        sample_pool.append(dict(support=S))
    for rec in sample_pool[:verify_sample]:
        ps = power_sums(rec['support'], n, q, zeta, t)
        checked += 1
        if any(v != 0 for v in ps):
            badpc += 1

    # positive control: exactly 2^R - 1 nonempty coset unions must be present
    coset_expected = (1 << R) - 1
    return dict(total=total, coset=coset, noncoset=noncoset,
                coset_expected=coset_expected, sig_tally=dict(sig_tally),
                stored=stored, reverified=checked, reverify_bad=badpc,
                M0=M0, R=R)

# --------------------------------------------- Tier B: fixed-weight window MITM
def contrib_forms(exps, n, q, zeta, t, wA, wB):
    ca = np.empty(len(exps), dtype=np.int64)
    cb = np.empty(len(exps), dtype=np.int64)
    for i, s in enumerate(exps):
        a = bb = 0
        for r in range(1, t + 1):
            z = pow(zeta, (r * s) % n, q)
            a += wA[r - 1] * z; bb += wB[r - 1] * z
        ca[i] = a % q; cb[i] = bb % q
    return ca, cb

def _combos(m, k, chunk=2_000_000):
    it = itertools.combinations(range(m), k)
    while True:
        buf = list(itertools.islice(it, chunk))
        if not buf:
            return
        yield np.asarray(buf, dtype=np.int16)

def _mask_from(arr, offset):
    masks = np.zeros(arr.shape[0], dtype=np.uint64)
    one = np.uint64(1)
    for j in range(arr.shape[1]):
        masks |= (one << (arr[:, j].astype(np.uint64) + np.uint64(offset)))
    return masks

def window_mitm(n, t, q, zeta, b_list, log):
    """Exhaustive fixed-weight MITM over 0/1 blocks of mu_n, weights in b_list.
       64-bit mixed key; every collision re-verified exactly."""
    M0 = least_2power_above(t); stride = n // M0
    half = n // 2
    P1 = list(range(0, half)); P2 = list(range(half, n))
    rng = np.random.default_rng(SEED ^ q)
    wA = [int(rng.integers(1, q)) for _ in range(t)]
    wB = [int(rng.integers(1, q)) for _ in range(t)]
    ca1, cb1 = contrib_forms(P1, n, q, zeta, t, wA, wB)
    ca2, cb2 = contrib_forms(P2, n, q, zeta, t, wA, wB)
    per_b = {}
    for b in b_list:
        b1 = b // 2; b2 = b - b1
        hits = {}     # frozenset support -> verify dict (t-null only)

        def do_split(k1, k2):
            # hash side: k1 from P1
            keys_parts, mask_parts = [], []
            for arr in _combos(len(P1), k1):
                fa = ca1[arr].sum(axis=1) % q
                fb = cb1[arr].sum(axis=1) % q
                keys_parts.append((fa.astype(np.uint64) * MIX_C1
                                   + fb.astype(np.uint64) * MIX_C2))
                mask_parts.append(_mask_from(arr, 0))
            keys = np.concatenate(keys_parts); masks = np.concatenate(mask_parts)
            order = np.argsort(keys, kind='stable')
            keys = keys[order]; masks = masks[order]
            for arr in _combos(len(P2), k2):
                fa = ca2[arr].sum(axis=1) % q
                fb = cb2[arr].sum(axis=1) % q
                fan = (q - fa) % q; fbn = (q - fb) % q
                ks = (fan.astype(np.uint64) * MIX_C1 + fbn.astype(np.uint64) * MIX_C2)
                lo = np.searchsorted(keys, ks, 'left')
                hi = np.searchsorted(keys, ks, 'right')
                sm2 = _mask_from(arr, half)
                for si in np.nonzero(lo < hi)[0]:
                    for hidx in range(lo[si], hi[si]):
                        fm = int(masks[hidx]) | int(sm2[si])
                        sup = frozenset(i for i in range(n) if (fm >> i) & 1)
                        if sup in hits:
                            continue
                        v = verify_hit(sup, n, q, zeta, t)   # EXACT re-verify
                        if v['tnull']:
                            hits[sup] = v
        do_split(b1, b2)
        if b1 != b2:
            do_split(b2, b1)
        cos = sum(1 for v in hits.values() if v['cls'] == 'coset')
        non = len(hits) - cos
        per_b[b] = dict(total=len(hits), coset=cos, noncoset=non,
                        sub_coset_weight=(b % M0 != 0))
        log(f"    b={b:2d} ({'<M0' if b % M0 else 'coset-wt'}): "
            f"tnull={len(hits)} coset={cos} noncoset={non}")
    return per_b

# ------------------------------------------- Tier C: exact known + sampled probe
def sampled_probe(n, t, q, zeta, b, K, log):
    """Falsifier-ONLY sampled MITM at fixed weight b (n large). Exact-vector
       match (no lossy hash).  Coverage stated honestly."""
    half = n // 2
    b1 = b // 2; b2 = b - b1
    rng = np.random.default_rng(SEED ^ (q + b))
    Zt = [[pow(zeta, (r * s) % n, q) for r in range(1, t + 1)] for s in range(n)]
    Zt = np.array(Zt, dtype=np.int64)  # (n,t)

    def sample_masks(lo, hi, k, K):
        idx = np.empty((K, k), dtype=np.int64)
        for i in range(K):
            idx[i] = rng.choice(np.arange(lo, hi), size=k, replace=False)
        return idx

    S1 = sample_masks(0, half, b1, K)
    S2 = sample_masks(half, n, b2, K)
    d = defaultdict(list)
    for i in range(K):
        key = tuple(int(x) for x in (Zt[S1[i]].sum(axis=0) % q))
        d[key].append(i)
    hits = 0; examples = []
    for j in range(K):
        v = Zt[S2[j]].sum(axis=0) % q
        key = tuple(int((-x) % q) for x in v)
        for i in d.get(key, ()):
            sup = sorted(set(int(x) for x in S1[i]) | set(int(x) for x in S2[j]))
            vv = verify_hit(sup, n, q, zeta, t)
            if vv['tnull']:
                hits += 1
                if len(examples) < 4:
                    examples.append(vv)
    tot_pairs = math.comb(half, b1) * math.comb(half, b2)
    cov = (K * K) / tot_pairs if tot_pairs else 0.0
    return dict(hits=hits, K=K, coverage=cov, examples=examples,
                cov_log2=(math.log2(cov) if cov > 0 else float('-inf')))

# ------------------------------------------------------------------- reporting
def mean_log2(n, t, q):
    return n - t * math.log2(q)

def verdict_row(n, noncoset, mean):
    """PASS unless a pre-registered spike."""
    spike = (noncoset >= SPIKE_FACTOR * (mean + 1.0)) and (noncoset >= SPIKE_ABS)
    within = noncoset <= poly_pass_bound(n, mean)
    return ('FAIL' if spike else 'PASS'), spike, within

def log2_or(x):
    return f"2^{math.log2(x):.2f}" if x > 0 else "0"

# ------------------------------------------------------------------- Tier drivers
TIER_A = [
    (32, 2, [6, 7, 9, 11, 13, 14, 15, 16, 17, 18, 19]),
    (32, 3, [6, 7, 8, 9, 10, 11, 12, 13, 15, 18]),
    (32, 4, [6, 7, 8, 9, 10, 11, 12, 14, 16]),
]
TIER_B = (64, 4, [6, 7, 8, 9, 10, 11, 12, 15, 16], list(range(5, 17)))
TIER_C = [(256, 16), (512, 32)]

def run_tier_A(log):
    any_fail = False
    for (n, t, kexps) in TIER_A:
        M0 = least_2power_above(t); R = n // M0
        log(f"\n#### Tier A census: n={n} t={t}  M0={M0} R={R} "
            f"coset_unions=2^{R}-1={2**R-1}  balance log2q={n/t:.2f} ####")
        log(f"     {'q':>8} {'log2q':>6} | {'total':>9} {'coset':>6} "
            f"{'noncoset':>9} | {'mean':>9} {'ratio nc/mean':>13} | verdict")
        for k in kexps:
            q = prime_1modn_near(n, k)
            g, zeta = get_zeta(q, n)
            res = census_full(n, t, q, zeta, log)
            assert res['reverify_bad'] == 0, ("re-verify FAILED", n, t, q, res)
            assert res['coset'] == res['coset_expected'], \
                ("coset positive-control mismatch", n, t, q, res['coset'],
                 res['coset_expected'])
            ml2 = mean_log2(n, t, q); mean = 2.0 ** ml2
            nc = res['noncoset']
            v, spike, within = verdict_row(n, nc, mean)
            any_fail = any_fail or spike
            ratio = (f"2^{math.log2(nc/mean):.2f}" if nc > 0 and mean > 0 else
                     ("0" if nc == 0 else "inf"))
            log(f"     {q:>8} {math.log2(q):>6.2f} | {res['total']:>9} "
                f"{res['coset']:>6} {nc:>9} | {log2_or(mean):>9} {ratio:>13} | {v}")
            # anatomy of non-coset extras (top signatures)
            if nc > 0:
                sig = sorted(res['sig_tally'].items(), key=lambda kv: -kv[1])[:4]
                for (b, anti, partial), c in sig:
                    log(f"          nc-anatomy: b={b} antipodal={bool(anti)} "
                        f"partial-occ={partial} count={c}")
    return any_fail

def run_tier_B(log):
    n, t, kexps, b_list = TIER_B
    M0 = least_2power_above(t)
    log(f"\n#### Tier B window: n={n} t={t}  M0={M0}  weights={b_list}  "
        f"(b<M0={[b for b in b_list if b % M0]}) balance log2q={n/t:.2f} ####")
    any_fail = False
    for k in kexps:
        q = prime_1modn_near(n, k)
        g, zeta = get_zeta(q, n)
        log(f"  -- q={q} (~2^{math.log2(q):.2f}) --")
        per_b = window_mitm(n, t, q, zeta, b_list, log)
        nc_win = sum(d['noncoset'] for d in per_b.values())
        nc_subcoset = sum(d['noncoset'] for b, d in per_b.items() if b % M0)
        ml2 = mean_log2(n, t, q)
        # window mean = sum of C(n,b)/q^t over window
        wmean = sum(math.comb(n, b) for b in b_list) / (q ** t)
        v, spike, _ = verdict_row(n, nc_win, wmean)
        any_fail = any_fail or spike
        log(f"     window noncoset total={nc_win} (sub-coset-weight={nc_subcoset}) "
            f"window-mean={log2_or(wmean)} verdict={v}")
    return any_fail

def run_tier_C(log):
    log(f"\n#### Tier C: prompt-scale analogues (EXACT known-class; "
        f"sampled probe is falsifier-only) ####")
    for (n, t) in TIER_C:
        M0 = least_2power_above(t); R = n // M0
        M0qa = 1 << int(math.log2(t)); Rqa = n // M0qa; e = t // M0qa
        q = prime_1modn_near(n, int(round(n / t)))  # near balance
        g, zeta = get_zeta(q, n)
        ml2 = mean_log2(n, t, q)
        coset = (1 << R) - 1
        bnd_log2 = R / 2 - e * math.log2(q)     # QA.25 giant-regime model
        log(f"\n  n={n} t={t}  M0(coset)={M0} R={R} coset_unions=2^{R}-1={coset} "
            f"| balance log2q={n/t:.2f}  q={q}(~2^{math.log2(q):.2f})")
        log(f"    balanced mean 2^n/q^t = 2^{ml2:.2f}   "
            f"(cushion n^3 = 2^{3*math.log2(n):.1f})")
        log(f"    QA.25 boundary model (M0qa={M0qa},Rqa={Rqa},e={e}): "
            f"2^(R/2)/q^e = 2^{bnd_log2:.2f}")
        # positive control: a single mu_M0 coset is t-null
        cosetS = list(range(0, n, R))
        ps = power_sums(cosetS, n, q, zeta, t)
        log(f"    positive-control single mu_{M0} coset t-null: {all(v==0 for v in ps)}")
        # falsifier-only sampled probe at the minimal weight b=t+1
        b = t + 1
        pr = sampled_probe(n, t, q, zeta, b, K=120_000, log=log)
        log(f"    sampled probe b={b}: hits={pr['hits']} K={pr['K']} "
            f"coverage~2^{pr['cov_log2']:.1f}  (falsifier-ONLY; cannot certify absence)")
        if pr['hits']:
            for ex in pr['examples']:
                log(f"       PROBE HIT support={ex['support']} cls={ex['cls']}")
    return False

# ------------------------------------------------------------------- selfcheck
def selfcheck():
    n, t = 32, 2
    q = prime_1modn_near(n, 8); g, zeta = get_zeta(q, n)
    M0 = least_2power_above(t); stride = n // M0
    # coset union t-null & 'coset'
    S = list(range(0, n, stride))
    v = verify_hit(S, n, q, zeta, t)
    assert v['tnull'] and v['cls'] == 'coset', v
    # union of two mu_4 cosets t-null & coset
    S2 = sorted(set(range(0, n, stride)) | set(range(1, n, stride)))
    v2 = verify_hit(S2, n, q, zeta, t)
    assert v2['tnull'] and v2['cls'] == 'coset', v2
    # random small set: not t-null
    v3 = verify_hit([0, 1, 2, 5, 11], n, q, zeta, t)
    assert not v3['tnull'], v3
    # rot/quotient-profile sanity
    mask = 0
    for s in range(0, n, stride):
        mask |= 1 << s
    assert rot(mask, stride, n) == mask
    assert quotient_profile(mask, n, M0) == tuple([M0] + [0] * (stride - 1))
    # full census returns exactly 2^R-1 cosets and re-verifies clean
    res = census_full(n, t, q, zeta, print)
    assert res['reverify_bad'] == 0, res
    assert res['coset'] == (1 << (n // M0)) - 1, (res['coset'], (1 << (n // M0)) - 1)
    # cross-check total against an independent brute count on a TINY case n=8
    _brute_check()
    print("SELFCHECK PASS: verifier, classifier, census consistent (brute-checked).")

def _brute_check():
    """Independent O(2^n) brute enumeration on a tiny case, matched vs census."""
    n, t = 8, 2
    q = prime_1modn_near(n, 6); g, zeta = get_zeta(q, n)
    # brute: all subsets, count t-null and coset
    tot = cos = 0
    M0 = least_2power_above(t); stride = n // M0
    for mask in range(1, 1 << n):
        S = [i for i in range(n) if (mask >> i) & 1]
        if all(v == 0 for v in power_sums(S, n, q, zeta, t)):
            tot += 1
            if is_coset_union(S, n, stride):
                cos += 1
    res = census_full(n, t, q, zeta, lambda *a: None)
    assert res['total'] == tot, ("brute total mismatch", res['total'], tot)
    assert res['coset'] == cos, ("brute coset mismatch", res['coset'], cos)
    print(f"  brute-check n=8,t=2,q={q}: total={tot} coset={cos} "
          f"noncoset={tot-cos} (census agrees)")

# ------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tier', choices=['A', 'B', 'C', 'all'], default='all')
    ap.add_argument('--selfcheck', action='store_true')
    args = ap.parse_args()
    if args.selfcheck:
        selfcheck(); return 0

    def log(m): print(m, flush=True)
    log(f"==== B2b BALANCE-POINT CONCENTRATION SCAN  seed={SEED} ====")
    log(f"PASS = no non-coset spike >= 2^20 above balanced mean at any q.")
    any_fail = False
    if args.tier in ('A', 'all'):
        any_fail = run_tier_A(log) or any_fail
    if args.tier in ('B', 'all'):
        any_fail = run_tier_B(log) or any_fail
    if args.tier in ('C', 'all'):
        any_fail = run_tier_C(log) or any_fail
    verdict = 'FAIL (B2b FALSIFIED at scaled params)' if any_fail else \
              'PASS (no >=2^20 non-coset concentration above balanced mean)'
    log(f"\n==== OVERALL VERDICT: {verdict} ====")
    return 1 if any_fail else 0

if __name__ == '__main__':
    sys.exit(main())
