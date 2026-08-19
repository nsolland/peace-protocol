# PEACE Protocol

PEACE is an open protocol for keeping authority and authoritative state under the control of the person or organisation they belong to, while models, agents, devices, compute and service providers remain replaceable.

> Everything can be routed except sovereignty.

## What PEACE defines

PEACE separates the governed domain from the workers operating inside it.

```text
authoritative state  != provider state
proposal             != decision
authorization        != effect
evidence             != authority
routing              != authority
credential           != actor
replica              != sovereign
```

Any consequence-bearing action must pass a fresh authority check at the effect boundary. No model, router, cloud, payment rail or other replaceable provider becomes an authority root merely by participating in execution.

## Read the protocol

- [Protocol specification](protocol/PEACE_PROTOCOL_V0.md)
- [World contract](protocol/PEACE_WORLD_V0.md)
- [Envelope schema](schemas/peace-envelope-v0.schema.json)
- [Conformance vectors](conformance/conformance-v0.json)

Current draft: `0.1.0-draft.1`

## Relationship to reht

PEACE defines the governed domain and authority semantics. `reht` is one possible implementation of a fresh consequence gate. It is not required by PEACE.

## Project

Apache License 2.0. Contributions and protocol governance are documented in [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md). Security reports: [SECURITY.md](SECURITY.md).
