### Autonomous run

For ChatGPT, first read the bundled resume-work skill. Use its native tools, scope, and persistence rules instead of Cursor-specific operations below.


**You own the exit condition. Define done, then drive to it without stopping.**

1. State the exit condition as a checkable predicate before the first iteration (tests green, repro fixed, all N PRs merged, pixel-diff zero).
2. For future continuation, use `resume-work` and create an automation only when the user explicitly requests future runs. Otherwise define the next check within this run. Use only exposed automation or subagent tools; do not imply background work is active when it is not. Inherit the parent model and effort unless the user configured supported overrides.
3. Each iteration makes the smallest change the evidence justifies, verifies it against the predicate, commits if it advanced, discards changes that didn't help. Belt-and-suspenders that "might help" gets reverted, not left to ride.
   Sequence the work via the **sequence-verifiable-units** principle skill, verifying each unit before the next instead of batching checks at the end.
4. Mid-run discoveries that support the goal are yours. Address broken skills, related bugs, flaky verifiers, review noise, tooling failures, orphaned follow-ups, and fixable drift yourself via poteto-mode. Put out-of-band fixes in their own PR. Do not park reversible work for the human. Ask only about a decision no available evidence or authorized default can settle. Surface only irreversible actions, genuine product or preference calls no experiment can settle, or a real dead end. Keep the predicate as the main drive, and return to it after each side fix.
5. Record each iteration in the task's authorized durable checkpoint, using the native **show-me-your-work** workflow when available. A local scratch note is not a durable checkpoint.
6. Stop when the predicate is met. A plateau is not a stop, so keep going and pivot your approach to push past it. Surface a genuine dead end rather than spinning, and never relax the predicate to declare victory.

**Reply:** the exit condition, iterations run, what landed, what was discarded, final predicate state.

