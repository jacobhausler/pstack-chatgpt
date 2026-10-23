# Continue work safely

The durable version of “keep going” is a bounded run with a clear finish condition and a checkpoint that another run can read. A checkpoint records progress; it is not a background process and does not make work continue after the current run ends.

![She waves goodnight from the door while robots keep the factory running, one updating a DECISION LOG wall board under a BUILD LOOP ACTIVE sign. Historical upstream illustration of Cursor's autonomous-run experience.](https://raw.githubusercontent.com/cursor/plugins/8b3326d99fd4b993cb33a24dad8af03175c642c5/pstack/docs/guide/images/overnight.jpg)

## Establish trust before handing work off

Before relying on an agent to continue later, make sure the goal and check are clear, the needed test or runtime tools are available, and each stage can stop when evidence misses the bar. Review a few completed runs and turn repeated mistakes into project checks or documentation. Keep consequential actions such as merging, deploying, or sending external messages within the authorization you actually gave.

## Leave a useful checkpoint

Use [`resume-work`](../../skills/resume-work/SKILL.md) when you ask to resume an authorized task across bounded runs. It needs a durable checkpoint location, and it refreshes repository and connected-service state before acting. Scratch files and an uncommitted chat note do not count as durable checkpoints.

For example:

```text
Continue the parser migration in the approved repository. Done means every caller uses the new parser, the fixture suite passes, and the old API is removed. Before this run ends, write a durable checkpoint with the current branch and commit, what passed, unresolved decisions, and the next bounded step. Do not merge or deploy.
```

A useful checkpoint records the goal, scope, authorized actions, stop condition, current branch and commit, evidence, decisions, and next action. At the next run, refresh that state against the repository instead of assuming it is unchanged.

## Request future or recurring work explicitly

If you want the system to wake on a schedule or event, say so directly and name the repository, trigger, and desired action. The native workflow must inspect actual automation and connector support before creating anything, then confirm the saved configuration separately from whether the workflow has run successfully. If the platform cannot support the requested trigger, it should say so rather than simulate one.

The earlier guide described Cursor `/loop`, Cursor Projects, cloud agents, a Benny Slack automation pack, and overnight PR autopilots. Those are historical upstream capabilities and instructions, not ChatGPT subscriptions or available tools. For Slack report intake, use [`triage-reports`](../../skills/triage-reports/SKILL.md) only for an explicitly requested one-off triage or recurring setup. For an evidenced report that needs a code fix, use [`reproduce-fix`](../../skills/reproduce-fix/SKILL.md) after resolving the repository and test scope.

Next: [Steer with principles](./08-principles.md).
