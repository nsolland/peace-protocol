# Work anchor — Cross-model KV cache transfer

Date: 2026-08-21
Owner: nsolland
Claim: document the NVIDIA cross-model KV cache transfer result and derive bounded implications for Peace Mesh and MCIP without changing PEACE authority semantics or coupling MCIP to model-specific latent formats.

Repository: `nsolland/peace-protocol`
Canonical base SHA: `5922a3222d376753f018365a735ace62e73e1c80`
Branch: `protocol/mcip-v0`
Draft PR: `#8`

Owned files:
- `docs/work-anchors/2026-08-21-cross-model-kv-cache-transfer.md`
- `docs/research/2026-08-21-cross-model-kv-cache-transfer.md`
- `README.md`

Dependencies:
- PEACE sovereign-domain, admission and authority semantics remain unchanged.
- MCIP remains transport-independent and model-independent.
- A latent-state transfer is a replaceable handoff optimization, not a required MCIP representation.
- Transferred or translated latent state is evidence-bearing cognitive input, never authority or authorization.
- Any consequence-bearing action remains subject to the sovereign host-domain consequence boundary.

Scope boundary:
- Record the source, method, results, limitations and derived architecture consequences.
- Distinguish direct evidence from inference and proposed experiments.
- Do not claim arbitrary cross-family transfer, identity transfer, consciousness, emergence or production readiness.
- Do not add a normative schema field or conformance requirement before an implementation experiment establishes need.
