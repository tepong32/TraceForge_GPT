# TraceForge Context Compression

**Answers the question:**

> **How should temporary work become durable project knowledge without preserving the whole conversation?**

## Purpose

Development produces more information than should become permanent project memory. Context Compression preserves conclusions, decisions, and current state while allowing conversational exploration to expire.

The objective is not to preserve more information. It is to make future work require less reconstruction.

## Knowledge Layers

### Temporary Conversation Knowledge

Questions, experiments, debugging paths, repeated explanations, speculative alternatives, and conversational reasoning exist to support current work. Discard them when they no longer affect a decision, risk, or next action.

### Current Working State

The active objective, completed and partial work, blockers, validation, assumptions, and next action belong in the canonical handoff. This state is replaceable and should remain small enough to resume quickly.

### Durable Project Knowledge

Architecture, accepted decisions, established conventions, material debt, released outcomes, and enduring constraints belong in canonical repository documentation. Demonstrated lessons that apply across projects may be promoted to [Applied Knowledge](../knowledge/README.md). They survive handoff replacement and conversation loss.

## Compression Process

At a meaningful stopping point:

1. Identify what changed in the project or its understanding.
2. Discard conversational material that does not affect future work.
3. Move durable conclusions to their canonical owner.
4. Separate project-specific rules from reusable engineering practice before promoting a lesson.
5. Update the handoff with only current resumable state.
6. Link the handoff to permanent records rather than copying them.
7. Remove resolved handoff content once its durable consequences are preserved.

## Preserve

Preserve information when losing it would cause unsafe continuation, repeated investigation, or loss of architectural intent. This includes:

- accepted decisions and material tradeoffs;
- rejected approaches whose reason prevents repeated work;
- incomplete implementation state and user-owned changes;
- known failures, risks, and compatibility constraints;
- validation results and unverified assumptions;
- roadmap or milestone consequences;
- the exact next starting point.

## Discard

Do not preserve greetings, filler, full transcripts, hidden reasoning, large raw logs, superseded plans, repeated documentation, or unsuccessful experiments that no longer influence the project.

## Staleness

Compression does not make a snapshot timeless. A handoff must retain enough source identity to be compared with the repository. When the branch, revision, release, or material working state differs, reconcile the snapshot before relying on it.

## Ownership

This document owns the boundary between temporary, current, and durable knowledge. Session Continuity owns the handoff schema and resume protocol. Canonical project documents own project truth. The Applied Knowledge index owns admission and categorization of reusable cross-project lessons.
