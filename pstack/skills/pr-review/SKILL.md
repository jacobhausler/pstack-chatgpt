---
name: pr-review
description: Use when the user asks for a one-shot GitHub pull request review, wants review findings on a PR, or explicitly asks to set up event-triggered reviews for scoped PRs.
---

Read [the native ChatGPT workflows](references/chatgpt.md) before following this skill.


# PR Review

Provide an evidence-based review of the current pull request. Keep a requested one-shot review separate from the optional setup of future event-triggered reviews. Never merge a PR.

## One-shot review

1. Resolve the exact `owner/repo` and PR number from the user's request or current context. If either is ambiguous, ask for it. Discover available tools at runtime; prefer the native GitHub connector. If GitHub access is missing or unauthorized, explain the limitation without claiming a review.
2. Use read-only GitHub calls to fetch the PR, latest head SHA, base SHA, description, changed files, diff, and relevant surrounding code. Read related tests and implementation as needed. Do not review a stale local checkout as if current.
3. Discover the bundled `interrogate` skill with the available skill-discovery mechanism and invoke it for the review. Follow its ChatGPT adapter and rubric. Use only exposed tools/models. If it is unavailable, do a careful single-pass review and disclose that limitation; never claim multi-model consensus.
4. Verify every candidate finding against the exact fetched head and surrounding context. Report only actionable defects introduced by the change. Include severity, file and line, the concrete failure mode, and evidence. Drop speculative, duplicate, stale, or non-actionable notes.
5. Before posting anything, fetch current PR review/comment records and head SHA again. Skip findings already represented for that head. If the head changed, refresh the PR, diff, and context, then re-review; never post findings from the old head. If a finding cannot be mapped to a valid current line, report it in chat instead of posting inline.
6. Return findings in chat by default. Publish a GitHub review or comments only when the user explicitly authorized publication. Immediately before a write, confirm the head still matches the reviewed SHA and use an exposed GitHub write tool. If that check fails, refresh and re-review. After a write or interrupted/ambiguous result, read back the PR head and review/comment records before retrying: skip a finding already present for that head, and do not repeat a write merely because its response was lost. If the head changed during the write window, report the resulting state and do not retry old findings; only clean up a stale comment when separately authorized. Do not claim exactly-once publication or concurrency safety unless the backend guarantees it.

## Set up future event-triggered reviews

This path is opt-in and separate from the one-shot review. Do not set up an automation merely because the user asked to review one PR now.

1. Require explicit intent to create an event-triggered review automation and exact scope: `owner/repo`, with a PR number or author filter when requested; an explicitly requested repository-wide scope is valid. Resolve author logins using authorized GitHub data; never guess. Ask when scope is missing or ambiguous; never silently widen it to the whole repository.
2. Run read-only GitHub preflight for the scoped PR, author/repository, or repository-wide request and confirm access. Discover the exposed Automations webhook schema for GitHub. Use only event names, trigger fields, and filter values returned by discovery; never invent a webhook schema. If GitHub, Automations, the event, or required access is unavailable, explain the blocker and do not claim setup succeeded. Do not substitute polling for an explicitly requested event.
3. Create only the single requested event automation, using the discovered GitHub pull-request event fields and exact scope. Its prompt must instruct each run to fetch the latest PR head, diff, and relevant context; invoke the bundled `interrogate` skill through skill discovery; validate findings at that head; check existing reviews/comments to avoid duplicates; and publish findings only if the user explicitly authorized publication, preserving that authorization in the automation prompt. Treat repeated deliveries as possible: re-read current PR and review state each run, and do not assume an event is unique or ordered. If it is absent or unclear, return findings in the automation run/chat. Never merge.
4. Treat the automation tool's result as authoritative. Report success only if it confirms creation, and describe its returned scope and event. Do not promise exactly-once execution or comment publication without a backend guarantee.

For webhook creation, supply the discovered triggers without an independent recurrence. If the exposed function schema requires `schedule` and `timing_mode`, use `schedule: ""` and `timing_mode: "condition_watch"` as required by that tool; these fields do not create polling. Do not invent trigger parameters to resolve schema conflicts.

For concurrent automated writers, a read-before-write duplicate check is insufficient. Use a backend-supported idempotency key, conditional creation, or serialized execution when available. If concurrent runs can create the same review, ticket, or PR and no such guarantee is available, return the proposed write in the run report and defer creation to a single authorized writer. Do not treat a local scratch lock as cross-host coordination.
