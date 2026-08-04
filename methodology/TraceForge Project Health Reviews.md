# TraceForge Project Health Reviews

**Answers the question:**

> **How is a project's engineering health communicated without arbitrary scoring?**

## Purpose

A health review communicates the current engineering condition, the evidence behind it, and the action it warrants. It does not reduce judgment to a numeric score.

## Health States

| State | Meaning |
| --- | --- |
| Healthy | Evidence shows the assessed area is controlled and supports planned work. |
| Stable | No material concern is active, but the area needs normal observation. |
| Needs Attention | A bounded concern should be addressed in planned work. |
| Growing Risk | Evidence indicates worsening cost, fragility, or architectural drift; ownership and timing are required. |
| Critical | Current risk threatens delivery, reliability, security, or maintainability; immediate decision or mitigation is required. |

## Review Record

For each assessed area, record the state, Repository Evidence, scope, observed change, risks, and recommended next action. State what would improve or worsen the assessment. Link to ADRs, drift findings, and debt entries where relevant.

## Scope

Review a named concern such as architecture, delivery readiness, dependency health, documentation continuity, or technical debt. Do not issue an undifferentiated project score.
