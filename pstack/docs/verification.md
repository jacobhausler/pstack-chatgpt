# Verification record

Release 0.16.1, checked on 2026-10-23.

## Executed checks

- All nine native workflows and their ChatGPT adapter were readable through the installed skill reader before this release. Explicit-only skills need not appear in the automatic discovery list.
- `python -m unittest discover -s pstack/tests -v` passed five checks. They cover package structure, native entry points and policy text, and real Git worktree cleanup classification. Text checks detect source regressions; they do not prove host enforcement.
- `bash -n skills/poteto-mode/scripts/worktree-audit.sh` passed. Cleanup fixtures retained untracked and ignored data, held tracked changes, and classified clean merged worktrees as requiring an active-use check. The script does not query native chat history; its retained LAST_CHAT output column is always `-`.
- Skill-local Markdown reference targets resolved. Each skill's ChatGPT adapter matches the shared adapter.
- An isolated Python/Git exercise followed reproduce-fix. An intentionally wrong parity predicate failed its focused test twice on baseline. A one-line fix and odd-number regression assertion passed. The parent independently reproduced both baseline failures, reran the patched test, and checked the diff. This tests a simple local workflow execution, not a live app or GitHub integration.

## Adversarial instruction review

Reviewed interrupted writes, duplicate events, changed PR heads, overlapping checkpoint writers, and concurrent artifact creation. The workflows now require destination readback after uncertain writes, refreshed heads before review publication, and deferred creation where concurrent automated writers lack backend deduplication or serialization. These are workflow instructions, not a runtime transaction implementation. They cannot guarantee exactly-once behavior from unsupported backends.

## Operating scope

The user selected local tests only. No live repository, Slack channel, tracker destination, or production checkpoint was configured. No external PRs, review comments, issues, or intake subscriptions were created for testing. Live connector behavior and cross-host race handling remain unverified.

The existing weekly pstack updater remains scheduled for Fridays around 9 a.m. America/Chicago. Its updated prompt preserves native workflows, invocation policies, adapter copies, cleanup and retry protections, and runs regression checks before guarded updates. A future scheduled run has not yet been observed.

The user's Luna delegation preference applied to this maintenance task. Other tasks continue to inherit the parent model unless the user requests supported model choices. Repository guidance and global preferences were not changed.

## 2026-10-30 update, release 0.16.2

Verified all 322 saved source files against the integration baseline before editing. All nine native workflows remain byte-identical. The package now has 66 skills, with ketchup-video explicit-only and its own adapter reference.

Executed five Python package/cleanup tests, 61 Bun watcher/plan tests, watcher strict TypeScript checking, and the retained statechart suite (29 passed, 38 skipped because TLC is unavailable). All executed tests passed. Watcher regressions cover fork branch collisions, cycle termination, and deadline-capped sleeps. Markdown local-reference checks passed.

Adversarial instruction review covered missing video rendering, unsupported model choices, changed PR heads, worker claims of approval, interrupted checkpoints and overlapping writes. Resulting instructions fall back to text, preserve user authorization, and reconcile current state before mutation. These are instruction checks, not live-service enforcement tests.

The upstream statechart replacement was separately attempted with Node 22.18.0 and --test-concurrency=1. Ninety-two tests passed before exit 137 terminated the process; no completed suite result was obtained. It was not shipped. The pending path and its old baseline are recorded in upstream-sync.json so later runs retry it even when no new upstream commit exists. No live GitHub/Slack monitors or external messages were created.
