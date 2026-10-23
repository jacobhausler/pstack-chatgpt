---
name: recall
description: Reconstruct the user's recent working context from this conversation,
  identified artifacts, and targeted personal context, then return a concise current-
  state brief. Use for 'recall my work on X', 'catch me up', 'where did I leave off',
  or before resuming work when prior context is missing.
---

Read [the ChatGPT adapter](references/chatgpt.md) before following this workflow.

# Recall

Rebuild only the context needed for the user's current topic and return a concise,
useful handoff. Prefer evidence in this order:

1. **Current conversation.** Use the user's request, corrections, decisions, and any
   state capsule already provided. Do not retrieve context that is already sufficient.
2. **Identified artifacts and canonical files.** Inspect files, Library items, or
   other artifacts the user named or clearly tied to the work. If the task concerns
   a repository, issue, branch, or checkpoint, inspect its present state when facts
   may have changed; current evidence supersedes remembered status.
3. **Targeted personal context.** If relevant history is still missing, search
   personal_context for the specific topic, project, or time window. Make each query
   self-contained: this source does not receive the conversation. Include necessary
   names, identifiers, and scope in the query. Retrieve only what can resolve a
   concrete gap, and stop when the handoff is adequately supported.

Do not claim access to a user's full conversation history or to Cursor/local
transcripts. Do not search unrelated sources or broaden a topic into adjacent work
unless it blocks the requested work. If a source is unavailable or returns no useful
result, say that briefly when it affects confidence; do not imply it was searched.

Keep evidence types distinct:

- **Recalled decision:** a prior preference or choice found in the conversation,
  an identified artifact, or retrieved personal context.
- **Verified now:** a present fact checked in the live repository, issue, artifact,
  or other authoritative current source.
- **Inference:** a conclusion drawn from evidence; label it as an inference.
- **Unknown:** a material gap not resolved by available sources.

Do not treat remembered plans, stale status, or unverified recollections as current
facts. When current state matters, inspect it rather than relying on older memory.
Avoid redundant retrieval once enough evidence is available.

Route related work to the right workflow: `resume-work` handles future tasks and
checkpoints; `project-defaults` handles persistent project configuration. Recall
itself does not create schedules, edit memory, or modify files. It may inspect
relevant current state to prepare the handoff.

## Output

Lead with the current goal and constraints, then give the briefest evidence-backed
handoff:

- **Goal and constraints:** what the user is trying to do and the constraints that
  still apply.
- **Completed:** relevant decisions or work, marking recalled decisions separately
  from facts verified now. Include a source or artifact reference where useful.
- **Next step:** the single most useful concrete action to resume.
- **Open decisions or unknowns:** only unresolved points that could change the work.

Keep it concise and on-topic. Explicitly mark important inferences and identify any
source gap that limits confidence. Do not invent a thread status, claim completeness,
or include private details irrelevant to the task.
