# TraceForge Session Continuity

## Purpose

TraceForge recognizes that software projects outlive individual development sessions.

Conversations are temporary. Context windows are finite. AI models may change over time. Human developers may return after hours, days, or months away from a project.

Despite these interruptions, the project itself should continue as though development never stopped.

Session Continuity defines the methodology for preserving development momentum across independent conversations by reconnecting each new session to the project's permanent knowledge rather than its temporary conversational history.

Its objective is not to recreate previous discussions, but to restore sufficient understanding for meaningful development to continue naturally.

---

# Core Principle

A development session is temporary.

The project is permanent.

Development should resume from the project's accumulated knowledge rather than depend upon complete conversational history.

TraceForge therefore preserves progress instead of conversations.

---

# Development Sessions

Within TraceForge, a development session is a bounded period of focused engineering work.

A session exists to accomplish a specific objective while contributing to the long-term evolution of the project.

Every session should have:

- A clearly defined objective.
- A practical scope.
- Meaningful progress.
- A logical stopping point.

Sessions represent working periods, not project milestones.

Multiple sessions may contribute toward a single feature, while a single session may complete multiple small objectives.

---

# Session Boundaries

Development sessions should end intentionally rather than arbitrarily.

Natural stopping points include:

- completion of the current objective,
- completion of an architectural decision,
- completion of a meaningful implementation phase,
- sufficient progress for the current work period,
- approaching context limitations,
- or any point where development can safely pause without introducing unnecessary ambiguity.

Ending at a logical checkpoint improves the quality of future continuity.

---

# Preserving Continuity

When a session concludes, TraceForge preserves the state of the project rather than the state of the conversation.

Continuity should capture the information necessary to resume productive development without requiring previous discussions to be revisited.

This includes:

- current project identity,
- active release and development branch,
- completed milestones,
- accepted architectural decisions,
- established conventions,
- current objective,
- unresolved work,
- known constraints,
- and the next logical development step.

These represent project knowledge rather than conversational history.

---

# What Carries Forward

The following should persist across every development session:

- Project identity.
- Architecture.
- Repository structure.
- Development methodology.
- Coding standards.
- Version history.
- Accepted design decisions.
- Completed implementations.
- Known limitations.
- Current roadmap.
- Current development objective.
- Outstanding engineering work.

These collectively represent the project's permanent memory.

---

# What Does Not Carry Forward

Not every part of a conversation deserves permanence.

The following should generally remain within the completed session:

- exploratory reasoning,
- abandoned approaches,
- speculative discussions,
- repeated explanations,
- temporary brainstorming,
- conversational digressions,
- intermediate AI reasoning,
- redundant implementation attempts,
- and information that did not influence the project's final direction.

Temporary work should not become permanent project knowledge unless it produces lasting engineering value.

---

# Restoring Context

Every new development session should begin by reconnecting to the project's permanent state.

Context restoration should establish:

- where the project currently stands,
- what has already been completed,
- what constraints exist,
- what objective is currently active,
- and what work logically follows.

The objective is not to rediscover previous decisions, but to continue building upon them.

A restored session should feel like returning to an active workbench rather than beginning a new project.

---

# Session Resume

Once context has been restored, development should continue immediately from the next meaningful engineering task.

The new session should avoid repeating previous discovery, redesigning settled decisions, or re-evaluating accepted architecture unless new information justifies doing so.

Progress should remain cumulative throughout the lifetime of the project.

---

# Session Continuity Package

Each completed development session should produce a concise continuity package describing the current project state.

A continuity package should include:

- Current Release
- Development Branch
- Completed Work
- Current Objective
- Outstanding Tasks
- Known Constraints
- Recommended Starting Point
- Suggested Next Version (when appropriate)

This package serves as the bridge between independent development sessions while remaining significantly smaller than the complete conversational history.

---

# Relationship to Context Compression

Context Compression and Session Continuity serve complementary purposes.

Context Compression determines what knowledge deserves permanent preservation.

Session Continuity determines how future development reconnects with that preserved knowledge.

Compression preserves understanding.

Continuity restores momentum.

Together they enable projects to evolve across countless independent conversations without relying on complete conversational history.

---

# Guiding Principles

TraceForge Session Continuity is governed by the following principles:

- Projects outlive conversations.
- Conversations are temporary workspaces.
- The repository is the project's permanent memory.
- Progress should accumulate across sessions.
- Resume development rather than restart it.
- Preserve decisions instead of discussions.
- Restore understanding before implementation.
- Maintain momentum without depending on conversational history.

A development session should feel like leaving a workshop at the end of the day.

The next session should feel like returning to the same workshop, where the tools remain in place, the plans remain on the table, and development simply continues.