# Design before you write code

One design attempt can lock in the first shape the model thought of. For a change with meaningful uncertainty, resolve the hard choices before implementation. Build a prototype when behavior or interaction is unclear; use a short design note to state ownership, types, and boundaries; then plan only what the evidence still leaves open.

![Three robots draft competing bridge models at their own tables under /architect, /arena, and /interrogate panels, while a judge robot with a clipboard inspects skeptically. Historical upstream illustration of broader pstack skills, not a native ChatGPT panel.](https://raw.githubusercontent.com/cursor/plugins/8b3326d99fd4b993cb33a24dad8af03175c642c5/pstack/docs/guide/images/design.jpg)

## Make alternatives concrete

When a choice is expensive to reverse, ask for two or three competing designs and compare them against the same constraints:

```text
Design the import pipeline. First trace the current flow and ownership boundaries. Give me two plausible designs with their types, module boundaries, failure behavior, and migration cost. Recommend one and name the evidence that would change your choice.
```

This is the useful idea behind the upstream `/architect` and `/arena` examples: ground the options in existing code, make their tradeoffs explicit, and compare alternatives before choosing. Those names belong to the broader source package; this ChatGPT port does not promise a multi-model panel. If you explicitly ask for delegation, [`delegate-work`](../../skills/delegate-work/SKILL.md) checks which native subagent tools are available and gives each worker a bounded scope.

## Prototype questions that need runtime evidence

Descriptions hide interaction problems. If the open question is how a user flow behaves, ask for a runnable prototype and evidence from the actual target environment when those tools are available:

```text
Prototype two settings layouts behind a simple switcher. Run them in the app and show screenshots of the same states for both options.
```

If the target cannot be run or controlled in the current session, the agent should report that limit instead of claiming a visual or behavior check passed. A prototype can answer layout and timing questions; it does not prove that the production architecture is correct.

## Review the built result

Plan after prototypes answer the important unknowns. Keep units small enough to verify, and review the code or behavior that actually exists. For a GitHub PR, [`pr-review`](../../skills/pr-review/SKILL.md) reviews the exact current PR head and reports only actionable defects. The native workflow does not claim independent-model consensus unless the required tools and distinct models are actually available.

For ordinary general-purpose engineering work, state the constraints and ask for the design or plan directly. Avoid listing upstream skill names as if ChatGPT commands or integrations were guaranteed.

Next: [Build and clean the change](./05-build-and-clean.md).
