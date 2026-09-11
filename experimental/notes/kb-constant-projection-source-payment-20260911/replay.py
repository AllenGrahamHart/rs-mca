"""Offline bounded replay of three constant-projection source theorems."""

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
MANIFEST_HASH = "9731c60403a1138ef5a1f219d42ded1b14def768b8b0f879ae5ae5265adbc8ca"
PARENT = "90df1307edfd8e5cab657e862caa42c74ccdd359"
PRIOR = "kb-rank-twenty-full-constant-prefix-20260911"
HELPER_HASH = "872841685acdcfdacfc9e06fce39cdbb67b1edfad24e5ecc2f46033fb9259288"
ROOTS = ["mca_constant_projection_singleton_fibre_census", "rate_half_mca_projection_rank_nine_source_payment", "rate_half_mca_raw_one_projection_rank_nine_source_tail_payment"]
SCOPE = {
    "lane": "K3 / DIRECT",
    "object": "MCA",
    "agreement": 1116048,
    "field": "2130706433^6",
    "n": 2097152,
    "k": 1048576,
    "target_epsilon": "2^-128",
    "original_error_rank": 12,
    "B_star": "274980728111395087",
    "near": 134944,
    "quantifier": "Every complete post-near source and every valid original owner assignment at the printed scope",
    "unit": "Entire original distinct bad-slope set",
    "projection_row": "One nonzero ORIGINAL-field constant row",
    "projection_affine_dimension_max": 9,
    "P2_case": {
    "J": [9965, 21499],
    "covered_J_integers": 11535,
    "bound": "270000000000000000",
    "reserve": "4980728111395087",
    "raw_cutoffs": [1, 2],
    "actual_P2_rank_restriction": False,
    "full_constant_rank20_equivalence": True
},
    "P1_case": {
    "J": [11925, 21499],
    "covered_J_integers": 9575,
    "bound": "274976274292770934",
    "reserve": "4453818624153",
    "raw_cutoff": 1,
    "P2_rank_restriction": False,
    "P2_projection_restriction": False,
    "previous_J": 11924,
    "previous_recipe": "274989633599798446",
    "previous_endpoint_unsafe_witness": False
},
    "raw_caps": ["31878195092556089", "31881321436908964"],
    "generic_rich_threshold": "n-2*A+K-1",
    "generic_census": "t+(n-A)*Q(n-A)+sum_bins u*P(l)*Q(u)",
    "generic_lemma_official_row_required": False,
    "projected_scalar_dimension": 9,
    "on_scalar_dimension": 11,
    "complement_min": 569051,
    "rich_complement_max": [913633, 913635],
    "global_inside_charge": "One global t",
    "anchors": 0,
    "packing_budget_assumed": False,
    "actual_pencil_occupation_assumed": False,
    "normalization_guard_required": False,
    "rank19_terminal_used": False,
    "original_weights_and_complete_unions": True,
    "whole_source_alternatives": "MAXIMUM, never addition",
    "higher_raw_and_near_included_once": True,
    "coefficient_field_unchanged": True,
    "gate_profiles": 13,
    "P2_bins": 70,
    "P2_LIST_transitions": 1418,
    "P1_bins": 35,
    "P1_LIST_transitions": 709,
    "full_constant_rank20_original_gap_paid": True,
    "all_rank20_closed": False,
    "all_original_rank12_sources_closed": False,
    "active_v4_atom": False,
    "ordinary_LIST_row_closed": False,
    "adjacent_safe_row_closed": False,
    "prize_closed": False
}


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
    need(len(published) == 1697, "inherited source inventory")
    return prior, published, graph, dict(pins, **{PRIOR: branch.MANIFEST_HASH})


def validate(manifest, prior, published, credited, pins):
    need(manifest["schema"] == "kb-constant-projection-source-payment-v1", "schema")
    need(manifest["parent_commit"] == PARENT and manifest["snapshot_roots"] == ROOTS,
         "snapshot identity")
    need(manifest["supplier_manifests"] == pins, "supplier pins")
    need(json.dumps(manifest["scope"], sort_keys=True) == json.dumps(SCOPE, sort_keys=True),
         "scope and types")
    need(manifest["inherited_proof_documents_compared"] == 333
         and manifest["published_source_hashes_checked"] == 1697, "inherited counts")
    files = {row["path"]: row for row in manifest["files"]}
    need(len(files) == len(manifest["files"]) == 32, "new file inventory")
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
    need(sum(map(len, sources.values())) == manifest["source_bytes"] == 163908,
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
    need(len(documents) == 333, "inherited proof inventory")
    graph = manifest["requirements"]
    need(len(graph) == 112 and set(graph) == set(manifest["origin_node_manifest_sha256"]),
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
            bad["requirements"][ROOTS[0]].append(ROOTS[0])
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
    print("PASS 1729 listed source hashes; 333 inherited proof documents; 112-node acyclic closure;",
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
        (ROOTS[0], "verify.py"),
        (ROOTS[1], "verify.py"), (ROOTS[1], "verify_audit.py"),
        (ROOTS[2], "verify.py"), (ROOTS[2], "verify_audit.py"),
        ("rate_half_mca_min_envelope_raw_mass", "verify.py"),
        ("rate_half_mca_min_envelope_raw_mass", "verify_audit.py"),
        ("rate_half_mca_regular_rational_plane_terminal_bounds", "verify_audit.py"),
    ]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    with tempfile.TemporaryDirectory(prefix="kb-constant-projection-") as temp:
        runtime = Path(temp)
        for relative, data in runtime_sources.items():
            path = runtime/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        for name, filename in checks:
            path = runtime/"source/background/nodes"/name/filename
            command = [sys.executable, "-B"]+(["-O"] if sys.flags.optimize else [])+[str(path)]
            subprocess.run(command, cwd=runtime, env=env, check=True, timeout=20)
    print("PASS five new and three inherited focused checks from frozen sources")
    print("Other inherited arithmetic not freshly replayed; external mathematical review due")
    print("Full-constant rank20 gap and P1-projection source tail paid; other classes and both Prizes remain open")


if __name__ == "__main__":
    main()
