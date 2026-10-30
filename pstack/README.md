# pstack for ChatGPT

Engineering workflows for investigation, code review, verification, and technical writing.

Select this plugin and ask to use poteto-mode for a task, interrogate for a review, or unslop to edit prose. Use setup-pstack to inspect available tools and choose supported model roles. The current model is the default. Setup does not configure future chats globally.

The package contains 66 skills. Most require explicit invocation; setup can be selected from ordinary language. Available tools determine which checks can run. No server or background job starts when the plugin is selected.

Native workflows now cover PR review, bounded continuation, report triage, reproduction and draft fixes, agent delegation, model roles, project defaults, GitHub operations, and recall. These use connected ChatGPT capabilities; schedules and external writes require explicit setup. Original Benny remains Cursor reference material. The guide now describes native ChatGPT workflows; retained upstream illustrations are labeled as historical.

Adapted from Lauren Tan's MIT-licensed pstack at commit 8b3326d99fd4b993cb33a24dad8af03175c642c5, upstream version 0.15.30. See LICENSE and the preserved guide under docs/guide. ChatGPT release 0.16.2 removes remaining operational Cursor assumptions, strengthens retry and concurrent-write rules, and adds package regression checks. See docs/verification.md for executed checks and integration limits.

Upstream update review: 2026-10-30, through commit 4dd1d05818d19792e7cd6e818f1667f95f7e1dbe (upstream 0.15.36). See docs/upstream-sync.json for incorporated changes and deferred paths.
