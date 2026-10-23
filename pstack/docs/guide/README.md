# The pstack guide

This guide explains how to work well with an agent using pstack's native ChatGPT workflows. State the result you want, the constraints that matter, and how to check the result. Use a native workflow by name when one fits; the host skill catalog discovers and applies its instructions.

The guide grew out of pstack's Cursor documentation. Its linked illustrations and a few quoted examples are historical upstream material; they show ideas, not ChatGPT controls or available integrations. For the current native workflow map and capability limits, see [the ChatGPT harness](../harness/chatgpt.md).

1. [Set up pstack](./01-setup.md). Discover native workflows and available tools.
2. [Prompt for a useful result](./02-poteto-mode.md). State the goal, proof, context, and constraints.
3. [Understand the code](./03-understand.md). Build a traced model before changing an unfamiliar system.
4. [Design the change](./04-design.md). Resolve important design questions with evidence before implementation.
5. [Build and clean the change](./05-build-and-clean.md). Reproduce first, test behavior, and keep the diff reviewable.
6. [Verify and ship](./06-verify-and-ship.md). Prove the real behavior and use native GitHub workflows only when requested.
7. [Continue work safely](./07-overnight.md). Use durable checkpoints for bounded follow-up runs.
8. [Steer with principles](./08-principles.md). Use pstack's principles as concise reminders for engineering decisions.
9. [Make it yours](./09-make-it-yours.md). Configure requested repository defaults without assuming they change other chats.
10. [Recipes and pitfalls](./10-recipes-and-pitfalls.md). Copy portable prompts and avoid common failure modes.

Read the pages in order the first time. After that, each page stands alone.

## If you only remember one thing

Give the agent a goal and a way to check it, in your own words:

```text
The export writes duplicate rows when a retry lands mid-run. Reproduce it first, then fix and verify. Show the row counts before and after.
```

For a reported bug with an issue or source and an authorized repository, use [`reproduce-fix`](../../skills/reproduce-fix/SKILL.md). For a general engineering request, state the task directly and ask for evidence appropriate to the change.

Next: [Set up pstack](./01-setup.md).
