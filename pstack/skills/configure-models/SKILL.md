---
name: configure-models
description: Configure model and reasoning choices for native subagents when the user explicitly asks to choose or change model roles.
---

Read [the native ChatGPT workflows](references/chatgpt.md) before following this skill.


# Configure model roles

Use only when the user explicitly asks to choose, change, or persist model-role settings. This skill configures choices; it does not authorize spawning agents on every task.

1. Inspect the current native subagent tool schema. Use only model identifiers and reasoning-effort values it exposes. Do not infer aliases, availability, access, or model-family properties from product names or prior sessions.
2. The default for each role is to inherit the parent model and effort by omitting overrides. Ask for preferences only when the user requests custom routing; otherwise preserve the default.
3. Keep the configuration to the five groups in [role map](references/role-map.md). Map upstream role names into these groups instead of adding per-skill entries unless the user asks for finer control.
4. Apply requested choices to subagent calls in the current session as soon as relevant. A stored preference cannot change the parent chat model. If the host does not expose a choice, keep inheritance and explain the limit.
5. Persist project choices in the applicable `AGENTS.md`, creating it only when authorized project setup requires it, or in a repo file the user approved and that `AGENTS.md` references. Follow the bundled project-defaults workflow for that edit. Do not write `~/.cursor/rules` or claim a project file changes other chats.
6. Keep any requested resource budget qualitative and compact. Do not promise fixed money, token, or time savings.

Use a different model family for independent review only when the live tool exposes a suitable choice and the user has configured it. Different roles or prompts on the same model are separate passes, not model-diverse consensus. Same-model independent passes can still add coverage when each has a distinct scope. Do not configure extra agents simply to create the appearance of diversity.
