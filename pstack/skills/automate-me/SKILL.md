---
name: automate-me
description: Use for "automate me", "create/update/refresh my -mode skill", "turn/capture
  my preferences or working style into a skill", or wanting agents to follow how the
  user works. Drafts or revises a personal -mode skill via create-skill + unslop,
  optionally pulling fresh evidence from recent transcripts.
---

Read [the ChatGPT adapter](references/chatgpt.md) before following this workflow.


# Automate me

A guided flow for turning the user's working conventions into a skill agents will follow. The output is one `-mode` skill tailored to them (e.g. `jay-mode`, `priya-mode`).

This skill orchestrates an evidence-gathering pass, the host's skill-creator workflow for durable skill authoring, and the **unslop** skill for prose discipline. Preserve the user's intended workflow while using only capabilities available in this session.

## Flow

### 0. Check for an existing skill

Use the host's skill catalog and any user-provided paths to find an existing personal skill matching the user's handle. Do not assume Cursor skill directories or global filesystem access. If one exists, establish whether to update it or start fresh; honor an explicit choice already made in the request or conversation. Otherwise use the host's user-input capability when available, or ask a concise question in chat:

- Update the existing skill (default for repeat runs)
- Start fresh (rare, ask why before doing it)

Update mode changes the rest of the flow:
- Step 1 mines only history since the skill was last edited (`git log -1 --format=%cI <path>`).
- Step 2 asks what's changed or missing, not what to capture from zero.
- Step 4 edits the existing file in place. Preserve sections the user hasn't contradicted. Revise ones with new evidence. Add new sections only for genuinely new rules.

### 1. Mine their history

Use the conversation context and transcript or personal-context tools actually available in this session. Do not assume the system prompt provides an `agent-transcripts/` path, or search Cursor's local project history. If history access is unavailable, mine only the visible conversation and label the evidence limit. Delegate slices only when native subagent tools are available and useful; follow [delegate-work](../delegate-work/SKILL.md).

Survey only available, user-authorized history for recurring patterns. Use multiple independent slices when the history and native subagent tools support it; otherwise perform one bounded pass. Each pass returns a short structured list of patterns with evidence pointers. Default signals worth hunting:

- Response preferences (length, tone, format, "dumb it down" corrections)
- Delegation habits (subagents, models, specialized workflows, parallelism)
- Verification posture (what "done" means, unit tests vs live repro, reviewers)
- Code and prose discipline (style, principles cited, lint/format tools)
- Process conventions (worktrees, commits, PRs, review/merge tooling)
- Meta preferences (fixing skills mid-task, proposing new ones)

Cross-check across slices before elevating a signal. Patterns seen in 2+ slices are high-confidence. Lone signals are weak and usually get dropped.

### 2. Ask the user directly

Mining misses intent that hasn't come up yet. Use a structured user-input tool if one is exposed; otherwise ask a concise question in chat.

Use the live user-input schema. When it offers multiple choice, ask one concise question at a time with only the supported number of mutually exclusive options; use chat for free-form detail or when no input tool is available.

Don't dump 20 questions.

### 3. Cluster findings

Group the combined signals into sections. Common ones (use only what applies):

- **Response style**: length, tone, format.
- **Autonomy**: how much to do without asking, MCP tool use.
- **Understand first**: which skills to reach for when scoping or investigating a change.
- **Subagents**: default, parallelism, model-to-task, specialized workflows.
- **Prose / code discipline**: principles, lint tools, style guides.
- **Review and verify**: repro posture, verification skills, live-testing tools.
- **Process**: git worktrees, commits, PRs, review/merge tooling.
- **Skills**: skill-authoring habits, fix-the-skill-first, proposing new skills.

The **poteto-mode** skill shows the shape. Read it for granularity. Don't copy its content. The user's rules are not the same as poteto-mode's.

### 4. Draft the skill

Use the host's skill-creator workflow to author a reusable skill. Do not create Cursor-specific paths or claim a project file auto-registers as a ChatGPT skill. For a repository guide instead of a reusable host skill, agree on a project path and make its local scope clear.

- Path: for updates, preserve the existing skill's location and format. For a new reusable skill, follow the host skill-creator's supported location and initialization steps. For a repository guide, use the explicitly agreed repository location.
- Handle: the user's first name or chosen identifier.
- Frontmatter `description`: name the user's handle, the request to work in their style, and the skill's purpose; do not depend on slash-command syntax or generic keywords like "write code" or "review PR".
- Frontmatter formatting: follow the host skill-creator's current validation and metadata rules.
- Set explicit-invocation behavior through the host's supported agent metadata when available. Do not add unsupported frontmatter fields or make a personal style skill apply on every turn unless the user asks for that behavior.

### 5. Iterate on prose

Apply the **unslop** skill and the host skill-creator's writing guidance to every line.

Show the draft to the user and take feedback. Expect multiple iterations. Cut ruthlessly. A mode skill is not a manual.

### 6. Land it

For a reusable host skill, save through the host skill-creator workflow. For a repository guide, preserve the user's changes and commit or open a PR only within the user's authorized write scope. Otherwise return the prepared local draft. Do not push directly to main.

## Guardrails

- **Don't overfit to one conversation.** A preference stated once and contradicted another time is noise. Require multiple instances before codifying it.
- **Don't be clever.** Restating other skills' contents, inventing metaphors, or writing "poetic" prose for an agent reader is cost without benefit. Keep it operational.
- **Reference, don't inline.** Other skills the user relies on should appear as path references, not pasted excerpts. Same for any principle docs they maintain elsewhere.
- **Keep sections minimal.** Only add a section if the user has a specific, non-default rule there. "Communicate clearly" is not a section. "Short paragraphs. Tables when comparing options. Bullets only when items are genuinely parallel." is.
- **Name conventions generic.** Use "the user" or "the human" in imperatives, not the author's first name.
- **Don't force symmetry.** If a user has no process rules worth writing down, skip the Process section entirely.

## Evaluation

A personal style skill is subjective output. Ask the user to review whether it sounds like them and whether it missed anything, then apply their feedback and validate it with the host workflow.

Run a description-optimization loop only if the skill's trigger accuracy turns out to be a problem in practice.

## When not to use

- User wants a task-specific skill (not working conventions): use the host skill-creator workflow directly, with no history mining unless requested.
- User wants to capture one narrow workflow (e.g. "how I write commit messages"). That's a regular skill, not a mode skill.


