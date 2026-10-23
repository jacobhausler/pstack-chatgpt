---
name: swarm
description: Fan out N parallel workers, drain them, and return one report. Use for
  /swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration.
---

Read [the ChatGPT adapter](references/chatgpt.md) before following this workflow.


# Swarm

## Start

Open a todolist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race N workers on identical briefs, or mix both. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before spawning.
4. Use [delegate-work](../delegate-work/SKILL.md) and the native subagent tools exposed in this session. Inherit the parent model by default. Apply a role choice only if the user configured it through [configure-models](../configure-models/SKILL.md) and the live schema supports it. Do not guess agent types, model IDs, or execution environments. If subagents are unavailable, run bounded sequential passes and label their limits.
5. Give each worker its own writable output when it writes. When workers verify or measure commits, each brief names the exact SHAs. A measurement brief also names the method (sample count, what one sample is, order). The worker records both in its result.

## Phase B: Fan out

Delegate workers using only the available native tool's schema. Do not assume support for background execution, cloud or local environments, or batch calls; if a needed capability is absent, run the available workflow or report the blocked slice.

When a worker needs a non-default branch, include the exact repository, branch, and commit in its brief. Select an execution checkout only through capabilities exposed by the host; do not invent branch-selection tool fields.

Every brief stands alone. Include the goal, scope, exact slice or race arm, how to verify, and what to report. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence. A worker that can prove a defect reports `ISSUES` and lists every issue it can prove, not only the first.

If a worker drops out, proceed with N-1 and note it.

## Phase C: Aggregate

Read the terminal results. Drop a result that does not record the SHAs and method its brief names, and respawn that worker once. After a second miss, record a gap. A gap does not count as a pass. For coverage, every required slice needs a result. For a race, apply the selection rule declared up front. Use first pass, rank all, or best-of. Do not paste raw worker dumps.

## Phase D: Report

Return one consolidated in-chat report with the table, issue one-liners, gaps or dropouts, and the race rule when used.

