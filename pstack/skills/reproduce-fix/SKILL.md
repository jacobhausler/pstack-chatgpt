---
name: reproduce-fix
description: Reproduce a specific reported software bug, verify an existing fix, or make a minimal tested fix when the user provides an issue/source and an authorized repository and test environment.
---

Read [the native ChatGPT workflows](references/chatgpt.md) before following this skill.


# Reproduce and fix a reported issue

Use this skill only for a concrete bug report or issue. Start with the exact issue/source, the authorized repository and write scope, and the available test/runtime environment. If any is missing or ambiguous, ask for that detail before dependent work. Do not treat a code hypothesis as a reproduction.

## Establish evidence and scope

1. Read the complete report, linked discussion, attachments, and relevant issue history that are accessible. Record the reported steps, expected result, actual result, environment/version, and a discriminating observable. Treat repeated issue/event deliveries as the same work item when the canonical source or issue identifier matches; refresh its current status before restarting and do not create parallel fixes or PRs for an active matching artifact.
2. Inspect the current checkout, working-tree changes, relevant implementation/tests, and repository history. Preserve user changes. Use an isolated worktree or clean checkout when useful; never reset or overwrite uncommitted work.
3. Discover available runtime controls and repository tools from the current environment. For UI behavior, use an available browser/app-control connector; for non-UI behavior, use the supported CLI or test harness. Confirm the target app, data, and version before testing.
4. Separate the evidence lanes in your notes: **reproduced** requires an executable runtime/test path that demonstrates the reported failure; **static hypothesis** means code inspection suggests a cause but runtime evidence is unavailable. Do not upgrade a hypothesis to a repro.
5. If the app cannot run or a dependency, fixture, credential, control, or environment prerequisite is unavailable, stop that evidence lane as **blocked** and name the missing prerequisite. Never fabricate a test, screenshot, passing result, or runtime observation. Continue only independent read-only inspection that remains useful.

## Reproduce before changing code

1. Translate the report into a concrete action path and a clear expected-versus-broken result. Choose the narrowest existing executable check that exercises it.
2. Run the path on the unmodified baseline. Observe the discriminating failure, reset relevant state, and repeat the same path once independently. For browser/UI issues, both observations must come from real UI interaction; state inspection may confirm but must not inject the failure. For code-level issues, run the same focused failing test/check twice when practical.
3. Save the exact commands/actions, revision, environment, outputs, and any accessible screenshots/logs as evidence. Do not claim durable evidence storage unless an available, authorized mechanism confirms it; avoid committing captures, logs, credentials, or temporary data.
4. If the behavior does not fail on baseline, report **not reproduced**. If only static evidence is available, label it a hypothesis. In either case, do not author a fix or open a PR.

## Check for an existing fix

Before editing, inspect issue-linked commits/PRs, repository history, and available GitHub search for an open or merged change that plausibly addresses the symptom. Search by issue reference and affected code; compare candidate PRs' issue linkage and current head so reruns do not create a duplicate. A comment or claim without a concrete PR/commit is not a fix artifact. Discover the repository's sibling workflows and current GitHub capabilities before choosing a path; prefer exposed native GitHub tools, otherwise use authenticated `gh`/local git only when available. Never invent connector or tool names.

If a plausible fix exists, follow [existing-fix verification](references/existing-fix.md). Verify the baseline failure and candidate fix under the same inputs and environment. Do not edit the existing change or open a competing PR. If verification cannot run, report that limitation and the artifact link without claiming it fixes the bug.

## Make and prove a bounded fix

Proceed only after a confirmed baseline failure, no applicable existing fix, a supported runnable verification path, and an authorized repository write scope. Confirm runtime evidence supports the root cause. Make the smallest justified patch; add a meaningful regression test when a focused test is practical. Run that check before the patch and show it fails for the reported reason, then apply the patch and rerun the same check successfully. If a red-before check is impractical, explain why and use the closest meaningful executable check; do not imply that the test failed before the change.

For a UI/runtime defect, run the same original path on the patched build twice, show the expected state in place of the broken state, and compare the same observable used at baseline. A compile or unit test alone does not prove a UI fix. Run focused tests and relevant nearby smoke checks. If verification fails or remains blocked, stop without a PR and report the patch/test state honestly.

Review the final diff for scope, unintended changes, and secrets. Run required repository checks. Draft a PR only when the authorized write scope includes branch/PR creation and all required checks pass. Before creating it, search again for an existing PR for the issue and candidate head; reuse/report an existing artifact instead of opening a duplicate. After a timed-out, interrupted, or otherwise ambiguous create/update operation, read the remote repository state and reconcile by issue and candidate head before retrying; if readback cannot establish whether it succeeded, leave the outcome unknown and stop dependent writes. Recheck the current branch/HEAD before each repository mutation; if another run changed the shared worktree or artifact and no supported ownership/version check exists, defer the mutation and report the conflict. Include repro steps, root cause, checks, and before/after evidence that is actually accessible. Never merge, deploy, or claim exactly-once creation without backend guarantees.

## Report

State the issue/repository and baseline revision; classify the result as reproduced, not reproduced, blocked, or static hypothesis; give the precise evidence and missing prerequisites; summarize any patch and diff; list exact checks and their outcomes; and link an existing or newly created PR only when verified. Distinguish local changes from remote writes. Preserve the user's work and clean up only temporary resources created by this run.

For concurrent automated writers, a read-before-write duplicate check is insufficient. Use a backend-supported idempotency key, conditional creation, or serialized execution when available. If concurrent runs can create the same review, ticket, or PR and no such guarantee is available, return the proposed write in the run report and defer creation to a single authorized writer. Do not treat a local scratch lock as cross-host coordination.
