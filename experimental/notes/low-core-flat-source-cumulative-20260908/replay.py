"""Serial arithmetic/control replay, not certification of the hand proofs."""

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
FINITE = "source/background/nodes/rate_half_mca_cancelled_low_core_relation_payment/"
GRAPH = "source/critical/nodes/mca_low_core_quadratic_graph_payment/"
STRIP = "source/background/nodes/rate_half_mca_low_core_kernel_quadratic_strip/"
JET = "source/critical/nodes/mca_polynomial_map_projective_jet_dimension/"
SMOOTH = "source/critical/nodes/mca_low_core_smooth_cubic_payment/"
RECEIVER_CHECKS = (
    "source/critical/nodes/mca_receiver_fiber_peeling/verify.py",
    "source/critical/nodes/rate_half_mca_receiver_fiber_payment/verify.py",
    "source/critical/nodes/rate_half_mca_receiver_fiber_payment/verify_audit.py",
    "source/critical/nodes/rate_half_mca_rank_twelve_paid_interval_assembly/verify.py",
)
CONTRACTION_CHECKS = (
    "source/critical/nodes/mca_fiber_contraction_core_basis_resource/verify.py",
    "source/critical/nodes/mca_fiber_contraction_core_basis_resource/verify_audit.py",
    "source/critical/nodes/rate_half_mca_fiber_contraction_interval/verify.py",
    "source/critical/nodes/rate_half_mca_fiber_contraction_interval/verify_audit.py",
    "source/critical/nodes/rate_half_mca_rank_twelve_paid_interval_assembly/verify.py",
)
CHECKS = (
    FINITE + "verify.py", FINITE + "verify_audit.py",
    FINITE + "verify_rational_pencil_cover.py",
    FINITE + "verify_rational_pencil_cover_audit.py",
    FINITE + "verify_polynomial_graph.py", FINITE + "verify_polynomial_graph_audit.py",
    FINITE + "verify_automatic_graph.py", FINITE + "verify_automatic_graph_audit.py",
    FINITE + "verify_homogeneous_level.py", FINITE + "verify_homogeneous_level_audit.py",
    FINITE + "verify_all_conics.py", FINITE + "verify_all_conics_audit.py",
    GRAPH + "verify_small.py", GRAPH + "verify_polynomial_graph_controls.py",
    GRAPH + "verify_rational_graph_controls.py", GRAPH + "verify_moving_parabola.py",
    "source/critical/nodes/mca_low_core_homogeneous_level_payment/verify_small.py",
    "source/critical/nodes/mca_maximal_margin_complete_core_selection/verify_controls.py",
    "source/background/nodes/mca_low_core_polynomial_relation_payment/verify_rational_line_controls.py",
    STRIP + "verify.py", STRIP + "verify_audit.py",
    JET + "verify.py", JET + "verify_audit.py",
    JET + "verify_moving_projection.py", JET + "verify_moving_projection_audit.py",
    SMOOTH + "verify.py", SMOOTH + "verify_audit.py",
    "source/critical/nodes/mca_normalization_unit_curve_payment/verify.py",
    STRIP + "verify_cubic_obstruction.py", STRIP + "verify_cubic_obstruction_audit.py",
    STRIP + "verify_affine_singular_normal_form.py",
    "source/critical/nodes/mca_singular_cubic_weighted_incidence_payment/verify.py",
    "source/critical/nodes/mca_singular_cubic_weighted_incidence_payment/verify_completed_high.py",
    "source/critical/nodes/mca_singular_cubic_weighted_incidence_payment/verify_audit.py",
    "source/critical/nodes/mca_core_completed_basis_margin_resource/verify_small.py",
    "source/critical/nodes/mca_geometric_progression_singular_cubic_payment/verify.py",
    "source/critical/nodes/mca_geometric_progression_singular_cubic_payment/verify_audit.py",
    "source/critical/nodes/mca_singular_cubic_component_list_payment/verify.py",
    "source/critical/nodes/mca_singular_cubic_component_list_payment/verify_audit.py",
    "source/critical/nodes/mca_singular_cubic_component_list_payment/verify_next_interval.py",
    "source/critical/nodes/mca_singular_cubic_component_list_payment/verify_next_interval_audit.py",
    "source/critical/nodes/mca_geometric_progression_singular_cubic_payment/verify_single_fiber.py",
    "source/critical/nodes/mca_geometric_progression_singular_cubic_payment/verify_single_fiber_audit.py",
    "source/critical/nodes/mca_multiplicity_interpolation_curve_escape/verify.py",
    "source/critical/nodes/mca_multiplicity_interpolation_curve_escape/verify_audit.py",
    "source/critical/nodes/mca_projective_split_product_list_payment/verify.py",
    "source/critical/nodes/mca_projective_split_product_list_payment/verify_audit.py",
    STRIP + "verify_quartic_obstruction.py", STRIP + "verify_quartic_obstruction_audit.py",
    STRIP + "verify_quartic_multiplier_geometry.py",
    STRIP + "verify_quartic_multiplier_geometry_audit.py",
    STRIP + "verify_low_cutoff_strip.py", STRIP + "verify_low_cutoff_strip_audit.py",
    STRIP + "verify_double_point_cubic_tail.py",
    STRIP + "verify_double_point_cubic_tail_audit.py",
    STRIP + "verify_raw_weighted_strip.py",
    STRIP + "verify_raw_weighted_strip_audit.py",
    "source/critical/nodes/mca_multiplicity_interpolation_curve_escape/verify_cubic_recipe_boundary.py",
    "source/critical/nodes/mca_projective_flat_core_basis_resource/verify.py",
    "source/critical/nodes/mca_projective_flat_core_basis_resource/verify_audit.py",
    "source/critical/nodes/mca_projective_fiber_core_basis_resource/verify.py",
    "source/critical/nodes/mca_projective_fiber_core_basis_resource/verify_audit.py",
    "source/critical/nodes/mca_maximum_density_flat_core_basis_resource/verify.py",
    "source/critical/nodes/mca_maximum_density_flat_core_basis_resource/verify_audit.py",
    "source/critical/nodes/rate_half_mca_maximum_density_high_interval/verify.py",
    "source/critical/nodes/rate_half_mca_maximum_density_high_interval/verify_audit.py",
    "source/critical/nodes/rate_half_mca_rank_twelve_paid_interval_assembly/verify.py",
    "source/background/nodes/mca_common_core_low_margin_transport/verify_small.py",
    "source/background/nodes/rate_half_mca_error_rank_twelve_common_core_forcing/verify_core_transport.py",
    "source/background/nodes/rate_half_mca_error_rank_twelve_common_core_forcing/verify_basis_child_payment.py",
    "source/background/nodes/rate_half_mca_error_rank_twelve_common_core_forcing/verify_basis_child_audit.py",
    "source/background/nodes/rate_half_mca_error_rank_twelve_common_core_forcing/verify.py",
    "source/background/nodes/rate_half_mca_error_rank_twelve_common_core_forcing/verify_audit.py",
    "source/background/nodes/mca_padded_johnson_scalar_descent/verify.py",
    "source/background/nodes/mca_scalar_agreement_dimension_descent/verify.py",
    "source/background/nodes/mca_scalar_agreement_dimension_descent/verify_two_anchor.py",
    "source/background/nodes/rate_half_mca_scan_free_error_rank_eleven_payment/verify_caps.py",
    "source/critical/nodes/bchks_affine_witness_collinearity_mca/verify_exact_gate.py",
) + CONTRACTION_CHECKS[:-1] + RECEIVER_CHECKS[:-1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify_dependency_inventory(manifest, sources):
    graph = manifest["interval_extension_requirements"]
    root = manifest["interval_extension_root"]
    require(root == "rate_half_mca_rank_twelve_paid_interval_assembly", "wrong proof root")
    require(len(graph) == 40, "changed proof inventory")
    active, seen = set(), set()

    def visit(node):
        require(node not in active, "cyclic proof inventory")
        if node in seen:
            return
        require(node in graph, "missing proof requirement")
        active.add(node)
        for filename in ("statement.md", "proof.md"):
            require(any("source/" + base + "/" + node + "/" + filename in sources
                        for base in ("critical/nodes", "background/nodes")),
                    "missing proof document: " + node + "/" + filename)
        for dependency in graph[node]:
            visit(dependency)
        active.remove(node)
        seen.add(node)

    visit(root)
    require(seen == set(graph), "unreachable proof inventory")


def verify_sources(manifest=None):
    if manifest is None:
        manifest = json.loads((ROOT / "SOURCE_MANIFEST.json").read_text())
    require(manifest["schema"] == "low-core-flat-source-cumulative-v1", "wrong schema")
    seen = set()
    for record in manifest["files"]:
        path = record["path"]
        require(path not in seen, "duplicate source")
        seen.add(path)
        require(path == "source/" + record["source_path"], "source-path mismatch")
        candidate = ROOT / path
        require(candidate.resolve().is_relative_to(ROOT / "source"), "nonlocal source")
        require(not candidate.is_symlink(), "symlink source")
        require(candidate.stat().st_size <= 128 * 1024, "oversized source")
        digest = hashlib.sha256(candidate.read_bytes()).hexdigest()
        require(digest == record["sha256"], "source drift: " + path)
    actual = {str(path.relative_to(ROOT)) for path in (ROOT / "source").rglob("*")
              if path.is_file()}
    require(actual == seen, "unlisted or missing source")
    require(set(CHECKS) <= seen, "unfrozen checker")
    verify_dependency_inventory(manifest, seen)
    return len(seen)


def verify_manifest_mutations():
    baseline = json.loads((ROOT / "SOURCE_MANIFEST.json").read_text())
    bad = []
    changed = copy.deepcopy(baseline)
    changed["files"][0]["sha256"] = "0" * 64
    bad.append(changed)
    changed = copy.deepcopy(baseline)
    changed["files"].append(copy.deepcopy(changed["files"][0]))
    bad.append(changed)
    changed = copy.deepcopy(baseline)
    changed["files"].pop()
    bad.append(changed)
    changed = copy.deepcopy(baseline)
    changed["files"][0].update(path="source/../../agents.md",
                               source_path="../../agents.md")
    bad.append(changed)
    changed = copy.deepcopy(baseline)
    changed["interval_extension_requirements"].pop(changed["interval_extension_root"])
    bad.append(changed)
    changed = copy.deepcopy(baseline)
    root = changed["interval_extension_root"]
    changed["interval_extension_requirements"][root].append(root)
    bad.append(changed)
    for changed in bad:
        try:
            verify_sources(changed)
        except (ValueError, OSError):
            continue
        raise ValueError("accepted a malformed source manifest")
    verify_sources(baseline)
    print("PASS: six source/inventory mutations rejected; baseline still passes")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--contraction-only", action="store_true",
                       help="run the five contraction checks; propagate -O")
    group.add_argument("--receiver-only", action="store_true",
                       help="run the four receiver-fiber checks; propagate -O")
    args = parser.parse_args()
    started = time.monotonic()
    count = verify_sources()
    verify_manifest_mutations()
    env = dict(os.environ)
    env.pop("PYTHONOPTIMIZE", None)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    selected = (RECEIVER_CHECKS if args.receiver_only else
                CONTRACTION_CHECKS if args.contraction_only else CHECKS)
    focused = args.contraction_only or args.receiver_only
    optimization = ["-O"] if focused and sys.flags.optimize else []
    for check in selected:
        result = subprocess.run([sys.executable, "-B", *optimization, str(ROOT / check)],
                                cwd=ROOT, env=env, timeout=15, check=False,
                                capture_output=True, text=True)
        if result.returncode:
            print(result.stdout, end="")
            print(result.stderr, end="", file=sys.stderr)
            raise RuntimeError("FAIL: " + check)
        print("PASS", check, flush=True)
    print("PASS:", count, "frozen sources;", len(selected), "serial checks;",
          "elapsed", round(time.monotonic() - started, 2), "seconds")
    print("Child optimization:", "-O" if optimization else "off")
    print("CHECKS PASS; 40-node proof inventory; original rank-twelve residual J=9941..52999")
    print("Additional receiver-fiber classes paid; no new whole-J interval claimed")
    print("Hand proofs are not certified by replay; higher ranks, unrestricted row and both prizes OPEN")


if __name__ == "__main__":
    try:
        main()
    except subprocess.TimeoutExpired as error:
        print("INCOMPLETE: checker exceeded 15 seconds:", error.cmd, file=sys.stderr)
        sys.exit(2)
    except (OSError, ValueError, KeyError, RuntimeError) as error:
        print("FAIL:", error, file=sys.stderr)
        sys.exit(1)
