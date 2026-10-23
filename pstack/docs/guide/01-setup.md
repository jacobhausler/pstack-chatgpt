# Set up pstack in ChatGPT

pstack's native ChatGPT port is a set of focused workflows, not a plugin installer or a model configuration wizard. Start with [`setup-pstack`](../../skills/setup-pstack/SKILL.md): it checks which repository, execution, subagent, automation, context, and app tools are actually available, then points you to the workflow that fits your task.

The native package centers on nine workflows:

| Goal | Workflow |
| --- | --- |
| Review a GitHub pull request | [`pr-review`](../../skills/pr-review/SKILL.md) |
| Continue authorized work across bounded runs | [`resume-work`](../../skills/resume-work/SKILL.md) |
| Triage one issue report or configure requested intake | [`triage-reports`](../../skills/triage-reports/SKILL.md) |
| Reproduce a reported bug and make a bounded fix | [`reproduce-fix`](../../skills/reproduce-fix/SKILL.md) |
| Delegate a bounded task when the active workflow calls for it | [`delegate-work`](../../skills/delegate-work/SKILL.md) |
| Set requested subagent model roles | [`configure-models`](../../skills/configure-models/SKILL.md) |
| Set requested repository guidance | [`project-defaults`](../../skills/project-defaults/SKILL.md) |
| Perform an explicitly requested GitHub action | [`github-workflow`](../../skills/github-workflow/SKILL.md) |
| Rebuild recent context on a topic | [`recall`](../../skills/recall/SKILL.md) |

Ask ChatGPT to use the relevant workflow by name. The host discovers the installed skill and reads its native instructions; there is no Cursor slash-command setup, Custom Mode, model-role file, or plugin installation step in this guide. The native workflows inherit the parent model by default and use only tools and model choices exposed in the current session.

## Choose the workflow that fits

For a general code change, describe the goal, constraints, and a checkable finish condition in your own words. For an evidenced bug report, use `reproduce-fix`; for a GitHub PR review, use `pr-review`; for a request to continue work over multiple bounded runs, use `resume-work`. Use `configure-models` or `project-defaults` only when you explicitly want those settings changed.

Here is a small first task:

```text
Add a --json flag to this command. Keep the current text output byte-identical. Run the real command in both modes and show the output comparison.
```

For work that may continue later, `resume-work` requires a durable checkpoint location and a clear stop condition. A checkpoint records progress; it does not keep a process running after the current run. Future or recurring work requires an explicitly requested, supported automation, and the workflow confirms what was actually created.

## Keep effort proportionate

Subagents and review passes use additional context and compute. The native defaults inherit the parent model. Ask for delegation only where the active workflow calls for it or you explicitly want a bounded task delegated. Keep the task small when the change is small, and give parallel workers separate scopes.

Next: [Prompt for a useful result](./02-poteto-mode.md).
