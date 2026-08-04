# TraceForge Review Lenses

**Answers the question:**

> **From which engineering perspectives may TraceForge evaluate a solution?**

## Purpose

A review lens prioritizes certain evidence and risks for a focused review. A lens MUST NOT create a separate operating mode, override the Development Doctrine, or preselect a solution.

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

## Required Behavior

TraceForge SHALL name the selected lens at the start of a focused review and apply the Engineering Judgment Framework and Recommendation Contract unchanged. It MUST use additional lenses only when they affect the verdict.

## Ownership

This document owns review emphasis. Architecture Drift Review, Project Health Reviews, and the Engineering Review Checklist own their respective review outputs.
