from __future__ import annotations

import json
import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ATLAS_ID = "github.com/sergio-sisternes-epam/discuss-atlas"
MOUNT = f".atlas/{ATLAS_ID}"
STORE_COMMIT = "6318b0add9596187b716954c93f2409d5a190fde"


class SourceContractTests(unittest.TestCase):
    def test_release_validation_uses_peeled_remote_tag_commit(self) -> None:
        release = (ROOT / ".github/workflows/release.yml").read_text(
            encoding="utf-8"
        )
        ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
        helper = (ROOT / "scripts/release_tag.py").read_text(encoding="utf-8")

        self.assertIn("refs/release-tags/", helper)
        self.assertIn("--github-output \"$GITHUB_OUTPUT\"", release)
        self.assertNotIn("git cat-file -t \"$TAG_REF\"", release)
        self.assertLess(
            release.index("Invalid release tag report"),
            release.index("python3 scripts/release_readiness.py"),
        )
        for variable in ("tag_object", "tag_commit", "main_commit"):
            self.assertIn(f'[ "${{#{variable}}}" -ne 40 ]', release)
            self.assertIn(f'[[ "${variable}" == *[!0-9a-f]* ]]', release)
        self.assertIn(
            "candidate_revision: ${{ needs.candidate.outputs.candidate_revision }}",
            release,
        )
        self.assertLess(
            ci.index("Validate reusable candidate revision"),
            ci.index("uses: actions/checkout@"),
        )
        self.assertIn('[[ "$CANDIDATE_REVISION" == *[!0-9a-f]* ]]', ci)
        self.assertEqual(
            ci.count("ref: ${{ inputs.candidate_revision || github.sha }}"), 4
        )
        readiness = ci[ci.index("  readiness:") :]
        self.assertLess(
            readiness.index("if: needs.metadata.result == 'success'"),
            readiness.index("ref: ${{ inputs.candidate_revision || github.sha }}"),
        )

    def test_manifest_uses_one_exact_atlas_dependency(self) -> None:
        manifest = (ROOT / "apm.yml").read_text(encoding="utf-8")
        dependencies = re.findall(r"^\s+-\s+(\S+)\s*$", manifest, re.MULTILINE)
        self.assertEqual(
            dependencies, ["sergio-sisternes-epam/atlas#v0.8.15"]
        )

    def test_mount_contract_has_no_deprecated_operational_path(self) -> None:
        for relative in ("SKILL.md", "README.md", ".gitmodules", "atlas-mesh.json"):
            content = (ROOT / relative).read_text(encoding="utf-8")
            self.assertNotIn("references/atlas", content, relative)
        for relative in ("SKILL.md", "README.md"):
            content = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn(
                f"atlas mount {ATLAS_ID} --ref main", content, relative
            )
            self.assertIn(f"atlas resolve {ATLAS_ID}", content, relative)
            mount_lines = [
                line for line in content.splitlines() if line.startswith("atlas mount ")
            ]
            self.assertTrue(mount_lines, relative)
            self.assertTrue(
                all("--target" not in line for line in mount_lines), relative
            )

    def test_mesh_and_submodule_use_default_mount(self) -> None:
        mesh = json.loads((ROOT / "atlas-mesh.json").read_text(encoding="utf-8"))
        self.assertEqual(
            mesh["stores"],
            [{"id": ATLAS_ID, "ref": "main", "path": MOUNT}],
        )
        modules = subprocess.run(
            ["git", "config", "-f", ".gitmodules", "--get-regexp", r"^submodule\..*"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        self.assertIn(f"submodule.{MOUNT}.path {MOUNT}", modules)
        self.assertIn(
            f"submodule.{MOUNT}.url "
            "https://github.com/sergio-sisternes-epam/discuss-atlas.git",
            modules,
        )

    def test_store_gitlink_is_exact(self) -> None:
        output = subprocess.run(
            ["git", "ls-files", "--stage", "--", MOUNT],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        self.assertRegex(output, rf"^160000 {STORE_COMMIT} 0\t{re.escape(MOUNT)}$")


if __name__ == "__main__":
    unittest.main()
