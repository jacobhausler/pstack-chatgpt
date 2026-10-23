---
name: github-workflow
description: Use for explicit GitHub repository, ref, commit, pull request, review, or merge tasks when native GitHub capabilities or authenticated local tools are available.
---

Read [the native ChatGPT workflows](references/chatgpt.md) before following this skill.


# GitHub workflow

Use only when the user explicitly requests a GitHub workflow action or names this skill. Do not infer permission to publish, review, or merge from a request to draft text or inspect code.

## Resolve the target and access

1. Resolve the exact repository and ref from the user's request, the active task context, or the current checkout's configured remote. If identity is ambiguous, ask before repository-dependent work. Never guess from a project name, package metadata, or a similar repository.
2. Discover the GitHub tools available in this run and inspect their descriptions. Prefer the native GitHub connector for supported repository, ref, PR, review, and merge reads or operations. Use only tool names and fields actually exposed; do not invent connector capabilities.
3. Read-only preflight: inspect local `git status`, current branch, `HEAD`, remotes, and user changes when a checkout exists. Then confirm the exact remote repository and requested ref with native GitHub reads. A connected repository or successful read does not establish write permission. If a checkout is absent, say so; do not fabricate a local branch or commit.
4. Use local `git` for working-tree inspection and commits when a usable checkout exists. Create commits or push only when the user's task scope authorizes them. Use `gh` only when authenticated and needed for an operation the native connector does not support. Check authentication and exact repo context first. Never fall back to another forge or assume access.
5. Preserve all user changes. Do not reset, clean, discard, force-push, or rewrite history. Keep existing local changes intact and avoid committing unrelated work.

## Pull requests

1. Before creating a PR, search the exact repository for an existing open PR matching the requested head and base or issue. Reuse or report an existing PR instead of creating a duplicate. Verify both branch names and the head commit.
2. Create, edit, retarget, or change PR readiness only when the user's authorized task scope includes that operation. Preserve draft intent: use draft creation when requested or when the workflow calls for a draft; do not blanket-mark PRs ready. For example, `reproduce-fix` requires a draft PR when it is authorized to open one.
3. Drafting a PR title/body or review findings in chat or source files is not publication. Submit a review, comment, or other GitHub content only when the user explicitly authorized that write. For a review, refresh the PR head and existing comments/reviews immediately before publication; do not publish findings against a stale head.
4. Preserve body text and newlines by passing structured text or a temporary body file. After a create/edit/readiness operation, read the PR back and verify its URL, head, base, title, body, and draft/open state as applicable. Report the result only after readback.
5. Merge only when the user explicitly authorized the merge. Immediately before merging, read the current PR head, required checks, and review state; confirm they refer to that head and satisfy repository requirements. If checks are pending/failing, required review is absent, requirements cannot be established, or head changed, stop and report the blocker. Use an expected-head argument when the merge tool supports one; if unavailable, disclose that read-before-write alone cannot guarantee the head remains unchanged. After a merge, read back and verify the merged state.

## Related skills and result

When a task is a one-shot PR review, discover and follow `pr-review`; when it is a reported bug, discover and follow `reproduce-fix`. This skill supplies GitHub access and write-scope rules; it does not replace their review, reproduction, or verification requirements.

Report the exact repository, ref or PR, access actually confirmed, local changes preserved, operations performed, and readback evidence. Distinguish local changes from remote writes and name unsupported or unavailable capabilities without claiming success.
