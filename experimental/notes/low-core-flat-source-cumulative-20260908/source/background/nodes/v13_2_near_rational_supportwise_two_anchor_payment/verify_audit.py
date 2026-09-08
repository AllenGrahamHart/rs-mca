#!/usr/bin/env python3
"""Independent audit path for the two-anchor payment (coordinator, 2026-08-12).

Three checks, sharing no code path with verify.py:

A. EXHAUSTIVE mu_16 census: support-wise MCA-badness of every finite slope
   in F_17 is decided by scanning ALL C(16,10)=8008 size-m supports with a
   full augmented-rank solver (no first-K interpolation shortcut, unlike
   verify.py, which checks only the two designated supports). The bad set
   must be exactly {3,5}: count 2 falsifies the former +1 charge (the far
   stratum is empty because every line word has weight <= w) and respects
   the proved 2w=4 bound.

B. Fresh-field falsifier replay over F_29 (D=F_29^*, n=28, K=14, w=3):
   the deployed construction pattern of upstream PR #1160 section 1 with
   three slopes. Each gamma_i is certified bad on its designated support
   by the same rank solver; the two-anchor coordinate-ratio recovery
   returns exactly the full slope set from the first anchor pair.
   3 > 1 falsifies the old charge at a second field; 3 <= 2w = 6 respects
   the theorem.

C. Deployed-row arithmetic: exact integer guards and charges for the
   KoalaBear and Mersenne-31 rows as recorded in the upstream packet
   (PR #1160), including the B_* difference consistency and the 2^24-1
   form of the Mersenne-31 reserve calibration.

RAMGUARD_TIMEOUT: run under `tools/ramguard local -- python3 ...`
(the exhaustive census takes on the order of a minute in CPython).
"""

from itertools import combinations


def explained(word, support, vand, p, K):
    """Does some polynomial of degree < K agree with word on support?

    Full augmented Gauss-Jordan rank comparison over F_p. Consistent iff
    the augmented column acquires no pivot.
    """
    rows = [vand[i] + [word[i] % p] for i in support]
    cols = K + 1
    r = 0
    for c in range(cols):
        piv = None
        for rr in range(r, len(rows)):
            if rows[rr][c] % p:
                piv = rr
                break
        if piv is None:
            continue
        if c == K:
            return False  # pivot in the augmented column: inconsistent
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = pow(rows[r][c], p - 2, p)
        rows[r] = [(v * inv) % p for v in rows[r]]
        for rr in range(len(rows)):
            if rr != r and rows[rr][c]:
                f = rows[rr][c]
                rows[rr] = [(a - f * b) % p
                            for a, b in zip(rows[rr], rows[r])]
        r += 1
    return True


def line_construction(p, xs, gammas):
    """The PR #1160 section-1 pattern: u(e_i)=-gamma_i, v(e_i)=1."""
    n = len(xs)
    u = [0] * n
    v = [0] * n
    for i, g in enumerate(gammas):
        u[i] = (-g) % p
        v[i] = 1
    return u, v


# ---------------------------------------------------------------- A
P, K, W = 17, 8, 2
M = K + W
XS = list(range(1, P))          # D = F_17^* = mu_16
N = len(XS)
GAMMAS = (3, 5)
assert W >= 1 and 3 * W <= N - K

VAND = [[pow(x, d, P) for d in range(K)] for x in XS]
u, v = line_construction(P, XS, GAMMAS)

supports = list(combinations(range(N), M))
assert len(supports) == 8008

pair_ok = [
    explained(u, S, VAND, P, K) and explained(v, S, VAND, P, K)
    for S in supports
]

bad = set()
for z in range(P):
    word = [(u[i] + z * v[i]) % P for i in range(N)]
    # far-stratum check: every line word is within distance w of the code
    # (witnessed by the zero codeword), so the old +1 inequality's
    # right-hand set is empty.
    assert sum(1 for t in word if t) <= W
    for S, ok in zip(supports, pair_ok):
        if ok:
            continue
        if explained(word, S, VAND, P, K):
            bad.add(z)
            break

assert bad == set(GAMMAS), bad
assert len(bad) == 2 > 1        # falsifies the former +1 charge
assert len(bad) <= 2 * W        # respects the proved 2w bound

# ---------------------------------------------------------------- B
P2, K2, W2 = 29, 14, 3
M2 = K2 + W2
XS2 = list(range(1, P2))        # D = F_29^*
N2 = len(XS2)
GAMMAS2 = (7, 11, 13)
assert W2 >= 1 and 3 * W2 <= N2 - K2

VAND2 = [[pow(x, d, P2) for d in range(K2)] for x in XS2]
u2, v2 = line_construction(P2, XS2, GAMMAS2)

for z in range(P2):
    word = [(u2[i] + z * v2[i]) % P2 for i in range(N2)]
    assert sum(1 for t in word if t) <= W2

base = tuple(range(len(GAMMAS2), len(GAMMAS2) + M2 - 1))
for i, g in enumerate(GAMMAS2):
    S = base + (i,)
    assert len(S) == M2
    word = [(u2[j] + g * v2[j]) % P2 for j in range(N2)]
    assert explained(word, S, VAND2, P2, K2)
    assert not (explained(u2, S, VAND2, P2, K2)
                and explained(v2, S, VAND2, P2, K2))

z0, z1 = GAMMAS2[0], GAMMAS2[1]
eta0 = [(u2[i] + z0 * v2[i]) % P2 for i in range(N2)]
eta1 = [(u2[i] + z1 * v2[i]) % P2 for i in range(N2)]
inv = pow(z1 - z0, P2 - 2, P2)
e_v = [((b - a) * inv) % P2 for a, b in zip(eta0, eta1)]
e_u = [(a - z0 * b) % P2 for a, b in zip(eta0, e_v)]
E = [i for i in range(N2) if e_u[i] or e_v[i]]
assert len(E) <= 2 * W2
ratios = {(-e_u[i] * pow(e_v[i], P2 - 2, P2)) % P2 for i in E if e_v[i]}
assert ratios == set(GAMMAS2)
assert len(GAMMAS2) == 3 > 1    # falsifier at a second field
assert len(GAMMAS2) <= 2 * W2   # theorem respected

# ---------------------------------------------------------------- C
KB_N, KB_K, KB_M = 2097152, 1048576, 1116048
KB_B = 274980728111395087
w = KB_M - KB_K
assert w == 67472
assert 2 * w == 134944
assert 3 * w <= KB_N - KB_K
assert KB_N - w == 2029680
assert KB_N - w > KB_M          # the common support off E exists
assert KB_B - 2 * w == 274980728111260143

w31 = 67448
assert 2 * w31 == 134896
assert 16642319 + 2 * w31 == 2 ** 24 - 1

print("V13_2_NEAR_RATIONAL_TWO_ANCHOR_AUDIT_OK",
      "mu16_bad=", sorted(bad),
      "f29_ratios=", sorted(ratios),
      "kb_2w=", 2 * w, "m31_2w=", 2 * w31)
