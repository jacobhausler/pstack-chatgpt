---
name: delegate-work
description: Delegate an explicitly authorized, bounded task to native subagents and integrate their evidence.
---

Read [the native ChatGPT workflows](references/chatgpt.md) before following this skill.


# Delegate work

Use this workflow only when the user explicitly asks for delegation or the active invoked workflow explicitly requires a subagent for this step. Invoking this skill alone is not blanket permission to fan out. Otherwise do the work in the parent conversation.

Use only native subagent tools exposed in the current session, such as `spawn_agent`, `send_message`, and `wait_agent`. Follow their actual schemas. Never invent a `Task` tool, a `subagent_type`, a registered agent name, or an unavailable capability. Preserve the host's concurrency limit. Do not send independent external messages; a delegated agent may communicate only with its parent through the native tools.

## Dispatch

1. Define a bounded objective and identify which parts can safely run in parallel.
2. Give each agent a distinct owned path or a read-only scope. Avoid overlapping writes. If worktree support is available, use isolated worktrees for concurrent writers; otherwise assign exclusive files and sequence any shared-file edits.
3. For every task, provide the relevant user request and later constraints, objective, owned paths, evidence to collect, permission boundary, output format, and stop criteria. Include necessary context directly when the native tool requires it. Do not rely on an inaccessible transcript or file pointer.
4. Inherit the parent model and effort by default. Apply a model or reasoning override only when the user configured it through the supported setup workflow and the native spawn schema supports it. Use only exposed model IDs and supported effort values. If unsupported, inherit the parent.
5. Dispatch the smallest useful set of workers. Ask for checkpoints only when useful; wait with the native wait tool rather than polling in a tight loop.

## Roles

Choose roles by task; these are prompt patterns, not registered agent names. See [roles](references/roles.md) for role boundaries and report formats.

- **Poteto worker:** implement a bounded change within owned paths and report evidence.
- **Comment reviewer:** inspect scoped code or a diff for removable comments and refactor targets; report only.
- **Investigator:** answer a bounded question from cited files, commands, or other inspectable evidence; read-only.
- **Verifier:** independently run relevant checks and report commands, results, and limits; read-only unless the parent explicitly authorizes a fix.
- **Lead synthesis:** the parent owns integration. Reconcile reports, inspect actual diffs, run or verify necessary checks, and report conclusions with evidence.

Independent reviewers may examine the same evidence and prompt. Their agreement is a reason to investigate, not a substitute for evidence. Using the same model for multiple reviewers does not create diverse consensus. Request an independent review only when it adds useful coverage, and identify the files or risk area it owns.

## Integration

The parent owns the task and all delegated changes. Treat agent summaries as claims to check, not proof. Inspect changed files and diffs, confirm scope and permissions, and run appropriate tests or verify the reported commands and outputs yourself when possible. Resolve conflicts before reporting. Do not claim a test passed from an agent's summary alone. Stop delegation when the requested objective is met, the remaining work is serial, the host limit is reached, or a stop condition is met.
