# PEACE Protocol Licensing Policy

Status: publication draft, 2026-08-19

## Decision

PEACE uses **Apache License 2.0** for the public specification text, schemas, conformance vectors, examples, reference code and repository automation unless a later accepted governance proposal changes that policy.

The objective is that PEACE remains free to adopt, free to implement, commercially usable, forkable and independently implementable without requiring a licence fee or permanent relationship with any vendor.

## Why Apache 2.0

Apache 2.0 provides:

- broad commercial and non-commercial use;
- modification and redistribution rights;
- an explicit contributor patent grant;
- patent-retaliation protection;
- preservation of attribution/NOTICE information;
- no field-of-use restriction;
- no requirement that independent implementations or derivative products be open sourced.

The explicit patent grant is important for an interoperability protocol intended for implementation by infrastructure providers, enterprises, device vendors and independent software projects.

## Royalty-free interoperability

A conforming PEACE implementation does not owe a licence fee merely for implementing the public protocol.

The public protocol, public schemas and mandatory conformance semantics are intended to be royalty-free under Apache 2.0.

This does not prevent commercial services around PEACE, including:

- managed control planes;
- certification and assurance;
- managed recovery services;
- hosted registries/resolvers;
- conformance services;
- enterprise adapters/deployment;
- support, warranty or indemnity;
- consequence/evidence infrastructure.

## No protocol capture

The licence and protocol MUST NOT:

- require use of VALO software;
- require use of a VALO-operated service;
- make VALO or any other provider a mandatory intermediary;
- restrict implementation to particular models, clouds, compute providers, payment rails, identity providers or devices;
- create field-of-use restrictions;
- condition the right to implement PEACE on buying certification.

A third party must be able to implement PEACE from the public specification and conformance material alone.

## Trademark separation

Apache 2.0 does not grant trademark rights.

Accurate descriptive statements such as `implements PEACE Protocol vX.Y` may be used subject to the trademark policy. Claims such as `PEACE Certified`, official badges, logos or endorsement remain controlled separately.

Certification is therefore a commercial/trust programme, not a licence gate to implementation.

## Contributions

Default contribution policy:

- inbound licence = outbound licence (Apache 2.0);
- contributors SHOULD use Developer Certificate of Origin style sign-off;
- no CLA is required initially;
- contributions that introduce known incompatible third-party licensing MUST NOT be accepted;
- normative contributions require provenance, compatibility and conformance impact under `GOVERNANCE.md`.

A CLA may be introduced later only by explicit governance decision if required by a foundation, standards body or material legal need.

## Patents

PEACE should not require a separate patent licence where Apache 2.0 already supplies the contributor patent grant.

If a contributor knows that implementation of a proposed normative requirement necessarily depends on patent claims they cannot license under the project terms, that fact MUST be disclosed during proposal review.

No contributor may describe a known patent-encumbered extension as mandatory PEACE conformance unless the applicable implementation rights are available under the project policy.

## Future standards transfer

If PEACE moves to an external foundation, consortium or formal standards body, the canonical venue may adopt its own IPR policy. Any transfer must preserve a clear mapping from the Apache-licensed repository history to the external standard and must not retroactively revoke rights already granted under Apache 2.0.

## Commercial boundary

> **The protocol is free. Operational trust infrastructure is commercial.**

Implementers may charge for implementation, hosting, certification, assurance, support, managed recovery, conformance services and consequence infrastructure. No one charges merely for the right to speak PEACE.
