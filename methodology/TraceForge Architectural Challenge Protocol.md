# TraceForge Architectural Challenge Protocol

**Answers the question:**

> **How must a significant recommendation attempt to invalidate itself?**

## Purpose

An implementation candidate is not evidence that implementation is warranted. Before a recommendation is accepted, TraceForge must test the smallest credible alternative that preserves the project better.

The protocol prevents implementation bias. It does not require artificial alternatives; it requires a recorded conclusion when an alternative is not viable.

## Challenge Sequence

Apply these challenges in order:

1. **Existing solution** — Can an established component, interface, process, or documented convention solve the problem without a new responsibility?
2. **Configuration** — Can a supported setting, policy, deployment change, or data change solve it without altering code or architecture?
3. **Deletion** — Can the problem disappear by removing obsolete behavior, a dependency, duplication, or an unnecessary requirement?
4. **Refactoring** — Can a bounded change to existing ownership solve it more clearly than adding a parallel path?
5. **Implementation** — If the prior challenges fail, is a new implementation the smallest coherent change?

At each stage, record the evidence for acceptance or rejection. Do not treat a preferred implementation as the baseline against which alternatives must compete.

## Final Challenge

Before the verdict, ask:

- Is this premature relative to the roadmap and evidence?
- Does it increase complexity, coupling, or operational burden more than it reduces them?
- Does it weaken incremental evolution or compatibility?
- What would make this recommendation wrong?

If the answer exposes an unresolved material risk, defer the recommendation or request the missing evidence.

## Output

Summarize the challenge in the `Self-Challenge` and `Alternatives` sections of the Recommendation Contract. The conclusion may be to retain the current design.
