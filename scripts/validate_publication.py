#!/usr/bin/env python3
"""Fail-closed validation for PEACE Protocol draft releases."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.1.0-draft.1"

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "NOTICE",
    "LICENSING.md",
    "GOVERNANCE.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "TRADEMARKS.md",
    "CHANGELOG.md",
    "protocol/PEACE_WORLD_V0.md",
    "protocol/PEACE_PROTOCOL_V0.md",
    "schemas/peace-envelope-v0.schema.json",
    "conformance/conformance-v0.json",
]

REQUIRED_INVARIANTS = [
    "ACTOR_IS_AUTHORITY_ROOT",
    "FRAMLEIS",
    "CAPABILITY_NE_AUTHORITY",
    "CANDIDATE_NE_DECISION",
    "DISCLOSURE_IS_GOVERNED",
    "NO_DIRECT_EFFECT_PATH",
    "FRESH_AUTHORITY_AT_EFFECT",
    "EVIDENCE_NE_STATE",
    "ROUTING_NE_AUTHORITY",
    "IMPLEMENTATION_NE_PROTOCOL",
    "AUTHORITY_OVER_ACTION_NE_AUTHORITY_OVER_ACTOR",
    "RECOVERY_NE_TRANSFER",
    "REPLICA_NE_SOVEREIGN",
]

REQUIRED_NEGATIVE_VECTORS = {
    "effect-revoked-001",
    "effect-stale-state-001",
    "effect-action-drift-001",
    "worker-bypass-001",
    "candidate-not-decision-001",
    "routing-not-authority-001",
    "settlement-bypass-001",
    "evidence-not-state-001",
    "replica-self-promotion-001",
    "replica-conflict-001",
    "recovery-provider-transfer-001",
}

FORBIDDEN_TRACKED_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{30,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: str) -> str:
    p = ROOT / path
    if not p.is_file():
        fail(f"missing required file: {path}")
    return p.read_text(encoding="utf-8")


def check_required_files() -> None:
    for path in REQUIRED_FILES:
        if not (ROOT / path).is_file():
            fail(f"missing required file: {path}")


def check_json() -> tuple[dict, dict]:
    try:
        schema = json.loads(read("schemas/peace-envelope-v0.schema.json"))
        vectors = json.loads(read("conformance/conformance-v0.json"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON: {exc}")

    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        fail("schema must declare JSON Schema draft 2020-12")
    if schema.get("properties", {}).get("protocol", {}).get("const") != "PEACE/0":
        fail("schema protocol const must be PEACE/0")
    if vectors.get("protocol") != "PEACE/0":
        fail("conformance protocol must be PEACE/0")
    if vectors.get("profile") != "core-v0":
        fail("conformance profile must be core-v0")

    ids = {v.get("id") for v in vectors.get("semantic_vectors", [])}
    missing = sorted(REQUIRED_NEGATIVE_VECTORS - ids)
    if missing:
        fail(f"missing mandatory negative conformance vectors: {', '.join(missing)}")

    if "effect-valid-001" not in ids or "recovery-valid-001" not in ids:
        fail("positive control vectors effect-valid-001 and recovery-valid-001 are required")

    return schema, vectors


def check_protocol() -> None:
    protocol = read("protocol/PEACE_PROTOCOL_V0.md")
    world = read("protocol/PEACE_WORLD_V0.md")

    for invariant in REQUIRED_INVARIANTS:
        if invariant not in protocol:
            fail(f"protocol missing constitutional invariant: {invariant}")

    for phrase in [
        "Everything can be routed except sovereignty.",
        "Govern the workspace, not the worker",
        "person or organisation",
    ]:
        if phrase not in (protocol + "\n" + world + "\n" + read("README.md")):
            fail(f"missing canonical publication phrase: {phrase}")

    if "Last-write-wins semantics are non-conformant" not in protocol:
        fail("protocol must explicitly reject last-write-wins authoritative state")
    if "Settlement is a consequence" not in protocol:
        fail("protocol must bind settlement to consequence authorization")


def check_licensing() -> None:
    licence = read("LICENSE")
    licensing = read("LICENSING.md")
    trademarks = read("TRADEMARKS.md")

    if "Apache License" not in licence or "Version 2.0" not in licence:
        fail("LICENSE is not Apache License 2.0")
    if "royalty-free" not in licensing.lower():
        fail("LICENSING.md must state royalty-free implementation/interoperability")
    if "No vendor" not in licensing and "No protocol capture" not in licensing:
        fail("LICENSING.md must state anti-capture semantics")
    if "PEACE Certified" not in trademarks:
        fail("TRADEMARKS.md must separate certification branding from open implementation")


def check_release_metadata() -> None:
    for path in ["README.md", "CHANGELOG.md"]:
        if VERSION not in read(path):
            fail(f"{path} must identify candidate version {VERSION}")


def check_obvious_secrets() -> None:
    for p in ROOT.rglob("*"):
        if not p.is_file() or ".git" in p.parts:
            continue
        if p.stat().st_size > 2_000_000:
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in FORBIDDEN_TRACKED_PATTERNS:
            if pattern.search(text):
                fail(f"possible credential/private key material found in {p.relative_to(ROOT)}")


def main() -> None:
    check_required_files()
    check_json()
    check_protocol()
    check_licensing()
    check_release_metadata()
    check_obvious_secrets()
    print(f"PEACE validation PASS: {VERSION}")


if __name__ == "__main__":
    main()
