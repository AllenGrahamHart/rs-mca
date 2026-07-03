#!/usr/bin/env python3
r"""
verify_u2c_falsifier_scan.py
============================

Falsification scan for U2-C (the tame giant-regime dichotomy).
See experimental/notes/roadmaps/u2c_falsifier_scan.md for the design.

U2-C claims: in the tame regime (n a 2-power, D = mu_n coset, n | q-1, q >> n),
every t-null block B (first t power sums zero over F_q) is a disjoint union of
full mu_M-cosets with 2-power M > t.  A *primitive* t-null block (t-null but NOT
such a coset union) at an admissible-shaped toy analogue FALSIFIES U2-C.

KEY REDUCTION (exact, char q > t):
  - mu_n = {zeta^s}, exponents S subset Z/n; p_r(B) = sum_{s in S} zeta^{rs}.
    t-null  <=>  p_1 = ... = p_t = 0  (mod q).
  - Every 2-power subgroup mu_M with M > t contains the smallest one mu_{M0}
    (M0 = least 2-power > t).  So a dictionary block's support S is a union of
    cosets of mu_{M0}, i.e. a union of residue classes mod (n / M0).
    => CLASSIFY: S is 'coset' iff S is invariant under +stride (stride = n/M0);
       else 'primitive' (a falsifier).  Dictionary weights are multiples of M0,
       so any t-null block whose weight is NOT a multiple of M0 is automatically
       primitive.
  - Complement duality: B t-null <=> mu_n\B t-null; weight b <=> n-b.  With the
    BCH min-weight bound (>= t+1) the spectrum is covered by b in [t+1, n/2].

SEARCHES
  (M) trade-level MITM for t-null 0/1 blocks (exhaustive small b, sampled large b);
  (A) sparse-relation / antipodal-lift (X-6 mechanism) in the *prime* field.

Every reported hit is INDEPENDENTLY re-verified (exact power sums recomputed on
the reconstructed support) and reclassified.  PASS = no primitive/falsifier hit
(dichotomy survives at this scale); FAIL = a primitive hit was found & verified.

Deterministic: fixed seed; least-primitive-root zeta.  Single process, <~2 GB.

Usage:
  python3 verify_u2c_falsifier_scan.py --selfcheck
  python3 verify_u2c_falsifier_scan.py --scale 1 --mode sparse
  python3 verify_u2c_falsifier_scan.py --scale 1 --mode mitm --primes 0 \
        --bmax-exh 21 --bmax-samp 32 --nbip 4
  python3 verify_u2c_falsifier_scan.py --scale 2 --mode all --primes 0
"""
import argparse, itertools, math, sys
import numpy as np
import sympy

# ---------------------------------------------------------------- parameters
SCALES = {
    1: dict(n=64,  t=8,  primes=[2147483713, 68719477313, 1099511628161]),
    2: dict(n=128, t=12, primes=[2147483777, 68719484929, 1099511628161]),
}
SEED = 20260703
MIX_C1 = np.uint64(0x9E3779B97F4A7C15)
MIX_C2 = np.uint64(0xC2B2AE3D27D4EB4F)

def least_2power_above(t):
    M = 1
    while M <= t:
        M *= 2
    return M

def get_zeta(q, n):
    """Deterministic primitive n-th root of unity: least primitive root ^ ((q-1)/n)."""
    g = sympy.primitive_root(q)
    zeta = pow(g, (q - 1) // n, q)
    assert pow(zeta, n, q) == 1
    # order exactly n (n a 2-power => suffices to check zeta^(n/2) != 1)
    assert pow(zeta, n // 2, q) != 1
    return int(g), int(zeta)

# ---------------------------------------------------------------- exact verifier
def power_sums(S, n, q, zeta, t):
    """Exact p_r(B) = sum_{s in S} zeta^{rs} mod q, r=1..t.  Ground truth."""
    ps = []
    for r in range(1, t + 1):
        acc = 0
        for s in S:
            acc += pow(zeta, (r * s) % n, q)
        ps.append(acc % q)
    return ps

def is_coset_union(S, n, stride):
    """S invariant under +stride (mod n)  <=>  union of mu_{M0}-cosets."""
    Sset = set(int(x) % n for x in S)
    return all(((s + stride) % n) in Sset for s in Sset)

def classify(S, n, t):
    M0 = least_2power_above(t)
    stride = n // M0
    return 'coset' if is_coset_union(S, n, stride) else 'primitive'

def verify_hit(S, n, q, zeta, t):
    ps = power_sums(S, n, q, zeta, t)
    tnull = all(v == 0 for v in ps)
    return dict(support=sorted(int(x) % n for x in S), b=len(set(int(x) % n for x in S)),
                power_sums=ps, tnull=tnull, cls=classify(S, n, t))

# ---------------------------------------------------------------- MITM machinery
def contrib_forms(part_exps, n, q, zeta, t, wA, wB):
    """For each exponent in part_exps, its two random-linear-form contributions:
       c*(s) = sum_{r=1..t} w*[r] * zeta^{rs} mod q."""
    ca = np.empty(len(part_exps), dtype=np.int64)
    cb = np.empty(len(part_exps), dtype=np.int64)
    for i, s in enumerate(part_exps):
        a = 0; bb = 0
        for r in range(1, t + 1):
            z = pow(zeta, (r * s) % n, q)
            a += wA[r - 1] * z
            bb += wB[r - 1] * z
        ca[i] = a % q
        cb[i] = bb % q
    return ca, cb

COMBO_CACHE = {}
CACHE_CAP = 12_000_000   # cache combos for k with C(m,k) <= this (prime-independent)

def _combo_chunks(m, k, chunk):
    """Yield int16 arrays (rows,k) of all C(m,k) index-combinations.
       Caches the (expensive) itertools generation for small k so it is done
       ONCE per k and reused across primes/bipartitions."""
    total = math.comb(m, k)
    if total <= CACHE_CAP:
        arr = COMBO_CACHE.get((m, k))
        if arr is None:
            flat = np.fromiter(
                itertools.chain.from_iterable(itertools.combinations(range(m), k)),
                dtype=np.int16, count=total * k)
            arr = flat.reshape(total, k)
            COMBO_CACHE[(m, k)] = arr
        for i in range(0, total, chunk):
            yield arr[i:i + chunk]
    else:
        it = itertools.combinations(range(m), k)
        while True:
            buf = list(itertools.islice(it, chunk))
            if not buf:
                return
            yield np.asarray(buf, dtype=np.int16)

def _mask_from(arr):
    # uint64: half-set can have up to 64 elements (n=128 => bit indices 0..63)
    masks = np.zeros(arr.shape[0], dtype=np.uint64)
    one = np.uint64(1)
    for j in range(arr.shape[1]):
        masks |= (one << arr[:, j].astype(np.uint64))
    return masks

def _mix(fa, fb, q):
    return (fa.astype(np.uint64) * MIX_C1 + fb.astype(np.uint64) * MIX_C2)

def mitm_split(P1, P2, ca1, cb1, ca2, cb2, k1, k2, q, sampled=None, rng=None,
               chunk=1_500_000):
    """MITM over subsets: k1 from P1 (hashed), k2 from P2 (streamed).
       Returns list of (support_set) candidate matches (key-collisions; caller verifies).
       sampled: if not None, (K1,K2) random samples per side instead of exhaustive."""
    schunk = min(chunk, 400_000)
    # ---- build hash side (k1 from P1) ----
    keys_parts, mask_parts = [], []
    if sampled is None:
        gen1 = _combo_chunks(len(P1), k1, chunk)
    else:
        gen1 = _sample_chunks(len(P1), k1, sampled[0], rng, schunk)
    for arr in gen1:
        fa = ca1[arr].sum(axis=1) % q
        fb = cb1[arr].sum(axis=1) % q
        keys_parts.append(_mix(fa, fb, q))
        mask_parts.append(_mask_from(arr))
    keys = np.concatenate(keys_parts); masks = np.concatenate(mask_parts)
    del keys_parts, mask_parts
    order = np.argsort(keys, kind='stable')
    keys = keys[order]; masks = masks[order]

    # ---- stream side (k2 from P2), negated forms ----
    cands = []
    if sampled is None:
        gen2 = _combo_chunks(len(P2), k2, chunk)
    else:
        gen2 = _sample_chunks(len(P2), k2, sampled[1], rng, schunk)
    for arr in gen2:
        fa = ca2[arr].sum(axis=1) % q
        fb = cb2[arr].sum(axis=1) % q
        fan = (q - fa) % q; fbn = (q - fb) % q
        ks = _mix(fan, fbn, q)
        lo = np.searchsorted(keys, ks, 'left')
        hi = np.searchsorted(keys, ks, 'right')
        hit = np.nonzero(lo < hi)[0]
        if hit.size == 0:
            continue
        smask = _mask_from(arr)
        for si in hit:
            for hidx in range(lo[si], hi[si]):
                m1 = int(masks[hidx]); m2 = int(smask[si])
                sup = set(P1[i] for i in range(len(P1)) if (m1 >> i) & 1)
                sup |= set(P2[i] for i in range(len(P2)) if (m2 >> i) & 1)
                cands.append(frozenset(sup))
    del keys, masks
    return cands

def _sample_chunks(m, k, K, rng, chunk):
    """Yield K random distinct k-subsets of range(m), vectorized:
       random keys per row, argsort, take first k (guarantees distinctness)."""
    produced = 0
    while produced < K:
        batch = min(chunk, K - produced)
        out = np.argsort(rng.random((batch, m)), axis=1)[:, :k].astype(np.int16)
        produced += batch
        yield out

# ---------------------------------------------------------------- search drivers
def run_mitm(n, t, q, zeta, bmax_exh, bmax_samp, nbip, Ksamp, log, bmin=None):
    rng = np.random.default_rng(SEED ^ q & 0xFFFFFFFF)
    wA = [int(rng.integers(1, q)) for _ in range(t)]
    wB = [int(rng.integers(1, q)) for _ in range(t)]
    all_hits = {}   # frozenset(support) -> verify dict
    HASH_CAP_K = 9  # C(32,9)=28M ; keep hashed side small for memory

    def register(cands):
        for sup in cands:
            if sup in all_hits:
                continue
            v = verify_hit(sup, n, q, zeta, t)
            if v['tnull']:
                all_hits[sup] = v

    half = n // 2
    # bipartitions: canonical first, then random balanced splits
    biparts = [(list(range(0, half)), list(range(half, n)))]
    for _ in range(nbip - 1):
        perm = [int(x) for x in rng.permutation(n)]
        biparts.append((sorted(perm[:half]), sorted(perm[half:])))

    lo_b = bmin if bmin is not None else t + 1
    for b in range(lo_b, min(bmax_samp, half) + 1):
        exhaustive = b <= bmax_exh
        if exhaustive:
            a1 = min(b // 2, HASH_CAP_K)
            a2 = b - a1
            if a2 > 12:
                log(f"  b={b}: EXH split ({a1},{a2}) a2>12 -> skip-exh, sampling")
                exhaustive = False
        if exhaustive:
            cnt_stream = math.comb(half, a2)
            # multi-bipartition only for cheap small weights; big-k weights: canonical only
            use_bip = biparts if cnt_stream <= 4_000_000 else biparts[:1]
            found0 = len(all_hits)
            for (P1, P2) in use_bip:
                ca1, cb1 = contrib_forms(P1, n, q, zeta, t, wA, wB)
                ca2, cb2 = contrib_forms(P2, n, q, zeta, t, wA, wB)
                # search split (a1 in P1, a2 in P2) and mirror (a2 in P1, a1 in P2)
                register(mitm_split(P1, P2, ca1, cb1, ca2, cb2, a1, a2, q))
                if a1 != a2:
                    register(mitm_split(P1, P2, ca1, cb1, ca2, cb2, a2, a1, q))
            log(f"  b={b}: EXH split=({a1},{a2}) bip={len(use_bip)} "
                f"hits_new={len(all_hits)-found0}")
        else:
            a1 = b // 2; a2 = b - a1
            P1, P2 = biparts[0]
            ca1, cb1 = contrib_forms(P1, n, q, zeta, t, wA, wB)
            ca2, cb2 = contrib_forms(P2, n, q, zeta, t, wA, wB)
            found0 = len(all_hits)
            register(mitm_split(P1, P2, ca1, cb1, ca2, cb2, a1, a2, q,
                                sampled=(Ksamp, Ksamp), rng=rng))
            tot = math.comb(half, a1) * math.comb(half, a2)
            cov = (Ksamp * Ksamp) / tot if tot else 0.0
            log(f"  b={b}: SAMP split=({a1},{a2}) K={Ksamp} pairs={Ksamp*Ksamp:.2e} "
                f"cov~{cov:.2e} hits_new={len(all_hits)-found0}")
    return all_hits

def positive_control(n, t, q, zeta, log):
    """The M0-cosets (residue classes mod n/M0) must be verified t-null & 'coset'."""
    M0 = least_2power_above(t); stride = n // M0
    ok = True
    for r0 in range(stride):
        S = list(range(r0, n, stride))
        v = verify_hit(S, n, q, zeta, t)
        good = v['tnull'] and v['cls'] == 'coset' and v['b'] == M0
        ok = ok and good
    log(f"  positive-control: {stride} mu_{M0}-cosets  all t-null & 'coset': {ok}")
    return ok

def run_sparse(n, t, q, zeta, wmax_exh, Ksamp, log):
    """Search sparse vanishing sums  sum_{e in E} zeta^e = 0  in the PRIME field.
       Separate char-0-trivial (antipodal-pair-containing) from PRIMITIVE relations;
       report how many consecutive moments each satisfies; attempt antipodal lift."""
    rng = np.random.default_rng(SEED ^ (q >> 3) & 0xFFFFFFFF)
    Z = np.array([pow(zeta, s, q) for s in range(n)], dtype=np.int64)
    half = n // 2
    prim_relations = []   # primitive first-moment vanishing sums
    triv_count = 0        # char-0-trivial (antipodal-pair-containing) vanishing sums
    total_van = 0

    def has_antipodal(E):
        Es = set(E)
        return any(((e + half) % n) in Es for e in Es)

    def moments_vanishing(E):
        """max r such that sum zeta^{je}=0 for j=1..r (exact)."""
        r = 0
        while r < t:
            j = r + 1
            acc = 0
            for e in E:
                acc += pow(zeta, (j * e) % n, q)
            if acc % q != 0:
                break
            r += 1
        return r

    for w in range(3, 7):
        if w <= wmax_exh:
            gen = _combo_chunks(n, w, 2_000_000)
            mode = 'EXH'; tot = math.comb(n, w)
        else:
            gen = _sample_chunks(n, w, Ksamp, rng, 2_000_000)
            mode = 'SAMP'; tot = math.comb(n, w)
        van_w = prim_w = 0
        for arr in gen:
            s = Z[arr].sum(axis=1) % q
            hit = np.nonzero(s == 0)[0]
            for hi in hit:
                E = [int(x) for x in arr[hi]]
                van_w += 1; total_van += 1
                if has_antipodal(E):
                    triv_count += 1
                else:
                    r = moments_vanishing(E)
                    prim_relations.append((E, r))
                    prim_w += 1
        cov = (Ksamp / tot) if mode == 'SAMP' and tot else 1.0
        log(f"  sparse w={w} [{mode} cov~{cov:.2e}]: vanishing_sums={van_w} "
            f"primitive(non-antipodal)={prim_w}")
    log(f"  sparse totals: vanishing_sums={total_van} "
        f"antipodal-trivial={triv_count} "
        f"PRIMITIVE(non-antipodal)={len(prim_relations)}")
    # X-6 shape probe: does 1 + zeta^s + zeta^{2s} + zeta^{4s} = 0 for some s?
    x6 = [s for s in range(n)
          if (1 + pow(zeta, s % n, q) + pow(zeta, (2 * s) % n, q)
              + pow(zeta, (4 * s) % n, q)) % q == 0]
    log(f"  X-6 shape 1+Y+Y^2+Y^4=0 with Y in mu_{n}: solutions s={x6}")
    # attempt antipodal lift of any primitive relation
    lifts = []
    for (E, r) in prim_relations:
        lift = sorted(set(E) | set((e + half) % n for e in E))
        v = verify_hit(lift, n, q, zeta, t)
        if v['tnull'] and v['cls'] == 'primitive':
            lifts.append((E, lift, v))
    log(f"  antipodal-lift: primitive t-null blocks produced = {len(lifts)}")
    return prim_relations, lifts

# ---------------------------------------------------------------- self-check
def selfcheck():
    n, t, q = 64, 8, 2147483713
    _, zeta = get_zeta(q, n)
    M0 = least_2power_above(t)
    # coset (mod-4 class) is t-null & coset
    S = list(range(0, n, n // M0))
    v = verify_hit(S, n, q, zeta, t)
    assert v['tnull'] and v['cls'] == 'coset', v
    # a random 9-set is (almost surely) not t-null
    v2 = verify_hit([0, 1, 2, 3, 5, 8, 13, 21, 34], n, q, zeta, t)
    assert not v2['tnull'], v2
    # union of two mod-4 classes: t-null & coset
    S2 = sorted(set(range(0, n, 4)) | set(range(1, n, 4)))
    v3 = verify_hit(S2, n, q, zeta, t)
    assert v3['tnull'] and v3['cls'] == 'coset' and v3['b'] == 32, v3
    # a coset shifted-but-broken (drop one, add a non-class point): not coset, and not t-null
    S4 = list(range(0, n, 4))[:-1] + [1]
    v4 = verify_hit(S4, n, q, zeta, t)
    assert v4['cls'] == 'primitive', v4
    print("SELFCHECK PASS: verifier + classifier consistent.")

# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--scale', type=int, default=1)
    ap.add_argument('--mode', choices=['mitm', 'sparse', 'all'], default='all')
    ap.add_argument('--primes', type=int, nargs='*', default=None,
                    help='indices into the scale prime list (default all)')
    ap.add_argument('--bmin', type=int, default=None)
    ap.add_argument('--bmax-exh', type=int, default=None)
    ap.add_argument('--bmax-samp', type=int, default=None)
    ap.add_argument('--nbip', type=int, default=4)
    ap.add_argument('--ksamp', type=int, default=2_000_000)
    ap.add_argument('--wmax-exh', type=int, default=5)
    ap.add_argument('--selfcheck', action='store_true')
    args = ap.parse_args()

    if args.selfcheck:
        selfcheck(); return

    sc = SCALES[args.scale]; n, t = sc['n'], sc['t']
    primes = sc['primes']
    idxs = args.primes if args.primes is not None else list(range(len(primes)))
    bmax_exh = args.bmax_exh if args.bmax_exh is not None else (21 if n == 64 else 20)
    bmax_samp = args.bmax_samp if args.bmax_samp is not None else n // 2
    M0 = least_2power_above(t)

    def log(msg): print(msg, flush=True)

    log(f"==== U2-C FALSIFIER SCAN  scale={args.scale}  n={n} t={t} "
        f"M0={M0} stride={n//M0} ====")
    log(f"mode={args.mode} primes_idx={idxs} bmax_exh={bmax_exh} "
        f"bmax_samp={bmax_samp} nbip={args.nbip} Ksamp={args.ksamp} seed={SEED}")

    any_primitive = False
    for pi in idxs:
        q = primes[pi]
        g, zeta = get_zeta(q, n)
        log(f"\n---- prime q={q} (~2^{q.bit_length()-1}) g={g} zeta={zeta} ----")
        pc = positive_control(n, t, q, zeta, log)

        if args.mode in ('mitm', 'all'):
            hits = run_mitm(n, t, q, zeta, bmax_exh, bmax_samp, args.nbip,
                            args.ksamp, log, bmin=args.bmin)
            # classify all verified hits
            by_cls = {}
            prims = []
            for sup, v in hits.items():
                by_cls[v['cls']] = by_cls.get(v['cls'], 0) + 1
                if v['cls'] == 'primitive':
                    prims.append(v)
            wt = sorted(set(v['b'] for v in hits.values()))
            log(f"  MITM verified t-null hits: total={len(hits)} by_class={by_cls} "
                f"weights={wt}")
            if prims:
                any_primitive = True
                log(f"  *** PRIMITIVE (FALSIFIER) HITS: {len(prims)} ***")
                for v in prims[:5]:
                    log(f"      support={v['support']} b={v['b']} "
                        f"cls={v['cls']} power_sums={v['power_sums']}")

        if args.mode in ('sparse', 'all'):
            prim_rel, lifts = run_sparse(n, t, q, zeta, args.wmax_exh,
                                         args.ksamp, log)
            if lifts:
                any_primitive = True
                log(f"  *** ANTIPODAL-LIFT FALSIFIERS: {len(lifts)} ***")
                for (E, lift, v) in lifts[:5]:
                    log(f"      seed_E={E} lifted_block={lift} "
                        f"power_sums={v['power_sums']}")

        log(f"  positive-control PASS={pc}")

    verdict = 'FAIL (U2-C FALSIFIED at toy scale)' if any_primitive \
              else 'PASS (no primitive/falsifier hit; dichotomy survives)'
    log(f"\n==== SCALE {args.scale} VERDICT: {verdict} ====")
    return 0 if not any_primitive else 1

if __name__ == '__main__':
    sys.exit(main())
