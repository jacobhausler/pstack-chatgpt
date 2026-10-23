# ChatGPT workflows

Use the native workflows below instead of Cursor-specific tool calls, paths, model tables, and persistence instructions in upstream playbooks. Discover sibling skills by their pstack names through the host skill catalog; if unavailable, read their installed files. Do not invent tool names or assume an integration is connected.

| Upstream operation | Native pstack workflow |
| --- | --- |
| Bugbot review | pr-review |
| /loop, overnight continuation, scheduled follow-up | resume-work |
| Benny Slack intake | triage-reports |
| Benny reproduction and bounded fix | reproduce-fix |
| Task, poteto-agent, Comment Sicko, review panels | delegate-work |
| Cursor model-role rule | configure-models |
| Cursor rules and Custom Modes | project-defaults |
| Origin and PR operations | github-workflow |
| Cursor transcript recall and handoff | recall |

For each mapped operation, read and follow that native skill before acting. These mappings supersede the upstream implementation, not the user's goal. Use only available native tools and validated model identifiers. Inherit the parent model by default. Independent same-model passes are not a diverse-model consensus.

Workflows that inspect or configure a service are not active subscriptions. Create automations only on an explicit request for future work, after required read-only connection checks. Preserve exact repository, channel, recipient, and event scope. Honor existing authorization without repeatedly asking. No workflow grants itself permission to send messages, merge, deploy, or delete user data.

Use skill-local references through the host resource reader. Use repository AGENTS.md only for repository guidance; it does not change all ChatGPT conversations. Use the host's persistent file workflow or an authorized repository record for checkpoints and evidence. Scratch files do not establish durable progress.

For UI and CLI verification, use an exposed browser/control capability or actual executable tests appropriate to the target. Cursor control-ui/control-cli names do not establish installed tools. If the target cannot be run, report the verification limit. Missing evidence cannot become a pass.

The original Benny files under automations/benny are historical Cursor reference material with WORKFLOW.md names. Use the native triage-reports and reproduce-fix skills for ChatGPT work. Bugbot branding, Cursor cloud environments, and external model providers are not supplied by this package.

Inspect script dependencies before running them. Do not install or execute bootstrap code merely because the plugin was selected. Follow the host skill-creator workflow when generating durable skills.
