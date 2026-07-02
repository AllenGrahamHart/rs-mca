#!/usr/bin/env python3
"""Verify ambient flexibility of the A=385 pair-core rank condition."""

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


SCHEMA_VERSION = "f17-32-m3-rank6-a385-pair-core-ambient-flexibility-v1"
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
REMAINDER_KERNEL_REF = (
    "experimental/data/certificates/hankel-f17-32-m3-rank6-a385-pair-core-remainder-kernel/"
    "f17_32_n512_k256_m3_rank6_a385_pair_core_remainder_kernel.json"
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


def build_certificate() -> dict[str, Any]:
    descriptor = load_json(ROW_DESCRIPTOR_REF)
    remainder = load_json(REMAINDER_KERNEL_REF)

    require(descriptor["row"]["n"] == N, "descriptor n mismatch")
    require(descriptor["row"]["k"] == K, "descriptor k mismatch")
    require(descriptor["row"]["field_order"] == Q_LINE, "descriptor q mismatch")
    require(
        remainder["schema_version"]
        == "f17-32-m3-rank6-a385-pair-core-remainder-kernel-v1",
        "remainder-kernel schema mismatch",
    )
    require(BUDGET == 6 and PROJECTIVE_BUDGET == 6, "unexpected budget")

    j_value = N - AGREEMENT
    t_value = AGREEMENT - K
    m_value = j_value + 1
    support_size = m_value + RANK
    h_value = support_size - t_value
    q_dimension = h_value
    external_core_size = remainder["summary"]["pair_core_min"]
    pair_line_dimension = 2
    linear_constraint_count = pair_line_dimension * external_core_size
    solution_dimension_lower_bound = m_value - linear_constraint_count
    numerator_degree_bound = external_core_size - 1 + (q_dimension - 1)
    vanishing_points_if_coordinate_forced = m_value - 1

    require(j_value == 127, "A385 j changed")
    require(t_value == 129, "A385 t changed")
    require(m_value == 128, "A385 m changed")
    require(h_value == 5, "A385 boundary defect changed")
    require(q_dimension == 5, "A385 Q dimension changed")
    require(external_core_size == 24, "pair-core size changed")
    require(linear_constraint_count == 48, "constraint count changed")
    require(solution_dimension_lower_bound == 80, "solution dimension lower bound changed")
    require(numerator_degree_bound == 27, "rowspace numerator degree bound changed")
    require(
        numerator_degree_bound < vanishing_points_if_coordinate_forced,
        "degree bound no longer rules out coordinate forcing",
    )
    require(
        Q_LINE > m_value,
        "field is too small for the hyperplane-union nonzero-coordinate argument",
    )

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "PROVED / AUDIT",
        "object": "A=385 pair-core ambient linear flexibility route cut",
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
            "a385_pair_core_remainder_kernel": {
                "ref": REMAINDER_KERNEL_REF,
                "sha256": sha256_file(REMAINDER_KERNEL_REF),
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
            "external_core_size": external_core_size,
            "pair_line_vector_dimension": pair_line_dimension,
        },
        "theorem": {
            "statement": (
                "For any 24-point external core E and any fixed two-dimensional "
                "subspace U of the degree-<5 Q-space, there exist nonzero base "
                "weights W_x on X such that L_Q vanishes on E for every Q in U.  "
                "Equivalently, dim ker Phi_E>=2 is ambient-linearly achievable "
                "with all base weights nonzero."
            ),
            "linear_constraints": (
                "Choose a basis Q0,Q1 of U.  For each s in E and i in {0,1}, "
                "the equation L_Qi(s)=0 is one homogeneous linear condition in "
                "the 128 base weights W_x.  Thus there are at most 48 linear "
                "constraints and a solution space of dimension at least 80."
            ),
            "coordinate_not_forced": (
                "No coordinate W_x0 is forced to zero by these constraints.  If "
                "the coordinate vector at x0 lay in the constraint rowspace, then "
                "after clearing denominators over C_E, a numerator of degree at "
                "most |E|-1+4=27 would vanish on X\\{x0}, which has 127 points, "
                "but not at x0.  Since 27<127, this is impossible."
            ),
            "nonzero_weight_choice": (
                "The solution space is not contained in any coordinate-zero "
                "hyperplane.  Since |F_17^32|>128, the union of the 128 proper "
                "coordinate-zero hyperplane sections cannot cover the solution "
                "space.  Hence some solution has every W_x nonzero."
            ),
            "route_cut": (
                "Therefore the rank<=3 / dim ker Phi_E>=2 condition cannot be "
                "ruled out using only the ambient linear transfer and arbitrary "
                "nonzero base weights.  Closure must use the split-locator "
                "divisor gate, quotient payment, finite noncontainment, or "
                "additional Hankel structure."
            ),
        },
        "dimension_accounting": {
            "base_weight_variables": m_value,
            "constraints_per_pair_line_basis_vector": external_core_size,
            "pair_line_basis_vectors": pair_line_dimension,
            "linear_constraint_count_at_most": linear_constraint_count,
            "solution_dimension_lower_bound": solution_dimension_lower_bound,
            "coordinate_forcing_rowspace_numerator_degree_bound": numerator_degree_bound,
            "coordinate_forcing_vanishing_points": vanishing_points_if_coordinate_forced,
            "field_size_exceeds_coordinate_hyperplane_count": Q_LINE > m_value,
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
            "external_core_size": external_core_size,
            "base_weight_variables": m_value,
            "linear_constraint_count_at_most": linear_constraint_count,
            "solution_dimension_lower_bound": solution_dimension_lower_bound,
            "all_base_weights_can_be_nonzero": True,
            "rank_condition_ambient_linearly_flexible": True,
            "rank_condition_alone_cannot_close_no_fixed_core_frontier": True,
        },
        "checks": [
            "A=385 dimensions give 128 base weights and a five-dimensional Q-space",
            "a two-dimensional Q-line and 24 external points impose at most 48 homogeneous linear constraints",
            "the ambient solution space has dimension at least 80",
            "no coordinate W_x is forced to zero because the cleared numerator degree is at most 27<127",
            "the field has more than 128 elements, so the coordinate hyperplanes cannot cover the solution space",
            "ambient rank-collapse flexibility does not assert split-locator or noncontainment witnesses",
        ],
        "nonclaims": [
            "does not produce a split-locator bad slope",
            "does not prove the no-fixed-core A=385 frontier is nonempty",
            "does not prove quotient-divisor gates can be passed",
            "does not prove finite noncontainment",
            "does not close or refute the full no-fixed-core A=385 branch",
            "does not classify overlapping-support rank-6 pencils",
            "does not produce a row-level M3 safe-side bound",
        ],
    }


def check_certificate(path: Path, certificate: dict[str, Any]) -> None:
    expected = render(certificate)
    actual = path.read_text(encoding="utf-8")
    if actual != expected:
        raise AssertionError(f"A=385 pair-core ambient-flexibility mismatch: {path}")


def print_summary(certificate: dict[str, Any]) -> None:
    summary = certificate["summary"]
    print("F_17^32 M3 rank-6 A=385 pair-core ambient flexibility")
    print(
        "constraints<={linear_constraint_count_at_most}; solution_dim>={solution_dimension_lower_bound}; nonzero_weights={all_base_weights_can_be_nonzero}".format(
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
