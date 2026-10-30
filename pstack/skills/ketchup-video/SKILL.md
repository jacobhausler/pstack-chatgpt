---
name: ketchup-video
description: Catch the user up like ketchup, using a short subtitled slide video when the current session can create and inspect one. Use for /ketchup-video.
---

Read [the ChatGPT adapter](references/chatgpt.md) before following this workflow.

# Ketchup video

Follow the native [ketchup workflow](../ketchup/SKILL.md) for the time window, evidence, voice, and every action waiting on the user. Keep its read-only boundary. Creating a video is allowed only when this session exposes a supported way to create and inspect the artifact without changing the project or posting externally. If it does not, say that video rendering is unavailable and return the normal ketchup summary and action items.

Use captured screenshots, recordings, diffs, and measured data rather than chat summaries. Draft one takeaway and one line per slide before drawing; use at most ten slides, one point per slide, and include only facts supported by evidence. Never invent a screen or number.

Give each slide one short subtitle, around ten words, below the picture. Render a silent landscape video with motion between slides and burned-in subtitles, if the available tool supports those requirements. Check a frame from every slide at chat size and verify the subtitle remains readable and does not cover content; measure holds against the words that appear. If verification cannot be done, do not present the video as checked.

Reply with ketchup’s opening sentence, the embedded video, one line for work still actionable by the assistant, and the user’s action items. Use the option names shown in the video. If rendering or inspection fails, state that briefly and provide only the calls waiting on the user.
