# Verify a candidate existing fix

Use this path when an open pull request or merged commit plausibly addresses the reported symptom. The existing artifact owns the change: do not edit it, create a competing patch, or open a replacement PR.

1. Confirm a concrete code artifact and record its URL, base revision, candidate revision, and how it maps to the report. Prefer an artifact linked by the issue; otherwise state why this candidate is the closest match.
2. Use an isolated worktree or clean checkout where practical. Preserve the original working tree and all user changes.
3. Run the exact baseline repro on the candidate's base (or the revision immediately before a merged fix), using the same app, fixture/data, configuration, and environment as the candidate build. Observe the broken result twice and retain the same discriminating state/value.
4. Run the same path twice on the candidate revision. Confirm the broken result is gone and the expected result appears. For UI behavior, use real UI actions; tests and source inspection are supporting evidence, not a substitute.
5. Report **verified** only when both baseline and candidate behavior are observed. If the symptom persists on the candidate, report **reproduced, not fixed**. If either build cannot run or evidence is inconclusive, report **inconclusive** and name the unmeasured half. Never claim success from compilation or tests alone.
6. Clean up only temporary resources created for verification. Attach or upload evidence only through an available, authorized mechanism that confirms durable access; otherwise report the evidence in the run result without promising a persistent artifact.
