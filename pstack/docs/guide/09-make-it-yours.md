# Make the workflow fit your project

Start with plain requests. When the same instruction matters for future work in one repository, ask to save it as project guidance and use [`project-defaults`](../../skills/project-defaults/SKILL.md). The skill reads existing `AGENTS.md` files and other repository guidance, makes the smallest requested edit, and does not imply that a project file configures other chats or installs skills.

For example:

```text
Set repository guidance for this project: run the integration test suite after changing request routing, and include the actual command output in the handoff. Preserve all existing instructions.
```

## Request model-role choices only when you need them

The native default is for subagents to inherit the parent model and effort. If you explicitly want different roles, use [`configure-models`](../../skills/configure-models/SKILL.md). It checks the current subagent tool schema and only uses model identifiers and reasoning-effort values actually exposed by the host. A saved project preference cannot change the parent model for the whole ChatGPT session.

Delegation is also explicit and scoped. [`delegate-work`](../../skills/delegate-work/SKILL.md) does not fan out just because it was mentioned; it requires a bounded task and an explicit request or a workflow step that calls for a subagent.

## Turn repeated corrections into enforceable checks

When an agent repeats the same mistake, look for a durable fix in this order: improve the architecture, constrain it with types, add a lint or CI check, add a behavior test, then document the rule. A reminder is less reliable than a check that fails when the rule is broken. Preserve evidence from the past failure so the new check can demonstrate that it would catch it.

The Cursor source package also includes skills for reflecting on a session, writing custom skills, and evaluating skill changes. Those are not among this port's nine native workflows. If you need to create or modify a reusable ChatGPT skill, use the host's skill-creation workflow and keep its instructions separate from repository defaults.

## Write technical docs for the reader

For docs, RFCs, readmes, and PR descriptions, state who does what, define unfamiliar terms, and keep each sentence focused on one idea. Review against the actual audience and document type. If a prose-review skill is available in the host catalog, use it; otherwise ask directly for a pass that checks clarity, evidence, and unsupported claims.

Next: [Recipes and pitfalls](./10-recipes-and-pitfalls.md).
