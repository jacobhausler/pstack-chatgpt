# Prompt for a useful result

The original pstack guide used `/poteto-mode` as a dispatcher. That Cursor command is not part of the native ChatGPT workflow set. In ChatGPT, state the task directly; use a native pstack workflow by name when one applies. The same prompting habits still help an agent choose a sound path and show its evidence.

![A dispatcher pulls a switch lever to route robots on rail handcars toward lit gates, under a /poteto-mode departure board listing BUG FIX, FEATURE, and INVESTIGATION. Historical upstream illustration; the Cursor-style board is not a ChatGPT control.](https://raw.githubusercontent.com/cursor/plugins/8b3326d99fd4b993cb33a24dad8af03175c642c5/pstack/docs/guide/images/router.jpg)

## What a useful prompt carries

A prompt often needs only a few things, each in a sentence:

- **The goal.** Say what's wrong or what you want.
- **The done check.** Name a result that can pass or fail.
- **The proof.** Ask for command output, a behavior check, a stored value, a video, or a before-and-after measurement.
- **What you know.** Include a symptom, repro step, log line, issue, or relevant path.
- **The constraints.** Say “reproduce first,” “don't change code yet,” “zero behavior change,” or “let me review before proceeding” when those change the work.

For example:

```text
The CSV export drops its last row after yesterday's deploy. The failing job is 4812. Reproduce it first, then fix it. Done means the 60k-row fixture exports every row; show the row counts before and after.
```

For a concrete reported bug with an identified source and authorized repository, ask ChatGPT to use [`reproduce-fix`](../../skills/reproduce-fix/SKILL.md). “Reproduce first” keeps a static code hypothesis separate from a demonstrated failure.

## Let the evidence shape the work

Don't write a long sequence of skill names unless you are deliberately overriding the workflow. State the result and the conditions that matter. A written theory of the cause can also narrow the search too early. For noisy reports, ask for a plain-language restatement before edits:

```text
Read this report and restate the underlying issue in plain English. Separate what the report proves from what you infer. Don't change code yet.
```

When you want an investigation rather than a fix, say so explicitly. For example, ask what the code does, which evidence it used, and which parts are still hypotheses. For a broader engineering task, ask the agent to propose a design or a short plan before implementation if the decision is costly to reverse.

## Follow up briefly

Once the conversation has the goal and constraints, a follow-up can be short: “continue,” “show the failing case,” or “keep going until the stated check passes.” Keep the finish condition visible. If the topic changes, say “new task” and state the new goal so old assumptions do not carry over.

For recurring work across bounded runs, use [`resume-work`](../../skills/resume-work/SKILL.md) and identify a durable checkpoint location. A normal follow-up is not a background loop, and no work continues after the run unless a supported automation was explicitly requested and confirmed.

## Keep parallel work separate

Delegation has cost and should have a bounded purpose. Use [`delegate-work`](../../skills/delegate-work/SKILL.md) when you explicitly request delegation or the active workflow requires a subagent. Give each worker an independent task, a scope, and a check. Keep shared files, branches, and external actions with one owner. The skill uses only native subagent tools exposed in the current session; it does not promise cloud machines or isolated environments.

Next: [Understand the code](./03-understand.md).
