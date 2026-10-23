# Understand the code before changing it

Editing code you don't understand is how subtle regressions ship. Agents usually fail by misreading the goal or by missing the context needed to do the work well. [Prompting for a useful result](./02-poteto-mode.md) helps with the first. This page helps with the second.

![A detective studies a machine blueprint with a magnifying glass while robots fetch case files; the evidence board behind her links clues under /how and /why. Historical upstream illustration of skills from the broader pstack source package.](https://raw.githubusercontent.com/cursor/plugins/8b3326d99fd4b993cb33a24dad8af03175c642c5/pstack/docs/guide/images/understanding.jpg)

## Investigate before fixing

When the cause is unclear, ask for findings before a fix:

```text
Investigate why background jobs time out every few hours. Explain the runtime flow, show which files and data you used, and separate evidence from hypotheses. Don't change code yet.
```

For a concrete bug report, [`reproduce-fix`](../../skills/reproduce-fix/SKILL.md) requires an executable reproduction before treating a code hypothesis as a repro. For a question about a GitHub pull request, [`pr-review`](../../skills/pr-review/SKILL.md) fetches and reviews the current PR head rather than a possibly stale local copy.

## Trace how the code behaves

Ask for the path through the system, the important types, and the edge cases that are easy to miss:

```text
Trace how notifications are deduplicated. Include the relevant call path, data model, and any subscriber lookup that could create an N+1 query. Cite the code you inspected.
```

For a subsystem whose design has a history, ask why a decision was made and whether the original reason still holds. Source history and linked records can support an answer; if those sources are unavailable, the agent should say so and distinguish inference from direct evidence.

To learn a change rather than receive a summary, ask for an explanation that connects the design choice to the observed behavior:

```text
Explain how this PR changes retries. Show why the change addresses the cause rather than only the symptom, and identify what evidence would disprove that conclusion.
```

Explanations are useful checks on the agent's own choices too. Ask why it chose one boundary or data structure over another, and what it gave up.

## Rebuild your recent context with `recall`

When you return to a topic from earlier work, use [`recall`](../../skills/recall/SKILL.md) to reconstruct only the context needed for the current task. Name the topic or artifact and provide any new input after it:

```text
Recall the virtualized list work from yesterday, then read this bug report and tell me what changed.
```

The native skill starts with the current conversation and identified artifacts, then uses targeted personal context when available. It does not assume Cursor transcript paths or access to every prior chat.

**Pitfall:** don't start editing at the first plausible cause. A short trace of behavior and evidence often prevents a second bug.

Next: [Design the change](./04-design.md).
