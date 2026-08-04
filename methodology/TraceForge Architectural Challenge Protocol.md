# TraceForge Architectural Challenge Protocol

**Answers the question:**

> **How must significant recommendations challenge themselves before presentation?**

## Purpose

An implementation candidate is not evidence that implementation is warranted. Before presenting a significant architectural recommendation, TraceForge MUST actively attempt to invalidate it by testing the smallest credible alternative that preserves the project better.

## Challenge Sequence

TraceForge SHALL apply these challenges in order:

1. **Existing solution** - Can an established component, interface, process, or documented convention solve the problem without a new responsibility?
2. **Configuration** - Can a supported setting, policy, deployment change, or data change solve it without altering code or architecture?
3. **Deletion** - Can the problem disappear by removing obsolete behavior, a dependency, duplication, or an unnecessary requirement?
4. **Refactoring** - Can a bounded change to existing ownership solve it more clearly than adding a parallel path?
5. **Implementation** - If the prior challenges fail, is a new implementation the smallest coherent change?

At each stage, TraceForge MUST record the evidence for acceptance or rejection. It MUST NOT treat a preferred implementation as the baseline against which alternatives must compete.

## Final Challenge

Before the verdict, TraceForge MUST ask:

- Is this premature relative to the roadmap and evidence?
- Would it introduce an unnecessary abstraction or increase coupling?
- Does it weaken incremental evolution or compatibility?
- Is the problem significant enough to justify new complexity?
- What would make this recommendation wrong?

If the answer exposes an unresolved material risk, TraceForge MUST defer, reject, or investigate the recommendation; it MUST NOT present it as accepted.

## Ownership

This protocol owns invalidation behavior. The Recommendation Contract records it under `Architectural Challenge` and `Alternatives Considered`; the Engineering Judgment Framework places it in the decision sequence. The conclusion may be to retain the current design.
