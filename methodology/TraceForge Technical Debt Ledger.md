# TraceForge Technical Debt Ledger

**Answers the question:**

> **How is intentional or discovered technical debt made visible and managed?**

## Purpose

Technical debt is a known engineering cost accepted, introduced, or discovered in the project. The ledger makes that cost explicit so it can be planned, not rediscovered as surprise work.

The ledger is not a generic task list. Record only debt with a durable architectural, maintainability, reliability, security, or operational consequence.

## Entry Schema

Maintain entries in the project’s chosen debt record using these fields:

| Field | Meaning |
| --- | --- |
| Area | Affected module, boundary, system, or documentation area. |
| Severity | Impact if the debt remains: `Low`, `Moderate`, `High`, or `Critical`. |
| Reason | Why the debt exists and the evidence supporting that conclusion. |
| Estimated Relative Effort | `Small`, `Medium`, `Large`, or `Unknown`; not a calendar estimate. |
| Suggested Milestone | The earliest roadmap placement that is responsible. |
| Status | `Open`, `Accepted`, `Scheduled`, `Resolved`, or `Won't Fix`. |

Reference the recommendation, ADR, or drift review that created the entry. Keep the record current when the decision changes.

## Decision Rules

Debt may be accepted only with an explicit tradeoff and revisit condition. Resolve or re-evaluate it when its assumptions, severity, or roadmap placement changes. A `Won't Fix` entry records a deliberate conclusion, not abandonment.
