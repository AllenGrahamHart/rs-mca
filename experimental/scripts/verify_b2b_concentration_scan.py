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
  B  fixed-weight EXHAUSTIVE-all-split MITM window at n=64,t=4, b in [5,10]
     (every (w1,w2) split shape across the halves is searched -- unlike a
     balanced-split-only MITM, this is a genuine in-window certificate);
     64-bit mixed key + exact re-verification of every collision.  Certifies
     the sub-coset-weight weights (b in {5,6,7,9,10}, not mult of M0=8) empty
     (or emits the primitive).
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
# GENUINELY EXHAUSTIVE over ALL split shapes: a weight-b block splits (w1, w2)
# across the two halves with w1 arbitrary in [0, b]; a balanced-split-only MITM
# (the U2-C engine shape) misses unbalanced splits and is only probabilistic
# under random bipartitions.  Here every unordered pair (w1-of-P1, w2-of-P2)
# is covered exactly once: the smaller-count side is fully hashed
# (wh <= bmax/2, tiny), the larger side fully streamed via vectorized
# outer-adds of quarter tables.  A t-null block makes BOTH random linear forms
# of (p_1..p_t) vanish on each side with opposite signs, so its 64-bit mixed
# key matches EXACTLY -- exhaustive-in-window; every key collision is
# re-verified exactly (two independent exact methods must agree).

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

def _quarter_tabs(ca, cb, wmax):
    """Split a half (len m) into two quarters; per quarter per weight j:
       (fa, fb, mask) over all C(m/2, j) subsets (within-half bit positions)."""
    m = len(ca); mq = m // 2
    tabs = []
    for lo in (0, mq):
        tab = {}
        for j in range(0, min(wmax, mq) + 1):
            combos = list(itertools.combinations(range(lo, lo + mq), j))
            k = len(combos)
            fa = np.zeros(k, dtype=np.int64); fb = np.zeros(k, dtype=np.int64)
            mk = np.zeros(k, dtype=np.uint64)
            if j > 0:
                idx = np.asarray(combos, dtype=np.int64)
                fa = ca[idx].sum(axis=1)
                fb = cb[idx].sum(axis=1)
                one = np.uint64(1)
                for c in range(j):
                    mk |= one << idx[:, c].astype(np.uint64)
            tab[j] = (fa, fb, mk)
        tabs.append(tab)
    return tabs[0], tabs[1]

def _enum_weight(tabA, tabB, w, q, chunk=4_000_000):
    """Yield (fa mod q, fb mod q, within-half masks) covering ALL weight-w
       subsets of the half, as outer combinations of the two quarter tables."""
    mq_max = max(tabA.keys())
    for j in range(max(0, w - mq_max), min(w, mq_max) + 1):
        Afa, Afb, Amk = tabA[j]
        Bfa, Bfb, Bmk = tabB[w - j]
        if len(Afa) == 0 or len(Bfa) == 0:
            continue
        step = max(1, chunk // max(1, len(Bfa)))
        for i0 in range(0, len(Afa), step):
            fa = (Afa[i0:i0 + step, None] + Bfa[None, :]) % q
            fb = (Afb[i0:i0 + step, None] + Bfb[None, :]) % q
            mk = (Amk[i0:i0 + step, None] | Bmk[None, :])
            yield fa.ravel(), fb.ravel(), mk.ravel()

def _mix64(fa, fb):
    return fa.astype(np.uint64) * MIX_C1 + fb.astype(np.uint64) * MIX_C2

def window_mitm_allsplit(n, t, q, zeta, bmin, bmax):
    """Exhaustive t-null census restricted to weights b in [bmin, bmax].
       Returns (per_b tallies, hits dict)."""
    half = n // 2
    P1 = list(range(0, half)); P2 = list(range(half, n))
    rng = np.random.default_rng(SEED ^ q)
    wA = [int(rng.integers(1, q)) for _ in range(t)]
    wB = [int(rng.integers(1, q)) for _ in range(t)]
    ca1, cb1 = contrib_forms(P1, n, q, zeta, t, wA, wB)
    ca2, cb2 = contrib_forms(P2, n, q, zeta, t, wA, wB)
    tabs = {0: _quarter_tabs(ca1, cb1, min(bmax, half)),
            1: _quarter_tabs(ca2, cb2, min(bmax, half))}
    # exact power table for fast exact verification (int64-safe: q < 2^20, n<=64)
    Zt = np.array([[pow(zeta, (r * s) % n, q) for r in range(1, t + 1)]
                   for s in range(n)], dtype=np.int64)

    # hash tables: per half, per wh <= bmax//2: sorted NEGATED mixed keys + masks
    wh_max = min(bmax // 2, half)
    hashed = {}
    for h in (0, 1):
        for wh in range(0, wh_max + 1):
            fparts, mparts = [], []
            for fa, fb, mk in _enum_weight(*tabs[h], wh, q):
                fparts.append(_mix64((q - fa) % q, (q - fb) % q))
                mparts.append(mk)
            keys = np.concatenate(fparts); masks = np.concatenate(mparts)
            order = np.argsort(keys, kind='stable')
            hashed[(h, wh)] = (keys[order], masks[order])

    hits = {}   # global support mask (python int) -> verify dict (t-null only)

    def check_candidate(gmask):
        if gmask in hits:
            return
        sup = [i for i in range(n) if (gmask >> i) & 1]
        ps = Zt[sup].sum(axis=0) % q          # exact (no int64 overflow)
        if not np.all(ps == 0):
            return
        v = verify_hit(sup, n, q, zeta, t)    # ground-truth pow() recompute
        assert v['tnull'], (sup, ps)          # two exact methods must agree
        hits[gmask] = v

    # stream: each unordered pair (w1-of-P1, w2-of-P2) covered exactly once.
    # Streaming half h at weight w matches hash tables (1-h, wh) with
    # wh <= w (strict < when h==1, so the tie w1==w2 is handled once at h==0).
    for h in (0, 1):
        shift = 0 if h == 0 else half
        oshift = half if h == 0 else 0
        for w in range(max(1, (bmin + 1) // 2), min(bmax, half) + 1):
            whs = [wh for wh in range(0, wh_max + 1)
                   if (wh < w or (wh == w and h == 0))
                   and bmin <= w + wh <= bmax]
            if not whs:
                continue
            for fa, fb, mk in _enum_weight(*tabs[h], w, q):
                ks = _mix64(fa, fb)
                for wh in whs:
                    keys, masks = hashed[(1 - h, wh)]
                    lo = np.searchsorted(keys, ks, 'left')
                    hi = np.searchsorted(keys, ks, 'right')
                    for si in np.nonzero(lo < hi)[0]:
                        for hidx in range(lo[si], hi[si]):
                            gmask = (int(mk[si]) << shift) | \
                                    (int(masks[hidx]) << oshift)
                            check_candidate(gmask)

    per_b = {}
    for v in hits.values():
        d = per_b.setdefault(v['b'], dict(total=0, coset=0, noncoset=0))
        d['total'] += 1
        d['coset' if v['cls'] == 'coset' else 'noncoset'] += 1
    return per_b, hits

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
TIER_B = (64, 4, [7, 9, 11, 13, 15, 16, 17], (5, 10))
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

def run_tier_B(log, kexps=None):
    n, t, kdefault, (bmin, bmax) = TIER_B
    kexps = kexps if kexps else kdefault
    M0 = least_2power_above(t)
    log(f"\n#### Tier B window: n={n} t={t}  M0={M0}  EXHAUSTIVE all-split "
        f"b in [{bmin},{bmax}] (sub-coset-weight b: {[b for b in range(bmin, bmax+1) if b % M0]})"
        f"  balance log2q={n/t:.2f} ####")
    any_fail = False
    for k in kexps:
        q = prime_1modn_near(n, k)
        g, zeta = get_zeta(q, n)
        log(f"  -- q={q} (~2^{math.log2(q):.2f}) --", )
        per_b, hits = window_mitm_allsplit(n, t, q, zeta, bmin, bmax)
        # positive control: all 8 mu_8-cosets (b=8, split (4,4)) must be found
        ncosets = per_b.get(M0, dict(coset=0))['coset']
        assert ncosets == n // M0, ("coset positive-control", q, ncosets)
        for b in range(bmin, bmax + 1):
            d = per_b.get(b, dict(total=0, coset=0, noncoset=0))
            bmean = math.comb(n, b) / (q ** t)
            log(f"    b={b:2d} ({'<M0 ' if b % M0 else 'cos-w'}): tnull={d['total']:>4} "
                f"coset={d['coset']} noncoset={d['noncoset']:>4} "
                f"b-mean={log2_or(bmean)}")
        nc_win = sum(d['noncoset'] for d in per_b.values())
        nc_subcoset = sum(d['noncoset'] for b, d in per_b.items() if b % M0)
        wmean = sum(math.comb(n, b) for b in range(bmin, bmax + 1)) / (q ** t)
        v, spike, _ = verdict_row(n, nc_win, wmean)
        any_fail = any_fail or spike
        ratio = (f"2^{math.log2(nc_win/wmean):.2f}" if nc_win > 0 else "0")
        log(f"     window noncoset={nc_win} (sub-coset-weight={nc_subcoset}) "
            f"window-mean={log2_or(wmean)} ratio={ratio} verdict={v}")
        # anatomy of any non-coset hits
        shown = 0
        for gm, vv in hits.items():
            if vv['cls'] != 'coset' and shown < 6:
                prof = quotient_profile(gm, n, M0)
                log(f"       nc-anatomy: b={vv['b']} support={vv['support']} "
                    f"profile={prof}")
                shown += 1
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
    _brute_check_windowB()
    print("SELFCHECK PASS: verifier, classifier, census + window engine "
          "consistent (brute-checked).")

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

def _brute_check_windowB():
    """Brute-check the Tier B all-split window engine on n=16, t=2 vs O(2^16)."""
    n, t = 16, 2
    q = prime_1modn_near(n, 7); g, zeta = get_zeta(q, n)
    bmin, bmax = 3, 8
    brute = {}
    for mask in range(1, 1 << n):
        b = popcount(mask)
        if not (bmin <= b <= bmax):
            continue
        S = [i for i in range(n) if (mask >> i) & 1]
        if all(v == 0 for v in power_sums(S, n, q, zeta, t)):
            d = brute.setdefault(b, [0, 0])
            d[0] += 1
            d[1] += 1 if classify(S, n, t) == 'coset' else 0
    per_b, _ = window_mitm_allsplit(n, t, q, zeta, bmin, bmax)
    for b in range(bmin, bmax + 1):
        bt = brute.get(b, [0, 0])
        et = per_b.get(b, dict(total=0, coset=0))
        assert et['total'] == bt[0] and et['coset'] == bt[1], \
            ("windowB brute mismatch", b, et, bt)
    print(f"  brute-check windowB n=16,t=2,q={q}, b in [{bmin},{bmax}]: "
          f"per-b tallies agree with O(2^16) enumeration "
          f"({ {b: v[0] for b, v in sorted(brute.items())} })")

# ------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tier', choices=['A', 'B', 'C', 'all'], default='all')
    ap.add_argument('--kexps', type=int, nargs='*', default=None,
                    help='Tier B only: override the swept log2-q exponents')
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
        any_fail = run_tier_B(log, kexps=args.kexps) or any_fail
    if args.tier in ('C', 'all'):
        any_fail = run_tier_C(log) or any_fail
    verdict = 'FAIL (B2b FALSIFIED at scaled params)' if any_fail else \
              'PASS (no >=2^20 non-coset concentration above balanced mean)'
    log(f"\n==== OVERALL VERDICT: {verdict} ====")
    return 1 if any_fail else 0

if __name__ == '__main__':
    sys.exit(main())
