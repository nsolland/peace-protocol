# PEACE Mesh Capability Surfaces v0

**Experimental companion note to PEACE MCIP v0**  
**Reach can move. Rights do not.**

## 1. Status

This note generalizes one implication of the PEACE world and MCIP interaction model: a PEACE mesh is not limited to model-to-model cognition or API-connected tools.

Any replaceable system that can perceive, compute, communicate, operate software, manipulate a device or cause a real-world effect may appear as a routable capability surface, provided the PEACE sovereignty and consequence boundaries remain intact.

This note is not a separate authority system and does not make any specific runtime, agent framework, API, GUI automation system, operating system or vendor a dependency.

## 2. Core observation

Modern computer-use runtimes can operate software through the same surfaces available to a human: browser, desktop, GUI, keyboard, pointer, terminal and device controls. This means large parts of the existing software estate can become addressable by agents even where no dedicated API, MCP server or native agent integration exists.

The architectural consequence is larger than GUI automation:

> The mesh may route work across heterogeneous capability surfaces. The interface used to reach a capability must never become the source of authority to use it.

A PEACE mesh may therefore include capability classes such as:

```text
reasoning / synthesis
perception / sensing
local or remote compute
API / tool execution
browser / GUI / operating-system control
device / edge control
physical or robotic actuation
human execution
settlement / value transfer
```

These are replaceable capability surfaces, not authority roots.

## 3. Derived distinctions

PEACE and MCIP already require `CAPABILITY_NE_AUTHORITY`, `ROUTE_NE_AUTHORITY`, `MESSAGE_NE_AUTHORIZATION` and `NO_DIRECT_EFFECT_PATH`.

For heterogeneous action surfaces, the same semantics imply:

```text
reach               != right
interface access    != authority
active session      != delegation
credential possession != permission
GUI grounding       != decision
route to executor   != authorization
low-level input     != authoritative action semantics
executor            != sovereign domain
```

A node may be technically capable of clicking a button, submitting a form, moving value, changing a configuration or actuating a device while having no current right to cause that consequence.

## 4. Capability advertisement and discovery

MCIP `CAPABILITY_OFFER` may advertise execution reach as routing evidence. An offer may describe, for example:

- surface class: API, browser, GUI, device, human, robot or settlement rail;
- target application or capability class;
- locality and isolation constraints;
- observation and evidence capabilities;
- expected cost, latency or reliability;
- whether the surface can reach consequence-bearing operations.

Such an offer is a claim about capability only. It MUST NOT establish standing, delegation, authority, trustworthiness or permission to disclose context.

Discovery may therefore select a GUI-capable runtime when no API exists, an API executor when one is safer or cheaper, a local device when privacy requires it, or a human when machine execution is inadmissible. Selection changes the route, not the sovereign rules.

## 5. From cognitive handoff to consequence

MCIP remains an interaction protocol. It MUST NOT become an effect-authorization channel merely because the destination node can execute actions.

A typical path is:

```text
bounded context
  -> reasoning / planning
  -> candidate action
  -> executor selection
  -> exact consequence semantics
  -> fresh PEACE authorization
  -> bounded effect attempt
  -> outcome evidence
  -> admission / state transition
```

The executor may use an API, GUI, browser, shell, device interface, robotic controller or another implementation mechanism. That choice is replaceable metadata from the PEACE perspective.

The final effect interface MAY be implemented outside MCIP. What matters is that no cognitive message, route selection, session, credential or executor capability can bypass the PEACE consequence boundary.

## 6. Semantic action before low-level actuation

Low-level interface operations are not sufficient authority semantics.

For example, a pointer coordinate, keystroke sequence or DOM selector identifies an implementation action, but it may not uniquely identify the intended consequence after the screen, application state or target object changes.

Before a material consequence, a conformant design must be able to bind authorization to the exact governed action semantics and current relevant state. The executor then maps that authorized action to the current interface mechanism.

Where the runtime cannot determine what material consequence a low-level interaction would cause with sufficient confidence for the governing policy, the effect path must fail closed, defer or require a higher-assurance execution mode.

This preserves the distinction:

```text
semantic consequence -> authorization -> actuation
```

rather than:

```text
click / keystroke -> hope the intended consequence occurred
```

## 7. Replaceability across interface regimes

A PEACE domain should be able to replace one execution surface with another without changing the logical actor or authority root.

For the same governed action, a deployment may move between:

```text
native API
<-> MCP / tool adapter
<-> browser automation
<-> GUI / desktop computer-use runtime
<-> local device executor
<-> human executor
```

The capability, latency, evidence quality and admissibility may change. The source of authority must not.

This makes PEACE independent not only of model and compute providers, but also of future interface standards and agent-runtime winners.

## 8. Mesh-level implication

The long-term PEACE mesh is therefore not merely a network of intelligences. It is a network of sovereign domains and replaceable capabilities, where cognition and action can be routed independently.

The important network effect is not that one platform owns every integration. It is that the mesh can learn which capability surface is fit for which task, under which constraints, while preserving bounded disclosure, provenance, current authority and consequence control.

A legacy application with only a human GUI can participate. A future autonomous device can participate. A cloud model can participate. A local model can participate. A human can participate. None becomes sovereign merely because it is the only current path to the capability.

## 9. Conformance implications

A PEACE/MCIP implementation that exposes effect-capable nodes should be testable for at least these derived properties:

- an execution-capable `CAPABILITY_OFFER` does not create authority;
- routing to a node with an active authenticated session does not create standing or delegation;
- a cognitive `HANDOFF` to an effect-capable node remains inert with respect to consequence;
- a GUI/browser/device executor cannot convert its own candidate directly into a material effect;
- authorization is bound to semantic consequence, not merely pointer coordinates, selectors or keystrokes;
- replacing an API executor with a GUI executor does not change the actor or authority root;
- outcome evidence from an executor remains evidence until governed admission gives it standing.

## 10. Canonical meaning

```text
PEACE preserves the sovereign domain.
MCIP lets capabilities discover and interact.
Execution surfaces let the mesh reach the world.

Reasoning can move.
Compute can move.
Interfaces can move.
Executors can move.

Reach can move.
Rights do not.
```
