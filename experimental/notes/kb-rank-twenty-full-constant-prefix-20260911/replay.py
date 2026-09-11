"""Offline bounded replay of the rank-twenty full-constant prefix payment."""

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
MANIFEST_HASH = "04f3b7c34e2ba8f39aec37413395a5ec6e82a38230514c59bfadc06ac1adeaa8"
PARENT = "9fce2f6588598b889ec6851620afde524c1f3a89"
PRIOR = "kb-rank-nineteen-source-payment-20260911"
HELPER_HASH = "18b47d3c66f493fa6948a8ce944aaa8691d1547bdd0b316de163701b483eb0c9"
ROOTS = ["rate_half_mca_rank_twenty_full_constant_prefix_payment"]
SCOPE = dict(
    lane="K3 / DIRECT", object="MCA", agreement=1116048,
    field="2130706433^6", n=2097152, k=1048576, target_epsilon="2^-128",
    original_error_rank=12, J=[9965,13964], actual_P2_rank=20,
    full_constant_dimension=11, shared_dimension=11,
    B_star="274980728111395087", near=134944, raw_cutoffs=[1,2],
    quantifier="Every complete post-near source and every valid original owner assignment at the printed scope",
    unit="Entire original distinct bad-slope set",
    source_bound="270378604704109625", reserve="4602123407285462",
    normalization_guard_required=False, actual_pencil_occupation_assumed=False,
    whole_source_alternatives="MAXIMUM, never addition",
    local_antecedent="After paid whole-source constant-pencil alternatives",
    anchors=8, factor_indices=list(range(2,10)),
    terminal_pair_dimension=4, terminal_shared_dimension=3,
    terminal_pencil_dimension=3, terminal_quotient_dimension=1,
    scalar_LIST_dimension=3, packing_budget=1048577,
    large_mass_threshold=349525, large_fibres_at_most=2,
    inside_charge="One global t", terminal_envelope="t+S*alpha+2*beta",
    original_weights_unchanged=True, original_union_complements=True,
    higher_raw_and_near_included_once=True, coefficient_field_unchanged=True,
    inherited_rank19_terminal_used=False,
    degree_profiles=5, covered_J_integers=4000, mass_boxes=3166,
    LIST_transitions=9498, certificate_shard_bytes=361476,
    declared_source_class_closed=True, whole_degree_closed=False,
    full_constant_tail_closed=False, all_rank20_closed=False,
    pair_ranks21_to22_closed=False, higher_original_error_ranks_closed=False,
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
    need(len(published) == 1681, "inherited source inventory")
    return prior, published, graph, dict(pins, **{PRIOR: branch.MANIFEST_HASH})


def validate(manifest, prior, published, credited, pins):
    need(manifest["schema"] == "kb-rank-twenty-full-constant-prefix-v1", "schema")
    need(manifest["parent_commit"] == PARENT and manifest["snapshot_roots"] == ROOTS,
         "snapshot identity")
    need(manifest["supplier_manifests"] == pins, "supplier pins")
    need(json.dumps(manifest["scope"], sort_keys=True) == json.dumps(SCOPE, sort_keys=True),
         "scope and types")
    need(manifest["inherited_proof_documents_compared"] == 337
         and manifest["published_source_hashes_checked"] == 1681, "inherited counts")
    files = {row["path"]: row for row in manifest["files"]}
    need(len(files) == len(manifest["files"]) == 16, "new file inventory")
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
    need(sum(map(len, sources.values())) == manifest["source_bytes"] == 397838,
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
    need(len(documents) == 337, "inherited proof inventory")
    graph = manifest["requirements"]
    need(len(graph) == 111 and set(graph) == set(manifest["origin_node_manifest_sha256"]),
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
    print("PASS 1697 listed source hashes; 337 inherited proof documents; 111-node acyclic closure;",
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
        (ROOTS[0], "verify.py"), (ROOTS[0], "verify_audit.py"),
        ("mca_rational_compression_fibre_weight", "verify.py"),
        ("mca_nested_product_all_coordinate_anchor", "verify.py"),
        ("rate_half_mca_regular_rational_plane_terminal_bounds", "verify_audit.py"),
    ]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    with tempfile.TemporaryDirectory(prefix="kb-rank-twenty-prefix-") as temp:
        runtime = Path(temp)
        for relative, data in runtime_sources.items():
            path = runtime/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        for name, filename in checks:
            path = runtime/"source/background/nodes"/name/filename
            command = [sys.executable, "-B"]+(["-O"] if sys.flags.optimize else [])+[str(path)]
            subprocess.run(command, cwd=runtime, env=env, check=True, timeout=20)
    print("PASS two new and three inherited focused checks from frozen sources")
    print("Other inherited arithmetic not freshly replayed; external mathematical review due")
    print("Declared rank20 full-constant prefix paid; its tail, other rank20 classes and both Prizes remain open")


if __name__ == "__main__":
    main()
