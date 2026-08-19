# PEACE Protocol

PEACE is a vendor-neutral protocol for preserving authoritative state and execution authority while models, agents, devices, compute providers, routers and settlement rails remain replaceable.

> Everything can be routed except sovereignty.

## Core idea

Govern the workspace, not the worker.

A PEACE domain keeps the parts that must remain authoritative outside replaceable capability providers:

- actor / domain identity
- authoritative state
- standing and delegation
- execution authority
- evidence and lineage

Models, agents, compute, routing and settlement may change without becoming authority roots.

## Protocol invariants

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

A consequence-bearing action must be checked against fresh authority at the effect boundary. A provider cannot acquire sovereignty merely because it stores state, holds credentials, routes intelligence, supplies compute or moves money.

## Start here

1. [Normative protocol draft](protocol/PEACE_PROTOCOL_V0.md)
2. [World contract and derivation](protocol/PEACE_WORLD_V0.md)
3. [Protocol envelope schema](schemas/peace-envelope-v0.schema.json)
4. [Conformance vectors](conformance/conformance-v0.json)

Current line: `0.1.0-draft.1`.

## Scope

This repository contains the public protocol, schemas and conformance material. It does not contain production control-plane logic, customer integrations, private deployment configuration or proprietary assurance infrastructure.

PEACE is independently implementable under Apache License 2.0. No vendor, including VALO, is required to implement the protocol.

## Relationship to reht

PEACE defines the sovereign domain and authority semantics. `reht` is one possible implementation of a fresh, exact consequence gate. It is not required by the protocol.

## Licence and governance

Apache License 2.0. See [LICENSE](LICENSE), [NOTICE](NOTICE), [LICENSING.md](LICENSING.md), [GOVERNANCE.md](GOVERNANCE.md), [SECURITY.md](SECURITY.md) and [TRADEMARKS.md](TRADEMARKS.md).
