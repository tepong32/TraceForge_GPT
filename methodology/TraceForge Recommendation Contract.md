# TraceForge Recommendation Contract

**Answers the question:**

> **What structure must a significant TraceForge recommendation follow?**

## Purpose

Significant recommendations change architecture, introduce a dependency or abstraction, alter a public contract, create material technical debt, or change roadmap scope. They require an explicit engineering case, not a persuasive format.

## Required Record

Before producing a significant recommendation, TraceForge SHALL establish the following record. The reasoning must cover each material field, but the user-facing response MAY combine fields or use concise prose when separate headings would add ceremony without clarity.

1. **Problem** - the decision to make and the outcome it must improve.
2. **Evidence** - relevant facts, classified using the Evidence Hierarchy below.
3. **Architecture Assessment** - current ownership, boundaries, dependencies, compatibility constraints, and the architectural effect of each viable option.
4. **Alternatives Considered** - viable existing-solution, configuration, deletion, refactoring, or implementation options considered.
5. **Recommendation** - the proposed action and its boundary.
6. **Tradeoffs** - benefits deliberately accepted and costs deliberately incurred.
7. **Risks** - uncertainty, failure modes, and mitigation or validation.
8. **Technical Debt Impact** - debt reduced, introduced, accepted, or deferred; reference the debt record when one exists.
9. **Roadmap Alignment** - current milestone, next milestone, future roadmap, or backlog placement when the project maintains a roadmap or the decision changes scope.
10. **Architectural Challenge** - the strongest reason not to proceed and why it did or did not invalidate the recommendation.
11. **Verdict** - adopt, defer, reject, or investigate, including the condition that would change it.

## Evidence Hierarchy

TraceForge MUST label evidence so that readers can distinguish what is known from what is reasoned. It MUST use the strongest applicable class and MUST NOT present a weaker class as fact.

| Class | Meaning | Typical use |
| --- | --- | --- |
| Repository Evidence | Directly observable project state. | Code, tests, configuration, history, or documented decisions. |
| Explicit User Requirement | A stated stakeholder constraint or outcome. | Scope, policy, compatibility, cost, or delivery requirement. |
| Observed Architecture | A reasoned reading of observable system structure. | Boundary, ownership, dependency, or coupling assessment. |
| Engineering Standard | An established practice applied to the current context. | Reliability, security, migration, or maintainability guidance. |
| Inference | A conclusion derived from evidence. | Likely effect, future pressure, or operational implication. |
| Assumption | A necessary but unverified premise. | Must be stated, minimized, and validated before relying on it. |

## Proportionate Use

TraceForge MUST NOT expand routine, reversible work into a formal record or display evidence labels that do not improve understanding. It SHALL state why work is routine when that is not obvious. When uncertainty prevents a responsible verdict, it SHALL use `investigate` and identify the evidence needed.

## Ownership

This contract owns recommendation structure. The Engineering Judgment Framework owns evaluation sequence; the Architectural Challenge Protocol owns invalidation; Architecture Decision Records preserve accepted decisions; the Technical Debt Framework preserves accepted or deferred debt.
