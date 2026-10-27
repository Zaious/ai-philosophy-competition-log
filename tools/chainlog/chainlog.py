#!/usr/bin/env python3
"""chainlog: tamper-evident hash chain over a line-oriented log (e.g. a chat log kept as NDJSON).

Scheme (format "chainlog-v1"):
    leaf_i  = SHA-256(raw line i, UTF-8, without the line terminator)
    chain_0 = SHA-256(b"CHAINLOG-v1")
    chain_i = SHA-256(chain_{i-1} || leaf_i)        # both as 32 raw bytes
    root    = chain_n

A bundle directory holds:
    manifest.json    format, genesis label, record count, root
    leaves.csv       index (1-based), leaf_sha256, chain_sha256  -- hashes only
    disclosed.jsonl  optional: {"index": i, "raw": "<line>"} for the records you choose to publish in full

Records you do not publish stay verifiable as hashes. Anyone holding the original file can check every line.

Commands:
    chainlog.py build   LOG.ndjson OUTDIR [--disclose 1-5,9]
    chainlog.py verify  OUTDIR [--source LOG.ndjson]
    chainlog.py commit  OUTDIR            # prints the SHA-256 of manifest.json, to post as a commitment
    chainlog.py selftest                  # builds a demo bundle and checks that tampering is detected
Standard library only.
"""
import argparse
import csv
import hashlib
import json
import os
import sys
import tempfile

FORMAT = "chainlog-v1"
GENESIS = b"CHAINLOG-v1"


def sha(b):
    return hashlib.sha256(b).digest()


def read_lines(path):
    with open(path, "rb") as fh:
        data = fh.read()
    lines = data.split(b"\n")
    if lines and lines[-1] == b"":
        lines.pop()
    return [ln[:-1] if ln.endswith(b"\r") else ln for ln in lines]


def chain_from_leaves(leaves):
    prev = sha(GENESIS)
    out = []
    for leaf in leaves:
        prev = sha(prev + leaf)
        out.append(prev)
    return out


def parse_selection(spec, n):
    chosen = set()
    if not spec:
        return chosen
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            chosen.update(range(int(a), int(b) + 1))
        else:
            chosen.add(int(part))
    bad = [i for i in chosen if i < 1 or i > n]
    if bad:
        raise SystemExit(f"selection out of range 1..{n}: {sorted(bad)}")
    return chosen


def build(log_path, out_dir, disclose=""):
    lines = read_lines(log_path)
    leaves = [sha(ln) for ln in lines]
    chain = chain_from_leaves(leaves)
    os.makedirs(out_dir, exist_ok=True)
    manifest = {"format": FORMAT, "genesis": GENESIS.decode(), "count": len(lines), "root": chain[-1].hex() if chain else sha(GENESIS).hex()}
    with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(manifest, fh, indent=2)
        fh.write("\n")
    with open(os.path.join(out_dir, "leaves.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["index", "leaf_sha256", "chain_sha256"])
        for i, (lf, ch) in enumerate(zip(leaves, chain), 1):
            w.writerow([i, lf.hex(), ch.hex()])
    chosen = parse_selection(disclose, len(lines))
    with open(os.path.join(out_dir, "disclosed.jsonl"), "w", encoding="utf-8", newline="\n") as fh:
        for i in sorted(chosen):
            fh.write(json.dumps({"index": i, "raw": lines[i - 1].decode("utf-8")}, ensure_ascii=False) + "\n")
    return manifest


def verify(out_dir, source=None):
    """Returns a list of problems; empty list means the bundle is consistent."""
    problems = []
    with open(os.path.join(out_dir, "manifest.json"), encoding="utf-8") as fh:
        manifest = json.load(fh)
    if manifest.get("format") != FORMAT:
        problems.append(f"unknown format {manifest.get('format')!r}")
    rows = []
    with open(os.path.join(out_dir, "leaves.csv"), encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            rows.append(r)
    if [int(r["index"]) for r in rows] != list(range(1, len(rows) + 1)):
        problems.append("leaves.csv indices are not 1..n in order")
    if manifest.get("count") != len(rows):
        problems.append(f"manifest count {manifest.get('count')} != {len(rows)} leaf rows")
    try:
        leaves = [bytes.fromhex(r["leaf_sha256"]) for r in rows]
    except ValueError:
        return problems + ["leaves.csv contains a non-hex leaf"]
    chain = chain_from_leaves(leaves)
    for r, c in zip(rows, chain):
        if r["chain_sha256"] != c.hex():
            problems.append(f"chain value mismatch at record {r['index']}")
            break
    root = chain[-1].hex() if chain else sha(GENESIS).hex()
    if manifest.get("root") != root:
        problems.append("manifest root does not match the recomputed root")
    disc = os.path.join(out_dir, "disclosed.jsonl")
    if os.path.exists(disc):
        with open(disc, encoding="utf-8") as fh:
            for ln in fh:
                if not ln.strip():
                    continue
                d = json.loads(ln)
                i = d["index"]
                if not (1 <= i <= len(leaves)):
                    problems.append(f"disclosed record {i} is out of range")
                elif sha(d["raw"].encode("utf-8")) != leaves[i - 1]:
                    problems.append(f"disclosed record {i} does not match its leaf hash")
    if source:
        lines = read_lines(source)
        if len(lines) != len(leaves):
            problems.append(f"source has {len(lines)} lines, bundle commits to {len(leaves)}")
        for i, ln in enumerate(lines[: len(leaves)], 1):
            if sha(ln) != leaves[i - 1]:
                problems.append(f"source line {i} does not match its leaf hash")
                break
    return problems


def commit_digest(out_dir):
    with open(os.path.join(out_dir, "manifest.json"), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def selftest():
    demo = [json.dumps({"seq": i, "who": "human" if i % 2 else "agent", "text": f"demo message {i}"}) for i in range(1, 13)]
    with tempfile.TemporaryDirectory() as tmp:
        log = os.path.join(tmp, "log.ndjson")
        with open(log, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(demo) + "\n")
        out = os.path.join(tmp, "bundle")
        build(log, out, "2-4,9")
        results = [("clean bundle verifies", verify(out, log) == [])]

        def tampered(name, fn):
            d = os.path.join(tmp, name)
            build(log, d, "2-4,9")
            fn(d)
            return (name + " is detected", verify(d, log) != [])

        def edit_csv(d, edit):
            p = os.path.join(d, "leaves.csv")
            with open(p, encoding="utf-8", newline="") as fh:
                rows = list(csv.reader(fh))
            edit(rows)
            with open(p, "w", encoding="utf-8", newline="") as fh:
                csv.writer(fh, lineterminator="\n").writerows(rows)

        def flip_leaf(d):
            edit_csv(d, lambda rows: rows[5].__setitem__(1, "0" * 64))

        def swap_rows(d):
            def sw(rows):
                rows[3][1], rows[4][1] = rows[4][1], rows[3][1]
            edit_csv(d, sw)

        def drop_row(d):
            edit_csv(d, lambda rows: rows.pop(6))

        def alter_disclosed(d):
            p = os.path.join(d, "disclosed.jsonl")
            t = open(p, encoding="utf-8").read().replace("demo message 3", "demo message X")
            open(p, "w", encoding="utf-8", newline="\n").write(t)

        def alter_root(d):
            p = os.path.join(d, "manifest.json")
            m = json.load(open(p, encoding="utf-8"))
            m["root"] = "f" * 64
            json.dump(m, open(p, "w", encoding="utf-8"))

        results += [
            tampered("a changed leaf", flip_leaf),
            tampered("two swapped records", swap_rows),
            tampered("a deleted record", drop_row),
            tampered("an altered disclosed record", alter_disclosed),
            tampered("an altered root", alter_root),
        ]
        bad_source = os.path.join(tmp, "edited.ndjson")
        with open(bad_source, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(demo).replace("demo message 7", "demo message 7 (edited)") + "\n")
        results.append(("an edited source file is detected", verify(out, bad_source) != []))
    ok = all(r for _, r in results)
    for name, r in results:
        print(("PASS " if r else "FAIL ") + name)
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("log")
    b.add_argument("out")
    b.add_argument("--disclose", default="")
    v = sub.add_parser("verify")
    v.add_argument("out")
    v.add_argument("--source")
    c = sub.add_parser("commit")
    c.add_argument("out")
    sub.add_parser("selftest")
    a = ap.parse_args(argv)
    if a.cmd == "build":
        m = build(a.log, a.out, a.disclose)
        print(json.dumps(m, indent=2))
        return 0
    if a.cmd == "verify":
        p = verify(a.out, a.source)
        print("OK: bundle is consistent" if not p else "FAILED:\n  " + "\n  ".join(p))
        return 0 if not p else 1
    if a.cmd == "commit":
        print(commit_digest(a.out))
        return 0
    return 0 if selftest() else 1


if __name__ == "__main__":
    sys.exit(main())
