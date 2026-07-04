#!/usr/bin/env python3
"""E33 verifier: near-k deep-link staircase census.

For a fixed aligned anchor (pair, support T0), count aligned partner supports
at distinct slopes whose overlap with T0 lies in the budget-relevant band

    k/2 < |T cap T0| < k.

The census is deliberately small and deterministic.  It uses the same
syndrome-pencil method as E27, but runs in chunks to keep memory low.

Rows:
  * F_97, n=16, k=8, A=11: the E27 corridor row.
  * F_17, n=16, k=8, A=11: denser stress row on F_17^*.

Stdlib + numpy; no Monte Carlo decisions beyond pinned seeds.
Run: python3 experimental/scripts/verify_e33_deep_link_staircase.py
To refresh the pinned certificate:
  python3 experimental/scripts/verify_e33_deep_link_staircase.py --write-certificate
"""

from __future__ import annotations

import itertools
import json
import math
import os
import sys
from dataclasses import dataclass

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "e33-deep-link-staircase",
    "e33_deep_link_staircase.json",
)

FAILS: list[str] = []
NCHECK = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global NCHECK
    NCHECK += 1
    tag = "PASS" if cond else "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    if not cond:
        FAILS.append(name)


def primitive_root(p: int) -> int:
    factors = set()
    m = p - 1
    d = 2
    while d * d <= m:
        if m % d == 0:
            factors.add(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        factors.add(m)
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in factors):
            return g
    raise RuntimeError(f"no primitive root mod {p}")


@dataclass(frozen=True)
class Row:
    q: int
    n: int
    k: int
    A: int
    samples: int
    seed: int


@dataclass
class Engine:
    row: Row
    xs: np.ndarray
    gmat: np.ndarray
    inv: list[int]
    inv_arr: np.ndarray
    supports: list[tuple[int, ...]]
    support_masks: list[int]
    H: np.ndarray

    @property
    def t(self) -> int:
        return self.row.A - self.row.k

    @property
    def all_code(self) -> int:
        return self.row.q

    @property
    def empty_code(self) -> int:
        return self.row.q + 1


def build_engine(row: Row) -> Engine:
    q, n, k, A = row.q, row.n, row.k, row.A
    g = primitive_root(q)
    omega = pow(g, (q - 1) // n, q)
    xs = np.array([pow(omega, i, q) for i in range(n)], dtype=np.int64)
    gmat = np.array([[pow(int(x), m, q) for x in xs] for m in range(k)], dtype=np.int64)
    inv = [0] + [pow(a, q - 2, q) for a in range(1, q)]
    inv_arr = np.array(inv, dtype=np.int64)
    supports = list(itertools.combinations(range(n), A))
    support_masks = [sum(1 << i for i in T) for T in supports]
    H = np.concatenate([dual_rows(q, k, xs, inv, T) for T in supports], axis=0)
    return Engine(row, xs, gmat, inv, inv_arr, supports, support_masks, H.astype(np.float64))


def dual_rows(q: int, k: int, xs: np.ndarray, inv: list[int], support: tuple[int, ...]) -> np.ndarray:
    s = len(support)
    rows = np.zeros((s - k, len(xs)), dtype=np.int64)
    local_xs = [int(xs[i]) for i in support]
    for a, i in enumerate(support):
        lam = 1
        for b in range(s):
            if b != a:
                lam = lam * ((local_xs[a] - local_xs[b]) % q) % q
        lam = inv[lam]
        for m in range(s - k):
            rows[m, i] = lam * pow(local_xs[a], m, q) % q
    return rows


def row_codes(engine: Engine, A: np.ndarray, B: np.ndarray) -> np.ndarray:
    q = engine.row.q
    return np.where(
        B != 0,
        (q - A) % q * engine.inv_arr[B] % q,
        np.where(A == 0, engine.all_code, engine.empty_code),
    ).astype(np.int16)


def code_intersect(engine: Engine, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.where(
        (a == engine.empty_code) | (b == engine.empty_code),
        engine.empty_code,
        np.where(
            a == engine.all_code,
            b,
            np.where(b == engine.all_code, a, np.where(a == b, a, engine.empty_code)),
        ),
    ).astype(np.int16)


def support_codes(engine: Engine, U: np.ndarray, V: np.ndarray) -> np.ndarray:
    q = engine.row.q
    ncheck = engine.t
    nsup = len(engine.supports)
    HT = engine.H.T.copy()
    SU = ((U.astype(np.float64) @ HT) % q).astype(np.int64)
    SV = ((V.astype(np.float64) @ HT) % q).astype(np.int64)
    codes = row_codes(engine, SU, SV).reshape(-1, nsup, ncheck)
    out = codes[:, :, 0]
    for m in range(1, ncheck):
        out = code_intersect(engine, out, codes[:, :, m])
    return out


def overlap_candidate_counts(row: Row) -> dict[int, int]:
    out: dict[int, int] = {}
    for r in range(row.A + 1):
        if 2 * r > row.k and r < row.k and row.A - r <= row.n - row.A:
            out[r] = math.comb(row.A, r) * math.comb(row.n - row.A, row.A - r)
    return out


def count_partners(
    engine: Engine,
    codes_row: np.ndarray,
    anchor_mask: int,
    anchor_z: int,
) -> tuple[dict[int, int], set[int], int, int]:
    by_overlap = {r: 0 for r in overlap_candidate_counts(engine.row)}
    slopes: set[int] = set()
    all_supports = 0
    subcore_counts: dict[int, int] = {}
    for idx, code in enumerate(codes_row.tolist()):
        mask = engine.support_masks[idx]
        r = (mask & anchor_mask).bit_count()
        if r not in by_overlap:
            continue
        if code == engine.empty_code or code == anchor_z:
            continue
        core = mask & anchor_mask
        if code == engine.all_code:
            multiplicity = engine.row.q - 1
            all_supports += 1
            slopes.update(z for z in range(engine.row.q) if z != anchor_z)
        elif 0 <= code < engine.row.q:
            multiplicity = 1
            slopes.add(code)
        else:
            raise AssertionError(f"unexpected code {code}")
        by_overlap[r] += multiplicity
        subcore_counts[core] = subcore_counts.get(core, 0) + multiplicity
    max_subcore = max(subcore_counts.values(), default=0)
    return by_overlap, slopes, all_supports, max_subcore


def run_row(row: Row) -> dict:
    engine = build_engine(row)
    rng = np.random.default_rng(row.seed)
    q, n, k, A = row.q, row.n, row.k, row.A
    candidate_counts = overlap_candidate_counts(row)
    expected_by_overlap = {
        str(r): row.samples * (q - 1) * count / (q ** engine.t)
        for r, count in candidate_counts.items()
    }
    totals = {r: 0 for r in candidate_counts}
    pairs_with_any = 0
    max_events = 0
    max_distinct_slopes = 0
    max_subcore = 0
    all_supports = 0

    chunk = 128
    done = 0
    while done < row.samples:
        m = min(chunk, row.samples - done)
        anchor_indices = rng.integers(0, len(engine.supports), m)
        anchor_z = rng.integers(0, q, m, dtype=np.int64)
        coeffs = rng.integers(0, q, (m, k), dtype=np.int64)
        codewords = coeffs @ engine.gmat % q
        V = rng.integers(0, q, (m, n), dtype=np.int64)
        U = rng.integers(0, q, (m, n), dtype=np.int64)
        for i, sidx in enumerate(anchor_indices.tolist()):
            T0 = engine.supports[sidx]
            U[i, list(T0)] = (codewords[i, list(T0)] - anchor_z[i] * V[i, list(T0)]) % q
        codes = support_codes(engine, U, V)
        for i, sidx in enumerate(anchor_indices.tolist()):
            by_overlap, slopes, all_ct, subcore_ct = count_partners(
                engine,
                codes[i],
                engine.support_masks[sidx],
                int(anchor_z[i]),
            )
            event_count = sum(by_overlap.values())
            pairs_with_any += int(event_count > 0)
            max_events = max(max_events, event_count)
            max_distinct_slopes = max(max_distinct_slopes, len(slopes))
            max_subcore = max(max_subcore, subcore_ct)
            all_supports += all_ct
            for r, count in by_overlap.items():
                totals[r] += count
        done += m

    expected_total = sum(expected_by_overlap.values())
    total_events = sum(totals.values())
    sigma = math.sqrt(max(expected_total, 1.0))
    in_band = abs(total_events - expected_total) <= 7 * sigma
    linear_cap = 8 * n
    subcore_cap = 4 * n
    check(
        f"F_{q}: near-k partner total in FM band",
        in_band,
        f"events={total_events}, expected={expected_total:.2f}, 7sigma={7*sigma:.2f}",
    )
    check(
        f"F_{q}: max partners per anchor is linear",
        max_events <= linear_cap,
        f"max={max_events}, cap={linear_cap}",
    )
    check(
        f"F_{q}: max subcore link is linear",
        max_subcore <= subcore_cap,
        f"max={max_subcore}, cap={subcore_cap}",
    )
    check(f"F_{q}: no all-slope support code in near-k band", all_supports == 0, f"all={all_supports}")

    return {
        "field": f"F_{q}",
        "n": n,
        "k": k,
        "A": A,
        "t": engine.t,
        "samples": row.samples,
        "seed": row.seed,
        "overlap_range": sorted(candidate_counts),
        "candidate_supports_by_overlap": {str(r): c for r, c in candidate_counts.items()},
        "expected_events_by_overlap": {k: round(v, 6) for k, v in expected_by_overlap.items()},
        "observed_events_by_overlap": {str(r): totals[r] for r in sorted(totals)},
        "expected_total_events": round(expected_total, 6),
        "observed_total_events": total_events,
        "pairs_with_any_partner": pairs_with_any,
        "max_partner_events_per_anchor": max_events,
        "max_distinct_partner_slopes_per_anchor": max_distinct_slopes,
        "max_partner_events_through_one_subcore": max_subcore,
        "all_slope_support_codes": all_supports,
        "linear_cap_used": linear_cap,
    }


def main() -> None:
    rows = [
        run_row(Row(q=97, n=16, k=8, A=11, samples=4096, seed=20260733)),
        run_row(Row(q=17, n=16, k=8, A=11, samples=512, seed=20260734)),
    ]
    result = {
        "node": "deep_link_staircase",
        "task": "E33",
        "checks": NCHECK,
        "rows": rows,
        "verdict": "linear in all checked toy rows; no super-linear near-k link population observed",
    }

    if "--write-certificate" in sys.argv:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w") as fh:
            json.dump(result, fh, indent=2, sort_keys=True)
            fh.write("\n")

    expected = None
    if os.path.exists(CERT):
        with open(CERT) as fh:
            expected = json.load(fh)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", result == expected)

    if FAILS:
        print("\nrecomputed summary:")
        print(json.dumps(result, indent=2, sort_keys=True))
        print("\nFAIL:")
        for name in FAILS:
            print("  -", name)
        sys.exit(1)

    print("\nsummary:")
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"\nPASS: {NCHECK} E33 deep-link staircase checks")


if __name__ == "__main__":
    main()
