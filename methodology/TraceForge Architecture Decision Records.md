# TraceForge Architecture Decision Records

**Answers the question:**

> **How are consequential architectural decisions preserved and revisited?**

## Purpose

An Architecture Decision Record (ADR) preserves a decision whose rationale would otherwise be costly to reconstruct. It is a durable project record, not a design diary or a substitute for implementation documentation.

## When to Create an ADR

Create an ADR when a decision materially changes or constrains architecture, such as a boundary, dependency direction, storage or integration choice, public interface, migration strategy, or cross-cutting operational policy.

Do not create an ADR for routine local implementation choices. Link related evidence and implementation work instead of repeating them.

## Lifecycle

1. Assign the next sequential identifier: `ADR-NNNN-short-title.md`.
2. Record the decision using the [ADR template](../templates/Architecture%20Decision%20Record%20Template.md).
3. Mark its status as `Proposed`, `Accepted`, `Superseded`, or `Rejected`.
4. When conditions change, create a new ADR that references the earlier one; do not rewrite history.

## Required Content

Every ADR records the decision, reason, alternatives, tradeoffs, consequences, and revisit conditions. It should identify related recommendation evidence without duplicating the Recommendation Contract.

## Location and Ownership

Store ADRs in `decisions/`. The ADR owns the durable decision outcome; the Decision Framework owns the evaluation process; project documentation owns the current architecture.
