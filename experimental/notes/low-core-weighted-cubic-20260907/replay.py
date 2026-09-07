"""Serial arithmetic/control replay, not certification of the hand proofs."""

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
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify_sources():
    manifest = json.loads((ROOT / "SOURCE_MANIFEST.json").read_text())
    require(manifest["schema"] == "low-core-weighted-cubic-source-v1", "wrong schema")
    seen = set()
    for record in manifest["files"]:
        path = record["path"]
        require(path not in seen, "duplicate source")
        seen.add(path)
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
    return len(seen)


def main():
    started = time.monotonic()
    count = verify_sources()
    env = dict(os.environ)
    env.pop("PYTHONOPTIMIZE", None)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    for check in CHECKS:
        result = subprocess.run([sys.executable, "-B", str(ROOT / check)],
                                cwd=ROOT, env=env, timeout=15, check=False,
                                capture_output=True, text=True)
        if result.returncode:
            print(result.stdout, end="")
            print(result.stderr, end="", file=sys.stderr)
            raise RuntimeError("FAIL: " + check)
        print("PASS", check, flush=True)
    print("PASS:", count, "frozen sources;", len(CHECKS), "serial checks;",
          "elapsed", round(time.monotonic() - started, 2), "seconds")
    print("CHECKS PASS; hand-proof review remains separate; d=7 and d=10 patterns UNPAID")


if __name__ == "__main__":
    try:
        main()
    except subprocess.TimeoutExpired as error:
        print("INCOMPLETE: checker exceeded 15 seconds:", error.cmd, file=sys.stderr)
        sys.exit(2)
    except (OSError, ValueError, KeyError, RuntimeError) as error:
        print("FAIL:", error, file=sys.stderr)
        sys.exit(1)
