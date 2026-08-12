# TraceForge Applied Knowledge

**Answers the question:**

> **How does TraceForge organize reusable engineering knowledge learned through project work?**

## Purpose

The methodology defines how TraceForge works. Applied Knowledge records reusable, evidence-earned guidance for a particular technology, artifact, platform, or engineering domain.

A knowledge guide helps future projects avoid rediscovering the same failure modes without turning one project's business rules into universal methodology.

## Admission Standard

A lesson belongs here only when it is:

- demonstrated through implementation, failure analysis, compatibility testing, or repeated project use;
- likely to apply beyond the project that revealed it;
- specific enough to change future engineering behavior;
- compatible with the core methodology;
- stripped of confidential data and project-only business rules;
- explicit about its scope, evidence limits, and final validation authority.

An unverified idea remains an assumption or experiment. A one-project decision remains in that project's documentation or ADRs. A universal collaboration behavior belongs in `methodology/`, not here.

## Organization

Knowledge is grouped by stable engineering domain rather than by originating project:

- [Spreadsheets](spreadsheets/README.md) — spreadsheet applications, workbook formats, formulas, compatibility, and workbook validation.

Add a new category only when at least one accepted guide has a clear owner there. Within a category, use one guide per distinct engineering question.

## Guide Contract

Every guide SHALL identify:

1. the question it answers;
2. its intended scope and exclusions;
3. its evidence posture and current maturity;
4. practices supported by observed evidence;
5. required validation gates;
6. failure and recovery behavior;
7. which knowledge remains project-specific;
8. conditions that would require revision.

Guides inform judgment; they do not override repository evidence, explicit user requirements, target-application behavior, or project-specific rules.

## Evidence Maturity

Each guide distinguishes how strongly a lesson has been established:

| Maturity | Meaning |
| --- | --- |
| Project-observed | Demonstrated in one project or one controlled incident. Useful, but not yet broadly replicated. |
| Repeated | Demonstrated across multiple projects, workbooks, environments, or independent checkpoints. |
| Externally anchored | Supported by an authoritative specification, vendor behavior, or documented platform contract. |
| Provisional | A plausible practice retained for deliberate testing; it must not be presented as established fact. |

A guide can contain lessons at different maturity levels. Maturity describes evidence breadth, not importance. TraceForge SHALL state when a conservative default comes from limited evidence and SHALL revise it when broader use contradicts it.

## Promotion Workflow

At a project checkpoint:

1. Collect the trial-and-error lessons and the evidence behind them.
2. Separate reusable engineering behavior from business-specific rules.
3. Assign an evidence-maturity level without overstating one-project experience.
4. Compare the candidate lesson with existing guides.
5. Refine an existing guide when it already owns the question.
6. Create a new guide only when the question has no owner.
7. Link the originating project's durable rules from that project rather than copying them here.
8. Validate the guide against the failure that produced it and at least one future use when possible.

## Ownership

This index owns admission, categorization, and evolution of applied knowledge. Category indexes own discovery. Individual guides own domain-specific practice. Context Compression determines when project learning deserves promotion.
