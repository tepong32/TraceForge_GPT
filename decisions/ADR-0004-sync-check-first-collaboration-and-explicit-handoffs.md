# ADR-0004: Adopt Sync-Check-First Collaboration and Explicit Handoffs

**Answers the question:**

> **How does TraceForge prevent stale-context edits and preserve work across local/cloud and conversation boundaries?**

- **Status:** Accepted
- **Date:** 2026-10-14
- **Deciders:** TraceForge maintainer
- **Related:** Conversation Workflow; Operational Behaviors; Session Continuity; Session Handoff Template

## Decision

Make sync-check-first the mandatory first operational gate before repository mutation. Inspect the latest available remote target branch and commit, recent history, relevant project instructions and canonical handoff, and working-tree state wherever the active environment can observe it. Re-check the remote before commit or push and reconcile divergence before proceeding.

Treat local clones, cloud-side editors, and other workspaces as separate working copies. A tool or collaborator must not claim that an inaccessible local working tree is clean or synchronized. Preserve staged, unstaged, untracked, and user-owned changes; do not force-push over newer work or resolve divergence by silently discarding changes.

At the end of a meaningful working session, workday, or before switching conversations, tools, environments, or AI collaborators, update the canonical handoff when authorized and provide a portable handoff when useful. Record actual completion, validation, blockers, next steps, and synchronization status. Routine informational exchanges that do not change project state do not require a handoff update.

## Reason

Repository-backed projects are often worked on from more than one context: a local IDE or Codex session, cloud-side repository tools, and separate conversations. These contexts can observe different state. A handoff can also become stale after new commits. Editing before reconciling state risks overwriting work, misreporting completion, or continuing from assumptions that no longer match the repository.

A concise end-of-session handoff reduces repeated context reconstruction while distinguishing committed remote state from local-only or uncommitted work.

## Alternatives Considered

- Assume a shared remote means local and cloud work are synchronized. Rejected because uncommitted changes and branch divergence are not visible from every environment.
- Sync only before pushing. Rejected because stale-state edits can already cause loss or conflict before the push stage.
- Require a handoff after every conversational exchange. Rejected because routine informational exchanges do not create meaningful state and would add noise.
- Rely on the conversation transcript as the handoff. Rejected because transcripts are not a reliable, concise representation of current repository state.

## Tradeoffs

The protocol adds a small inspection cost before changes and before Git side effects. That cost is proportionate to the risk of lost work, stale assumptions, and misleading completion claims. Handoff updates are required at meaningful stopping points, not after every exchange.

## Consequences

Conversation Workflow owns the order of work. Operational Behaviors makes the sync-check and remote recheck mandatory. Session Continuity owns the lifecycle and reconciliation of canonical and portable handoffs. The Session Handoff Template records synchronization state explicitly. Project-specific instructions may impose stricter controls but must not weaken this baseline without an explicit decision.

## Revisit Conditions

Reconsider the protocol if practical use shows that its checks are redundant, too costly for routine low-risk tasks, or fail to detect meaningful divergence. Any simplification must preserve protection for uncommitted work and explicit honesty about state the current environment cannot observe.
