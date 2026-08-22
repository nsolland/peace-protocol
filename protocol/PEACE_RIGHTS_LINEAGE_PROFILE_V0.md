# PEACE Rights-Lineage Profile v0

Status: draft interoperability profile.

This profile defines observable semantics for preserving and evaluating declared or otherwise applicable rights, restrictions and provenance obligations as material is transformed or transferred through AI systems.

It does not determine whether a legal right exists, does not create copyright or other statutory rights, and does not prescribe any specific licensing regime.

## Core invariant

> **RIGHTS_FOLLOW_LINEAGE** — technical derivation MUST NOT by itself be treated as extinguishing or broadening applicable rights, restrictions or provenance obligations.

Equivalent observable invariants:

```text
transformation != rights extinction
compression    != rights extinction
distillation   != rights extinction
transfer       != rights extinction
replication    != permission
regeneration   != rights reset
capability     != license
```

## Required semantics

A conformant implementation MUST preserve the following semantics where a downstream use depends on rights clearance:

1. **TRANSFORMATION_NE_RIGHTS_EXTINCTION** — format conversion, summarization, embedding, inference or other transformation MUST NOT by itself clear restrictions.
2. **COMPRESSION_NE_RIGHTS_EXTINCTION** — a compact, latent, distilled or model-incorporated representation MUST NOT be assumed rights-free merely because original bytes are absent.
3. **TRANSFER_NE_RIGHTS_EXTINCTION** — transfer between human, agent, model, provider or runtime MUST NOT by itself broaden permitted use.
4. **REGENERATION_NE_RIGHTS_RESET** — reconstruction on new substrate MUST preserve the need to evaluate applicable upstream rights lineage.
5. **MULTIPLICATION_NE_PERMISSION** — technical ability to copy, fork, replicate or scale MUST NOT create permission to do so.
6. **CAPABILITY_NE_LICENSE** — access, possession or technical ability to infer, reproduce or transform MUST NOT be treated as a license.
7. **NO_RIGHTS_LAUNDERING_BY_AGENT_CHAIN** — passing material through additional agents or models MUST NOT be treated as creating a clean unencumbered origin.
8. **PROVENANCE_FOR_REQUIRED_CLEARANCE** — where rights clearance is required, enough lineage MUST remain available to evaluate the requested downstream use.
9. **UNRESOLVED_RIGHTS_FAIL_CLOSED** — materially required rights/provenance bindings that are missing, stale, contradictory or unresolved MUST NOT be treated as permission.

## Direction neutrality

These semantics apply to human→AI, AI→human and AI→AI transfers.

This profile does not grant AI legal personhood. The relevant rights holder, licensor, principal or authorized party is determined outside this protocol by applicable law, contract and admitted authority state.

## Downstream-use binding

Where relevant, a rights decision SHOULD bind:

- source or lineage reference;
- rights-holder/licensor reference where known;
- asserted/applicable rights basis;
- requested use class;
- recipient/destination;
- purpose;
- replication/transfer scope;
- commercialization scope;
- provenance obligations;
- current unresolved or conflicting restrictions.

Permission for one use class MUST NOT imply permission for another.

Examples include `analyze_for_task`, `transform_for_task`, `train_persistent_model`, `distill_into_model`, `build_person_model`, `redistribute_derivative`, `share_with_agent`, `commercialize_derivative` and `replicate_at_scale`.

## Relationship to person-model sovereignty

A materially person-specific representation MAY be governed simultaneously by the PEACE Person-Model Sovereignty Profile and this Rights-Lineage Profile.

Permission to access or transform source material MUST NOT automatically create permission to build a persistent person-model. Conversely, permission to build a person-model MUST NOT automatically clear copyright, contractual, confidentiality, trade-secret or other applicable source restrictions.

## Conformance boundary

Conformance demonstrates only the observable semantics above. It is not legal advice, proof of ownership, a copyrightability determination, or proof that any particular restriction is enforceable in a jurisdiction.
