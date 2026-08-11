# ADR-0002: Adopt Collaborative Execution and Reliable Continuity

**Answers the question:**

> **Why did TraceForge adopt the v0.5 request-to-delivery and handoff model?**

- **Status:** Accepted
- **Date:** 2026-08-12
- **Deciders:** TraceForge maintainer
- **Related:** v0.5 Collaborative Execution milestone; ADR-0001

## Decision

Adopt a proportionate request-to-delivery workflow and a two-form continuity system: one canonical current-state handoff in the repository and a portable block for transfer between conversations or AI environments.

The workflow classifies the user's request, grounds itself in repository evidence, operates within explicit authority, verifies the result, and captures current or durable knowledge in the correct owner. The repository remains authoritative when a handoff conflicts with current state.

## Reason

TraceForge v0.4 makes significant engineering judgment explicit but does not fully define how behavior changes across ordinary inquiries, reviews, diagnoses, plans, implementations, and monitoring. Its continuity guidance lists useful state but does not define a canonical artifact lifecycle, staleness detection, portable transfer, or a deterministic resume protocol.

Users who begin a new conversation need current work to resume without replaying the prior transcript or trusting a stale summary.

## Alternatives Considered

- Retain v0.4 behavior and rely on conversational judgment. Rejected because request boundaries and completion claims would remain inconsistent.
- Generate only copy-paste handoffs. Rejected because portable blocks can drift from repository truth and are difficult to maintain as canonical state.
- Maintain only a repository handoff. Rejected because another conversation or AI may not have repository access.
- Produce a handoff after every exchange. Rejected because routine conversations would create noise and stale-state churn.

## Tradeoffs

The model improves scope control, completion honesty, and resumability at the cost of maintaining one small current-state artifact after meaningful work. Separating volatile state from durable records prevents the handoff from becoming a second documentation system.

## Consequences

Conversation Workflow owns request progression. Session Continuity owns canonical and portable handoffs, reconciliation, and resume behavior. Context Compression owns the durable-knowledge boundary. `SESSION_HANDOFF.md` becomes the default project-level snapshot, while projects may document another location.

Release actions remain explicitly authorized rather than inferred from implementation work.

## Revisit Conditions

Reconsider the model if repeated use shows that the canonical handoff becomes duplicative, produces frequent merge conflicts, cannot be reconciled reliably, or fails to reduce context reconstruction in new conversations.
