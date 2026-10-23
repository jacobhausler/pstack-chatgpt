# Durable work checkpoint

Copy this structure into the user-selected durable repository issue/file or supported persistent file facility. Do not keep the only copy in scratch.

```markdown
# Work checkpoint

- Updated: <date/time and timezone>
- Goal: <user's requested outcome>
- Scope: <included work and explicit exclusions>
- Authorized actions: <actions the user authorized>
- Repository: <name/path or N/A>
- Branch and HEAD: <branch, full commit SHA; refresh each run>
- Completed work and evidence: <changes, checks/results, links>
- Next action: <one bounded, concrete unit>
- Blockers: <none or details>
- Stop condition: <when to stop or ask>
- Automation ID: <exact returned ID, or none>
```

Before updating, reread the latest version. If the storage system exposes an expected revision/version, submit it and resolve conflicts by rereading; do not assume a cross-host lock.
