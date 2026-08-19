# PEACE Protocol Publication Plan

Status: active publication plan, 2026-08-19

## Objective

Establish PEACE as a public, independently implementable, vendor-neutral protocol before the architecture becomes captured by any single provider or product stack.

The publication objective is not to publish every implementation detail. It is to publish the **protocol physics**: world contract, invariants, normative semantics, schemas, conformance vectors, governance and release provenance.

## Publication principles

1. Publish semantics before product polish.
2. Open protocol; commercial operational infrastructure.
3. No vendor — including VALO — is a required intermediary.
4. Normative protocol != reference implementation.
5. Historical snapshots are immutable and forward-only.
6. Every substantive normative change has public provenance.
7. Conformance is observable behaviour, not branding.

## Phase 0 — Public seed / lineage

Origin: `nsolland/reht-standard` PR #21, `proposals/peace-v0/`.

Purpose:

- establish public lineage and timestamp;
- publish the derivation from `govern the workspace, not the worker`;
- publish the world contract, protocol proposal, schema and conformance seed;
- make clear PEACE is broader than REHT and not normative REHT material.

This phase is complete as historical lineage once this repository becomes canonical.

## Phase 1 — Dedicated canonical repository

Venue: `nsolland/peace-protocol`.

Required repository surface:

```text
README.md
LICENSE
NOTICE
LICENSING.md
GOVERNANCE.md
CONTRIBUTING.md
SECURITY.md
TRADEMARKS.md
PUBLICATION_STATUS.md
PUBLICATION_PLAN.md
CHANGELOG.md
protocol/
  PEACE_WORLD_V0.md
  PEACE_PROTOCOL_V0.md
schemas/
  peace-envelope-v0.schema.json
conformance/
  conformance-v0.json
.github/workflows/
```

Migration requirements:

- preserve originating REHT proposal PR and exact lineage references;
- leave the original proposal directory intact as historical lineage;
- point the original proposal to this repository after canonical transfer;
- do not claim a release until the exact release head is validated and tagged.

## Phase 2 — First immutable draft release

Target: `v0.1.0-draft.1`.

Required gate:

- Apache-2.0 licence/NOTICE/trademark terms present and consistent;
- specification and schemas agree;
- mandatory conformance vectors validate cleanly;
- threat/security reporting process present;
- governance and contribution process present;
- no private/customer/partner material present;
- exact release head green;
- tag, version and commit hash aligned;
- release notes identify status as draft/prerelease.

The first immutable draft becomes the first clean public citation target.

## Phase 3 — Independent derivation and implementation challenge

PEACE must be tested by independent implementation, not internal architecture resemblance.

Publish two exercises:

1. **Derivation challenge** — give only the world contract to an independent implementer/reasoning system and ask for the minimum required boundaries/invariants.
2. **Black-box conformance challenge** — implement PEACE without reading a VALO reference implementation and run the mandatory vectors.

Desired evidence:

- at least two implementation languages or independent implementations;
- one implementation not maintained by the original editor if available;
- documented divergence points;
- negative-case results for direct-effect bypass, stale authority, route-as-authority, evidence-as-state, settlement bypass and recovery transfer.

Independent derivation is design evidence. Passing the normative conformance profile is the interoperability claim.

## Phase 4 — Public v0.x protocol line

Publish forward-only draft/minor releases as semantics mature.

Priority profiles:

- core sovereign-domain profile;
- state replication/lineage profile;
- recovery federation profile;
- capability/disclosure profile;
- execution-boundary profile;
- organisation-domain profile;
- settlement/consequence profile;
- provider/route interchangeability profile.

Do not force every profile into core if interoperability is cleaner through optional profiles.

## Phase 5 — External governance / standardisation

Once external implementations exist, evaluate transfer or co-governance through a neutral foundation, consortium, IETF-like process or other standards venue.

A transfer requires:

- explicit canonical-authority decision;
- exact last repository-owned release tag/hash;
- public mapping from local versions to external versions;
- preservation of Apache-licensed history;
- no simultaneous competing canonical source;
- continued availability of conformance artifacts.

## Publication channels

Minimum:

- public GitHub canonical repository;
- immutable Git tags/releases;
- DOI/archive snapshot when first coherent draft is ready;
- short protocol paper/preprint describing derivation, invariants and boundaries;
- public conformance vectors.

Optional later:

- IETF/standards draft;
- foundation/consortium submission;
- independent test/certification programme.

## Deliberately outside the public protocol

Publication does not require release of:

- production control-plane code;
- proprietary evaluation logic;
- internal risk thresholds;
- customer adapters/configuration;
- deployment secrets;
- commercial recovery operations;
- certification backend;
- internal assurance methods;
- private partner material.

## Canonical sequence

```text
public seed
  -> dedicated canonical repo
  -> licensing/governance/security complete
  -> green immutable draft tag
  -> independent derivation/conformance
  -> v0.x evolution
  -> external governance if warranted
```

> **PEACE is free to adopt and independently implement. No vendor, including VALO, is required for the protocol to remain usable.**
