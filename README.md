# TraceForge

**Answers the question:**

> **What is TraceForge and where is each part of its methodology owned?**

TraceForge is an AI-assisted software-development methodology for making engineering decisions that remain understandable, maintainable, and useful over the life of a project.

It treats the repository as permanent project memory and conversations as temporary development workspaces. Its purpose is not to accelerate implementation at any cost, but to establish whether a proposed change is the right change for the project.

## Core Methodology

- [Manifesto](manifesto/TraceForge%20Manifesto.md) — Why TraceForge exists.
- [Development Doctrine](methodology/TraceForge%20Development%20Doctrine.md) — The engineering beliefs that guide it.
- [Project Identity](methodology/TraceForge%20Project%20Identity.md) — What defines a TraceForge project.
- [Engineering Judgment Framework](methodology/TraceForge%20Decision%20Framework.md) — How significant recommendations are developed.
- [Recommendation Contract](methodology/TraceForge%20Recommendation%20Contract.md) — What significant recommendations must demonstrate.
- [Architectural Challenge Protocol](methodology/TraceForge%20Architectural%20Challenge%20Protocol.md) — How a recommendation tests itself.
- [Project and Conversation Workflows](methodology/README.md) — How work progresses and continuity is preserved.

## Architectural Intelligence

TraceForge v0.4 adds explicit operational contracts without replacing the existing methodology:

- Architecture Decision Records preserve consequential decisions and revisit conditions.
- Architecture Drift Reviews identify unintended boundary, ownership, dependency, and coupling changes.
- The Technical Debt Ledger makes accepted or discovered debt visible and planable.
- Project Health Reviews use evidence-backed health states rather than arbitrary scores.
- Review Lenses focus a review while preserving the same engineering principles.
- The Engineering Review Checklist verifies a change proportionately before completion.

## Repository Guide

| Area | Responsibility |
| --- | --- |
| `manifesto/` | Purpose and immutable methodology philosophy. |
| `methodology/` | Workflows, decision practices, continuity, and review methodology. |
| `templates/` | Reusable records that apply the methodology. |
| `decisions/` | Consequential accepted, rejected, or superseded architectural decisions. |
| `standards/` | Project-level standards when a project adopts TraceForge. |
| `examples/` | Worked examples when an example is necessary to clarify application. |

## Adoption

For a significant change, begin with the Engineering Judgment Framework, record the result using the Recommendation Contract, and preserve a consequential accepted decision in an ADR. Use the Engineering Review Checklist before delivery and the Session Handoff Template when work spans sessions.

## Version

Current release: **v0.4.0 — Architectural Intelligence**.

TraceForge evolves incrementally. New practices must have a distinct responsibility, preserve canonical ownership, and measurably improve engineering decisions.
