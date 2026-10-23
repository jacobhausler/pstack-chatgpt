# Steer with principle names

pstack's broader source package includes 24 principles as individual skills. In this native ChatGPT port, they are useful engineering heuristics, not rules automatically loaded into every conversation. State the principle in plain words when you want to steer a decision; ask for the concrete choice it changed and the evidence behind it.

You can use a principle name as shorthand, then explain the outcome you expect. If the corresponding skill is available in the host catalog, it can provide the full rule; otherwise the name is only a reminder in your prompt.

## Steering in practice

Say the agent is about to bolt a new adapter onto three existing ones:

```text
use subtract before you add. delete the obsolete adapters first, then design what's left.
```

Say it claims success because the build passed:

```text
apply prove it works. run the real import flow and show me the written records.
```

For two independent workers, avoid shared mutable state:

```text
separate before serializing shared state. give each attempt its own worktree, no locks.
```

The phrase is useful when it changes a real decision. Ask the agent to say which choice changed and why; naming a principle without applying it adds no evidence.

## The 24, briefly

The core principles decide how much to build and when to rethink the design:

- [Laziness Protocol](../../skills/principle-laziness-protocol/SKILL.md) prefers deletion and the smallest change that solves the problem.
- [Foundational Thinking](../../skills/principle-foundational-thinking/SKILL.md) chooses the core data structures before writing logic.
- [Redesign from First Principles](../../skills/principle-redesign-from-first-principles/SKILL.md) integrates a new requirement as if it had been there from day one.
- [Attack the Premise](../../skills/principle-attack-the-premise/SKILL.md) writes down the premise that two or more failed fixes shared and tests it directly before the next fix.
- [Subtract Before You Add](../../skills/principle-subtract-before-you-add/SKILL.md) removes dead weight before building on top of it.
- [Minimize Reader Load](../../skills/principle-minimize-reader-load/SKILL.md) collapses layers and hidden state a reader must hold in their head.
- [Outcome-Oriented Execution](../../skills/principle-outcome-oriented-execution/SKILL.md) converges rewrites on the target design instead of preserving throwaway compatibility states.
- [Experience First](../../skills/principle-experience-first/SKILL.md) chooses the user's result over implementation convenience.
- [Exhaust the Design Space](../../skills/principle-exhaust-the-design-space/SKILL.md) builds two or three competing prototypes when there's no precedent.
- [Build the Lever](../../skills/principle-build-the-lever/SKILL.md) builds the script that does or proves the work, so a reviewer can rerun it. When an agent keeps doing the same thing by hand, have it write the tool or skill it wishes it had. If a script can do a step the same way every time, use the script, and save agents for the judgment calls.

The architecture principles decide where state, validation, and compatibility live:

- [Model the Domain](../../skills/principle-model-the-domain/SKILL.md) encodes repeated rules in one structure, not scattered conditionals.
- [Boundary Discipline](../../skills/principle-boundary-discipline/SKILL.md) validates at the boundary and trusts internal types.
- [Type System Discipline](../../skills/principle-type-system-discipline/SKILL.md) makes illegal states unrepresentable.
- [Make Operations Idempotent](../../skills/principle-make-operations-idempotent/SKILL.md) converges retries on the same end state.
- [Migrate Callers Then Delete Legacy APIs](../../skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) migrates and deletes in one wave.
- [Separate Before Serializing Shared State](../../skills/principle-separate-before-serializing-shared-state/SKILL.md) removes the sharing before adding coordination.

The verification principles define what counts as proof:

- [Prove It Works](../../skills/principle-prove-it-works/SKILL.md) verifies the real artifact, not a proxy.
- [Fix Root Causes](../../skills/principle-fix-root-causes/SKILL.md) reproduces and traces to the cause before changing code.
- [Sequence Work into Verifiable Units](../../skills/principle-sequence-verifiable-units/SKILL.md) ends each small unit in a check before starting the next.
- [Test Behavior, Not Implementation](../../skills/principle-test-behavior-not-implementation/SKILL.md) asserts what the code's users can observe, so a test fails when that behavior breaks and survives a change to the internals.
- [Explain the Number](../../skills/principle-explain-the-number/SKILL.md) names what limits a measured number and rules out that it measured something else, before anyone trusts or reports it. [`/benchmark-checklist`](../../skills/benchmark-checklist/SKILL.md) turns it into seven questions you answer from real runs.

The delegation principles keep parallel work sane:

- [Guard the Context Window](../../skills/principle-guard-the-context-window/SKILL.md) routes bulk reading to subagents and keeps findings in the main chat.
- [Never Block on the Human](../../skills/principle-never-block-on-the-human/SKILL.md) proceeds on reversible work and presents the result.

And one meta principle:

- [Encode Lessons in Structure](../../skills/principle-encode-lessons-in-structure/SKILL.md) turns advice you've repeated twice into a lint, check, or script. For a repeat mistake, see [Make it yours](./09-make-it-yours.md#turn-repeated-corrections-into-enforceable-checks).

Don't memorize the list. Use it as a set of prompts when you catch a recurring failure. The native [`project-defaults`](../../skills/project-defaults/SKILL.md) workflow can save repository guidance when you explicitly ask for persistent project defaults; it does not make those instructions apply to other chats.

Next: [Make it yours](./09-make-it-yours.md).

