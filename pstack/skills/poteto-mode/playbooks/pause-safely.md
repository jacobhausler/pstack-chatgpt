### Pause safely

For ChatGPT, first read the bundled resume-work skill. Use its native tools, scope, and persistence rules instead of Cursor-specific operations below.


**You own a clean stop. Leave a checkpoint a cold-start agent can resume from.** This is explicit only. On "keep going", "going to bed, keep going", or "don't stop", do not pause.

1. Stop at a safe boundary. Finish the current atomic step or back out of it. Start nothing new, and cancel any nested subagents.
2. Take no irreversible action to pause. No PR and no push unless you already had one out.
3. Make the work durable in the task's authorized checkpoint or repository record. Do not commit or publish solely to create a checkpoint unless the user authorized that operation. If no durable destination is available, leave changes at a safe boundary and report the limitation.
4. Update the durable checkpoint with intent, progress and evidence, current state, next steps, key files, and gotchas, following native **resume-work** guidance. Do not treat a temporary or scratch file as durable. If no approved durable destination is available, report that limit.

**Reply:** where you are in the loop, what's on disk versus still in your head (paths, no diff dumps), the commits you made and whether the tree is clean, and the first action on resume. This is a pause, not a final report.

