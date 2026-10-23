# Build the change and clean the diff

State what you observed and what must remain true. Ask for proof that fits the behavior. For a reported bug, use [`reproduce-fix`](../../skills/reproduce-fix/SKILL.md) when the issue source, repository, and test environment are identified and authorized.

```text
This command emits two records after a retry. Reproduce the failure first, then make the smallest fix and rerun the same check.
```

For a feature, pin the behavior that must not change:

```text
Add a --json flag. Keep the existing text output byte-identical. Run the real command in both modes and compare the output.
```

For a refactor, record the current behavior before moving structure. For performance work, name the fixture and measurement, profile before optimizing, and compare before and after under the same conditions. A number without its run conditions and limitations is not enough to establish a win.

## Test behavior, not the implementation

When a focused local test can demonstrate the failure, write the smallest test that fails for the intended reason, then make the fix and rerun it. If the test needs brittle mocks or broad harness setup, use the closest real command or runtime check instead. Report what actually ran and what it proves.

## Keep the diff reviewable

Before review, remove unrelated edits, dead compatibility paths, unsupported defensive code, and comments that only narrate the implementation. Keep comments that explain a public contract, external constraint, or fact that code cannot express. A cleanup request can simply ask for a focused diff review and the reason for each proposed removal.

Avoid assuming that upstream helper skills, custom agents, slash commands, model roles, or automatic cleanup tools are installed in ChatGPT. The pstack native harness defines the available workflows; other engineering guidance in these pages is portable advice.

Next: [Verify and ship](./06-verify-and-ship.md).
