# Recipes and pitfalls

Prompts worth copying, then common mistakes to avoid. The examples use ordinary ChatGPT requests and the nine native pstack workflows.

![She tastes a finished dish while robots cook from a recipe box, with pinned cards reading /how, /tdd, and /loop above the counter. Historical upstream illustration of broader pstack skills and Cursor commands.](https://raw.githubusercontent.com/cursor/plugins/8b3326d99fd4b993cb33a24dad8af03175c642c5/pstack/docs/guide/images/recipes.jpg)

## Understand an unfamiliar subsystem

```text
Trace how initialization works, including the call path, key types, and any non-obvious behavior. Then explain what evidence could show why it changed recently. Cite the files you inspected.
```

## Restate a noisy report before touching code

```text
Read this report and restate the underlying issue in plain English. Separate reported facts from hypotheses. Don't change code yet.
```

For an evidenced bug report, use [`reproduce-fix`](../../skills/reproduce-fix/SKILL.md) after confirming the issue source, repository, and test environment.

## Fix a bug with proof

```text
The import skips the final record when a retry overlaps the upload. Reproduce it with this fixture first. If it fails, make a minimal fix and rerun the same check. Show the input, expected result, and actual result before and after.
```

Keep “reproduced” separate from “static hypothesis.” If no executable test path is available, ask for a diagnosis and state the limitation.

## Review a pull request

```text
Use pr-review to review owner/repo PR 123 against its current head. Report only actionable defects introduced by this change, with severity, file and line, failure mode, and evidence.
```

The native [`pr-review`](../../skills/pr-review/SKILL.md) workflow reads the current GitHub PR and never merges it.

## Continue work in a later run

```text
Use resume-work to continue the migration in the approved repository. Done means all callers use the new API and the migration tests pass. Before this run ends, record a durable checkpoint with current branch and commit, evidence, unresolved decisions, and the next step. Do not merge.
```

[`resume-work`](../../skills/resume-work/SKILL.md) requires a durable checkpoint and refreshes actual repository state. A checkpoint does not schedule future work.

## Configure repository guidance

```text
Use project-defaults to add this rule to the repository guidance: changes to the billing schema must run the migration test and include its result. Preserve other guidance.
```

Use [`project-defaults`](../../skills/project-defaults/SKILL.md) only for an explicitly requested repository change. For model role choices, use [`configure-models`](../../skills/configure-models/SKILL.md); its defaults inherit the parent model.

## Ask for an explicitly scoped parallel task

```text
Use delegate-work to have one worker inspect the parser tests for missing boundary cases. Read-only; return file references and suggested cases. Do not edit files.
```

[`delegate-work`](../../skills/delegate-work/SKILL.md) uses available native subagent tools and keeps the task bounded. Independent same-model passes are not a diverse-model consensus.

## Triage an issue report

```text
Use triage-reports to classify this report and identify the expected and actual behavior. Do not contact anyone or create a tracker issue.
```

For recurring Slack intake, say explicitly that you want to configure an event-driven workflow and identify its scope. [`triage-reports`](../../skills/triage-reports/SKILL.md) inspects available connections before setup and will not pretend an unsupported trigger exists.

## Perform a GitHub action

```text
Use github-workflow to open a draft pull request for the current branch in owner/repo. Include these test results in the description.
```

Name the exact repository and action. Read access alone does not authorize creating or merging a PR.

## Pitfalls to avoid

- **A vague finish condition.** “Make it better” gives the agent nothing to check. Name a command, artifact, or behavior that can pass or fail.
- **Leading with a theory.** Ask for a restatement or reproduction before telling the agent where you think the bug is.
- **Reporting success off a green build.** Ask for the real command, flow, stored value, or profile and the evidence it produced.
- **Parallel work in shared state.** Give each worker an independent scope and check; avoid shared files, branches, and external actions.
- **Treating a checkpoint as a background job.** `resume-work` records durable progress. A future wake requires an explicitly requested automation that the platform supports and confirms.
- **Assuming integrations or controls exist.** Follow [`the native ChatGPT harness`](../harness/chatgpt.md); available tools and connected accounts must be discovered in the current session.
- **Assuming model diversity.** Independent passes on the inherited model do not establish independent-model consensus.
- **Assuming project instructions configure every chat.** `project-defaults` changes repository guidance only.
- **Enumerating upstream skills as commands.** Names such as `/how`, `/architect`, `/loop`, and `/correct` come from the broader Cursor source package. They are not native ChatGPT commands unless the host independently exposes the corresponding skill.

Back to the [guide index](./README.md).
