# TraceForge Architecture Decision Records

**Answers the question:**

> **How must consequential architectural decisions be preserved and revisited?**

## Purpose

An Architecture Decision Record (ADR) preserves a decision whose rationale would otherwise be costly to reconstruct. It is a durable project record, not a design diary or a substitute for implementation documentation.

## Required Behavior

TraceForge MUST create an ADR after a decision is accepted when it materially changes or constrains architecture, such as a boundary, dependency direction, storage or integration choice, public interface, migration strategy, or cross-cutting operational policy. A recommendation or proposal alone does not authorize an `Accepted` ADR. TraceForge MUST NOT create an ADR for routine local implementation choices.

TraceForge SHALL:

1. Assign the next sequential identifier: `ADR-NNNN-short-title.md`.
2. Record the decision using the [ADR template](../templates/Architecture%20Decision%20Record%20Template.md).
3. Mark its status as `Proposed`, `Accepted`, `Superseded`, or `Rejected`.
4. Create a new ADR that references the earlier one when conditions change; it MUST NOT rewrite history.

## Required Content

Every ADR MUST record the decision, reason, alternatives, tradeoffs, consequences, and revisit conditions. It SHALL link related recommendation evidence without duplicating the Recommendation Contract.

## Ownership

Store ADRs in `decisions/`. ADRs own durable decision outcomes; the Engineering Judgment Framework owns evaluation sequence; project documentation owns the current architecture.
