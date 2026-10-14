# Session Handoff

**Answers the question:**

> **What current state must another conversation receive to resume safely?**

> Resume from this snapshot. Inspect any available repository state before acting, treat the repository as authoritative, and reconcile differences rather than assuming this handoff is current.

## Snapshot

- **Last updated:** YYYY-MM-DD HH:MM timezone
- **Release:**
- **Active milestone:**
- **Branch:** _Omit when Git is unavailable._
- **Source commit:** _Omit when Git is unavailable._
- **Working tree:** Clean | Dirty — identify relevant uncommitted or user-owned changes.
- **Snapshot state:** Current | Needs Reconciliation

## Synchronization State

- **Remote checked:** YYYY-MM-DD HH:MM timezone, or Not Checked.
- **Remote branch / commit:** Record the exact target branch and commit inspected.
- **Local state:** Clean | Dirty | Not Observable — identify uncommitted, staged, untracked, or user-owned changes when known.
- **Divergence:** In Sync | Local Ahead | Remote Ahead | Diverged | Unknown.
- **Before next mutation:** State what must be fetched, reconciled, preserved, or confirmed.

Do not label local state clean or synchronized if the active environment cannot inspect it. Before committing or pushing, re-check the remote branch and reconcile new changes.

## Current Objective

- **Outcome:**
- **Scope:**
- **Status:** Ready | In Progress | Blocked | Awaiting Decision

## Completed Work

- Change, affected area, and supporting validation.

## Work in Progress

- Exact partial state, remaining work, and any unsafe continuation point.

## Decisions

- **Accepted:** Decision and ADR or canonical-document link.
- **Rejected:** Approach and reason, only when retaining it prevents rework.
- **Assumptions:** Unverified premise and validation needed.

## Risks and Blockers

- Risk or blocker, evidence, mitigation, and authority or user input needed.

## Validation

- **Passed:** Check and result.
- **Failed:** Check and concise failure summary.
- **Skipped:** Check and reason.

## Next Starting Point

- **Next objective:**
- **First step:**
- **Completion criteria:**

## Open Questions

- Only questions that can materially change the next action.
