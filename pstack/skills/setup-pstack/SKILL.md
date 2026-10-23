---
name: setup-pstack
description: Set up native pstack workflows for ChatGPT or Codex, inspect available tools, and configure supported project and model defaults.
---

# Set up pstack

Read [native workflows](references/chatgpt.md).

1. Inspect available repository, execution, subagent, automation, context, and app tools. Report observed capabilities and missing connections.
2. Start with parent-model inheritance. For requested role settings, invoke configure-models. For durable repository guidance, invoke project-defaults. Preserve existing user choices.
3. Offer the workflow that fits the user's stated task: pr-review for PR reviews, resume-work for continued runs, triage-reports for intake, reproduce-fix for an evidenced bug fix, or poteto-mode for general engineering. Do not create services or schedules merely during setup.
4. For requested live setup, collect only missing repository/channel/destination/trigger details, then follow that workflow's connector preflight and creation instructions. Confirm actual saved state separately from runtime verification.
