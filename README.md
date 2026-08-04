# TraceForge

**Answers the question:**

> **What is TraceForge and where is each part of its methodology owned?**

TraceForge is an AI-assisted software-development methodology for making engineering decisions that remain understandable, maintainable, and useful over the life of a project.

It treats the repository as permanent project memory and conversations as temporary development workspaces. Its purpose is not to accelerate implementation at any cost, but to establish whether a proposed change is the right change for the project.

## Core Methodology

- [Manifesto](manifesto/TraceForge%20Manifesto.md) - Why TraceForge exists.
- [Development Doctrine](methodology/TraceForge%20Development%20Doctrine.md) - The engineering beliefs that guide it.
- [Project Identity](methodology/TraceForge%20Project%20Identity.md) - What defines a TraceForge project.
- [Methodology Index](methodology/README.md) - The canonical ownership map and reading order.

## Architectural Intelligence

TraceForge v0.4 makes its existing philosophy operational through the Engineering Judgment Framework, Operational Behaviors, Recommendation Contract, Architectural Challenge Protocol, Review Lenses, Architecture Decision Records, Architecture Drift Review, Technical Debt Framework, Project Health Reviews, and Engineering Review Checklist.

## Repository Guide

| Area | Responsibility |
| --- | --- |
| `manifesto/` | Purpose and immutable methodology philosophy. |
| `methodology/` | Workflows, decision practices, continuity, and review methodology. |
| `templates/` | Reusable records that apply the methodology. |
| `decisions/` | Consequential accepted, rejected, or superseded architectural decisions. |

## Adoption

For a significant change, follow the Engineering Judgment Framework and record the result using the Recommendation Contract. Preserve consequential accepted decisions in an ADR, verify delivery with the Engineering Review Checklist, and use the Session Handoff Template when work spans sessions.

## Version

Current release: **v0.4.0 - Architectural Intelligence**.
