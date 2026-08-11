# Engineering Review Checklist

**Answers the question:**

> **How must a change be verified before completion?**

Use only sections relevant to the change. Record evidence for every material concern and mark a material but non-applicable section with a reason.

## Intent and Authority

- [ ] The delivered outcome matches the request and stated scope.
- [ ] Destructive actions, external effects, releases, and scope expansion had explicit authority.
- [ ] Unrelated and user-owned changes were preserved.

## Architecture

- [ ] Responsibilities and ownership remain clear.
- [ ] Boundaries and dependency direction are preserved or explicitly changed.
- [ ] Existing solutions and simpler alternatives were considered where material.
- [ ] Accepted consequential architecture decisions have an ADR.

## Consistency

- [ ] Naming, conventions, and interfaces fit the existing project.
- [ ] No duplicate responsibility or contradictory documentation was introduced.

## Testing and Verification

- [ ] Relevant behavior received proportionate automated or manual verification.
- [ ] Material failure paths and regressions were considered.
- [ ] Passed, failed, and skipped checks are reported accurately.
- [ ] Partial or blocked work is not presented as complete.

## Documentation and Continuity

- [ ] Durable knowledge was updated in its canonical location.
- [ ] User, operator, or contributor impact is documented when needed.
- [ ] The canonical handoff reflects material current state at a meaningful stopping point.
- [ ] The handoff links to permanent records instead of duplicating them.

## Migration and Backward Compatibility

- [ ] Data, API, configuration, and workflow migration impact was assessed.
- [ ] Compatibility expectations and rollback conditions are explicit.

## Deployment and Monitoring

- [ ] Deployment, configuration, and operational impact were assessed.
- [ ] Monitoring, diagnostics, and recovery needs are addressed where applicable.

## Technical Debt

- [ ] Material debt reduced, introduced, accepted, or deferred is recorded.
- [ ] Roadmap placement, revisit conditions, and follow-up ownership are explicit.
