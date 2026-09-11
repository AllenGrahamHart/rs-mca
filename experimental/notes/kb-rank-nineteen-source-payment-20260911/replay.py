"""Offline bounded replay of the full rank-nineteen original-source payment."""

import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
MANIFEST_HASH = "1a22f451aa1bc65bc1e46e9ddcbe00c396ca6888496c18537e36455c7e05ce18"
PARENT = "4dd81e92f41bb2accb22fc188f9706d6e7c2f451"
PRIOR = "kb-full-constant-source-payment-20260911"
HELPER_HASH = "27fe6ff5c736459c047758ee6a66d2521d9d0a98bf56385a06768524dac09415"
ROOTS = ["mca_all_coordinate_pair_rank_descent","mca_small_pair_terminal_weight_bounds","rate_half_mca_all_coordinate_rank_nineteen_tail_payment","mca_normalization_ceiling_paid_anchor_descent","rate_half_mca_rank_nineteen_source_payment"]
SCOPE = dict(
    lane="K3 / DIRECT", object="MCA", agreement=1116048,
    field="2130706433^6", n=2097152, k=1048576, target_epsilon="2^-128",
    original_error_rank=12, J=[9965,21499], actual_P2_rank_at_most=19,
    B_star="274980728111395087", near=134944, raw_cutoffs=[1,2],
    quantifier="Every complete post-near source and every valid original owner assignment at the printed scope",
    unit="Entire original distinct bad-slope set",
    source_bound="274839785069298661", reserve="140943042096426",
    prefix_J=[9965,13964], prefix_source_bound="274462040894062110",
    new_regular_prefix_maximum="249682145677014171", tail_J=[13965,21499],
    generic_projection_guard_required=False, pencil_class_guard_required=False,
    normalization_guard_required=False, actual_pencil_occupation_assumed=False,
    original_source_remainder="Actual P2 ranks20,21,22 in the declared error-rank12 interval",
    excessive_finite_rank_drop_directions_at_most=[2,1,0],
    whole_source_alternatives="Combine whole-source caps by MAXIMUM, never addition",
    terminal_allowance_antecedent="Residual source AFTER proved whole-source pencil alternatives are removed",
    degree_excess="kappa=D-(s-1)", all_coordinates=True,
    U_child_joint_ranks=[0,1,2], G_child_joint_ranks=[1,2],
    nonregular_rank_two_children_paid=True, state_count_per_UG_table=42,
    low_ceiling_shared_dimensions=[3,11],
    ceiling_crossings="Paid by unrestricted-normalization prices, never free or discarded",
    geometric_budget_less_than_A_required=False,
    original_weights_unchanged=True, higher_raw_and_near_included_once=True,
    extra_regular_anchor_factor=False, coefficient_field_unchanged=True,
    tail_degree_bands=844, tail_LIST_transitions=190088, tail_UG_identities=64144,
    low_degree_bands=254, geometric_rows=1016, normalization_candidates=900184,
    quotient_intervals=160107, low_ceiling_identities=2032, inherited_low_UG_identities=19304,
    declared_rank19_source_class_closed=True, whole_degree_closed=False,
    pair_ranks20_to22_closed=False, higher_original_error_ranks_closed=False,
    active_v4_atom=False, ordinary_LIST_row_closed=False,
    adjacent_safe_row_closed=False, prize_closed=False,
)


def need(ok, why):
    if not ok:
        raise ValueError(why)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load_prior():
    path = ROOT.parent/PRIOR/"replay.py"
    need(not path.is_symlink() and path.stat().st_size < 65536, "prior helper path")
    need(digest(path.read_bytes()) == HELPER_HASH, "prior helper pin")
    spec = importlib.util.spec_from_file_location("frozen_branch_custody", path)
    branch = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(branch)
    prior, published, graph, pins = branch.load_prior()
    raw = prior.checked_file(branch.ROOT, "SOURCE_MANIFEST.json")
    need(digest(raw) == branch.MANIFEST_HASH, "parent manifest pin")
    manifest = json.loads(raw)
    sources = branch.validate(manifest, prior, published, graph, pins)
    published.update({(PRIOR, path): data for path, data in sources.items()})
    graph.update(manifest["requirements"])
    need(len(published) == 1613, "inherited source inventory")
    return prior, published, graph, dict(pins, **{PRIOR: branch.MANIFEST_HASH})


def validate(manifest, prior, published, credited, pins):
    need(manifest["schema"] == "kb-rank-nineteen-source-payment-v1", "schema")
    need(manifest["parent_commit"] == PARENT and manifest["snapshot_roots"] == ROOTS,
         "snapshot identity")
    need(manifest["supplier_manifests"] == pins, "supplier pins")
    need(json.dumps(manifest["scope"], sort_keys=True) == json.dumps(SCOPE, sort_keys=True),
         "scope and types")
    need(manifest["inherited_proof_documents_compared"] == 446
         and manifest["published_source_hashes_checked"] == 1613, "inherited counts")
    files = {row["path"]: row for row in manifest["files"]}
    need(len(files) == len(manifest["files"]) == 68, "new file inventory")
    actual = {str(p.relative_to(ROOT)) for p in (ROOT/"source").rglob("*") if p.is_file()}
    need(actual == set(files), "unlisted/missing source")
    sources = {}
    for relative, row in files.items():
        need(relative == "source/"+row["origin_path"], "origin identity")
        parts = PurePosixPath(row["origin_path"]).parts
        need(len(parts) >= 4 and parts[:2] == ("background", "nodes")
             and parts[2] in ROOTS, "source scope")
        data = prior.checked_file(ROOT, relative)
        need(digest(data) == row["sha256"], "new source pin")
        sources[relative] = data
    need(sum(map(len, sources.values())) == manifest["source_bytes"] == 8198982,
         "source byte inventory")
    documents = {}
    for row in manifest["inherited_sources"]:
        key = row["node"], row["filename"]
        need(key not in documents, "duplicate inherited document")
        data = published[row["packet"], row["path"]]
        parts = PurePosixPath(row["path"]).parts
        need(parts[0] == "source" and parts[2] == "nodes" and parts[3] == row["node"]
             and "/".join(parts[4:]) == row["filename"], "inherited identity")
        need(digest(data) == row["sha256"], "inherited document pin")
        documents[key] = data
    need(len(documents) == 446, "inherited proof inventory")
    graph = manifest["requirements"]
    need(len(graph) == 140 and set(graph) == set(manifest["origin_node_manifest_sha256"]),
         "closure inventory")
    for name, deps in graph.items():
        if name not in ROOTS:
            need(deps == credited[name], "inherited dependency drift")
            need(all((name, f) in documents for f in ("statement.md", "proof.md")),
                 "missing inherited proof")
            continue
        prefix = "source/background/nodes/"+name+"/"
        data = sources[prefix+"node.json"]
        need(digest(data) == manifest["origin_node_manifest_sha256"][name], "new node provenance")
        node = json.loads(data)
        need(node["node"]["id"] == name and node["node"]["status"] == "PROVED"
             and [edge["from"] for edge in node["requires"]] == deps, "new node status/graph")
        need(all(prefix+f in sources for f in ("statement.md", "proof.md")), "missing new proof")
    active, done = set(), set()

    def visit(name):
        need(name not in active, "dependency cycle")
        if name in done:
            return
        active.add(name)
        for child in graph[name]:
            visit(child)
        active.remove(name)
        done.add(name)

    for name in ROOTS:
        visit(name)
    need(done == set(graph), "unreachable dependency")
    return sources


def mutations(manifest, prior, published, graph, pins):
    cases = []
    for key, value in {"schema": "wrong", "parent_commit": "0"*40, "snapshot_roots": [],
                       "supplier_manifests": {}, "inherited_sources": [], "source_bytes": 0}.items():
        bad = copy.deepcopy(manifest)
        bad[key] = value
        cases.append(bad)
    for key in SCOPE:
        bad = copy.deepcopy(manifest)
        bad["scope"][key] = None
        cases.append(bad)
    for key, value in (("path", "../../escape"), ("origin_path", "wrong"), ("sha256", "0"*64)):
        bad = copy.deepcopy(manifest)
        bad["files"][0][key] = value
        cases.append(bad)
    for mode in ("duplicate", "missing", "cycle", "pin", "proof-pin"):
        bad = copy.deepcopy(manifest)
        if mode == "duplicate":
            bad["files"].append(bad["files"][0])
        elif mode == "missing":
            bad["files"].pop()
        elif mode == "cycle":
            bad["requirements"][ROOTS[0]].append(ROOTS[1])
        elif mode == "pin":
            bad["origin_node_manifest_sha256"][ROOTS[0]] = "0"*64
        else:
            bad["inherited_sources"][0]["sha256"] = "0"*64
        cases.append(bad)
    for bad in cases:
        try:
            validate(bad, prior, published, graph, pins)
        except (ValueError, KeyError, TypeError):
            continue
        raise ValueError("accepted malformed manifest")
    return len(cases)


def main():
    prior, published, graph, pins = load_prior()
    raw = prior.checked_file(ROOT, "SOURCE_MANIFEST.json")
    need(digest(raw) == MANIFEST_HASH, "manifest pin")
    manifest = json.loads(raw)
    sources = validate(manifest, prior, published, graph, pins)
    print("PASS 1681 listed source hashes; 446 inherited proof documents; 140-node acyclic closure;",
          mutations(manifest, prior, published, graph, pins), "malformed manifests rejected", flush=True)

    # Earlier amendments were checked by their own frozen custody validators.
    runtime_sources = {}
    for (_, relative), data in published.items():
        parts = PurePosixPath(relative).parts
        if (len(parts) >= 5 and parts[0] == "source" and parts[2] == "nodes"
                and parts[3] in manifest["requirements"]):
            runtime_sources[relative] = data
    need(not set(runtime_sources).intersection(sources), "new node runtime collision")
    runtime_sources.update(sources)
    checks = [
        (ROOTS[0], "verify.py"), (ROOTS[1], "verify.py"),
        (ROOTS[2], "verify.py"), (ROOTS[2], "verify_audit.py"),
        (ROOTS[3], "verify.py"),
        (ROOTS[4], "verify.py"), (ROOTS[4], "verify_audit.py"),
        ("rate_half_mca_regular_rational_plane_terminal_bounds", "verify_audit.py"),
        ("rate_half_mca_inherited_normalization_frontier", "verify_audit.py"),
        ("rational_curve_inner_projection_branch_budget", "verify.py"),
        ("polynomial_carrier_inner_projection_degree_ledger", "verify.py"),
    ]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    with tempfile.TemporaryDirectory(prefix="kb-rank-nineteen-") as temp:
        runtime = Path(temp)
        for relative, data in runtime_sources.items():
            path = runtime/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        for name, filename in checks:
            path = runtime/"source/background/nodes"/name/filename
            command = [sys.executable, "-B"]+(["-O"] if sys.flags.optimize else [])+[str(path)]
            subprocess.run(command, cwd=runtime, env=env, check=True, timeout=20)
    print("PASS seven new and four inherited focused checks from frozen sources")
    print("Other inherited arithmetic not freshly replayed; external mathematical review due")
    print("Declared rank<=19 source class paid; pair ranks20..22 and both Prizes remain open")


if __name__ == "__main__":
    main()
