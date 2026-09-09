"""Check frozen custody and exact arithmetic; not automated proof certification."""

import copy
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
PARENT = "78a12ec166916babdb1a557744525de6eef5d931"
BASE = "low-core-flat-source-cumulative-20260908"
BASE_HASH = "656b342982896233bf8f906b6ba93aae785c9179414d02f982f47b095a60027b"
MANIFEST_HASH = "375c15045f34386d787b559a8705fc1c1f66653ce5a6568630a2d0f79ee75bbc"
RAW = "mca_raw_margin_basis_mass"
CUBIC = "rate_half_mca_raw_mass_cubic_interval"
ASSEMBLY = "rate_half_mca_rank_twelve_paid_interval_assembly"
ROOTS = [RAW, CUBIC, ASSEMBLY]
NEW = {
    RAW: ["mca_fiber_contraction_core_basis_resource", "mca_nonuniform_support_margin_resource"],
    CUBIC: [RAW, "mca_multiplicity_interpolation_curve_escape",
            "rate_half_mca_cancelled_low_core_relation_payment",
            "mca_singular_cubic_weighted_incidence_payment",
            "mca_singular_cubic_component_list_payment",
            "mca_geometric_progression_singular_cubic_payment"],
}
REFRESH = {
    "rate_half_mca_low_core_kernel_quadratic_strip",
    "mca_geometric_progression_singular_cubic_payment",
    "mca_multiplicity_interpolation_curve_escape",
    "mca_singular_cubic_component_list_payment",
    "rate_half_mca_fiber_contraction_interval",
}
HELPER = "source/critical/nodes/mca_fiber_contraction_core_basis_resource/verify.py"


def need(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked_file(root, relative):
    need(isinstance(relative, str), "path type")
    path = PurePosixPath(relative)
    need(not path.is_absolute() and ".." not in path.parts and str(path) == relative,
         "noncanonical path")
    need(not any((root/Path(*path.parts[:i])).is_symlink()
                 for i in range(1, len(path.parts)+1)), "source symlink")
    target = root/path
    need(target.resolve().is_relative_to(root.resolve()) and target.is_file(), "missing/escaping source")
    need(target.stat().st_size < 1024*1024, "oversized source")
    return target.read_bytes()


def validate(manifest):
    need(manifest["schema"] == "kb-raw-mass-cubic-interval-v1", "schema")
    need(manifest["parent_commit"] == PARENT, "parent pin")
    need(manifest["snapshot_roots"] == ROOTS, "three exact snapshots")
    need(manifest["base_packet"] == "../"+BASE, "supplier location")
    need(manifest["base_manifest_sha256"] == BASE_HASH, "supplier pin")
    need(manifest["bound_including_near"] == 274861473951141154
         and manifest["reserve"] == 119254160253933, "bound and reserve")
    need(manifest["inherited_proof_documents_compared"] == 225, "comparison inventory")
    folder = ROOT.parent/BASE
    data = checked_file(folder, "SOURCE_MANIFEST.json")
    need(digest(data) == BASE_HASH, "changed supplier manifest")
    supplier = json.loads(data)
    inherited, sources = {}, {}
    for row in supplier["files"]:
        path = row["path"]
        need(path == "source/"+row["source_path"] and path not in inherited, "supplier path")
        data = checked_file(folder, path)
        need(digest(data) == row["sha256"], "changed supplier source")
        inherited[path] = data
        p = PurePosixPath(path)
        sources[p.parent.name, p.name] = data
    need(len(inherited) == 698, "inherited inventory")
    files = {row["path"]: row for row in manifest["files"]}
    need(len(files) == len(manifest["files"]) == 34, "extension inventory")
    need(set(files) == {str(p.relative_to(ROOT)) for p in (ROOT/"source").rglob("*") if p.is_file()},
         "missing/unlisted source")
    for path, row in files.items():
        need(path == "source/"+row["origin_path"], "extension source path")
        data = checked_file(ROOT, path)
        need(digest(data) == row["sha256"], "changed extension source")
        p = PurePosixPath(path)
        need(p.parent.name in ROOTS or path == HELPER
             or (p.parent.name in REFRESH and p.name == "statement.md"), "unexpected source")
        sources[p.parent.name, p.name] = data
    need(checked_file(ROOT, HELPER) == inherited[HELPER], "borrowed helper drift")
    refresh = manifest["refreshed_supplier_statements"]
    need(set(refresh) == REFRESH, "five reviewed statement refreshes")
    for name, row in refresh.items():
        old = PurePosixPath(row["base_path"])
        need(old.parent.name == name and old.name == "statement.md", "summary source identity")
        need(digest(inherited["source/"+str(old)]) == row["base_sha256"], "summary prior pin")
        need(digest(sources[name, "statement.md"]) == row["current_sha256"], "summary current pin")
    old = supplier["interval_extension_requirements"]
    need(len(old) == 72, "old assembly inventory")
    expected = {name: list(deps) for name, deps in old.items()}
    expected[ASSEMBLY].append(CUBIC)
    expected.update(NEW)
    graph = manifest["requirements"]
    need(graph == expected and len(graph) == 74, "exact dependency graph")
    need(set(manifest["origin_node_manifest_sha256"]) == set(graph), "node provenance inventory")
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

    visit(ASSEMBLY)
    need(done == set(graph), "unreachable dependency")
    for name in ROOTS:
        data = sources[name, "node.json"]
        need(digest(data) == manifest["origin_node_manifest_sha256"][name], "snapshot node provenance")
        node = json.loads(data)
        need(node["node"]["id"] == name and node["node"]["status"] == "PROVED", "snapshot status")
        need([edge["from"] for edge in node["requires"]] == graph[name], "snapshot requirements")
        evidence = [] if name == RAW else [{"to": "rate_half_mca_global_core_rank_support_distance_router"}]
        need(node["evidence_for"] == evidence and not node["alternatives"] and not node["refutes"],
             "router evidence is not a proved requirement")
    for name in graph:
        for filename in ("statement.md", "proof.md"):
            need((name, filename) in sources, "unfrozen statement/proof")


def mutations(manifest):
    cases = []
    for key, value in (("schema", "wrong"), ("parent_commit", "0"*40),
                       ("base_manifest_sha256", "0"*64), ("base_packet", "../../"),
                       ("snapshot_roots", [CUBIC]), ("bound_including_near", 0),
                       ("reserve", 0), ("refreshed_supplier_statements", {})):
        bad = copy.deepcopy(manifest)
        bad[key] = value
        cases.append(bad)
    for key, value in (("path", "../../escape"), ("origin_path", "wrong"), ("sha256", "0"*64)):
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
    bad["requirements"][CUBIC].append(ASSEMBLY)
    cases.append(bad)
    bad = copy.deepcopy(manifest)
    bad["requirements"][ASSEMBLY].remove(CUBIC)
    cases.append(bad)
    bad = copy.deepcopy(manifest)
    bad["origin_node_manifest_sha256"][RAW] = "0"*64
    cases.append(bad)
    for bad in cases:
        try:
            validate(bad)
        except (KeyError, ValueError):
            continue
        raise ValueError("accepted malformed manifest")
    return len(cases)


def main():
    data = checked_file(ROOT, "SOURCE_MANIFEST.json")
    need(digest(data) == MANIFEST_HASH, "manifest pin")
    manifest = json.loads(data)
    validate(manifest)
    print("PASS 34 new and 698 inherited hashes; 74-node acyclic graph;",
          mutations(manifest), "malformed manifests rejected", flush=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    for name, filename in ((RAW, "verify.py"), (CUBIC, "verify.py"),
                           (CUBIC, "verify_audit.py"), (ASSEMBLY, "verify.py")):
        path = ROOT/"source/critical/nodes"/name/filename
        command = [sys.executable, "-B"]+(["-O"] if sys.flags.optimize else [])+[str(path)]
        subprocess.run(command, cwd=ROOT, env=env, check=True, timeout=20)
    print("PASS four focused checks; inherited arithmetic suites not freshly replayed")
    print("Independent mathematical review due; unrestricted MCA, LIST and both Prizes remain open")


if __name__ == "__main__":
    main()
