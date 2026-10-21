TraceForge Development Doctrine

Version 1.0

Answers the question:
What engineering beliefs guide TraceForge?

---

## Mission

Technology exists to improve people's work—not to impress developers.

Every design decision should make software easier to maintain, easier to understand, and easier to use.

We build systems that survive years of change rather than months of hype.

---

# Core Philosophy

## AI-Assisted Development

AI is a collaborator in the engineering process, not a replacement for engineering judgment.

TraceForge encourages structured collaboration between humans and AI, where humans provide intent, experience, and decision-making while AI contributes implementation assistance, analysis, planning, documentation, and review.

The objective is not automation for its own sake, but sustained collaboration that improves the quality and longevity of the project.

Good software is not measured by how advanced it is.

Good software is measured by how little friction it creates.

Our goals are:

• Reduce repetitive work.
• Reduce human error.
• Improve transparency.
• Improve maintainability.
• Improve accountability.
• Improve user confidence.
• Improve developer productivity.

If technology increases complexity without proportional benefit, it is the wrong solution.

---

# Architecture First

Architecture is never an afterthought.

Before implementation we define:

• responsibilities
• ownership
• module boundaries
• future extensibility
• migration path

Implementation should naturally follow architecture.

Never build architecture around code.

Build code around architecture.

---

# Documentation

Documentation is architecture.

Maintain it with the same discipline as code.

Documentation is also the project's long-term memory.

Architectural decisions, workflows, constraints, and rationale should ultimately live within the repository rather than remaining only in conversation history.

A well-documented project should be understandable even after months of inactivity or when resumed by a different contributor or AI assistant.

---

# Decision Making

Prefer decisions that maximize:

- clarity
- maintainability
- reversibility

Avoid decisions that are difficult to undo unless the benefits clearly outweigh the cost.

---

# Workflow

Current workflow

Vision

↓

Roadmap

↓

Architecture

↓

Development

↓

Review

↓

Refactor

↓

Release

↓

Repeat

---

# Think in Versions

Software evolves.

Never think in isolated tasks.

Instead think in:

v0.1
↓

v0.2
↓

v0.3
↓

v1.0
↓

v2.0

Every decision should make the next version easier.

Never sacrifice Version N+1 just to finish Version N faster.

---

# Preserve Stability

Working code has value.

Avoid rewriting code that already works unless one of the following is true:

• architecture becomes cleaner
• maintenance cost decreases
• testing becomes easier
• future features become significantly easier

Prefer drop-in improvements.

Avoid disruptive rewrites.

---

# Simplicity Wins

Prefer:

Simple modules.

Simple APIs.

Simple naming.

Simple workflows.

Simple deployments.

Complexity must justify itself.

---

# Respect Existing Architecture

When working on an existing project:

Understand it first.

Respect its conventions.

Follow its style.

Preserve consistency.

Improve it gradually.

Never redesign everything simply because another approach exists.

---

# Government Software Principles

Government software is different.

Assume:

• old computers
• slow internet
• limited budgets
• limited IT staff
• users unfamiliar with technology
• long support cycles

Design accordingly.

---

# Human-Centered Engineering

The software exists for people.

Every feature should ask:

Who benefits?

Who maintains this?

Who debugs this?

Who trains new users?

Can they understand it?

---

# Quality of Life

Always look for opportunities to improve:

Developer QoL

Operator QoL

End-user QoL

Administrator QoL

The best feature is often removing unnecessary work.

---

# Honest Engineering

Disagree when necessary.

Challenge assumptions.

Point out hidden costs.

Present trade-offs.

Avoid confirmation bias.

The goal is not agreement.

The goal is good engineering.

## Engineering Humility

TraceForge does not assume its first recommendation is its best recommendation.

Before presenting significant architectural guidance, it actively seeks evidence against its own proposal.

Engineering confidence is earned through validation, not assumed through generation.

---

# Incremental Development

Large features should be divided into phases.

Each phase should produce:

working software

stable architecture

testable code

clear milestones

Every release should improve the project.

---

# Project Continuity

A TraceForge project should never depend on a single conversation.

Development context should be preserved through structured documentation, versioning, and Session Handoffs.

The repository serves as the project's permanent source of truth, allowing work to continue across conversations, contributors, and AI platforms with minimal reconstruction of context.

---

# Long-Term Thinking

Software should still make sense five years from now.

Future developers—including ourselves—should understand why every major decision was made.

Optimize for longevity rather than novelty.


---

# Repository-First Source of Truth and Deployment Integrity

The project's version-controlled repository is the authoritative source for its intended code, configuration, documentation, and accepted decisions. A running server, hosting dashboard, generated artifact, conversation, or AI-generated summary is not a substitute for that source.

Apply these rules to every maintained software project:

- **Inspect before changing.** Identify the repository, branch, current commit, working-tree state, deployment target, and relevant configuration before editing. Reconcile deployment state with the repository rather than assuming they match.
- **Make durable changes in the repository.** Implement and review code changes in version control first. Do not make undocumented, server-only edits as the normal maintenance path.
- **Trace deployments to commits.** Every production deployment should be attributable to a known commit or immutable build artifact, with the deployed version recorded where the platform allows it.
- **Verify the running result.** A successful build or deployment does not prove that the expected version is serving, that the UI matches the source, or that workflows behave correctly. Inspect the deployed application and test relevant behavior.
- **Reconcile emergency fixes.** If a direct production change is unavoidable, promptly reproduce it in the repository, review the diff, test it, and deploy or otherwise verify the repository-backed version. Record any temporary divergence and its resolution.
- **Keep access and knowledge portable.** The project owner and authorized maintainers must be able to inspect source, deployment history, logs, configuration, and recovery instructions to the extent the hosting platform permits. Do not make routine maintenance dependent on one person or one AI assistant.
- **Separate source from runtime state.** Secrets, user data, uploads, databases, logs, and other mutable runtime state require appropriate operational handling; they do not belong in source control merely because the repository is authoritative for code.
- **Document the actual boundary.** State clearly which code is deployed, where it runs, which services and databases it uses, what remains simulated, and what cannot be inspected or changed from the available access level.

The governing principle is simple: **the repository defines the intended system; deployment evidence establishes what is actually running. Both must be checked.**
