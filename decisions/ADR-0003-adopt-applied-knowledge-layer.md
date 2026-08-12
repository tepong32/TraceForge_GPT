# ADR-0003: Adopt an Applied Knowledge Layer

**Answers the question:**

> **Why does TraceForge preserve reusable project lessons outside the core methodology?**

- **Status:** Accepted
- **Date:** 2026-08-12
- **Deciders:** TraceForge maintainer
- **Related:** v0.6 knowledge-base milestone; ADR-0002

## Decision

Add `knowledge/` as the canonical home for reusable, evidence-earned engineering guidance tied to a technology, artifact, platform, or domain. Organize guides by stable subject area and keep the core methodology provider- and technology-neutral.

Adopt Excel 365 Workbook Engineering as the first guide under `knowledge/spreadsheets/`.

## Reason

Project work produces valuable trial-and-error knowledge that is too specific for universal methodology but too reusable to leave in a conversation or one project's handoff. Without a distinct owner, that knowledge is either lost, duplicated into core methodology, or mixed with project-specific business rules.

## Alternatives Considered

- Add Excel practices directly to the core methodology. Rejected because it would make universal collaboration rules technology-specific.
- Preserve only the originating project's Phase 5 notes. Rejected because future projects would not have a discoverable, generalized guide.
- Store the entire project lesson document unchanged. Rejected because its payroll rules are not universal Excel behavior.
- Create a separate repository for each subject. Deferred because the current volume does not justify fragmented ownership.

## Tradeoffs

The repository gains an additional documentation layer and taxonomy. In return, it can accumulate practical engineering memory without weakening the separation between methodology, reusable practice, and project truth.

## Consequences

Context Compression may promote demonstrated cross-project lessons into Applied Knowledge. Each guide must state scope, evidence limits, validation authority, and project-specific exclusions. Runtime behavior consults relevant guides after repository evidence and explicit requirements are understood.

## Revisit Conditions

Reconsider the structure if guides frequently overlap, category ownership becomes ambiguous, the repository grows beyond practical discovery, or a subject requires an independently versioned body of knowledge.
