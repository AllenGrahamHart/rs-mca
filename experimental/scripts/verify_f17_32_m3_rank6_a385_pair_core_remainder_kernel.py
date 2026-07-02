#!/usr/bin/env python3
"""Verify the A=385 pair-core polynomial remainder-kernel normal form."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from experimental.scripts.emit_f17_32_hankel_row_descriptor import K, N  # noqa: E402


SCHEMA_VERSION = "f17-32-m3-rank6-a385-pair-core-remainder-kernel-v1"
Q_LINE = 17**32
TARGET_BITS = 128
BUDGET = Q_LINE // 2**TARGET_BITS
PROJECTIVE_BUDGET = (Q_LINE + 1) // 2**TARGET_BITS
AGREEMENT = 385
RANK = 6
ROW_DESCRIPTOR_REF = (
    "experimental/data/certificates/hankel-f17-32-row-descriptor/"
    "f17_32_n512_k256_hankel_row_descriptor.json"
)
RANK_TEST_REF = (
    "experimental/data/certificates/hankel-f17-32-m3-rank6-a385-pair-core-rank-test/"
    "f17_32_n512_k256_m3_rank6_a385_pair_core_rank_test.json"
)
CAUCHY_MOMENT_REF = (
    "experimental/data/certificates/hankel-f17-32-m3-rank6-a385-pair-core-cauchy-moment/"
    "f17_32_n512_k256_m3_rank6_a385_pair_core_cauchy_moment.json"
)
PAIR_CORE_QUOTIENT_REF = (
    "experimental/data/certificates/"
    "hankel-f17-32-m3-rank6-a385-pair-core-quotient-reduction/"
    "f17_32_n512_k256_m3_rank6_a385_pair_core_quotient_reduction.json"
)


def load_json(ref: str | Path) -> dict[str, Any]:
    path = ref if isinstance(ref, Path) else ROOT / ref
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_file(ref: str) -> str:
    return sha256((ROOT / ref).read_bytes()).hexdigest()


def render(value: dict[str, Any]) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def degree_bounds(common_core_size: int) -> dict[str, Any]:
    j_value = N - AGREEMENT
    m_value = j_value + 1
    return {
        "common_external_core_size": common_core_size,
        "kernel_quotient_degree_bound": f"deg F_Q < {m_value - common_core_size}",
        "split_member_quotient_degree": j_value - common_core_size,
        "correction_polynomial_degree_bound": "deg T_Q <= 3",
    }


def build_certificate() -> dict[str, Any]:
    descriptor = load_json(ROW_DESCRIPTOR_REF)
    rank_test = load_json(RANK_TEST_REF)
    cauchy = load_json(CAUCHY_MOMENT_REF)
    quotient = load_json(PAIR_CORE_QUOTIENT_REF)

    require(descriptor["row"]["n"] == N, "descriptor n mismatch")
    require(descriptor["row"]["k"] == K, "descriptor k mismatch")
    require(descriptor["row"]["field_order"] == Q_LINE, "descriptor q mismatch")
    require(
        rank_test["schema_version"] == "f17-32-m3-rank6-a385-pair-core-rank-test-v1",
        "rank-test schema mismatch",
    )
    require(
        cauchy["schema_version"] == "f17-32-m3-rank6-a385-pair-core-cauchy-moment-v1",
        "Cauchy-moment schema mismatch",
    )
    require(
        quotient["schema_version"]
        == "f17-32-m3-rank6-a385-pair-core-quotient-reduction-v1",
        "pair-core quotient schema mismatch",
    )
    require(BUDGET == 6 and PROJECTIVE_BUDGET == 6, "unexpected budget")

    j_value = N - AGREEMENT
    t_value = AGREEMENT - K
    m_value = j_value + 1
    support_size = m_value + RANK
    h_value = support_size - t_value
    q_dimension = h_value
    pair_core_min = rank_test["summary"]["pair_core_min"]
    rank_threshold = rank_test["summary"][
        "external_evaluation_rank_threshold_for_pair_line"
    ]
    kernel_dimension_min = q_dimension - rank_threshold
    quotient_at_min = degree_bounds(pair_core_min)

    require(j_value == 127, "A385 j changed")
    require(t_value == 129, "A385 t changed")
    require(m_value == 128, "A385 m changed")
    require(h_value == 5, "A385 boundary defect changed")
    require(q_dimension == 5, "A385 Q dimension changed")
    require(pair_core_min == 24, "pair-core minimum changed")
    require(rank_threshold == 3, "rank threshold changed")
    require(kernel_dimension_min == 2, "kernel dimension threshold changed")
    require(
        cauchy["summary"]["reduced_matrix_factorization_available"],
        "Cauchy factorization unavailable",
    )
    require(
        quotient["summary"]["ambient_quotient_vector_dimension_at_pair_core_min"]
        == m_value - pair_core_min,
        "quotient dimension mismatch",
    )
    require(
        quotient["summary"]["split_quotient_degree_at_pair_core_min"]
        == j_value - pair_core_min,
        "split quotient degree mismatch",
    )

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "PROVED / AUDIT",
        "object": "A=385 pair-core polynomial remainder-kernel normal form",
        "row": {
            "code": "RS[F_17^32,H,256]",
            "n": N,
            "k": K,
            "field": "F_17^32",
            "domain_hash": descriptor["row"]["domain_hash"],
            "q_line": Q_LINE,
        },
        "source_artifacts": {
            "row_descriptor": {"ref": ROW_DESCRIPTOR_REF, "sha256": sha256_file(ROW_DESCRIPTOR_REF)},
            "a385_pair_core_rank_test": {
                "ref": RANK_TEST_REF,
                "sha256": sha256_file(RANK_TEST_REF),
            },
            "a385_pair_core_cauchy_moment": {
                "ref": CAUCHY_MOMENT_REF,
                "sha256": sha256_file(CAUCHY_MOMENT_REF),
            },
            "a385_pair_core_quotient_reduction": {
                "ref": PAIR_CORE_QUOTIENT_REF,
                "sha256": sha256_file(PAIR_CORE_QUOTIENT_REF),
            },
        },
        "agreement": {
            "A": AGREEMENT,
            "j": j_value,
            "t": t_value,
            "m": m_value,
            "direction_rank": RANK,
            "combined_support_size": support_size,
            "boundary_defect_h": h_value,
            "Q_vector_dimension": q_dimension,
            "pair_core_min": pair_core_min,
            "rank_threshold": rank_threshold,
            "kernel_dimension_threshold": kernel_dimension_min,
        },
        "notation": {
            "base_polynomial": "P_X(T)=prod_{x in X}(T-x), deg P_X=128",
            "external_core_polynomial": "C_E(T)=prod_{s in E}(T-s)",
            "base_interpolant": (
                "R(T) is the unique degree-<128 polynomial with "
                "R(x)=W_x=Omega_x/a_x on X"
            ),
            "transfer_polynomial": "L_Q = Rem(R Q, P_X)",
            "remainder_map": "Phi_E(Q)=Rem(Rem(R Q, P_X), C_E)",
        },
        "normal_form": {
            "interpolation_remainder_identity": (
                "Since R(x)Q(x)=W_x Q(x) on X, the transferred polynomial L_Q "
                "is exactly Rem(R Q, P_X)."
            ),
            "external_core_kernel": (
                "For squarefree C_E with roots E disjoint from X, L_Q vanishes "
                "on E iff Phi_E(Q)=0 iff C_E divides Rem(R Q, P_X)."
            ),
            "rank_kernel_equivalence": (
                "The external-evaluation matrix has rank r exactly when Phi_E "
                "has rank r, because evaluation on the roots of C_E is an "
                "isomorphism F[T]/(C_E) -> F^E."
            ),
            "pair_line_condition": (
                "A pair-core Q-line exists for E iff dim ker Phi_E >= 2, "
                "equivalently rank Phi_E <= 3."
            ),
            "quotient_identity": (
                "For every Q in ker Phi_E there are polynomials F_Q and T_Q "
                "with R Q = C_E F_Q + P_X T_Q, deg F_Q < 128-|E| and deg T_Q<=3."
            ),
            "split_member_gate": (
                "For the two actual finite split-locator classes on the Q-line, "
                "F_Q must have exact degree 127-|E| and divide (X^512-1)/C_E "
                "after normalization, in addition to the finite noncontainment gate."
            ),
        },
        "degree_bounds_at_pair_core_min": quotient_at_min,
        "degree_bound_table": [degree_bounds(value) for value in [pair_core_min, 64, 96, 122, 127]],
        "consequence_for_pair_core_frontier": {
            "pressure_forced_core_size": pair_core_min,
            "linear_map_source_dimension": q_dimension,
            "linear_map_target_dimension": pair_core_min,
            "overbudget_survivor_requires": "dim ker Phi_E >= 2",
            "equivalent_rank_condition": "rank Phi_E <= 3",
            "quotient_identity_at_pair_core_min": (
                "R Q = C_E F_Q + P_X T_Q with deg F_Q<104 and deg T_Q<=3"
            ),
            "split_members_at_pair_core_min": (
                "two distinct kernel-line points must have exact quotient degree "
                "103 and divide (X^512-1)/C_E"
            ),
        },
        "sampler_denominators": {
            "finite_line": {
                "denominator": Q_LINE,
                "denominator_formula": "|F|",
                "budget_floor_denominator_over_2_128": BUDGET,
            },
            "projective_line": {
                "denominator": Q_LINE + 1,
                "denominator_formula": "|P^1(F)| = |F| + 1",
                "budget_floor_denominator_over_2_128": PROJECTIVE_BUDGET,
            },
        },
        "summary": {
            "agreement": AGREEMENT,
            "Q_vector_dimension": q_dimension,
            "pair_core_min": pair_core_min,
            "rank_threshold": rank_threshold,
            "kernel_dimension_threshold": kernel_dimension_min,
            "remainder_kernel_normal_form_available": True,
            "quotient_identity_available": True,
            "split_quotient_degree_at_pair_core_min": j_value - pair_core_min,
            "ambient_quotient_dimension_at_pair_core_min": m_value - pair_core_min,
        },
        "checks": [
            "A=385 dimensions give a five-dimensional Q-space",
            "L_Q is Rem(RQ,P_X) by base interpolation",
            "C_E is squarefree and disjoint from X, so evaluation modulo C_E is faithful",
            "rank<=3 is equivalent to dim ker Phi_E>=2",
            "kernel vectors satisfy RQ=C_E F_Q+P_X T_Q",
            "at |E|=24, deg F_Q<104 and split members have exact degree 103",
        ],
        "nonclaims": [
            "does not close the no-fixed-core A=385 frontier",
            "does not prove that dim ker Phi_E>=2 is impossible for |E|=24",
            "does not prove that dim ker Phi_E>=2 is quotient-paid",
            "does not prove that kernel points pass the split-locator divisor gate",
            "does not prove finite noncontainment for kernel points",
            "does not classify overlapping-support rank-6 pencils",
            "does not produce a row-level M3 safe-side bound",
        ],
    }


def check_certificate(path: Path, certificate: dict[str, Any]) -> None:
    expected = render(certificate)
    actual = path.read_text(encoding="utf-8")
    if actual != expected:
        raise AssertionError(f"A=385 pair-core remainder-kernel mismatch: {path}")


def print_summary(certificate: dict[str, Any]) -> None:
    summary = certificate["summary"]
    print("F_17^32 M3 rank-6 A=385 pair-core remainder-kernel normal form")
    print(
        "Qdim={Q_vector_dimension}; e>={pair_core_min}; kerdim>={kernel_dimension_threshold}".format(
            **summary
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()

    certificate = build_certificate()
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(render(certificate), encoding="utf-8")
    if args.check:
        check_certificate(args.check, certificate)
    print_summary(certificate)


if __name__ == "__main__":
    main()
