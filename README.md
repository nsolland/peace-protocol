# PEACE Protocol

**Personal Execution, Authority & Compute Environment**  
**Your Sovereign State.**

> **Everything can be routed except sovereignty.**

PEACE is an open, vendor-neutral protocol for preserving a person’s or organisation’s sovereign digital domain while models, agents, devices, credentials, services, compute providers, routers and settlement rails remain replaceable.

The protocol separates what must persist from what may move:

```text
PEACE          = actor/domain + authoritative state + standing + authority
Factory        = replaceable capability
Model router   = replaceable intelligence routing
Compute        = replaceable capacity
Settlement     = replaceable economic rail
reht           = one possible fresh exact consequence gate
```

The core derivation is simple:

> **Govern the workspace, not the worker.**

If workers are replaceable, then models, devices, compute, services and providers must also be replaceable. What must persist is the governed domain.

## Status

Current line: **`0.1.0-draft.1` publication candidate**.

This repository is intended to become the canonical public PEACE protocol and conformance surface. It is not a VALO production runtime repository and does not contain private deployment logic, customer integrations, internal thresholds or commercial certification infrastructure.

## Start here

- [`protocol/PEACE_WORLD_V0.md`](protocol/PEACE_WORLD_V0.md) — world contract and derivation question
- [`protocol/PEACE_PROTOCOL_V0.md`](protocol/PEACE_PROTOCOL_V0.md) — normative draft protocol
- [`schemas/peace-envelope-v0.schema.json`](schemas/peace-envelope-v0.schema.json) — protocol envelope schema
- [`conformance/conformance-v0.json`](conformance/conformance-v0.json) — machine-readable conformance vectors
- [`LICENSING.md`](LICENSING.md) — open/royalty-free implementation policy
- [`GOVERNANCE.md`](GOVERNANCE.md) — normative change authority
- [`PUBLICATION_PLAN.md`](PUBLICATION_PLAN.md) — publication and standardisation sequence
- [`PUBLICATION_STATUS.md`](PUBLICATION_STATUS.md) — exact release status

## Constitutional distinctions

```text
knowledge       != authority
proposal        != decision
authorization   != effect
evidence        != authoritative state
credential      != actor
compute route   != authority source
payment rail    != economic authority
implementation  != protocol
```

A replaceable provider cannot become the sovereignty root merely because it stores data, holds a credential, routes a model, supplies compute or moves money.

## Open protocol / commercial infrastructure

PEACE is intended to be free to adopt and independently implement under Apache License 2.0. No vendor — including VALO — is required merely to implement the public protocol.

Commercial services may exist around the protocol, including managed control planes, certification, assurance, recovery services, hosted registries/resolvers, adapters, enterprise deployment and support.

> **The protocol is free. Operational trust infrastructure is commercial.**

## Lineage

The first public PEACE proposal seed was published in `nsolland/reht-standard` PR #21 before this dedicated repository was created. That proposal remains historical lineage; this repository is the intended canonical home once the first validated draft release is accepted.

## Licence

Apache License 2.0. See [`LICENSE`](LICENSE), [`LICENSING.md`](LICENSING.md), [`NOTICE`](NOTICE) and [`TRADEMARKS.md`](TRADEMARKS.md).
