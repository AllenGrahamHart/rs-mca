"""Bounded serial controls for two theorems; not automated proof certification."""

import copy
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
BASE_HASH = "656b342982896233bf8f906b6ba93aae785c9179414d02f982f47b095a60027b"
MANIFEST_HASH = "b93f34d83b297e4370a4d6cb3b949432f99ebb4293b059fc7a926fd6b427ce1c"
BOUNDARY = "mca_weighted_fiber_resource_method_boundary"
SPREAD = "rate_half_mca_parameter_graph_spread"
NEW = {
    BOUNDARY: ["mca_projective_fiber_switching_resource", "mca_fiber_contraction_core_basis_resource"],
    SPREAD: ["rate_half_mca_scan_free_error_rank_eleven_payment",
             "rate_half_mca_rank_twelve_paid_interval_assembly", "mca_coordinate_weighted_collision_resource"],
}
HELPER = "source/critical/nodes/mca_fiber_contraction_core_basis_resource/verify.py"


def need(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked_file(root, relative):
    path = PurePosixPath(relative)
    need(isinstance(relative, str) and not path.is_absolute()
         and ".." not in path.parts and str(path) == relative, "noncanonical path")
    target = root/path
    need(not any((root/Path(*path.parts[:i])).is_symlink()
                 for i in range(1, len(path.parts)+1)), "symlink in source path")
    need(target.resolve().is_relative_to(root.resolve()) and target.is_file(), "missing/escaping source")
    need(target.stat().st_size < 1024*1024, "oversized source")
    return target.read_bytes()


def validate(manifest):
    need(manifest["schema"] == "kb-parameter-graph-spread-v1", "schema")
    need(manifest["parent_commit"] == "e21d9e41a8b5e40664e76deaeef80a06f2eec95e", "parent pin")
    need(manifest["base_packet"] == "../low-core-flat-source-cumulative-20260908", "base location")
    need(manifest["base_manifest_sha256"] == BASE_HASH, "base digest pin")
    need(manifest["new_roots"] == list(NEW), "two exact roots")
    base = ROOT.parent/"low-core-flat-source-cumulative-20260908"
    data = checked_file(base, "SOURCE_MANIFEST.json")
    need(digest(data) == BASE_HASH, "changed published supplier manifest")
    inherited = json.loads(data)
    base_files = {row["path"]: row for row in inherited["files"]}
    need(len(base_files) == len(inherited["files"]) == 698, "base inventory")
    for path, row in base_files.items():
        need(path == "source/"+row["source_path"], "base source path")
        need(digest(checked_file(base, path)) == row["sha256"], "changed base source")
    files = {row["path"]: row for row in manifest["files"]}
    need(len(files) == len(manifest["files"]) == 19, "extension inventory")
    need(set(files) == {str(path.relative_to(ROOT)) for path in (ROOT/"source").rglob("*")
                        if path.is_file()}, "missing or unlisted extension source")
    for path, row in files.items():
        need(path == "source/"+row["origin_path"], "extension source path")
        need(digest(checked_file(ROOT, path)) == row["sha256"], "changed extension source")
    need(files[HELPER]["sha256"] == base_files[HELPER]["sha256"], "borrowed helper must be identical")
    graph = manifest["requirements"]
    old_graph = inherited["interval_extension_requirements"]
    need(len(old_graph) == 72 and len(graph) == 74 and graph == dict(old_graph, **NEW),
         "exact dependency graph; no evidence-to-requirement promotion")
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
        node_path = "source/background/nodes/"+name+"/node.json"
        node = json.loads(checked_file(ROOT, node_path))
        need(digest(checked_file(ROOT, node_path)) == manifest["origin_node_manifest_sha256"][name],
             "new node provenance")
        need(node["node"]["id"] == name and node["node"]["status"] == "PROVED", "new node status")
        need([r["from"] for r in node["requires"]] == NEW[name], "new owned requirements")
        need(node["evidence_for"] == [{"to": "rate_half_mca_global_core_rank_support_distance_router"}]
             and not node["alternatives"] and not node["refutes"], "evidence-only router interface")
    need(done == set(graph), "unreachable dependency")
    for name in graph:
        for filename in ("statement.md", "proof.md"):
            need(any(PurePosixPath(p).parent.name == name and PurePosixPath(p).name == filename
                     for p in (*files, *base_files)), "unfrozen statement/proof")


def mutations(manifest):
    cases = []
    for key, value in (("schema", "wrong"), ("parent_commit", "0"*40),
                       ("base_manifest_sha256", "0"*64), ("base_packet", "../../"),
                       ("new_roots", [SPREAD])):
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
    bad["requirements"][SPREAD].append(SPREAD)
    cases.append(bad)
    bad = copy.deepcopy(manifest)
    bad["requirements"]["rate_half_mca_rank_twelve_paid_interval_assembly"].append(SPREAD)
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
    print("PASS 19 extension files, 698 inherited hashes, 74-node acyclic graph;",
          mutations(manifest), "malformed manifests rejected", flush=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    for name in NEW:
        for filename in ("verify.py", "verify_audit.py"):
            relative = "source/background/nodes/"+name+"/"+filename
            command = [sys.executable, "-B"]+(["-O"] if sys.flags.optimize else [])+[str(ROOT/relative)]
            subprocess.run(command, cwd=ROOT, env=env, check=True, timeout=20)
    print("PASS four focused checks; inherited arithmetic suite not replayed")
    print("Hand proofs still require independent mathematical review; no row or Prize closure")


if __name__ == "__main__":
    main()
