"""Package-level guardrails for the ChatGPT-native workflow port.

These are source-integrity checks only. They make sure native workflow entry
points, adapters, and visible policy statements stay packaged together; they do
not establish that a host skill runtime enforces or executes the prose.
"""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]

NATIVE_SKILLS = {
    "configure-models",
    "delegate-work",
    "github-workflow",
    "pr-review",
    "project-defaults",
    "recall",
    "reproduce-fix",
    "resume-work",
    "triage-reports",
}

NATIVE_MAPPINGS = {
    "Bugbot review": "pr-review",
    "/loop, overnight continuation, scheduled follow-up": "resume-work",
    "Benny Slack intake": "triage-reports",
    "Benny reproduction and bounded fix": "reproduce-fix",
    "Task, poteto-agent, Comment Sicko, review panels": "delegate-work",
    "Cursor model-role rule": "configure-models",
    "Cursor rules and Custom Modes": "project-defaults",
    "Origin and PR operations": "github-workflow",
    "Cursor transcript recall and handoff": "recall",
}

# These names identify Cursor-only controls that can be mistaken for live
# ChatGPT capabilities when they appear as operational instructions. Ordinary
# historical/comparative mentions of Cursor are allowed. Benny is preserved as
# historical source under automations/, outside this native skill scan.
CURSOR_ONLY_CONTROLS = (
    r"\brun_in_background\b",
    r"\bcloud_base_branch\b",
    r"\bAskQuestion\b",
    r"\bupdate_state\b",
    r"\bSendToUser\b",
    r"api2\.cursor\.sh",
    r"\bcursor-agent\b",
    r"\bcontrol-(?:ui|cli)\b",
)


class NativeWorkflowPackageTests(unittest.TestCase):
    def test_native_workflows_ship_with_chatgpt_adapters(self):
        for name in sorted(NATIVE_SKILLS):
            with self.subTest(skill=name):
                skill = ROOT / "skills" / name / "SKILL.md"
                adapter = ROOT / "skills" / name / "references" / "chatgpt.md"
                self.assertTrue(skill.is_file(), f"missing native skill: {skill}")
                self.assertTrue(adapter.is_file(), f"missing ChatGPT adapter: {adapter}")

                source = skill.read_text(encoding="utf-8")
                self.assertRegex(source, r"(?m)^name:\s*" + re.escape(name) + r"\s*$")
                self.assertRegex(
                    source,
                    r"(?i)read\s+\[[^\]]*(?:ChatGPT|native)[^\]]*\]\(references/chatgpt\.md\)",
                    f"{name} must direct users to its packaged ChatGPT adapter",
                )

        shared_adapter = (ROOT / "docs" / "harness" / "chatgpt.md").read_text(encoding="utf-8")
        for source_label, name in NATIVE_MAPPINGS.items():
            with self.subTest(shared_mapping=name):
                self.assertIn(f"| {source_label} | {name} |", shared_adapter)

    def test_native_skills_do_not_instruct_cursor_only_controls(self):
        # Benny's original automation sources are intentionally outside this
        # scan; native skills live only in skills/*/SKILL.md.
        problems = []
        for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
            for line_number, line in enumerate(skill.read_text(encoding="utf-8").splitlines(), 1):
                for pattern in CURSOR_ONLY_CONTROLS:
                    if not re.search(pattern, line, flags=re.IGNORECASE):
                        continue
                    # Explicit warnings that name a nonexistent upstream
                    # control are useful adapter prose, not instructions to
                    # invoke it. Flag positive/actionable references only.
                    occurrence = re.search(pattern, line, flags=re.IGNORECASE)
                    prefix = line[: occurrence.start()]
                    if re.search(r"\b(?:do not|don't|never|not|no longer|does not|isn't|is not)\b", prefix, re.IGNORECASE):
                        continue
                    problems.append(f"{skill.relative_to(ROOT)}:{line_number} contains {pattern}")
        self.assertEqual([], problems, "Remove Cursor-only operational controls from native skills")

    def test_external_write_and_evidence_policies_remain_explicit(self):
        # Guard the safety boundary that matters for these workflows while
        # allowing surrounding copy to evolve. This checks for policy text,
        # not runtime enforcement.
        required_phrases = {
            "pr-review": ("never merge", "explicitly authorized publication"),
            "github-workflow": ("explicitly requests a github workflow action", "merge only when the user explicitly authorized"),
            "reproduce-fix": ("confirmed baseline failure", "authorized repository write scope"),
            "triage-reports": ("explicitly authorized that exact write and destination", "never automatically ping"),
            "resume-work": ("durable checkpoint", "never claim work continues after the current run"),
            "delegate-work": ("explicitly asks for delegation", "native subagent tools"),
            "project-defaults": ("explicitly asks to configure", "do not write cursor rules"),
            "configure-models": ("inherit the parent model", "model identifiers and reasoning-effort values it exposes"),
            "recall": ("do not claim access", "current evidence supersedes remembered status"),
        }
        for name, phrases in required_phrases.items():
            source = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8").lower()
            for phrase in phrases:
                with self.subTest(skill=name, phrase=phrase):
                    self.assertIn(phrase.lower(), source)


if __name__ == "__main__":
    unittest.main()
