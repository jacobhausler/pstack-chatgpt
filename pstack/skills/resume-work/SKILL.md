---
name: resume-work
description: Continue an authorized multi-step task across bounded runs using durable checkpoints, and optionally set up an explicitly requested supported automation. Use when a user asks to resume, keep working in runs, hand off progress, or schedule future continuation of repository work.
---

Read [the native ChatGPT workflows](references/chatgpt.md) before following this skill.


# Resume Work

Use this workflow to make concrete progress in a bounded run and leave enough durable state for a later run. A checkpoint is a record, not a background process: never claim work continues after the current run unless a supported automation was actually created and confirmed.

## Start each run

1. Find and read the latest checkpoint at the user's selected repository issue/file or supported persistent file facility. Never use scratch, a temporary file, or an uncommitted session-only note as the durable checkpoint. If no durable destination is identified, ask the user to choose one; continue only independent, reversible work that can be checkpointed there before exit.
2. Restate the checkpoint's goal, scope, authorized actions, stop condition, and next action. Treat authorization as limited to those actions. Do not merge, publish, send messages, delete data, or make other consequential external changes without explicit authorization for that action.
3. Refresh actual state before acting: inspect the current repository, branch, HEAD, working tree, relevant tests, and connected GitHub records or runtime state when available and relevant. Use native tools actually exposed in this session; discover their schemas and skill guidance instead of assuming Cursor commands, APIs, or tool names exist.
4. Compare refreshed state with the checkpoint. Reconcile stale assumptions with current evidence and record the current branch and HEAD. If the user changed scope or authorization, follow the latest instruction.

## Work one bounded run

5. Choose one small, independently verifiable unit that advances the goal. Set a concrete cap (for example, one bug fix plus its focused verification, or one review area) and do not expand scope to fill the run.
6. Preserve unrelated user changes. Before any write, check the target and current state. Use connected GitHub operations for supported repository tasks; use local git or `gh` only if they are actually available and authorized.
7. Verify the unit with the narrowest useful checks and record observed evidence, including commands/results or linked records. Distinguish completed work from assumptions and failed checks. If a run is interrupted during an external write or its result is ambiguous, inspect the destination and reconcile what actually happened before resuming; do not replay the write just because no success response was recorded. If readback is unavailable, mark the outcome unknown and stop dependent writes.
8. Before exit, update the durable checkpoint with the goal, scope, authorized actions, repository/branch/HEAD, completed work and evidence, next action, blockers, stop condition, and automation ID only if an automation was actually created. Save before reporting the run complete. If the destination is unavailable, do not substitute scratch; report the blocker and leave work at a safe boundary.
9. Handle overlapping runs by rereading immediately before update and using expected-version/revision checks when the destination supports them. Reconcile conflicts by rereading and merging facts. If another run is actively writing the same branch or artifact and no enforceable ownership mechanism exists, defer shared mutations and report the conflict; rereading alone is not a lock. Never claim a file lock or exclusive ownership across hosts unless the facility explicitly guarantees it. For external writes with no conditional update, recheck immediately before acting and read back after acting; this narrows but does not eliminate races, so report any unresolved conflict rather than claiming exclusivity.
10. Stop at the cap, the checkpoint stop condition, an authorization boundary, or a blocker. Report what changed, evidence, remaining next action, and whether a durable checkpoint was saved. Do not imply a process survives this session.

## Optional scheduled or event continuation

11. Configure automation only after the user explicitly opts in to future runs. “Keep working now,” “continue,” or “resume this” authorizes the current bounded run, not a repeating job. Explain that an automation schedules later bounded runs; it does not preserve an active process.
12. For a scheduled run, resolve the requested cadence and the user's IANA timezone from available context before creating it; ask only for missing material details. Use the current Automations tool schema and instructions. Polling condition checks must be no more frequent than hourly; never create a 45-second loop. Before a task that needs an external connector, successfully perform a harmless read-only preflight on every required connector. Stop if a connector is unavailable, disconnected, or requires setup; do not create a job with a caveat that access may work later.
13. For an explicitly requested supported event trigger, first call the exposed `discover_webhook_schema` action for the connected, authorized connector. Use only returned event names, trigger parameters, and guidance; never replace an event request with polling. Create using the current tool schema and webhook guidance, preserving the requested filters and action. If no supported event or connector is available, explain that limitation and ask before offering a different trigger.
The automation prompt must name this plugin and resume-work, the exact durable checkpoint locator, allowed actions, bounded unit, and stop condition. At the stop condition, disable the associated continuation automation through its returned identifier when authorized by this setup; report success only after readback. Do not spawn new automations on each run.

14. Confirm setup only from the create result. Record the returned automation ID, cadence/timezone or event trigger, and bounded-run prompt in the checkpoint. If creation fails, record the error and do not claim it was scheduled. Do not create or alter automations as a side effect of ordinary continuation.

Use [checkpoint.md](references/checkpoint.md) as the field checklist when creating or updating a checkpoint; put the actual checkpoint only in the durable destination selected for the task.

For webhook creation, supply the discovered triggers without an independent recurrence. If the exposed function schema requires `schedule` and `timing_mode`, use `schedule: ""` and `timing_mode: "condition_watch"` as required by that tool; these fields do not create polling. Do not invent trigger parameters to resolve schema conflicts.
