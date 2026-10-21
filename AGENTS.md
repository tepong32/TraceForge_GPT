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
- Before substantial work read AGENTS.md, CONTINUE.md (and its canonical handoff target), the relevant roadmap/architecture/feature documents, recent Git history/status and affected tests. Reconcile stale snapshots against source; do not ask the user to repeat documented context.
- At task completion update the canonical handoff for immediate state, actual validation, blockers and next steps; update the roadmap for agreed direction changes and specialized architecture/feature/audit/testing documents where applicable. Cross-link instead of duplicating them. Do not invent completed phases or new priorities.
- Test the changed area first: direct unit/feature tests, related integration tests and dependent regressions. Expand for shared models/services/utilities, auth/permissions, middleware, schema/migrations, settings/environments, shared UI, cross-app APIs, reporting, jobs or build/deployment changes. Uncertain impact requires broader validation.
- Full suites are appropriate for broad refactors, cross-module/security/infrastructure changes, major milestones and release/production gates, not automatically every isolated edit. Preserve stricter project-specific safety, reachability, hardware and release checks.
- Record relevant commands, scope rationale and outcomes in the handoff or appropriate validation report: PASS; FAIL - CAUSED BY CURRENT WORK; FAIL - PRE-EXISTING (with evidence); NOT RUN - OUT OF SCOPE (with rationale); NOT RUN - ENVIRONMENTAL (with limitation).
- Investigate failures before calling them unrelated. Fix regressions caused by the change and document evidence for pre-existing failures. A skipped test or unperformed human/operational acceptance is never a pass.
- Keep documentation, code and validation evidence sufficient for a fresh session to resume without a conversation transcript.
- Install additional standalone software/tooling under C:/xxx/_INSTALLS/_HERE/_xxx unless the user specifies otherwise.


## Repository-to-runtime integrity

- Treat the version-controlled repository as the source of truth for intended code, configuration, architecture, and accepted decisions. Treat the running deployment as separate evidence that must be checked against it.
- Before maintenance, inspect the current branch/commit, working-tree state, deployment target, and available deployment metadata. Never assume localhost, a preview, the default branch, and production are identical.
- Make normal changes in the repository, review the diff, run proportionate tests, and deploy a known commit or build artifact. Verify the actual deployed behavior after publishing.
- Do not leave undocumented server-only edits. If an emergency hotfix is necessary, back-port it into version control, validate it, and record any temporary divergence.
- Preserve owner/maintainer ability to inspect source and deployment evidence. Do not make maintenance dependent on one AI assistant; document platform access limits, recovery steps, and the actual boundary between code and runtime data.
- Keep secrets and mutable production data out of source control. Repository authority for code does not mean runtime data belongs in Git.
