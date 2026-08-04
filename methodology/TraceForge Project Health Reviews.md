# TraceForge Project Health Reviews

**Answers the question:**

> **How must TraceForge communicate a project's engineering health without arbitrary scoring?**

## Purpose

A health review communicates the current engineering condition, the evidence behind it, and the action it warrants. TraceForge MUST NOT reduce judgment to a numeric score.

## Health States

| State | Meaning |
| --- | --- |
| Healthy | Evidence shows the assessed area is controlled and supports planned work. |
| Stable | No material concern is active, but the area needs normal observation. |
| Needs Attention | A bounded concern requires planned work. |
| Growing Risk | Evidence indicates worsening cost, fragility, or architectural drift; ownership and timing are required. |
| Critical | Current risk threatens delivery, reliability, security, or maintainability; immediate decision or mitigation is required. |

## Required Record

For each assessed area, TraceForge SHALL record the state, Repository Evidence, scope, observed change, risks, and recommended next action. It SHALL state what would improve or worsen the assessment and link to ADRs, drift findings, and debt entries where relevant.

## Ownership

This document owns evidence-backed health communication. Review Lenses select emphasis; Architecture Drift Review and the Technical Debt Framework provide specific findings.
