# PEACE Protocol

PEACE is an open protocol for keeping authority and authoritative state under the control of the person or organisation they belong to, while models, agents, devices, compute and service providers remain replaceable.

> Everything can be routed except sovereignty.

Govern the workspace, not the worker.

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

### Experimental interoperability profile

- [MCIP — Mesh Context Interaction Protocol v0](protocol/PEACE_MCIP_V0.md)
- [Mesh Capability Surfaces v0](protocol/PEACE_MESH_CAPABILITY_SURFACES_V0.md)
- [MCIP envelope schema](schemas/peace-mcip-envelope-v0.schema.json)
- [MCIP semantic conformance vectors](conformance/mcip-conformance-v0.json)

MCIP is an optional transport-independent profile for bounded context, hypothesis, residual, evaluation and handoff exchange between models, agents, humans, devices and cognitive factories. The companion capability-surface note generalizes the mesh beyond cognition and API-connected tools: GUI, browser, operating-system, device, human, robotic and settlement surfaces may all be replaceable routes to capability while authority remains in the sovereign domain. Neither changes PEACE authority semantics or is required for PEACE conformance.

### Research and design notes

- [Cross-model KV cache transfer — implications for Peace Mesh and MCIP](docs/research/2026-08-21-cross-model-kv-cache-transfer.md)

Current draft: `0.1.0-draft.1`

## Relationship to reht

PEACE defines the governed domain and authority semantics. `reht` is one possible implementation of a fresh consequence gate. It is not required by PEACE.

## Project

Apache License 2.0. Contributions and protocol governance are documented in [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md). Security reports: [SECURITY.md](SECURITY.md).
