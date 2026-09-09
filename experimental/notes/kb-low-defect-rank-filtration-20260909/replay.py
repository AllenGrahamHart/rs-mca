"""Bounded custody and arithmetic checks, not automated proof certification."""

import copy
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
PARENT = "401ddd3350c15ff5ec7b2f65fa4988f65e7b3e52"
BASE = "low-core-flat-source-cumulative-20260908"
SPREAD = "kb-parameter-graph-spread-20260908"
BASE_HASH = "656b342982896233bf8f906b6ba93aae785c9179414d02f982f47b095a60027b"
SPREAD_HASH = "b93f34d83b297e4370a4d6cb3b949432f99ebb4293b059fc7a926fd6b427ce1c"
MANIFEST_HASH = "bc3b337d2c369a06ab82d5d6d5a2fa8f9edfe2931f34e0244b94345286d42645"
RAW = "mca_raw_margin_basis_mass"
FINITE = "rate_half_mca_low_raw_rank_filtration"
BOUNDARY = "mca_weighted_fiber_resource_method_boundary"
ASSEMBLY = "rate_half_mca_rank_twelve_paid_interval_assembly"
NEW = {
    RAW: ["mca_fiber_contraction_core_basis_resource", "mca_nonuniform_support_margin_resource"],
    FINITE: [RAW, "rate_half_mca_parameter_graph_spread", "mca_padded_johnson_scalar_descent",
             ASSEMBLY, "mca_maximal_margin_complete_core_selection"],
}
HELPER = "source/critical/nodes/mca_fiber_contraction_core_basis_resource/verify.py"


def need(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked_file(root, relative):
    need(isinstance(relative, str), "path must be a string")
    path = PurePosixPath(relative)
    need(not path.is_absolute() and ".." not in path.parts and str(path) == relative,
         "noncanonical path")
    target = root/path
    need(not any((root/Path(*path.parts[:i])).is_symlink()
                 for i in range(1, len(path.parts)+1)), "symlink in source path")
    need(target.resolve().is_relative_to(root.resolve()) and target.is_file(), "missing/escaping source")
    need(target.stat().st_size < 1024*1024, "oversized source")
    return target.read_bytes()


def validate(manifest):
    need(manifest["schema"] == "kb-low-defect-rank-filtration-v1", "schema")
    need(manifest["parent_commit"] == PARENT, "parent pin")
    need(manifest["new_roots"] == list(NEW), "two exact roots")
    inherited, sources = {}, {}
    for key, name, pin, count in (("base", BASE, BASE_HASH, 698),
                                  ("graph", SPREAD, SPREAD_HASH, 19)):
        need(manifest[key+"_packet"] == "../"+name, "supplier location")
        need(manifest[key+"_manifest_sha256"] == pin, "supplier pin")
        folder = ROOT.parent/name
        data = checked_file(folder, "SOURCE_MANIFEST.json")
        need(digest(data) == pin, "changed published manifest")
        supplier = json.loads(data)
        files = {row["path"]: row for row in supplier["files"]}
        need(len(files) == len(supplier["files"]) == count, "supplier inventory")
        for path, row in files.items():
            relative = row.get("source_path", row.get("origin_path"))
            need(path == "source/"+relative, "supplier source path")
            data = checked_file(folder, path)
            need(digest(data) == row["sha256"], "changed supplier source")
            sources.setdefault(path, []).append(data)
        inherited[key] = supplier
    files = {row["path"]: row for row in manifest["files"]}
    need(len(files) == len(manifest["files"]) == 18, "extension inventory")
    need(set(files) == {str(path.relative_to(ROOT)) for path in (ROOT/"source").rglob("*")
                        if path.is_file()}, "missing/unlisted extension source")
    for path, row in files.items():
        need(path == "source/"+row["origin_path"], "extension source path")
        data = checked_file(ROOT, path)
        need(digest(data) == row["sha256"], "changed extension source")
        sources.setdefault(path, []).append(data)
    need(all(data == sources[HELPER][0] for data in sources[HELPER]), "borrowed helper drift")
    old_graph = inherited["graph"]["requirements"]
    need(len(old_graph) == 74 and len(inherited["base"]["interval_extension_requirements"]) == 72,
         "inherited graph inventories")
    expected = {name: deps for name, deps in old_graph.items() if name != BOUNDARY}
    expected.update(NEW)
    graph = manifest["requirements"]
    need(graph == expected and len(graph) == 75, "exact dependency graph")
    need(set(manifest["origin_node_manifest_sha256"]) == set(graph), "node provenance inventory")
    done, active = set(), set()

    def visit(name):
        need(name not in active, "dependency cycle")
        if name in done:
            return
        active.add(name)
        for child in graph[name]:
            visit(child)
        active.remove(name)
        done.add(name)

    for name in NEW:
        visit(name)
        path = "source/background/nodes/"+name+"/node.json"
        data = checked_file(ROOT, path)
        node = json.loads(data)
        need(digest(data) == manifest["origin_node_manifest_sha256"][name], "new node provenance")
        need(node["node"]["id"] == name and node["node"]["status"] == "PROVED", "new node status")
        need([r["from"] for r in node["requires"]] == NEW[name], "new owned requirements")
        evidence = [] if name == RAW else [{"to": "rate_half_mca_global_core_rank_support_distance_router"}]
        need(node["evidence_for"] == evidence and not node["alternatives"] and not node["refutes"],
             "unchanged router interface")
    need(done == set(graph), "unreachable dependency")
    for name in graph:
        for filename in ("statement.md", "proof.md"):
            need(any(PurePosixPath(path).parent.name == name and PurePosixPath(path).name == filename
                     for path in sources), "unfrozen statement/proof")


def mutations(manifest):
    cases = []
    for key, value in (("schema", "wrong"), ("parent_commit", "0"*40),
                       ("base_manifest_sha256", "0"*64), ("graph_manifest_sha256", "0"*64),
                       ("base_packet", "../../"), ("graph_packet", "../../"),
                       ("new_roots", [FINITE])):
        bad = copy.deepcopy(manifest)
        bad[key] = value
        cases.append(bad)
    for key, value in (("path", "../../escape"), ("sha256", "0"*64), ("origin_path", "wrong")):
        bad = copy.deepcopy(manifest)
        bad["files"][0][key] = value
        cases.append(bad)
    bad = copy.deepcopy(manifest)
    bad["files"].append(bad["files"][0])
    cases.append(bad)
    bad = copy.deepcopy(manifest)
    bad["files"].pop()
    cases.append(bad)
    bad = copy.deepcopy(manifest)
    bad["requirements"][FINITE].append(FINITE)
    cases.append(bad)
    bad = copy.deepcopy(manifest)
    bad["requirements"][ASSEMBLY].append(FINITE)
    cases.append(bad)
    for bad in cases:
        try:
            validate(bad)
        except (ValueError, KeyError):
            continue
        raise ValueError("accepted malformed manifest")
    return len(cases)


def main():
    data = (ROOT/"SOURCE_MANIFEST.json").read_bytes()
    need(digest(data) == MANIFEST_HASH, "extension manifest pin")
    manifest = json.loads(data)
    validate(manifest)
    print("PASS 18 new and 717 inherited file hashes; 75-node acyclic graph;",
          mutations(manifest), "malformed manifests rejected", flush=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    for name, filename in ((RAW, "verify.py"), (FINITE, "verify.py"), (FINITE, "verify_audit.py")):
        path = ROOT/"source/background/nodes"/name/filename
        command = [sys.executable, "-B"]+(["-O"] if sys.flags.optimize else [])+[str(path)]
        subprocess.run(command, cwd=ROOT, env=env, check=True, timeout=20)
    print("PASS three focused checks; inherited arithmetic suites not replayed")
    print("Independent mathematical review due; complete-pair census and unrestricted row remain open")


if __name__ == "__main__":
    main()
