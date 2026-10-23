# Verify the result and use GitHub workflows

“It compiles” is not evidence that behavior is right. Name a check that exercises the real artifact and ask for the output or captured result. If the target cannot be run in the current session, report the verification limit instead of claiming a pass.

![A prototype plane flies a real test course while she times it with a stopwatch and robots film and checklist the run; the terminal reads verify: pass, evidence: captured. Historical upstream illustration.](https://raw.githubusercontent.com/cursor/plugins/8b3326d99fd4b993cb33a24dad8af03175c642c5/pstack/docs/guide/images/verification.jpg)

## State the finish condition

Make “done” observable. Examples:

- A CLI change runs the real command with representative input.
- A UI change checks the actual user flow and captures the relevant state.
- A refactor compares behavior before and after.
- A performance claim includes repeated measurements, the range, and conditions that could affect the number.

For a small diff whose consequences are unclear, ask the agent to identify the most important fact that makes it safe and to prove that fact by running code where possible. For measured claims, name the fixture, baseline, and environment so the comparison can be evaluated.

## Verify complex app behavior

If you maintain a project-specific verification harness, keep its launch, drive, evidence, and cleanup steps documented in the repository and run it against the actual app. Check that captured evidence survives cleanup. Keep that harness in the repo so later runs use the same method. A green build alone does not replace a behavior check.

For concurrency, retries, state machines, parsers, or other cases tests rarely reach, state one important property and ask what formal or generated-input checks can establish it. Report the tool and bounds used. A pass proves the stated model or scope; it does not prove the whole system.

## Review or act on a pull request

Use [`pr-review`](../../skills/pr-review/SKILL.md) when you want an evidence-based review of a GitHub pull request. It reads the current PR head and reports actionable defects; it never merges the PR.

Use [`github-workflow`](../../skills/github-workflow/SKILL.md) for an explicitly requested GitHub action such as reading a ref, creating or updating a PR, or merging. The workflow verifies the exact repository and access first. A request to inspect a diff or draft PR text does not itself authorize publishing or merging. State the action and target clearly.

The Cursor-origin examples in the previous version described automatic rebases, Bugbot, PR queues, and shipping playbooks. They are historical upstream workflows, not native ChatGPT capabilities. For recurring review or event-driven work, ask explicitly for setup; the relevant workflow checks actual connected tools and confirms saved state separately from runtime behavior.

Next: [Continue work safely](./07-overnight.md).
