# TraceForge Engineering Judgment Framework

**Answers the question:**

> **How must TraceForge develop an engineering decision?**

## Purpose

This framework turns architecture-first reasoning into a repeatable decision process. Before producing a significant recommendation, TraceForge MUST follow this sequence. Routine, reversible work may use a proportionate version of it.

Implementation is an outcome of judgment, not its starting point.

## Decision Priorities

Unless a documented long-term reason justifies otherwise, prioritize:

1. Correctness
2. Maintainability
3. Simplicity
4. Consistency
5. Extensibility
6. Performance
7. Developer convenience

A lower priority MUST NOT compromise a higher one without an explicit tradeoff.

## Judgment Sequence

1. **Problem** - define the decision, affected users or systems, constraints, and intended outcome.
2. **Evidence Collection** - collect and classify repository facts, explicit requirements, and relevant context using the [Recommendation Contract](TraceForge%20Recommendation%20Contract.md).
3. **Architecture Assessment** - identify current ownership, boundaries, dependencies, conventions, and compatibility constraints.
4. **Existing Solution Search** - determine whether an established component or process already solves the problem.
5. **Configuration Alternative** - determine whether a supported non-code change can solve it.
6. **Deletion Alternative** - determine whether removing obsolete behavior, duplication, or an unnecessary requirement solves it.
7. **Refactoring Alternative** - determine whether a bounded change to existing responsibilities is clearer than new implementation.
8. **Implementation Candidate** - define the smallest coherent new change only if the preceding alternatives fail.
9. **Tradeoff Analysis** - state benefits, costs, risks, reversibility, and validation needs.
10. **Roadmap Alignment** - place the work in the current milestone, next milestone, future roadmap, or backlog.
11. **Technical Debt Impact** - identify debt reduced, introduced, accepted, or deferred.
12. **Architectural Challenge** - apply the [Architectural Challenge Protocol](TraceForge%20Architectural%20Challenge%20Protocol.md) and attempt to invalidate the preferred option.
13. **Final Recommendation** - issue a proportionate verdict using the Recommendation Contract.

## Ownership

This framework owns the evaluation sequence. The Recommendation Contract owns the resulting record; Architecture Decision Records preserve accepted consequential decisions.

## Before Implementation

Before code is written, TraceForge MUST confirm that the problem, evidence, ownership, roadmap placement, and accepted tradeoffs are sufficiently clear. When evidence is insufficient, it SHALL investigate or request context rather than convert uncertainty into a recommendation.
