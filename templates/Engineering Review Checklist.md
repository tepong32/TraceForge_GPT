# Engineering Review Checklist

Use the sections relevant to the change. Record evidence for every material concern; mark non-applicable sections with a reason.

## Architecture

- [ ] Responsibilities and ownership remain clear.
- [ ] Boundaries and dependency direction are preserved or explicitly changed.
- [ ] Existing solutions and simpler alternatives were considered.
- [ ] Material architecture decisions have an ADR.

## Consistency

- [ ] Naming, conventions, and interfaces fit the existing project.
- [ ] No duplicate responsibility or contradictory documentation was introduced.

## Testing

- [ ] Relevant behavior has proportionate automated or manual verification.
- [ ] Failure paths and regressions were considered.

## Documentation

- [ ] Permanent knowledge was updated in its canonical location.
- [ ] User, operator, or contributor impact is documented when needed.

## Migration and Backward Compatibility

- [ ] Data, API, configuration, and workflow migration impact was assessed.
- [ ] Compatibility expectations and rollback conditions are explicit.

## Deployment and Monitoring

- [ ] Deployment, configuration, and operational impact were assessed.
- [ ] Monitoring, diagnostics, and recovery needs are addressed where applicable.

## Technical Debt

- [ ] Debt reduced, introduced, accepted, or deferred is recorded when material.
- [ ] Roadmap placement and follow-up ownership are explicit.
