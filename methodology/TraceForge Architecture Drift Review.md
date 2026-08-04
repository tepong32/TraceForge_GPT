# TraceForge Architecture Drift Review

**Answers the question:**

> **How must TraceForge detect and evaluate unintended architectural change?**

## Purpose

Architecture drift is a meaningful divergence between the intended architecture and the system that now exists. A drift review makes that divergence visible before it becomes accepted by accident. It is evidence-based review, not a compliance score or a demand for idealized purity.

## Review Scope

TraceForge SHALL compare the current repository with its documented architecture and accepted ADRs. It MUST assess only areas changed by the milestone unless a broader review is explicitly required.

The review assesses boundary changes, dependency direction, ownership changes, coupling, layer violations, naming consistency, and responsibility movement.

## Findings

Each finding MUST state the observed evidence, intended state, impact, and one of: `No action`, `Accept`, `Correct now`, or `Track as debt`. An accepted consequential deviation requires an ADR. Tracked debt requires a debt record.

## Cadence

TraceForge SHALL perform a bounded review before release, after a cross-boundary change, and when repeated local exceptions indicate a possible design shift.

## Ownership

This document owns detection and evaluation of unintended architectural change. The Technical Debt Framework owns tracked debt; Architecture Decision Records own accepted consequential deviations.
