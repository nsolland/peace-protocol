# PEACE Protocol Publication Status

Status date: 2026-08-19

## Current repository state

`nsolland/peace-protocol` is the dedicated public repository for the PEACE Protocol.

Current protocol line: **`0.1.0-draft.1` publication candidate**.

No immutable PEACE release tag has been published yet. Repository visibility alone is not a release claim.

## Canonical lineage

The initial public PEACE proposal seed was published in `nsolland/reht-standard` PR #21 under `proposals/peace-v0/` before this dedicated repository was created.

That proposal remains historical lineage. This repository becomes the canonical PEACE protocol source when the first accepted draft release is merged, validated and tagged here.

## Public surface

The intended public protocol surface includes:

- world contract / derivation question;
- normative protocol draft;
- schemas;
- machine-readable conformance vectors;
- licensing and IPR policy;
- governance and contribution process;
- security policy;
- trademark/compatibility policy;
- publication/release provenance.

## Licence

Apache License 2.0 applies to covered repository content.

Protocol implementation is intended to be royalty-free. Trademark and certification rights are separate. See `LICENSING.md` and `TRADEMARKS.md`.

## First release gate

Before publishing `v0.1.0-draft.1`, verify all of the following on the exact release head:

1. `LICENSE`, `NOTICE`, `LICENSING.md` and `TRADEMARKS.md` are present and internally consistent;
2. `README.md`, `protocol/PEACE_PROTOCOL_V0.md`, schemas and conformance vectors agree on scope and semantics;
3. validation workflow is green;
4. no credentials, customer data, private partner correspondence or unpublished third-party material are tracked;
5. third-party references are linked/referenced rather than copied without redistribution rights;
6. governance and contribution rules are present;
7. security reporting process is present;
8. changelog identifies the candidate version;
9. tag, version and exact commit hash are aligned;
10. release notes clearly state draft/prerelease status.

## Release vocabulary

- **public repository** — repository is visible publicly;
- **publication candidate** — content is prepared for an identified draft release but not yet tagged as an immutable release;
- **published draft** — public repository plus immutable version/tag/hash on a validated head;
- **conformant implementation** — an implementation has passed the mandatory requirements for the claimed profile/version; publication alone does not establish this;
- **certified implementation** — assessed under a separately authorized certification programme.

## Commercial boundary

Publication of PEACE does not publish or grant access to any commercial managed control plane, proprietary evaluator, deployment configuration, customer integration, recovery operation, certification backend or assurance service.
