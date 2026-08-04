# TraceForge Architecture Drift Review

**Answers the question:**

> **How is unintended architectural change detected and evaluated?**

## Purpose

Architecture drift is a meaningful divergence between the intended architecture and the system that now exists. A drift review makes that divergence visible before it becomes accepted by accident.

It is evidence-based review, not a compliance score or a demand for idealized purity.

## Review Scope

Compare the current repository with its documented architecture and accepted ADRs. Assess only areas changed by the milestone unless a broader review is explicitly required.

Evaluate these concerns:

- **Boundary changes** — responsibilities crossing or bypassing intended module boundaries.
- **Dependency direction** — dependencies that reverse or bypass the intended direction.
- **Ownership changes** — responsibilities that have moved, duplicated, or become unowned.
- **Coupling** — new knowledge, synchronization, or change propagation between components.
- **Layer violations** — layer-specific policies, infrastructure, or presentation concerns leaking across layers.
- **Naming consistency** — names that obscure established concepts or imply incorrect ownership.
- **Responsibility movement** — accumulation of unrelated responsibilities within a component.

## Findings

Each finding states the observed evidence, the intended state, the impact, and one of: `No action`, `Accept`, `Correct now`, or `Track as debt`. An accepted deviation requires an ADR when it is consequential. Tracked debt requires a ledger entry.

## Cadence

Perform a bounded review before release, after a cross-boundary change, and when repeated local exceptions indicate a possible design shift.
