---
name: poteto-help
description: Explain how to use this ChatGPT pstack plugin and choose a workflow. Use when the user asks for pstack help, setup guidance, or troubleshooting.
---

Read [the ChatGPT adapter](references/chatgpt.md) before following this workflow.


# Pstack help

Answer the question without starting an engineering task unless the user asks for that work. Read the selected skill before explaining its behavior.

## Start here

Select this private plugin, then ask for a workflow by name. For example, "Use poteto-mode to investigate this bug" or "Use interrogate to review this change." Slash notation in upstream documents names a workflow; it does not establish that this host has slash commands or Custom Modes.

Use setup-pstack to inspect the available tools and model choices. Roles use the current model by default. Setup applies choices within the session. It can update existing project agent instructions when authorized. It does not create Cursor rules or configure every future chat. Do not infer setup status from a .cursor file.

## Choose a workflow

| Goal | Skill |
| --- | --- |
| Carry out an engineering task | poteto-mode |
| Understand implementation or its rationale | how or why |
| Catch up on this chat as a short subtitled slide video when supported | ketchup-video |
| Challenge a change | interrogate |
| Design types and module boundaries | architect |
| Compare alternatives or divide work | arena or swarm |
| Reproduce a bug with a regression test | tdd |
| Check evidence behind a performance claim | benchmark-checklist |
| Remove unnecessary comments | no-comments |
| Edit prose | unslop or technical-writing |
| Build a project verification workflow | create-verification-skill |
| Check a state machine or invariant | statechart or create-formal-verification-skill |

For pre-commit code review, use the bundled interrogate skill. This port does not require deslop from cursor-team-kit. Unslop edits prose and is not a substitute for code review. Apply accepted review findings only when the user has requested fixes.

## Explain limitations

Use only tools and model identifiers exposed in the current session. When subagents are unavailable, perform separate sequential passes and say so. Same-model passes are not a multi-model consensus. Repository access and executable checks require the appropriate connected tools or runtime.

Use pr-review for GitHub review automation, resume-work for bounded future runs, triage-reports for Slack intake, and reproduce-fix for reproduction and draft fixes. These workflows require live setup before monitoring begins. Original Benny files remain historical Cursor references. Use delegate-work for agents, configure-models for role choices, project-defaults for repository guidance, github-workflow for PR operations, and recall for context.

## Link the correct implementation

For this adapted plugin, link https://chatgpt.com/plugins/plugins_6adb721f0aa0819185aca267861470e6 and explain the behavior from the installed files. Never construct an upstream URL for an adapted or locally added file.

For historical Cursor behavior, label it as upstream documentation and use https://github.com/cursor/plugins/tree/8b3326d99fd4b993cb33a24dad8af03175c642c5/pstack. That revision is the imported baseline, not a promise about this port. Read the installed README for any later baseline update.
