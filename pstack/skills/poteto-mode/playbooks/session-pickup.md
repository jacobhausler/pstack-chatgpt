### Session pickup

For ChatGPT, first read the bundled recall skill. Use its native tools, scope, and persistence rules instead of Cursor-specific operations below.


**You own the resume point. Read the prior trail, don't redo it.**

1. Locate the prior trail from this conversation, identified artifacts, the named repository or branch, or targeted personal context through the native **recall** workflow. Do not assume access to private chat transcripts or cloud-agent dashboards. If a source is unavailable, state that limit and continue from current repository evidence. Use native subagents only when exposed and useful; inherit the parent model and effort by default.
2. Reconstruct operational state. The branch and worktree, what already landed (`git log`, `git diff` against the base), the open todos, the decisions made. The prior trail is authoritative input. Resist the bias to re-derive it.
3. Diff done vs pending. Compare what shipped against what was planned, name the resume point, do not re-run the prior repro or redo completed work. A "let me verify from scratch" pass means you're treating the trail as untrustworthy when it's authoritative.
4. Route the remaining work to the matching playbook and pick the verdict: continue the execution, ship a finished recommendation, ratify or override a prior conclusion, or postmortem a failed run. The pickup playbook ends here. The routed playbook owns the rest.
5. Verify inherited claims against the original goal on the real artifact (the **principle-prove-it-works** skill). A prior self-report is not proof.

**Reply:** where the prior agent stopped, what you inherited vs redid (ideally nothing redone), the resume point, and the outcome.

