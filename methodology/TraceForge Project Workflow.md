# TraceForge Project Workflow

**Answers the question:**

> **How does a TraceForge project progress from conception to long-term maintenance?**

---

# Purpose

Every TraceForge project follows a consistent lifecycle that prioritizes understanding before implementation, architecture before features, and documentation before memory is lost.

The workflow exists to create software that remains maintainable, understandable, and continuously improvable throughout its lifetime.

Every phase should leave the project in a better state than it was before.

---

# Project Lifecycle

## 1. Discovery

Begin by understanding the problem before proposing solutions.

Define:

- Why the project exists.
- Who benefits from it.
- What real-world problem it solves.
- What success looks like.

A project should never begin with code.

It begins with understanding.

---

## 2. Foundation

Establish the project's long-term direction.

This includes defining:

- Project vision
- Core principles
- Architecture
- Repository structure
- Development methodology

A strong foundation reduces future complexity.

---

## 3. Planning

Break the project into manageable milestones.

Each milestone should:

- solve a meaningful problem,
- be independently valuable,
- produce a stable result,
- prepare the next milestone.

Planning provides direction without restricting future improvement.

---

## 4. Architecture

Design responsibilities before implementation.

Clearly separate concerns such as:

- User Interface
- Business Logic
- Services
- Models
- Utilities
- Infrastructure

Architecture should make future development easier, not harder.

---

## 5. Incremental Development

Implement one working phase at a time.

Prefer small, complete improvements over large unfinished changes.

Every completed phase should leave the project in a working state.

Avoid building multiple unfinished systems simultaneously.

---

## 6. Review

Review before expanding.

Evaluate:

- Architecture
- Maintainability
- Readability
- Simplicity
- User experience

Problems found during review are cheaper to solve than problems discovered after release.

---

## 7. Refinement

Improve existing work when doing so increases the project's long-term quality.

Refactoring should aim to:

- reduce duplication,
- simplify complexity,
- clarify architecture,
- improve maintainability.

Refactoring is an investment, not a goal.

---

## 8. Documentation

Capture knowledge before it is forgotten.

Document:

- important decisions,
- architectural reasoning,
- methodology improvements,
- lessons learned.

When a demonstrated lesson is reusable beyond the project, distill it into Applied Knowledge. Keep the originating project's business rules in that project's documentation.

The repository serves as the project's permanent memory.

Documentation should preserve understanding, not duplicate code.

---

## 9. Release

Publish only stable milestones.

A release represents a dependable checkpoint in the project's evolution.

Working software is more valuable than unfinished perfection.

### Deployment integrity

Before and after deployment, preserve a traceable relationship between repository and runtime:

- Record the repository, branch or release reference, and commit/build identifier being deployed whenever the platform supports it.
- Verify the actual deployment target and configuration; do not infer production behavior from localhost, a preview, or a successful deployment message.
- After deployment, inspect the running application and exercise representative workflows. Compare the result with the intended source and acceptance criteria.
- If the platform builds from a different branch, generated files, or a separate deployment project, document that relationship explicitly.
- If a hotfix must be applied outside version control, back-port it into the repository immediately and verify that the source-backed deployment contains the fix.
- Never claim production verification when only a local build, static validation, or deployment status was checked.

A deployment is complete only when the deployed version is identifiable and the relevant runtime checks have been reported honestly.

---

## 10. Learn

Every release teaches something.

Evaluate:

- what worked,
- what failed,
- what can be improved,
- what should become part of the methodology.

Projects improve by learning from themselves.

---

# The Continuous Cycle

TraceForge projects are never truly "finished."

Every release creates new understanding.

That understanding influences future planning, architecture, documentation, and development.

The lifecycle therefore becomes:

Discovery

↓

Foundation

↓

Planning

↓

Architecture

↓

Development

↓

Review

↓

Refinement

↓

Documentation

↓

Release

↓

Learn

↓

Discovery

---

# Guiding Principles

Throughout every phase:

- Understanding comes before implementation.
- Architecture comes before features.
- Stable progress is preferred over rapid progress.
- Knowledge is treated as a project asset.
- Every document must earn its place.
- Every milestone should leave the repository healthier than before.

---

# Relationship to the Methodology

This document describes **how a TraceForge project progresses.**

Related methodology documents own specific parts of that workflow:

- Conversation Workflow governs request-to-delivery work.
- AI Collaboration Guide governs human and AI responsibilities.
- Context Compression governs durable knowledge selection.
- Session Continuity governs handoffs and resumption.
- Engineering Review Checklist governs delivery verification.

Together, these documents form the complete TraceForge methodology.
