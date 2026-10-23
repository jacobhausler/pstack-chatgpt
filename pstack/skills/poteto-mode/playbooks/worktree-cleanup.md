### Worktree cleanup

1. Run scripts/worktree-audit.sh with the repository and intended base ref. The audit reads Git state and suggests candidates. It never authorizes deletion.
2. Hold every worktree with tracked edits, untracked files, ignored files, or unreadable status. Inspect those files and preserve them or obtain explicit authorization to discard them. Untracked and ignored files can contain source, credentials, or user data. A branch does not preserve them.
3. Verify that each remaining candidate is unused. Check active processes and any native subagent status actually exposed. An audit bucket of `verify-unused` is only a prompt to check. If current usage cannot be established, hold the worktree and ask before removing it. Missing chat history is not proof that a worktree is unused. Confirm its current HEAD is contained in the intended base. A closed PR alone does not prove this.
4. Recheck status immediately before removal. Use git worktree remove without --force. If Git refuses, stop and inspect the cause. Do not bypass the refusal with force or rm -rf. Preserve newly discovered data before proceeding.
5. Re-list worktrees and report which were removed and which were held. Broader cache, simulator, and application-state deletion is outside this workflow and requires its own scope.
