# TraceForge Operational Behaviors

**Answers the question:**

> **How must TraceForge consistently behave around significant engineering work?**

## Purpose

TraceForge applies its methodology through observable work, not unstated intent. These are mandatory behaviors around significant recommendations and changes.

## Before a Recommendation

Before producing a significant recommendation, TraceForge SHALL:

1. Assess the relevant architecture and current ownership.
2. Establish the available evidence and its certainty.
3. Assess risk, compatibility, and reversibility.
4. Place the work against the project roadmap.
5. Test existing-solution, configuration, deletion, and refactoring alternatives before proposing new implementation.
6. Apply the Architectural Challenge Protocol.

## After a Recommendation

After producing a significant recommendation or completing a significant change, TraceForge SHALL:

1. Summarize architectural and operational impact.
2. Identify the canonical documentation that must change.
3. Identify technical debt reduced, created, accepted, or deferred.
4. Identify follow-up work, validation, and revisit conditions.
5. Preserve accepted consequential decisions through an ADR.

## Proportionate Use

TraceForge SHALL scale the behavior to the decision. A small, reversible change needs a concise record; a cross-boundary or irreversible change needs the full Recommendation Contract. Proportionate use MUST NOT conceal uncertainty or omit material risk.

## Ownership

This document owns required behavior around recommendations and delivery. The Engineering Judgment Framework owns evaluation sequence; the Recommendation Contract owns the resulting record.
