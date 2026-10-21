# Changelog

## Unreleased

### Added

- Repository-first source-of-truth and deployment-integrity rules: trace deployments to known commits, verify the running result rather than trusting deployment status, reconcile emergency hotfixes back into version control, and keep maintenance knowledge portable.

**Answers the question:**

> **What released changes have altered TraceForge?**

## [0.6.0] - 2026-08-12

### Added

- Applied Knowledge layer for reusable, evidence-earned engineering guidance organized by subject rather than originating project.
- Excel 365 Workbook Engineering guide derived from phased workbook compatibility and validation lessons.
- Spreadsheet Assessment and Business-Rule Discovery guide with an explicit assumption register and implementation-risk gates.
- Rules for reading, preserving, and interpreting Excel Notes and threaded Comments, including native-language slang, shorthand, keyword-only annotations, and tool capability limits.
- Evidence-maturity labels that prevent one-project lessons from being presented as broadly proven.
- ADR-0003 defining the boundary between core methodology, reusable knowledge, and project-specific rules.

### Changed

- Runtime and knowledge-compression guidance now promote demonstrated cross-project lessons without weakening project-specific ownership.
- Spreadsheet assessment now separates observed design, confirmed intent, inference, and assumptions before implementation.

### Validation

- Added regression checks for guide discovery, evidence maturity, assumption visibility, multilingual annotations, and exclusion of project-only payroll rules.
- All 16 standard-library tests pass.

## [0.5.0] - 2026-08-12

### Added

- Collaborative Execution workflow for inquiry, review, diagnosis, planning, implementation, and monitoring requests.
- Canonical `SESSION_HANDOFF.md` lifecycle, portable handoff format, stale-state reconciliation, and deterministic resume protocol.
- Standard-library tests for release behavior and repository consistency.
- ADR-0002 documenting the v0.5 execution and continuity model.

### Changed

- Runtime and operational contracts now define authority boundaries, repository-first clarification, progress communication, and evidence-backed completion.
- Context Compression now separates temporary conversation knowledge, current handoff state, and durable project knowledge.
- The release helper is standard-library-only, preserves the original version during secondary updates, and requires explicit flags for Git side effects.
- README, methodology index, review checklist, handoff template, and release metadata now reflect v0.5.

### Fixed

- Removed stale references to methodology documents that do not exist.
- Replaced the malformed v0.4.1 changelog entry and corrected release-version drift.

## [0.4.1] - 2026-08-04

### Changed

- Refined v0.4 terminology, behavioral contracts, recommendation ordering, document ownership, and Engineering Humility guidance.
- Completed the Architectural Intelligence consistency and validation pass.

## [0.4.0] - 2026-08-04

### Added

- Engineering Judgment Framework with a mandatory alternative-first decision sequence.
- Recommendation Contract with an explicit evidence hierarchy and architectural challenge verdict.
- Architectural Challenge Protocol, Architecture Decision Record methodology and template.
- Architecture Drift Review, Technical Debt Framework, Project Health Reviews, Review Lenses, and Operational Behaviors.
- Engineering Review Checklist and expanded Session Handoff template.

### Changed

- The primary TraceForge instruction now operationalizes significant recommendations, review, delivery, and continuity without adding personality or automated judgment.
- Session Continuity now captures accepted decisions, rejected approaches, deferred work, known risks, assumptions, module responsibilities, and open questions.
- README and methodology index now reflect v0.4 Architectural Intelligence.

### Removed

- Empty standards, templates, examples, and an unowned methodology placeholder that had no defined responsibility or usable content.

## [0.3.4] - 2026-07-17
### ✨ Added
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TraceForge v0.3.4
Session Continuity
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Current Milestone
AI-Assisted Development Methodology

Completed
✓ TraceForge Session Continuity

This release establishes how development continues across
multiple independent AI conversations without relying on
complete conversational history.

Introduced

• Development Sessions
  Defines sessions as bounded periods of focused engineering work
  that contribute to the project's long-term evolution.

• Session Boundaries
  Establishes intentional stopping points to preserve clarity and
  maintain development momentum.

• Project Continuity
  Defines the permanent knowledge that carries forward between
  sessions while distinguishing it from temporary conversation.

• Context Restoration
  Establishes how new development sessions reconnect with the
  project's current state and resume work naturally.

• Session Continuity Package
  Defines a concise engineering checkpoint containing the
  information required to restore meaningful project context.

• Relationship with Context Compression
  Clarifies how permanent knowledge preservation and session
  restoration work together to support long-term development.

Result

TraceForge now defines not only how projects are created,
developed, and remembered, but also how they continue
seamlessly across unlimited development sessions.

The methodology now treats conversations as temporary
workspaces while recognizing the repository as the project's
authoritative source of truth.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## [0.3.3] - 2026-07-17
### ✨ Added
========================================
TraceForge Release Summary
Version   : v0.3.3
Milestone : AI-Assisted Development Methodology
========================================

Release
-------
Define Context Compression methodology

Highlights
----------
+ Established Context Compression as the process of
  preserving engineering understanding rather than
  conversational history.

+ Introduced the three layers of project knowledge:
  Temporary, Session, and Project Knowledge.

+ Defined what information should be preserved,
  discarded, and distilled throughout development.

+ Reinforced the repository as the project's
  permanent memory and emphasized preserving
  conclusions over conversations.

Outcome
-------
TraceForge now defines how project knowledge evolves
from temporary discussions into permanent engineering
understanding, ensuring that every completed milestone
strengthens the project's long-term continuity.

Next
----
v0.3.4 — TraceForge Session Continuity

========================================

## [0.3.2] - 2026-07-17
### ✨ Added
========================================
TraceForge Release Summary
Version   : v0.3.2
Milestone : AI-Assisted Development Methodology
========================================

Release
-------
Establish AI Collaboration Guide

Highlights
----------
+ Defined the roles and responsibilities of both the
  human developer and the AI development partner.

+ Established the collaboration philosophy centered on
  understanding, architectural integrity, consistency,
  and long-term maintainability.

+ Formalized the principles that guide AI behavior,
  including proactive collaboration, knowledge
  preservation, and constructive engineering feedback.

+ Clarified decision ownership by reinforcing that AI
  provides recommendations while the human developer
  retains final authority over the project.

Outcome
-------
TraceForge now defines not only how projects and
conversations progress, but also how humans and AI
collaborate as long-term engineering partners.

Next
----
v0.3.3 — TraceForge Context Compression

========================================

## [0.3.1] - 2026-07-17
### ✨ Added
========================================
TraceForge Rel.1ease Summary
Version : v0.3.1
Milestone : AI-Assisted Development Methodology
========================================

Release
-------
Define Project & Conversation Workflows

Highlights
----------
+ Established the Project Workflow lifecycle.
+ Formalized the Conversation Workflow lifecycle.
+ Introduced Capture as a dedicated development phase.
+ Reinforced repository memory before session handoff.

Outcome
-------
The methodology now defines both software evolution
and human-AI collaboration, creating the operational
foundation for all future TraceForge documents.

Next
----
AI Collaboration Guide

========================================

## [0.2.0] - 2026-07-15
### ✨ Added
v0.2: Introduce Architectural Judgment methodology

- Rewrite primary GPT instruction set with emphasis on engineering judgment
- Replace technology-specific expertise with architecture-first decision making
- Add project discovery and architectural review workflows
- Introduce Decision Framework and Conversation Workflow documents
- Expand README with project philosophy, collaboration guidance, repository structure, and roadmap
- Refine documentation to position TraceForge as a long-term software architecture methodology rather than a prompt collection
