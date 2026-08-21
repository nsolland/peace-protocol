# Work anchor — Peace Mesh ERP capability

Date: 2026-08-21
Owner: nsolland
Claim: integrate the externally validated AI-native ERP operating pattern as a replaceable Peace Mesh capability without changing PEACE authority semantics.

Repository: `nsolland/peace-protocol`
Canonical base SHA: `5c49dc0dce5c0517fc728ab7ea16f2b503d4ec80`
Branch: `feat/peace-mesh-erp-capability`
Draft PR: `#9`

Owned files:
- `docs/work-anchors/2026-08-21-peace-mesh-erp-capability.md`
- `docs/peace-mesh/erp-agent-operations-capability.md`

Dependencies:
- PEACE sovereign-domain and authority-state semantics remain unchanged.
- MCIP remains transport/context interoperability only and does not mint authority.
- Consequence-bearing actions require the governing execution-authorization boundary of the host domain; in VALO deployments this is fresh `valo-reht` authorization plus bounded enforcement/evidence.

External reference pattern:
- Trope AI-native ERP integration and managed-agent model: agent-assisted Business Central implementation/migration; custom agents that own named ERP processes end to end; live ERP data access; read/create/post operations; process KPIs; production monitoring; release-wave retesting; per-run trace/log evidence; human process-owner review before unattended posting.

Scope boundary:
- Adopt the capability pattern, not Trope as a dependency.
- No vendor-specific authority semantics enter PEACE.
- ERP systems remain replaceable state/effect surfaces behind sovereign domain boundaries.
