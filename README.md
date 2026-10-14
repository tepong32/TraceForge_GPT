# TraceForge

**Answers the question:**

> **What is TraceForge and where is each part of its methodology owned?**

TraceForge is a provider-neutral, AI-assisted software-development methodology for turning user intent into engineering decisions and changes that remain understandable, maintainable, and resumable over the life of a project.

It treats the repository as authoritative project memory and conversations as temporary development workspaces. Its purpose is not to accelerate implementation at any cost, but to establish the right change, deliver it within authority, verify it, and preserve enough state for work to continue safely.

## Core Methodology

- [Manifesto](manifesto/TraceForge%20Manifesto.md) - Why TraceForge exists.
- [Development Doctrine](methodology/TraceForge%20Development%20Doctrine.md) - The engineering beliefs that guide it.
- [Project Identity](methodology/TraceForge%20Project%20Identity.md) - What defines a TraceForge project.
- [Methodology Index](methodology/README.md) - The canonical ownership map and reading order.
- [Runtime Contract](You%20are%20TraceForge.md) - The behaviors TraceForge follows during engineering work.

## Collaborative Execution

TraceForge v0.5 adds a proportionate request-to-delivery workflow and reliable session continuity. It distinguishes inquiry, review, diagnosis, planning, implementation, and monitoring; grounds itself in repository evidence before asking questions; respects the user's authority boundary; and verifies outcomes before claiming completion.

**Sync-check first:** before any repository mutation, inspect the latest available remote branch and commit, recent history, relevant instructions, handoff, and working-tree state. Re-check the remote before committing or pushing. Treat local and cloud environments as separate working copies; never assume remote inspection reveals uncommitted local changes.

Meaningful work is carried between conversations through a canonical [`SESSION_HANDOFF.md`](SESSION_HANDOFF.md) snapshot and, when needed, a portable copy-paste handoff. At the end of a meaningful work session or before switching conversations/tools/environments, record actual completion, validation, blockers, next steps, and what is or is not synchronized. The repository remains authoritative when a handoff becomes stale.

## Applied Knowledge

TraceForge v0.6 introduces the [Applied Knowledge index](knowledge/README.md), preserving reusable engineering practices learned through real project work without making the core methodology technology-specific. Its first subject area covers [spreadsheet assessment](knowledge/spreadsheets/Spreadsheet%20Assessment%20and%20Business-Rule%20Discovery.md) and [Excel 365 workbook engineering](knowledge/spreadsheets/Excel%20365%20Workbook%20Engineering.md).

## Repository Guide

| Area | Responsibility |
| --- | --- |
| `manifesto/` | Purpose and foundational methodology philosophy. |
| `methodology/` | Workflows, decision practices, continuity, and review methodology. |
| `templates/` | Reusable records that apply the methodology. |
| `decisions/` | Consequential accepted, rejected, or superseded architectural decisions. |
| `knowledge/` | Reusable, evidence-earned guidance grouped by engineering domain. |
| `tests/` | Release-tool and repository-consistency verification. |
| `SESSION_HANDOFF.md` | Replaceable current working-state snapshot. |

## Adoption

Start with the Conversation Workflow and Runtime Contract. For a significant decision, apply the Engineering Judgment Framework and Recommendation Contract. Preserve an accepted consequential decision in an ADR, verify delivery with the Engineering Review Checklist, and update the canonical handoff at a meaningful stopping point.

## Release Preparation

`version_manager.py` updates VERSION and CHANGELOG locally by default. Use `--dry-run` to preview. Git effects require the explicit `--commit`, `--tag`, and `--push` flags; each stronger effect requires the preceding one.

## Version

Current release: **v0.6.0 - Applied Knowledge**.
