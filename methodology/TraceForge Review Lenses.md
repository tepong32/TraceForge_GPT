# TraceForge Review Lenses

**Answers the question:**

> **How should TraceForge change review emphasis without changing its engineering principles?**

## Purpose

A review lens prioritizes certain evidence and risks for a particular review. It does not create a separate operating mode, override the Development Doctrine, or preselect a solution.

## Available Lenses

| Lens | Primary emphasis |
| --- | --- |
| Architecture | Boundaries, ownership, dependency direction, and coherence. |
| Maintainability | Comprehension, change cost, testing, and operational clarity. |
| Security | Trust boundaries, data exposure, least privilege, and failure handling. |
| Performance | Measured bottlenecks, resource cost, and capacity constraints. |
| Refactoring | Safe simplification, migration cost, and responsibility clarity. |
| Documentation | Source-of-truth ownership, accuracy, and continuity. |
| Release Readiness | Compatibility, migration, deployment, monitoring, and rollback. |
| Technical Debt | Debt severity, accumulation, and responsible roadmap placement. |

## Use

Name the selected lens at the start of a focused review. Apply the Engineering Judgment Framework and Recommendation Contract unchanged. Use additional lenses only when they affect the verdict; otherwise avoid expanding the review.
