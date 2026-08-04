# TraceForge Recommendation Contract

**Answers the question:**

> **What must a significant TraceForge recommendation demonstrate before it can be accepted?**

## Purpose

Significant recommendations change architecture, introduce a dependency or abstraction, alter a public contract, create material technical debt, or change roadmap scope. They require an explicit engineering case, not a persuasive format.

This contract makes the basis, limits, and consequences of that case reviewable. It complements the [Engineering Judgment Framework](TraceForge%20Decision%20Framework.md), which defines how the case is developed.

## Required Record

Each significant recommendation must contain the following sections. Concise entries are sufficient when the decision is small; omission is not.

1. **Problem** — the decision to make and the outcome it must improve.
2. **Evidence** — relevant facts, classified using the Evidence Hierarchy below.
3. **Recommendation** — the proposed action and its boundary.
4. **Alternatives** — viable existing-solution, configuration, deletion, refactoring, or implementation options considered.
5. **Tradeoffs** — benefits deliberately accepted and costs deliberately incurred.
6. **Risks** — uncertainty, failure modes, and mitigation or validation.
7. **Architectural Impact** — changed ownership, boundaries, dependencies, or interfaces; state `None` when applicable.
8. **Roadmap Alignment** — current milestone, next milestone, future roadmap, or backlog placement.
9. **Technical Debt Impact** — debt reduced, introduced, accepted, or deferred; reference the ledger entry when one exists.
10. **Self-Challenge** — the strongest reason not to proceed and why it did or did not invalidate the recommendation.
11. **Verdict** — adopt, defer, reject, or investigate, including the condition that would change it.

## Evidence Hierarchy

Evidence must be labeled so that readers can distinguish what is known from what is reasoned. Use the strongest applicable class and do not present a weaker class as fact.

| Class | Meaning | Typical use |
| --- | --- | --- |
| Repository Evidence | Directly observable project state. | Code, tests, configuration, history, or documented decisions. |
| Explicit User Requirement | A stated stakeholder constraint or outcome. | Scope, policy, compatibility, cost, or delivery requirement. |
| Architecture Observation | A reasoned reading of system structure. | Boundary, ownership, dependency, or coupling assessment. |
| Engineering Best Practice | A generally established practice applied to the current context. | Reliability, security, migration, or maintainability guidance. |
| Inference | A conclusion derived from evidence. | Likely effect, future pressure, or operational implication. |
| Assumption | A necessary but unverified premise. | Must be stated, minimized, and validated before relying on it. |

## Applicability

Do not expand routine, reversible work into a formal record. State why the work is routine when that is not obvious. When uncertainty prevents a responsible verdict, use `investigate` and identify the evidence needed.

## Relationship to the Methodology

The contract governs the content of recommendations. Architecture Decision Records preserve accepted decisions; the Technical Debt Ledger preserves accepted or deferred debt; the Session Continuity Package preserves the outcome for later work.
