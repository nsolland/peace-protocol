# PEACE Mesh Context Interaction Protocol v0

**MCIP — Mesh Context Interaction Protocol**  
**Context can move. Sovereignty does not.**

## 1. Status and relationship to PEACE

This is an experimental interoperability profile for PEACE v0.

MCIP defines how models, agents, humans, devices, factories and other cognitive nodes may exchange bounded context, hypotheses, challenges, residuals, evaluations and handoffs across a mesh without confusing communication with admission, standing, authority or consequence.

MCIP is **not** a mandatory dependency for PEACE conformance. A PEACE implementation may use MCIP, another protocol, or an equivalent local mechanism.

MCIP is transport-independent. HTTP, QUIC, WebTransport, local IPC, message buses, radio links, peer-to-peer overlays or future transports MAY carry MCIP messages. The transport is not the protocol and MUST NOT become an authority source.

Normative words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are requirements of this draft.

## 2. Purpose

MCIP exists to make the *interaction architecture* between intelligences explicit and portable.

The protocol is designed for systems where effective capability may depend not only on the model executing a task, but also on:

- which nodes interact;
- what context each node receives;
- what epistemic role each node performs;
- what unresolved residual is handed forward;
- what alternative framing or challenge is introduced;
- what evaluation is returned;
- how the interaction topology changes over time.

The protocol therefore carries **cognitive state and interaction semantics**, not merely RPC payloads.

## 3. Core principle

> **A message may change what another node knows. It does not by itself change what the sovereign domain accepts, authorizes or does.**

MCIP MUST preserve the PEACE distinctions:

```text
context       != authoritative state
message       != admission
hypothesis    != fact
route         != standing
capability    != authority
handoff       != delegation
synthesis     != decision
evaluation    != authorization
transport     != protocol
```

Any consequence-bearing action remains subject to PEACE current exact authorization at the effect boundary.

## 4. MCIP invariants

A conformant MCIP implementation MUST preserve all of the following:

1. **MESSAGE_NE_ADMISSION** — receipt, repetition, signature, confidence, majority agreement or persistence of an MCIP message MUST NOT make its content authoritative state. Material that requires standing must pass PEACE ADMIT.
2. **MESSAGE_NE_AUTHORIZATION** — no MCIP message, including a handoff, route suggestion, synthesis or evaluation, authorizes a consequence-bearing effect.
3. **ROUTE_NE_STANDING** — being selected as the next node MUST NOT create standing, delegation or authority.
4. **CONTEXT_IS_BOUNDED** — disclosed context MUST be minimized to the declared purpose, destination, scope and validity conditions.
5. **PROVENANCE_PRESERVED** — context, hypotheses, residuals and synthesized material MUST remain traceable to their source messages or stable references.
6. **UNRESOLVED_PRESERVED** — unresolved material MUST remain explicitly unresolved until a governed admission process resolves it. Mesh consensus MUST NOT silently collapse unresolved material.
7. **NO_IMPLICIT_MERGE** — incompatible hypotheses, referents or interpretations MUST NOT be silently merged merely because they traverse the same interaction.
8. **EPISTEMIC_STATUS_EXPLICIT** — a node MUST distinguish at least observation/evidence, hypothesis, challenge, residual, synthesis and evaluation where those semantics differ.
9. **FRESHNESS_EXPLICIT** — context whose meaning depends on time, state version or authority state MUST carry sufficient freshness/version information for the receiver to detect staleness.
10. **TRANSPORT_NE_PROTOCOL** — transport identity, connection ownership, network position or possession of a session MUST NOT create authority or protocol standing.
11. **PATTERN_NE_CONTEXT** — learned interaction patterns MAY be shared independently of task content, but a pattern receipt MUST NOT imply permission to disclose the underlying private context.
12. **NO_DIRECT_EFFECT_PATH** — an MCIP-capable node MUST NOT turn an incoming message directly into a consequence-bearing effect without the applicable PEACE authorization path.

## 5. Interaction model

MCIP models a mesh interaction as a lineage of messages linked by `interaction_id`, `message_id`, `parent_message_ids` and stable content digests.

A typical interaction may look like:

```text
TASK / RESIDUAL
      |
      v
CONTEXT_REQUEST
      |
      v
CONTEXT_CAPSULE
      |
      +--> HYPOTHESIS
      +--> CHALLENGE
      +--> FRAME_EXPANSION
      +--> RESIDUAL
                |
                v
             HANDOFF
                |
                v
             SYNTHESIS
                |
                v
                EVAL
```

The graph MAY branch, merge explicitly, recurse, or cross devices/factories. There is no required central coordinator.

## 6. Required envelope semantics

Every MCIP message MUST contain semantics equivalent to:

- `mcip_version` — protocol version;
- `message_id` — unique message identifier;
- `interaction_id` — identifier for the cognitive interaction lineage;
- `parent_message_ids` — zero or more direct causal/input parents;
- `kind` — message semantic type;
- `sender` — logical sending node identifier;
- `destination` — intended node, group, capability class or mesh scope;
- `protected_domain` — PEACE actor/domain whose context or task is being served, when applicable;
- `purpose` — declared purpose for this interaction/message;
- `created_at` — creation time;
- `validity` — expiry, state/version binding or other freshness constraints when applicable;
- `epistemic_status` — status of the payload;
- `provenance` — source references/digests sufficient to reconstruct lineage;
- `disclosure` — scope/grant reference or equivalent statement describing what may be disclosed;
- `payload` — kind-specific content;
- `content_digest` — canonical digest of the protocol content object used for lineage/integrity.

Implementations MAY add signatures, encryption, capability tokens, transport metadata or attestation. These mechanisms MUST NOT change the semantic separation above.

## 7. Message kinds

### 7.1 `CAPABILITY_OFFER`

Advertises what a node claims it can do, under what resource/locality/privacy constraints.

A capability offer is routing evidence only. It is not standing, authority or proof of competence.

Typical payload:

```json
{
  "capabilities": ["causal_reasoning", "code_review"],
  "locality": "device",
  "resource_class": "small-model",
  "constraints": ["no_external_network"]
}
```

### 7.2 `CONTEXT_REQUEST`

Requests the smallest context capsule required for a declared purpose.

The requester SHOULD state what it needs and what it does not need. The sender MUST apply the sovereign domain's disclosure rules before returning context.

### 7.3 `CONTEXT_CAPSULE`

Carries a bounded projection of context.

A context capsule SHOULD distinguish:

- admitted/authoritative references;
- candidate material;
- unresolved material;
- evidence/provenance;
- state/version/freshness binding.

Receiving a context capsule does not admit its contents into the receiver's authoritative state.

### 7.4 `HYPOTHESIS`

Proposes an explanatory, predictive or solution candidate.

A hypothesis MUST remain candidate material unless independently admitted by the applicable governed process.

### 7.5 `FRAME_EXPANSION`

Introduces a materially different problem framing, object, system boundary, actor set, objective, assumption set or cross-domain mechanism.

This message exists specifically to resist premature convergence on the shortest obvious reasoning path.

A frame expansion SHOULD identify what changed relative to its parent frame.

### 7.6 `CHALLENGE`

Attacks a hypothesis, frame, assumption, evidence binding or proposed synthesis.

A challenge SHOULD identify the target message(s), the failure mode being tested and what observation would discriminate between alternatives.

### 7.7 `RESIDUAL`

Represents the concrete portion of a problem that remains unresolved after bounded work.

A residual SHOULD contain:

- what has already been tried;
- which alternatives were considered;
- what remains unresolved;
- why another iteration at the current capability is unlikely to resolve it;
- what capability or missing information may reduce it.

A residual is suitable for capability escalation or targeted human input. It is not permission to escalate blindly.

### 7.8 `HANDOFF`

Transfers cognitive work state to another node.

A handoff MUST preserve lineage, purpose, relevant context bounds and unresolved status. Handoff does not transfer authority unless a separate valid delegation exists and is independently verified by the receiving/effect system.

### 7.9 `SYNTHESIS`

Combines multiple inputs into a candidate next state.

A synthesis MUST preserve material disagreement and unresolved bindings rather than majority-voting them away. It SHOULD identify which parent contributions materially changed the synthesis.

### 7.10 `EVAL`

Evaluates an interaction, answer, route, topology or outcome.

An eval MAY include correctness, calibration, cost, latency, residual reduction, novelty, contradiction detection, human-value delta or other declared metrics.

An eval is evidence for future routing/learning. It is not authority.

### 7.11 `PATTERN_OFFER`

Shares a generalized interaction pattern learned from prior evaluated work without requiring disclosure of the underlying private task content.

Typical pattern semantics:

```text
problem_signature
+ interaction_topology
+ capability classes
+ cost/latency envelope
+ outcome metrics
+ failure modes
+ confidence / sample size
```

Pattern offers are intended to enable a network effect in which factories learn from evaluated interaction structures while sovereign task context remains local.

### 7.12 `ROUTE_SUGGESTION`

Suggests the next node, capability class or interaction topology.

A route suggestion SHOULD state its basis and expected marginal value. It MUST NOT be treated as authority or delegation.

### 7.13 `ACK` / `ERROR`

Acknowledges protocol receipt/processing or reports protocol failure. ACK means only that the protocol message was handled at the declared layer; it does not mean accepted, admitted, authorized or effected.

## 8. Epistemic status

MCIP v0 defines the following minimum epistemic status vocabulary:

```text
OBSERVATION
EVIDENCE
HYPOTHESIS
CHALLENGE
UNRESOLVED
SYNTHESIS
EVALUATION
ROUTE_SUGGESTION
PROTOCOL_CONTROL
```

Implementations MAY extend this vocabulary but MUST NOT collapse semantically distinct statuses in a way that would cause candidate or unresolved material to be treated as authoritative.

## 9. Context capsule rules

A context capsule SHOULD be smaller than the sender's full local context and SHOULD carry only what is needed for the receiving node's declared operation.

Where available, a capsule SHOULD contain stable references instead of copied raw material.

Sensitive or sovereign data SHOULD remain local whenever the requested cognitive operation can be performed on a minimized projection, derived feature, digest, local result or generalized interaction pattern.

The receiver MUST NOT infer broader disclosure permission from possession of a capsule.

## 10. Expansion before escalation

MCIP does not mandate a fixed reasoning topology, but it supports a recommended exploration pattern for cognitive factories:

```text
current task
  -> bounded space expansion
  -> alternate frames / assumption inversion / cross-domain bridge
  -> challenge
  -> convergence attempt
  -> residual
  -> route or capability escalation only if residual remains
```

The number of expansion passes is local policy and SHOULD be learned from evaluated outcomes rather than fixed globally.

Factories MAY recursively learn which interaction topology yields the best outcome for a given problem signature, resource envelope and risk class.

## 11. Learned topology and network effect

MCIP permits evaluated interaction patterns to become reusable network knowledge.

A factory MAY publish a `PATTERN_OFFER` such as:

```text
signature: semantic-drift + incomplete-evidence
best observed topology:
  frame_expander -> contradiction_hunter -> synthesis
resource envelope:
  3 small-model calls + 1 synthesis
observed result:
  +18% task success vs local one-shot
sample size:
  84
```

Another factory MAY use that pattern as routing evidence.

This creates a network effect from **learned relationships between intelligences**, not from centralizing sovereign raw context.

Pattern exchange MUST remain subordinate to disclosure policy, provenance, privacy, admission and consequence controls.

## 12. Transport and discovery

MCIP is transport-independent.

A deployment MAY use:

- direct peer-to-peer links;
- local mesh discovery;
- relays;
- pub/sub buses;
- opportunistic edge links;
- cloud rendezvous;
- HTTP/QUIC/WebTransport gateways;
- offline store-and-forward.

Transport peers MUST NOT be assumed to be trusted cognitive peers merely because a connection exists.

Node discovery MAY use capability advertisements, registries or local broadcasts. Discovery results remain routing candidates only.

## 13. Security and privacy considerations

MCIP implementations SHOULD assume that any remote node, relay or transport may be compromised, stale, mistaken or adversarial.

Implementations SHOULD support:

- purpose-bound disclosure;
- selective/minimized context release;
- replay detection;
- expiry and freshness checks;
- provenance verification;
- confidentiality and integrity protection appropriate to the deployment;
- rate/resource limits;
- explicit treatment of untrusted node claims;
- revocation of disclosure/delegation references;
- isolation of private raw context from pattern-learning exports.

A valid signature proves integrity/origin under a key. It does not prove truth, standing, authority, correct referent binding or admissibility.

## 14. Conformance profile v0

An implementation claiming `PEACE-MCIP-v0` conformance MUST demonstrate at minimum that:

- unsupported transport metadata cannot create authority;
- a `CONTEXT_CAPSULE` remains candidate/unadmitted material at receipt;
- `UNRESOLVED` survives handoff and synthesis without silently becoming accepted;
- a `HANDOFF` cannot create delegation;
- a `ROUTE_SUGGESTION` cannot authorize an effect;
- incompatible parent hypotheses remain distinguishable after synthesis;
- expired/stale context is detectable from the envelope;
- pattern sharing can omit underlying private raw context;
- provenance lineage survives at least one branch and explicit synthesis;
- an MCIP message cannot bypass the PEACE effect authorization boundary.

Machine-readable envelope schema is `schemas/peace-mcip-envelope-v0.schema.json`.

## 15. Non-goals

MCIP v0 does not define:

- a universal model ranking;
- a fixed number of reasoning passes;
- a required agent framework;
- a consensus algorithm;
- a distributed ledger;
- a global identity provider;
- a mandatory transport;
- a global authority system;
- a claim that mesh interaction creates consciousness, AGI or general emergence.

MCIP defines the semantic surface required to test and build distributed cognitive interaction without sacrificing PEACE sovereignty boundaries.

## 16. Canonical meaning

```text
PEACE governs the sovereign domain.
MCIP lets intelligences interact across it.

Context can move.
Capability can move.
Hypotheses can move.
Residuals can move.
Learned interaction patterns can move.

Authority does not move merely because any of them do.
```
