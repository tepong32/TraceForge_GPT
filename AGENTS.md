# TraceForge - repository guide

## Project context and documentation map

Provider-neutral AI-assisted software-development methodology. manifesto/, methodology/, templates/, decisions/ and knowledge/ own distinct durable guidance; repository memory is authoritative over stale conversation snapshots.

### Durable boundaries

Preserve canonical ownership and cross-links instead of duplicating the methodology. Separate reusable evidence-earned guidance from project-specific anecdotes. Retain evidence-maturity labels and portable session handoffs.

### Development state

The repository's v0.6 Applied Knowledge release is complete; SESSION_HANDOFF.md describes evidence collection for the next increment. No new methodology release is implied by this documentation setup.

### Read next

- [README.md](README.md)
- [SESSION_HANDOFF.md](SESSION_HANDOFF.md)
- [methodology/README.md](methodology/README.md)
- [knowledge/README.md](knowledge/README.md)
- [You are TraceForge.md](You%20are%20TraceForge.md)
- [Continuation entry point](CONTINUE.md)

### Project validation

For methodology/document changes run the relevant link/ownership checks in `tests/test_repository_consistency.py`. For release-tool changes run `tests/test_version_manager.py` and isolated temporary-repository tests. Broaden at methodology/release milestones; do not release or push as a validation side effect.

## Repository continuity and proportional testing

- Maintain this root AGENTS.md in version control as portable operational context. Preserve applicable nested instructions. Update it in the same phase as durable architecture, security, integration, major completion/deferral or testing-policy changes.
- Keep this file concise: identity, boundaries, decisions and a documentation map. Replace stale summaries; never append transcripts, line-by-line diaries or duplicate full specifications.
- **Sync-check first before any repository mutation.** Inspect the latest remote target branch/commit, recent history, AGENTS.md, CONTINUE.md and its canonical handoff target, relevant decisions/docs, and working-tree status/diff wherever available. Preserve staged, unstaged, untracked, and user-owned changes. Re-check/fetch the remote before commit or push and reconcile divergence before proceeding.
- Local and cloud-side editors are separate working copies. A cloud view cannot prove that a local clone is clean or synchronized; mark local state as not observable when appropriate and never assume there are no uncommitted changes.
- Before substantial work read AGENTS.md, CONTINUE.md (and its canonical handoff target), the relevant roadmap/architecture/feature documents, recent Git history/status and affected tests. Reconcile stale snapshots against source; do not ask the user to repeat documented context.
- At the end of a meaningful work session/day, or before switching conversations, tools, environments, or AI collaborators, update the canonical handoff for immediate state, actual validation, sync status, blockers and next steps. Update the roadmap for agreed direction changes and specialized architecture/feature/audit/testing documents where applicable. Cross-link instead of duplicating them. Do not invent completed phases or new priorities.
- Test the changed area first: direct unit/feature tests, related integration tests and dependent regressions. Expand for shared models/services/utilities, auth/permissions, middleware, schema/migrations, settings/environments, shared UI, cross-app APIs, reporting, jobs or build/deployment changes. Uncertain impact requires broader validation.
- Full suites are appropriate for broad refactors, cross-module/security/infrastructure changes, major milestones and release/production gates, not automatically every isolated edit. Preserve stricter project-specific safety, reachability, hardware and release checks.
- Record relevant commands, scope rationale and outcomes in the handoff or appropriate validation report: PASS; FAIL - CAUSED BY CURRENT WORK; FAIL - PRE-EXISTING (with evidence); NOT RUN - OUT OF SCOPE (with rationale); NOT RUN - ENVIRONMENTAL (with limitation).
- Investigate failures before calling them unrelated. Fix regressions caused by the change and document evidence for pre-existing failures. A skipped test or unperformed human/operational acceptance is never a pass.
- Keep documentation, code and validation evidence sufficient for a fresh session to resume without a conversation transcript.
- Install additional standalone software/tooling under C:/xxx/_INSTALLS/_HERE/_xxx unless the user specifies otherwise.
