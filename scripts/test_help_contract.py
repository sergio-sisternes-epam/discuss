from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_IDS = (
    "getting-started",
    "help",
    "speak",
    "from-conversation",
    "sprout",
    "terminate",
    "lint",
    "consolidate",
    "constellation",
)
PATH_ID_RE = re.compile(r"\|\s*\*\*([a-z0-9-]+)\*\*\s*\|")


def _ids(text: str) -> list[str]:
    return PATH_ID_RE.findall(text)


def _flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


class HelpContractTests(unittest.TestCase):
    def test_path_modules_exist(self) -> None:
        for path_id in REGISTRY_IDS:
            path = ROOT / "references" / "paths" / f"{path_id}.md"
            self.assertTrue(path.is_file(), path)

    def test_skill_registry_lists_every_module(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        start = skill.index("## Path registry")
        end = skill.index("Default live loop")
        self.assertEqual(_ids(skill[start:end]), list(REGISTRY_IDS))

    def test_help_catalog_matches_registry(self) -> None:
        help_text = (ROOT / "references/paths/help.md").read_text(encoding="utf-8")
        start = help_text.index("## Installed registry")
        end = help_text.index("## Named module")
        self.assertEqual(_ids(help_text[start:end]), list(REGISTRY_IDS))

    def test_readme_modules_table_names_help_and_getting_started(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        start = readme.index("## Modules")
        end = readme.index("## Related")
        table = readme[start:end]
        self.assertIn("| Getting started |", table)
        self.assertIn("| Help |", table)
        self.assertNotIn("activation path", table.lower())
        self.assertNotIn("activation path", readme.lower())

    def test_readme_install_stays_marketplace_only(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("apm install discuss@atlas", readme)
        self.assertNotIn("discuss#v", readme)
        self.assertNotIn("sergio-sisternes-epam/discuss#", readme)

    def test_help_explains_and_does_not_execute(self) -> None:
        help_text = (ROOT / "references/paths/help.md").read_text(encoding="utf-8")
        self.assertIn("Explain Discuss. Do not execute Discuss.", help_text)
        self.assertIn("## Explain, do not execute", help_text)
        for forbidden in (
            "mutates the discussion graph",
            "atlas mount",
            "runs from-conversation, sprout, terminate",
        ):
            self.assertIn(forbidden, help_text)
        self.assertIn("Do not emit `path: terminate`", help_text)
        self.assertIn("Do not `atlas mount`. Do not auto-mount.", help_text)

    def test_help_baseline_then_optional_readonly_atlas(self) -> None:
        help_text = (ROOT / "references/paths/help.md").read_text(encoding="utf-8")
        self.assertIn("## Bundled baseline first", help_text)
        self.assertIn("Help must work with no Atlas mounted.", _flat(help_text))
        self.assertIn("## Optional Atlas enrichment", help_text)
        self.assertIn("when it is already resolvable", _flat(help_text))
        self.assertIn("atlas_used", help_text)
        self.assertIn("intent", help_text)
        self.assertIn("help_status", help_text)
        self.assertIn("atlas_status", help_text)

    def test_unknown_target_lists_valid_choices(self) -> None:
        help_text = (ROOT / "references/paths/help.md").read_text(encoding="utf-8")
        self.assertIn("say it is unknown and list the valid module names", help_text)
        self.assertIn("Do not require a clarifying question just to list", help_text)
        self.assertIn("Unqualified “help” outside Discuss context must not activate", help_text)

    def test_activation_cards_are_fenced_text(self) -> None:
        for relative in (
            "references/paths/help.md",
            "references/paths/getting-started.md",
        ):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn("```text", text, relative)
            self.assertIn("intent:", text, relative)
            self.assertIn("atlas_used:", text, relative)
            self.assertIn("speak_loaded: yes", text, relative)

    def test_getting_started_covers_first_journey(self) -> None:
        text = (ROOT / "references/paths/getting-started.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("### Purpose", text)
        self.assertIn("### Prerequisites", text)
        self.assertIn("### Shortest useful first journey", text)
        self.assertIn("discuss-atlas", text)
        self.assertIn("path **speak**", text)
        self.assertIn("apm install discuss@atlas", text)
        self.assertIn("This path must not run", text)
        self.assertIn("Point the user at path **help**", text)

    def test_live_loop_does_not_create_hub_for_help(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Exception — help and getting-started.", skill)
        self.assertIn("do not create a hub", skill)
        self.assertIn(
            "zero implement authority, no product writes outside this Atlas, "
            "no discussion-to-implement short-circuit.",
            skill,
        )
        self.assertIn("Unqualified help outside Discuss must not activate this skill.", skill)

    def test_changelog_records_unreleased_modules(self) -> None:
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        unreleased = changelog.split("## [0.3.10]", 1)[0]
        self.assertIn("getting-started", unreleased)
        self.assertIn("help", unreleased)
        self.assertNotIn("activation path", unreleased.lower())


if __name__ == "__main__":
    unittest.main()
