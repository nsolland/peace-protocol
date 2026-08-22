# Public repository publication policy

This repository is already a publication surface. A branch push is public disclosure; merge review is therefore too late to be the primary IP gate.

## Mandatory rule

No person, model, agent, automation or external tool may push new substantive protocol, research, architecture or implementation material to this repository until an explicit human IP/publication review has approved the exact material for public disclosure.

Development of unreleased or potentially IP-sensitive material must happen in a private repository or other non-public workspace. Only the minimum approved interoperability surface may be promoted here.

## Public by design

The approved public surface is limited to material required for independent PEACE interoperability:

- normative core protocol semantics;
- public envelope schemas;
- public conformance vectors;
- licensing, governance, contribution and security process;
- released interoperability corrections and clarifications.

## Not public by default

The following require a separate explicit decision before any public push:

- research derivations or discovery lineage;
- unpublished mechanisms or invariants beyond the released protocol contract;
- experimental routing, capability-composition or adaptive-network work;
- model-specific state-transfer techniques or evaluation results;
- internal product topology, commercial implementation strategy or roadmap;
- cross-project synthesis that reveals how independently useful components combine into a protected architecture;
- partner/customer material, private data, credentials, thresholds or assurance methods.

## Review test

Before promotion to this public repository, the reviewer must answer:

1. Is every disclosed element necessary for interoperability, adoption, auditability or a deliberate public standard claim?
2. Could the material be combined with other public artifacts to reconstruct a protected mechanism, architecture or research direction?
3. Does disclosure weaken patent, trade-secret, licensing, standards, negotiation or competitive position?
4. Can the same public objective be achieved with less disclosure?
5. Has the exact proposed public diff, not merely its topic, been reviewed?

If any answer is uncertain, do not push the material here.

## Secondary CI gate

CI checks the current tree for known non-public research markers and obvious secret material. This is defense in depth only. It does not replace pre-push IP review because a failed branch in a public repository is already public.
