# TraceForge Session Continuity

**Answers the question:**

> **How does a TraceForge project preserve and resume meaningful work across independent sessions?**

## Purpose

Projects outlive conversations, context windows, contributors, and AI models. Session Continuity preserves the current working state needed to resume safely without treating a transcript as project memory.

The repository is authoritative. A handoff is a replaceable snapshot of current work, not a permanent account of the project and not authority to perform actions the user has not authorized.

## Continuity Artifacts

Each TraceForge project SHOULD maintain one canonical current-state artifact. The default location is `SESSION_HANDOFF.md` at the project root; a project MAY document another location.

When work moves to another conversation or AI, TraceForge SHOULD also produce a portable handoff block derived from the canonical artifact. Both forms use the same information model, but the portable block includes enough context to be useful without repository access.

The canonical handoff is replaced as state changes. It is not an append-only diary. Durable outcomes move to their permanent owners before old working state is removed.

## Required Handoff Record

### Snapshot

Record the last-updated timestamp, current release and milestone, branch and source commit when Git is available, and relevant working-tree state. Identify uncommitted or user-owned changes that the next session must preserve.

### Current Objective

Record the intended outcome, scope boundary, and one status: `Ready`, `In Progress`, `Blocked`, or `Awaiting Decision`.

### Completed Work

Record material work completed since the previous handoff, affected areas, and the validation supporting completion. Do not list an outcome as complete when required checks have failed or remain unknown.

### Work in Progress

Record exact partial state, what remains, and any unsafe point from which work must not blindly continue.

### Decisions

Link accepted decisions to ADRs or canonical documentation. Retain a rejected approach only when its reason prevents repeated work. State assumptions that still require validation.

### Risks and Blockers

Record known failures, constraints, compatibility concerns, mitigations, and any user decision or authority required.

### Validation

Record checks run and their outcome as passed, failed, or skipped. Summarize relevant failures without embedding large logs.

### Next Starting Point

Record the next independently useful objective, the first concrete inspection or implementation step, and its completion criteria.

### Open Questions

Record only unresolved questions that can materially change the next action.

## Update Cadence

TraceForge SHALL refresh continuity state:

- after material implementation or an accepted engineering decision;
- when work pauses in an incomplete state;
- before likely context exhaustion;
- at a milestone or release boundary;
- at the end of a meaningful working session or workday when project state changed or unresolved work must be carried forward;
- when the user intends to continue in another conversation, tool, environment, or with another AI.

Routine explanations and exchanges that do not change project state do not require an update. The purpose is a reliable resume point, not a transcript or a handoff after every casual exchange.

## Sync-Check Before Mutation

Before changing repository files, TraceForge SHALL inspect the latest available repository state and reconcile it with the handoff and conversation context. The check includes the target branch and latest remote commit, recent history, relevant instructions and decisions, and working-tree status/diff wherever visible.

When local and cloud environments are separate, each is a distinct working copy. A remote inspection cannot establish whether a local clone has uncommitted changes. Record this limitation when relevant, and reconcile the copies before merging or pushing. Before committing or pushing, re-fetch the target remote branch and handle any divergence deliberately.

A handoff is a checkpoint, not permission to overwrite the current repository. When the handoff's source commit or material state differs from current evidence, mark it Needs Reconciliation and reconcile before proceeding.

## Durable Knowledge Boundary

Before replacing resolved handoff content, move lasting knowledge to its canonical owner:

| Knowledge | Owner |
| --- | --- |
| Current objective, partial work, blockers, and next action | Canonical handoff |
| Current architecture and established conventions | Project documentation |
| Accepted consequential architectural decisions | ADRs |
| Material accepted or discovered debt | Debt record |
| Released outcomes | Changelog |

The handoff links to these records instead of duplicating their rationale. At a milestone boundary, distill durable knowledge first, then reset the handoff to the next objective.

## Portable Handoff

A portable handoff SHALL begin with this direction:

> Resume from this snapshot. Inspect any available repository state before acting, treat the repository as authoritative, and reconcile differences rather than assuming this handoff is current.

It SHALL include the required handoff record in compact form and make failing tests, incomplete edits, dirty working-tree state, blockers, and decisions awaiting the user explicit. It MUST NOT contain hidden reasoning, complete transcripts, large diffs, raw logs, or duplicated permanent documentation.

## Resume Protocol

At the start of a resumed session, TraceForge SHALL:

1. **Sync-check first:** inspect the live repository/target branch, latest remote commit, recent history, and working-tree state wherever available before editing.
2. Read project identity, the canonical handoff, relevant accepted decisions, and current repository state.
3. Compare the recorded release, milestone, branch, source commit, working tree, and objective with current evidence.
4. Treat the repository as authoritative when evidence conflicts.
5. Mark the snapshot Needs Reconciliation when its branch, revision, or material state no longer matches.
6. Reconstruct the current objective and constraints from canonical evidence.
7. Briefly state the restored objective, material discrepancies, sync status, and next action.
8. Resume without asking the user to repeat settled context.

## Non-Git Projects

Projects without Git omit branch, commit, and working-tree fields. They still record a timestamp, project version or milestone when available, current state, validation, and next action.

## Ownership

This document owns canonical handoff lifecycle, portable transfer, stale-state reconciliation, and resume behavior. Context Compression owns what becomes durable knowledge. Conversation Workflow owns when the lifecycle invokes a handoff.
