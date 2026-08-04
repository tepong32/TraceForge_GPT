# TraceForge Technical Debt Framework

**Answers the question:**

> **How must intentional or discovered technical debt be made visible and managed?**

## Purpose

Technical debt is a known engineering cost accepted, introduced, or discovered in the project. This framework requires that cost to be explicit so it can be planned, not rediscovered as surprise work.

The debt record is not a generic task list. TraceForge MUST record only debt with a durable architectural, maintainability, reliability, security, or operational consequence.

## Required Debt Record

TraceForge SHALL maintain debt entries in the project's chosen record using these fields:

| Field | Meaning |
| --- | --- |
| Area | Affected module, boundary, system, or documentation area. |
| Severity | Impact if the debt remains: `Low`, `Moderate`, `High`, or `Critical`. |
| Reason | Why the debt exists and the evidence supporting that conclusion. |
| Estimated Relative Effort | `Small`, `Medium`, `Large`, or `Unknown`; not a calendar estimate. |
| Suggested Milestone | The earliest responsible roadmap placement. |
| Status | `Open`, `Accepted`, `Scheduled`, `Resolved`, or `Won't Fix`. |

Each entry MUST reference the recommendation, ADR, or drift review that created it and remain current when the decision changes.

## Decision Rules

TraceForge MAY accept debt only with an explicit tradeoff and revisit condition. It MUST resolve or re-evaluate debt when its assumptions, severity, or roadmap placement changes. A `Won't Fix` entry records a deliberate conclusion, not abandonment.

## Ownership

This framework owns how debt is recorded and governed. The Recommendation Contract owns debt impact for one recommendation; Architecture Drift Review identifies drift that must become debt.
