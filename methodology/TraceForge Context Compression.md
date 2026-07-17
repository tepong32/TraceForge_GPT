# TraceForge Context Compression

**Answers the question:**

> **How should project knowledge be compressed and preserved?**

---

# Purpose

TraceForge recognizes that software development produces far more information than should become permanent project knowledge.

Conversations contain questions, experiments, debugging, alternative ideas, and temporary reasoning. While valuable during development, not all of this information deserves to become part of the project's long-term understanding.

Context Compression is the process of preserving meaningful engineering knowledge while allowing temporary conversation to be discarded.

The objective is not to reduce information.

The objective is to preserve understanding.

---

# Philosophy

Project knowledge should grow continuously, even as individual conversations end.

Every completed milestone should leave the project easier to understand, maintain, and continue than before.

Context should become smaller.

Understanding should become larger.

---

# The Three Layers of Knowledge

TraceForge organizes knowledge into three distinct layers.

## Temporary Knowledge

Temporary knowledge exists only to solve the current problem.

Examples include:

- debugging sessions,
- exploratory discussions,
- rejected ideas,
- implementation experiments,
- conversational reasoning.

Temporary knowledge serves development but does not become part of the project's permanent memory.

It may be discarded once its purpose has been fulfilled.

---

## Session Knowledge

Session knowledge captures meaningful progress made during a development session.

Examples include:

- completed work,
- architectural decisions,
- roadmap progress,
- pending objectives,
- important discoveries.

Session knowledge prepares the next development session without requiring the entire conversation to be retained.

---

## Project Knowledge

Project knowledge represents the long-term understanding of the project.

Examples include:

- architecture,
- methodology,
- documented conventions,
- established workflows,
- accepted design decisions,
- permanent project documentation.

Project knowledge belongs in the repository.

It should survive individual conversations, development environments, and AI implementations.

---

# What Should Be Preserved

Context Compression should preserve information that improves future development.

Examples include:

- architectural decisions,
- completed milestones,
- accepted conventions,
- project structure,
- design rationale,
- lessons learned,
- important trade-offs,
- roadmap evolution.

If losing the information would make the project harder to continue in the future, it should be preserved.

---

# What Should Be Discarded

Not every conversation contributes to the project's permanent understanding.

Examples of information that generally should not be preserved include:

- greetings,
- conversational filler,
- repeated explanations,
- temporary debugging,
- implementation dead ends,
- superseded approaches,
- obsolete plans,
- transient reasoning.

The repository should preserve conclusions rather than conversations.

---

# When Compression Should Occur

Context Compression should occur after meaningful progress has been achieved.

Typical opportunities include:

- completing a milestone,
- finalizing an architectural decision,
- finishing a feature,
- concluding a refactor,
- ending a development session.

Compression is a deliberate engineering activity rather than a continuous process.

---

# Compression Principles

## Preserve Meaning, Not Conversation

The objective is to retain what was learned rather than everything that was said.

Engineering knowledge is more valuable than conversational history.

---

## Distill Rather Than Summarize

Compression should identify the essential understanding produced by development.

The result should communicate decisions, reasoning, and outcomes rather than replaying discussion.

---

## Preserve Decisions

Future developers benefit more from understanding why decisions were made than from reading every conversation that led to them.

Where appropriate, important rationale should accompany major architectural decisions.

---

## Eliminate Redundancy

Information that already exists within permanent documentation should not be repeated elsewhere.

Each piece of project knowledge should have a clear, authoritative location.

---

## Favor Long-Term Value

Knowledge should be preserved according to its future usefulness rather than its immediate importance during development.

Temporary complexity often produces permanent simplicity.

---

# Repository as Permanent Memory

The repository serves as TraceForge's permanent memory.

Documentation should contain the project's accumulated understanding rather than its conversational history.

A project should remain understandable even if every previous conversation disappears.

---

# Relationship to the Methodology

This document defines **how project knowledge is preserved over time.**

Other methodology documents describe:

- why the project exists,
- how projects progress,
- how development conversations progress,
- how humans and AI collaborate,
- how sessions transition between conversations.

Together, they ensure that knowledge accumulates continuously throughout the lifetime of a TraceForge project.