---
name: reflect
description: Review the current conversation for durable learnings, surface
  learnings, and route each to a concrete edit on an existing skill. Use when the
  user says reflect.
---

Read [the ChatGPT adapter](references/chatgpt.md) before following this workflow.


# Reflect

Mine the current conversation for durable learnings, then route them into skill edits.

Invoke when the user says "reflect" or "/reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## 1. Read the conversation

Use only conversation history or transcript access actually exposed in this session. Do not assume an `agent-transcripts/` directory or search local Cursor project data. If the current conversation cannot be retrieved, review the visible conversation context and state that limitation; do not invent a transcript or mine unrelated sessions.

Use the current conversation directly. If the host exposes an authorized transcript or continuity tool, use it to fill gaps; otherwise pass a tight digest of the visible session.

## 2. Spawn three reviewers in parallel

Use [delegate-work](../delegate-work/SKILL.md) and the native subagent tools actually available to run independent review lenses. Never assume a Task tool, agent type, writable mode, or MCP access. If subagents are unavailable, run separate direct passes and label them as same-session reviews.

Inherit the parent model unless the user configured supported role choices through [configure-models](../configure-models/SKILL.md). Use only choices exposed by the live tool schema; do not guess alternatives after a rejection.

| Lens | Prompt template |
|---|---|
| Judgment | `references/judgment-reviewer.md` |
| Tooling | `references/tooling-reviewer.md` |
| Divergent | `references/divergent-reviewer.md` |

Pass each template with the conversation digest where marked. Reviewers return findings through the native delegation tool.

## 3. Synthesize

Use a distinct synthesis pass when the native delegation tool is available, providing each reviewer's full output and the synthesizer template. It must spot-check citations using only available sources. If no independent synthesis pass is available, synthesize directly and label the review limitation.

## 4. Structural enforcement check

Move any Accepted item that a lint rule, script, metadata flag, or runtime check would enforce more reliably to Backlog. See the **encode-lessons-in-structure** principle skill.

## 5. Apply

Present the synthesizer's Accepted / Rejected / Backlog output. Apply only changes the user authorized; if the user asked to reflect and fix accepted findings, treat that as authorization for those in-scope edits. Skill changes affect future runs, so keep the edits within the requested scope.

File Backlog items only when the user explicitly authorized the destination and the connected tracker is available. Otherwise include them in the report without creating external records.

Do not edit a skill inside an installed plugin or cache. Before proposing a change, identify the owning source repository or skill source and show that destination. Edit only that supported source under the user's authorization; if it is unavailable, provide a proposed patch instead. Do not publish, push, or open a PR unless explicitly requested.

Follow each approved row's Routing exactly:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): the parent does it directly.
- Substantive skill edit or a new skill: follow the host's skill-creator workflow when available. Do not assume Cursor's built-in `create-skill` or a slash command exists.
- Description tuning follows the same host skill-creator workflow; preserve the skill's purpose and test triggering against concrete examples.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done.

## 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.

