---
name: project-defaults
description: Configure concise, persistent pstack guidance for an explicitly requested repository. Use only when the user asks to set up or update project defaults.
---

Read [the native ChatGPT workflows](references/chatgpt.md) before following this skill.


# Project defaults

Use this only when the user explicitly asks to configure or update project guidance. Do not invoke it implicitly for routine coding work.

## Scope

- Inspect the repository's existing guidance and applicable `AGENTS.md` files before editing. Follow higher-level and host instructions.
- Make the smallest change in the requested repository. Prefer a clearly delimited pstack-managed section in the applicable project instructions. Preserve all surrounding content; replace only that section on reruns.
- If no suitable project instruction file exists, create one only when persistent repository configuration is part of the request. Do not write to user-global config or unrelated files.
- Do not write Cursor rules or custom modes as the solution. Do not imply that a repository file applies to ordinary ChatGPT chats or automatically installs skills, plugins, or model settings.
- For non-repository ChatGPT use, work through the selected plugin or current session instructions. Edit a reusable plugin only when the user explicitly asks for that change.

## Guidance to configure

The managed project section should say, concisely:

- For relevant, substantial engineering requests, invoke the available `poteto-mode` skill. Keep small, obvious tasks lightweight.
- Inherit the current parent model by default. Apply role-specific models only when `configure-models` supplies validated values supported by the current host; otherwise leave model routing unset.
- Follow the repository's existing build, test, review, and safety instructions. Preserve host policies and local repository rules.
- Treat saved project guidance and active session behavior as separate. Confirm whether the host observes the saved file; if activation cannot be verified, report that it is saved but unverified.

Do not add blanket instructions to overwrite existing guidance, use agents on every task, or claim this file changes a model or global setting. Do not invent model IDs or capabilities.

## Finish

Read back the edited file and verify that only the intended managed section changed. Report the file and the verification performed. State plainly when activation could not be observed.
