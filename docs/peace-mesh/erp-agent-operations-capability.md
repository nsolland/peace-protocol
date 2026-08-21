# Peace Mesh capability — AI-native ERP implementation and operations

Status: adopted capability pattern
Date: 2026-08-21
Reference signal: Trope

## Capability statement

Peace Mesh may route ERP work to replaceable AI-native ERP workers that can implement, migrate, configure, verify and continuously operate named ERP processes.

The capability is intentionally decoupled from authority. A worker may be technically capable of reading, creating or posting ERP records without thereby having standing or current permission to cause that effect.

```text
ERP capability worker
→ proposed operation
→ sovereign-domain current state / standing / authority
→ fresh consequence authorization where required
→ bounded effect path
→ effect + outcome evidence
```

Trope is a reference implementation signal for the pattern, not a dependency or privileged provider.

## Adopted capability surface

### 1. ERP implementation and migration worker

A replaceable worker may:

- configure an ERP environment from an agreed scope;
- load and transform customer records;
- validate data before admission rather than forcing invalid records through;
- rerun deterministic or bounded test suites after changes;
- produce load, reconciliation and test evidence for review;
- support cutover only when the required evidence is complete.

### 2. Managed ERP process agent

A replaceable agent may own one named ERP process end to end against explicit KPIs, including patterns such as:

- pricing review;
- payables processing and triage;
- reconciliation;
- exception monitoring;
- order and invoice entry;
- recurring reporting;
- master-data hygiene;
- collections follow-up;
- order-to-cash analysis.

### 3. ERP record/tool operation

Subject to the host domain's authority and execution boundary, an ERP worker may expose tools to:

- read records;
- create records;
- update records;
- post records or documents;
- generate reports and dashboards;
- link findings to underlying source records;
- surface ambiguous or exceptional cases for escalation.

`tool_access != execution_authority`

### 4. Continuous verification and drift handling

A managed ERP capability may:

- monitor each run in production;
- compare results with agreed KPIs;
- detect output or platform drift;
- rerun capability tests when the underlying ERP platform changes;
- redesign, constrain, suspend or retire a worker whose output no longer meets its contract.

Verification establishes current capability fitness. It does not mint standing or authority.

### 5. Trace and evidence emission

Every material run should be able to emit a trace sufficient to reconstruct:

- worker/provider/version;
- named process and intended outcome;
- source records consulted;
- proposed mutations/effects;
- test/reconciliation evidence;
- exceptions and escalations;
- review state where human review is part of the contract;
- resulting effect/outcome identifiers.

The trace is evidence. It is not itself authorization.

## Peace Mesh placement

The ERP worker sits in the replaceable capability layer:

```text
PEACE sovereign domain
├── current actor/domain/state/standing/authority
├── Mesh capability routing
│   ├── ERP implementation worker
│   ├── ERP process operator
│   ├── ERP reconciliation / assurance worker
│   └── ERP release-wave verifier
├── optional MCIP context/handoff exchange
└── host-domain consequence boundary
    ├── fresh authorization where required
    ├── bounded effect dispatch
    └── evidence / state admission
```

This preserves the core separation:

```text
Capability != Authority
Protocol participation != Authority
Successful prior run != Current authorization
ERP permission != Consequence authorization
Monitoring != Enforcement
```

## Provider contract

A Peace Mesh ERP capability adapter SHOULD declare at least:

- `provider_id`
- `capability_id`
- `erp_systems`
- `process_classes`
- `operations`
- `read_write_effect_classes`
- `required_context`
- `evidence_outputs`
- `test_contract`
- `health_or_drift_state`
- `version`

An adapter MUST NOT claim or derive sovereign standing, delegation or execution authority merely from provider credentials, ERP permissions, process ownership or historical approvals.

## Reference mapping: Trope

Trope currently demonstrates the useful external pattern:

- agent-assisted Microsoft Dynamics 365 Business Central implementation/migration;
- agents that configure environments, load records and rerun test passes;
- custom managed agents scoped to named ERP processes and KPIs;
- agents operating on live ERP data with read/create/post tooling;
- production monitoring and per-run records;
- retesting against Microsoft release waves;
- process-owner review before unattended posting in the deployment model.

Peace Mesh adopts these as capabilities that any conforming provider may supply. It does not couple the Mesh, PEACE or the authority boundary to Trope, Microsoft Dynamics, Copilot Studio or any specific model/harness.

## Design consequence

The ERP is not the control plane. It is a state and effect surface.

The ERP agent is not the authority. It is a capability worker.

This allows the Mesh to replace the ERP agent provider, model, harness or ERP connector independently while preserving sovereign domain state, standing, authority, consequence controls and evidence lineage.

## Sources

- Trope, `https://trope.ai/`
- Trope process model, `https://trope.ai/process`
- Trope AI agents deployment, `https://trope.ai/services/ai-agents-deployment`
- Trope managed agents, `https://trope.ai/services/managed-agents`
- Trope Dynamics 365 Finance & Operations agents, `https://trope.ai/products/dynamics-365-finance-operations`
- Trope real agent demos, `https://trope.ai/resources/real-agent-demos`
