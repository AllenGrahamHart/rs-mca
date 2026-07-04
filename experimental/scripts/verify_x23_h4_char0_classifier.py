#!/usr/bin/env python3
"""X23 h=4 characteristic-zero classifier.

For n=2^s over characteristic zero, every h=4 same-top-three trade in mu_n is
a difference of two full mu_4 fibers.  The proof is elementary:

  * equality of e1 gives a signed word f with f(zeta)=0;
  * Phi_n(X)=X^(n/2)+1, so f is antipodal as an integer word;
  * the quotient h=2 sum collision on the complex unit circle is trivial
    except at sum zero, hence each quotient pair is antipodal.

This verifier checks the finite combinatorial reductions behind the proof for
representative powers of two and records the theorem packet.  It does not claim
the same statement in finite characteristic; X21/X22 show finite p-specific
antipodal quotient-lift exceptions.
"""

from __future__ import annotations

from itertools import combinations
import json
import os
import sys
from typing import Any


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x23-h4-char0-classifier",
    "x23_h4_char0_classifier.json",
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
    print(line, flush=True)
    if not cond:
        FAILS.append(name)


def coeff_word(n: int, pos: tuple[int, ...], neg: tuple[int, ...]) -> list[int]:
    c = [0] * n
    for i in pos:
        c[i % n] += 1
    for i in neg:
        c[i % n] -= 1
    return c


def divisible_by_phi_power_two(c: list[int]) -> bool:
    """For n=2m, Phi_n=X^m+1 and deg f<n, so c[i+m]=c[i]."""
    n = len(c)
    m = n // 2
    return all(c[i + m] == c[i] for i in range(m))


def signed_word_is_antipodal(c: list[int]) -> bool:
    n = len(c)
    m = n // 2
    return all(c[i + m] == c[i] for i in range(m))


def is_antipodal_pair(pair: tuple[int, int], m: int) -> bool:
    a, b = pair
    return (a - b) % m == m // 2


def quotient_pair_sum_relation_is_zero_family(m: int, pair1: tuple[int, int], pair2: tuple[int, int]) -> bool:
    """Exact char-zero relation u+v=r+s in mu_m, for m a power of two.

    For a 4-term signed word of degree < m, divisibility by Phi_m is exact.
    Distinct unordered pairs with equal complex sum occur only at sum zero,
    i.e. both pairs are antipodal.
    """
    c = coeff_word(m, pair1, pair2)
    if not divisible_by_phi_power_two(c):
        return False
    if sorted(pair1) == sorted(pair2):
        return True
    return is_antipodal_pair(pair1, m) and is_antipodal_pair(pair2, m)


def full_mu4_fiber(mask: tuple[int, int, int, int], n: int) -> bool:
    step = n // 4
    s = set(mask)
    return any({(r + j * step) % n for j in range(4)} == s for r in range(step))


def quotient_pair_for_antipodal_h4(n: int, s: tuple[int, ...]) -> tuple[int, int] | None:
    m = n // 2
    pair = tuple(sorted({i % m for i in s}))
    if len(pair) != 2:
        return None
    c = coeff_word(n, s, ())
    if not signed_word_is_antipodal(c):
        return None
    return pair


def h4_trade_is_mu4_fiber_pair(n: int, p_set: tuple[int, ...], q_set: tuple[int, ...]) -> bool | None:
    """Return True/False for actual char-zero h=4 trades, None for non-trades."""
    c = coeff_word(n, p_set, q_set)
    if not divisible_by_phi_power_two(c):
        return None
    if not signed_word_is_antipodal(c):
        return False

    # Collapse through X^2.  Antipodal pairs in mu_n map to unordered pairs in
    # mu_{n/2}; e2 equality is quotient sum equality.
    m = n // 2
    p_pair = quotient_pair_for_antipodal_h4(n, p_set)
    q_pair = quotient_pair_for_antipodal_h4(n, q_set)
    if p_pair is None or q_pair is None:
        return False
    if not quotient_pair_sum_relation_is_zero_family(m, p_pair, q_pair):
        return None
    return full_mu4_fiber(tuple(sorted(p_set)), n) and full_mu4_fiber(tuple(sorted(q_set)), n)


def check_pair_sum_classifier(m: int) -> dict[str, Any]:
    pairs = list(combinations(range(m), 2))
    relation_count = 0
    nontrivial_count = 0
    bad: list[dict[str, Any]] = []
    for a, pair1 in enumerate(pairs):
        for pair2 in pairs[a + 1 :]:
            c = coeff_word(m, pair1, pair2)
            if divisible_by_phi_power_two(c):
                relation_count += 1
                if sorted(pair1) != sorted(pair2):
                    nontrivial_count += 1
                    ok = is_antipodal_pair(pair1, m) and is_antipodal_pair(pair2, m)
                    if not ok and len(bad) < 5:
                        bad.append({"pair1": pair1, "pair2": pair2})
    expected = (m // 2) * (m // 2 - 1) // 2
    check(
        f"m={m}: nontrivial complex h=2 sum collisions are exactly zero-sum pairs",
        not bad and nontrivial_count == expected,
        f"nontrivial={nontrivial_count}, expected={expected}",
    )
    return {
        "m": m,
        "unordered_pairs": len(pairs),
        "nontrivial_sum_collisions": nontrivial_count,
        "expected_zero_sum_pair_collisions": expected,
        "bad_examples": bad,
    }


def check_h4_classifier(n: int) -> dict[str, Any]:
    """Enumerate the char-zero h=4 classifier at small n.

    The test uses the cyclotomic divisibility conditions rather than floating
    complex arithmetic:
      e1 equality -> Phi_n divides the signed word;
      e2 equality after antipodal descent -> quotient h=2 sum relation.
    """
    subsets = list(combinations(range(n), 4))
    candidate_count = 0
    bad: list[dict[str, Any]] = []
    for idx, p_set in enumerate(subsets):
        p_mask = sum(1 << i for i in p_set)
        for q_set in subsets[idx + 1 :]:
            q_mask = sum(1 << i for i in q_set)
            if p_mask & q_mask:
                continue
            c = coeff_word(n, p_set, q_set)
            if not divisible_by_phi_power_two(c):
                continue
            # The e2 condition in the antipodal quotient.
            classified = h4_trade_is_mu4_fiber_pair(n, p_set, q_set)
            if classified is None:
                continue
            if not classified:
                bad.append({"P": p_set, "Q": q_set})
                if len(bad) >= 5:
                    break
            candidate_count += 1
        if len(bad) >= 5:
            break
    check(
        f"n={n}: char-zero h=4 candidates are mu4 fiber pairs",
        not bad,
        f"candidates={candidate_count}",
    )
    return {
        "n": n,
        "h4_candidates_after_cyclotomic_descent": candidate_count,
        "bad_examples": bad,
    }


def build_certificate() -> dict[str, Any]:
    pair_rows = [check_pair_sum_classifier(m) for m in (4, 8, 16, 32, 64, 128)]
    h4_rows = [check_h4_classifier(n) for n in (8, 16)]
    check("pair-sum classifier had no bad examples", all(not row["bad_examples"] for row in pair_rows))
    check("h4 classifier had no bad examples", all(not row["bad_examples"] for row in h4_rows))
    return {
        "task": "X23 h=4 characteristic-zero classifier",
        "node": "active_core_count_bound",
        "status": "PROVED over characteristic zero: h=4 trades in mu_{2^s} are exactly mu4 full-fiber trades",
        "theorem": (
            "If n=2^s and P,Q are disjoint 4-subsets of complex mu_n with "
            "equal first three elementary symmetric sums, then P and Q are "
            "full mu_4 fibers.  Finite-field antipodal quotient lifts are "
            "therefore p-specific reductions, not characteristic-zero trades."
        ),
        "pair_sum_rows": pair_rows,
        "h4_rows": h4_rows,
        "checks": NCHECK,
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    cert = build_certificate()
    if write:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w", encoding="utf-8") as fh:
            json.dump(cert, fh, indent=2, sort_keys=True)
            fh.write("\n")
        print(f"[write] {CERT}")

    expected = None
    if os.path.exists(CERT):
        with open(CERT, encoding="utf-8") as fh:
            expected = json.load(fh)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", cert == expected)

    print("\npair-sum rows:")
    for row in cert["pair_sum_rows"]:
        print(
            f"m={row['m']:<3d} nontrivial={row['nontrivial_sum_collisions']:<5d} "
            f"expected={row['expected_zero_sum_pair_collisions']:<5d}"
        )
    print("h4 rows:")
    for row in cert["h4_rows"]:
        print(
            f"n={row['n']:<3d} candidates={row['h4_candidates_after_cyclotomic_descent']:<5d}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X23 h=4 char-zero classifier checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
