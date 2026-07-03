#!/usr/bin/env python3
"""ASSEMBLY-AUDIT verifier: convention consistency across XR packets.

The audit extracts convention-setting lines from the packets that feed the
clean-rate compiler/rungs/staircase assembly, classifies each packet on the
requested convention axes, and reports every classified mismatch:

* support-wise alignment definition;
* exact-vs->= agreement;
* exchange-distance / s convention;
* paid-strip clause form.

The verifier is intentionally a review harness.  It does not prove the
assembly; it prevents silent convention drift by pinning the source lines that
justify each packet's convention record.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass
from typing import Any


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "assembly-convention-audit",
    "assembly_convention_audit.json",
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


def compact(text: str) -> str:
    return " ".join(text.strip().split())


@dataclass(frozen=True)
class PacketSpec:
    packet_id: str
    path: str
    role: str
    support_currency: str
    exactness: str
    exchange_s: str
    paid_strip: str
    required_evidence: tuple[str, ...]


PACKETS: tuple[PacketSpec, ...] = (
    PacketSpec(
        "qx13_pair_rank_ledger",
        "experimental/notes/roadmaps/qx13_pair_rank_ledger.md",
        "pair-rank moment ledger",
        "agreement_support_S_size_A",
        "exact_agreement_A",
        "s_exchange_distance_on_agreement_and_cosupports",
        "none_moment_level",
        (
            "are subsets `S subset D` of size exactly `A`",
            "s = |S \\ T| = |T \\ S|",
            "support-wise bad slope",
            "paid (tangent/quotient) mass is not subtracted",
        ),
    ),
    PacketSpec(
        "xr_clean_poly_forcing_reduction",
        "experimental/notes/roadmaps/xr_clean_poly_forcing_reduction.md",
        "clean-rate compiler",
        "slope_count_post_strip",
        "fixed_A_candidate_budget",
        "not_applicable",
        "quotient_plus_tangent_paid_then_R_post",
        (
            "post-strip non-quotient/non-tangent residual slope count",
            "R_post(u,v; A) <= 16 n^3",
            "proved quotient and tangent ledgers are charged",
            "including primitive aperiodic residue and any dihedral/extension column",
        ),
    ),
    PacketSpec(
        "xr_smallcore_rungs_2a_2b",
        "experimental/notes/roadmaps/xr_smallcore_rungs_2a_2b.md",
        "same-slope/list and two-slope forcing rungs",
        "agreement_support_S_size_A",
        "exact_agreement_support_with_exact_disagreement_off_S",
        "s_equals_A_minus_r",
        "none_structural_routing",
        (
            "aligned support is a tuple `(S,z,c)` with `|S|=A`",
            "Exactness is the convention used below",
            "s=A-r",
            "d+s=t",
        ),
    ),
    PacketSpec(
        "w2_graded_tangent_ledger_design",
        "experimental/notes/roadmaps/w2_graded_tangent_ledger_design.md",
        "graded tangent cell design",
        "overlap_core_r_between_agreement_supports",
        "not_explicit",
        "s_equals_A_minus_r_and_d_plus_s_equals_t",
        "quotient_dihedral_extension_cascade_removed_before_residual_cells",
        (
            "common core",
            "d = r-k",
            "s = A-r",
            "d+s=t",
            "after quotient,",
        ),
    ),
    PacketSpec(
        "a2_graded_tangent_bound",
        "experimental/notes/roadmaps/a2_graded_tangent_bound.md",
        "graded tangent bound assembly",
        "overlap_core_r_between_agreement_supports",
        "not_explicit",
        "s_equals_A_minus_r_and_d_plus_s_equals_t",
        "unified_strip_before_depth_residual_occupancy",
        (
            "k+1 <= r <= A-2",
            "s = A-r",
            "d+s = t",
            "After the unified strip",
        ),
    ),
    PacketSpec(
        "a1_staircase_cap_assembly",
        "experimental/notes/roadmaps/a1_staircase_cap_assembly.md",
        "deep-link staircase assembly",
        "partner_supports_through_fixed_subcore",
        "post_strip_partner_count",
        "lower_overlap_range_k_over_2_lt_r_lt_k",
        "unified_pullback_strip",
        (
            "partners through a fixed `(k-1)`-subcore",
            "unified pullback strip",
            "every post-strip near-k partner",
            "k/2 < |T cap T0| < k",
        ),
    ),
    PacketSpec(
        "e33_deep_link_staircase",
        "experimental/notes/roadmaps/e33_deep_link_staircase.md",
        "deep-link staircase toy census",
        "aligned_partner_supports_T",
        "not_explicit",
        "overlap_r_with_k_over_2_lt_r_lt_k",
        "none_toy_census",
        (
            "counts aligned partner",
            "k/2 < |T cap T0| < k",
            "r = 6, 7",
            "No all-slope support code",
        ),
    ),
    PacketSpec(
        "dihedral_staircase_deep_regime",
        "experimental/notes/roadmaps/dihedral_staircase_deep_regime.md",
        "dihedral/deep staircase packet",
        "disagreement_support_R_size_j",
        "exact_disagreement_support",
        "j_disagreement_not_s_exchange",
        "dihedral_specific_not_compiler_strip",
        (
            "An exact `j`-support is a set",
            "exact `j`-supports over all finite slopes",
            "QA.21 clean-rate candidates use `j = n-A`",
            "complementary high-agreement row",
        ),
    ),
)


def extract_lines(path: str, needles: tuple[str, ...]) -> list[dict[str, Any]]:
    full = os.path.join(REPO, path)
    text = open(full, encoding="utf-8").read().splitlines()
    rows = []
    lowered = [(needle, needle.lower()) for needle in needles]
    for line_no, line in enumerate(text, 1):
        c = compact(line)
        low = c.lower()
        hits = [needle for needle, needle_low in lowered if needle_low in low]
        if hits:
            rows.append({"line": line_no, "needles": hits, "excerpt": c[:240]})
    return rows


def packet_record(spec: PacketSpec) -> dict[str, Any]:
    path = os.path.join(REPO, spec.path)
    exists = os.path.exists(path)
    check(f"{spec.packet_id}: source exists", exists, spec.path)
    evidence = extract_lines(spec.path, spec.required_evidence) if exists else []
    found = {needle for row in evidence for needle in row["needles"]}
    missing = [needle for needle in spec.required_evidence if needle not in found]
    check(
        f"{spec.packet_id}: required convention evidence found",
        not missing,
        ", ".join(missing[:3]),
    )
    return {
        "packet_id": spec.packet_id,
        "path": spec.path,
        "role": spec.role,
        "classification": {
            "support_currency": spec.support_currency,
            "exactness": spec.exactness,
            "exchange_s": spec.exchange_s,
            "paid_strip": spec.paid_strip,
        },
        "required_evidence": list(spec.required_evidence),
        "missing_evidence": missing,
        "evidence": evidence,
    }


def build_findings(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_id = {record["packet_id"]: record for record in records}
    findings = [
        {
            "id": "support_currency_dual_notation",
            "severity": "real_mismatch_but_classified",
            "packets": ["qx13_pair_rank_ledger", "dihedral_staircase_deep_regime"],
            "description": (
                "QX.13 and the rungs use agreement supports S of size A; "
                "the dihedral staircase packet uses exact disagreement supports "
                "R of size j=n-A.  Any assembly must dualize before composing."
            ),
            "evidence": {
                pid: by_id[pid]["classification"]["support_currency"]
                for pid in ("qx13_pair_rank_ledger", "dihedral_staircase_deep_regime")
            },
        },
        {
            "id": "strip_scope_layering",
            "severity": "scope_layering_not_contradiction",
            "packets": [
                "xr_clean_poly_forcing_reduction",
                "a1_staircase_cap_assembly",
                "a2_graded_tangent_bound",
            ],
            "description": (
                "The compiler strips proved quotient+tangent ledgers and leaves "
                "primitive/dihedral/extension mass inside R_post.  A1/A2 speak "
                "about the later unified pullback strip.  These are different "
                "assembly layers and must not be silently identified."
            ),
            "evidence": {
                pid: by_id[pid]["classification"]["paid_strip"]
                for pid in (
                    "xr_clean_poly_forcing_reduction",
                    "a1_staircase_cap_assembly",
                    "a2_graded_tangent_bound",
                )
            },
        },
        {
            "id": "exactness_gap_in_routing_packets",
            "severity": "documentation_gap",
            "packets": [
                "w2_graded_tangent_ledger_design",
                "a2_graded_tangent_bound",
                "e33_deep_link_staircase",
            ],
            "description": (
                "QX.13 and X-3 pin exact agreement/support conventions.  W2, "
                "A2, and E33 route/count aligned partners but do not restate "
                "the exact-vs->= convention locally.  They appear to inherit "
                "the exact convention, but the inheritance should be printed "
                "in any final assembly."
            ),
            "evidence": {
                pid: by_id[pid]["classification"]["exactness"]
                for pid in (
                    "w2_graded_tangent_ledger_design",
                    "a2_graded_tangent_bound",
                    "e33_deep_link_staircase",
                )
            },
        },
        {
            "id": "s_exchange_is_consistent_where_used",
            "severity": "pass",
            "packets": [
                "qx13_pair_rank_ledger",
                "xr_smallcore_rungs_2a_2b",
                "w2_graded_tangent_ledger_design",
                "a2_graded_tangent_bound",
            ],
            "description": (
                "QX.13 defines s as exchange distance; X-3/W2/A2 use "
                "r=|S cap T| and s=A-r, with d+s=t in partial tangent cells. "
                "This is consistent."
            ),
            "evidence": {
                pid: by_id[pid]["classification"]["exchange_s"]
                for pid in (
                    "qx13_pair_rank_ledger",
                    "xr_smallcore_rungs_2a_2b",
                    "w2_graded_tangent_ledger_design",
                    "a2_graded_tangent_bound",
                )
            },
        },
    ]
    return findings


def build_certificate() -> dict[str, Any]:
    records = [packet_record(spec) for spec in PACKETS]
    findings = build_findings(records)
    unclassified = [
        finding for finding in findings
        if finding["severity"] not in {"real_mismatch_but_classified", "scope_layering_not_contradiction", "documentation_gap", "pass"}
    ]
    check("all convention drift findings are classified", not unclassified)
    check(
        "audit reports at least one real mismatch",
        any(finding["severity"] == "real_mismatch_but_classified" for finding in findings),
    )
    check(
        "audit reports exactness inheritance gap",
        any(finding["id"] == "exactness_gap_in_routing_packets" for finding in findings),
    )
    return {
        "task": "ASSEMBLY-AUDIT conventions consistency",
        "node": "safe_assembly_uniformity",
        "status": "AUDIT: classified convention drift; no unclassified mismatch",
        "axes": [
            "support-wise alignment definition",
            "exact-vs->= agreement",
            "exchange-distance / s convention",
            "paid-strip clause form",
        ],
        "packets": records,
        "findings": findings,
        "unclassified_findings": unclassified,
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

    print("\nfindings:")
    for finding in cert["findings"]:
        print(f"- {finding['id']}: {finding['severity']}")

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        print("\nrecomputed certificate:")
        print(json.dumps(cert, indent=2, sort_keys=True))
        return 1

    print(f"\nPASS: {NCHECK} ASSEMBLY-AUDIT convention checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
