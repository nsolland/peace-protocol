# Publication status

Status date: 2026-08-21

PEACE is a public, vendor-neutral protocol for the governed domain and authority semantics. It is not an authorization engine, execution runtime or source of authority. Public availability does not make PEACE responsible for deciding whether an action is permitted.

## Public surface

The intended public surface includes:

- protocol specification and normative world contracts;
- deterministic envelope schemas;
- conformance vectors;
- the distinction between authority, authorization, evidence and effect.

## Explicit exclusions

The public surface does not include or require:

- proprietary authorization/evaluation logic;
- private organizational policy or authority data;
- production credentials or deployment configuration;
- private runtime, model or infrastructure implementation.

## Release rule

Repository visibility is not a release by itself. A release requires an immutable version/tag, exact commit, declared license and green conformance checks on that commit.