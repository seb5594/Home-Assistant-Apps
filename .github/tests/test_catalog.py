"""Check direct app publication and safe updates without a network connection."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "catalog", Path(__file__).resolve().parents[1] / "scripts/update_repo.py"
)
catalog = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(catalog)


# Disabled: these tests covered the reverted generated-copy layout.
# class PublicationTests(unittest.TestCase):
#     def setUp(self):
#         self.temporary = tempfile.TemporaryDirectory()
#         self.addCleanup(self.temporary.cleanup)
#         self.root = Path(self.temporary.name)
#         self.patch = patch.object(catalog, "ROOT", self.root)
#         self.patch.start()
#         self.addCleanup(self.patch.stop)
#         source = self.root / ".sources/Rsync-Local"
#         app = source / "rsync-local"
#         app.mkdir(parents=True)
#         (source / "LICENCE").write_text("Source license\n")
#         (app / "config.yaml").write_text(
#             "name: Rsync Local\nversion: '1.74'\nslug: rsync-local\n"
#             "description: USB backups\narch: [amd64]\n"
#         )
#         (app / "Dockerfile").write_text("FROM alpine:20260805\n")
#         (app / "root").mkdir()
#         (app / "root/run.sh").write_text("#!/bin/bash\n")
#         (source / ".github").mkdir()
#         (source / ".github/config.yaml").write_text("invalid: [")
#         self.entry = {
#             "path": "Rsync-Local", "repository": "seb5594/Home-Assistant-Rsync-Local-Addon",
#             "commit": "a" * 40, "apps": catalog.app_metadata(source),
#         }
#
#     def test_full_build_folder_is_visible_and_hidden_source_is_ignored(self):
#         catalog.materialize_apps([self.entry])
#         configs = [p for p in self.root.glob("**/config.*")
#                    if not any(part.startswith(".") or part == "rootfs"
#                               for part in p.relative_to(self.root).parts)]
#         self.assertEqual(configs, [self.root / "rsync-local/config.yaml"])
#         self.assertTrue((self.root / "rsync-local/Dockerfile").is_file())
#         self.assertTrue((self.root / "rsync-local/root/run.sh").is_file())
#         self.assertEqual((self.root / "rsync-local/LICENCE").read_text(), "Source license\n")
#         self.assertNotIn("image", catalog.yaml.safe_load(configs[0].read_text()))
#         marker = json.loads((self.root / "rsync-local/.catalog-source.json").read_text())
#         self.assertEqual(marker["commit"], self.entry["commit"])
#
#     def test_resync_removes_stale_files_and_keeps_pinned_metadata(self):
#         catalog.materialize_apps([self.entry])
#         (self.root / "rsync-local/stale.txt").write_text("old")
#         catalog.materialize_apps([self.entry])
#         self.assertFalse((self.root / "rsync-local/stale.txt").exists())
#         self.assertEqual(catalog.app_metadata(self.root)[0]["version"], "1.74")
#
#     def test_unmanaged_folder_is_never_overwritten(self):
#         (self.root / "rsync-local").mkdir()
#         sentinel = self.root / "rsync-local/keep.txt"
#         sentinel.write_text("keep")
#         with self.assertRaisesRegex(ValueError, "unmanaged"):
#             catalog.materialize_apps([self.entry])
#         self.assertEqual(sentinel.read_text(), "keep")
#
#     def test_failed_staging_preserves_previous_app(self):
#         catalog.materialize_apps([self.entry])
#         self.entry["apps"][0]["path"] = "missing"
#         with self.assertRaises(FileNotFoundError):
#             catalog.materialize_apps([self.entry])
#         self.assertTrue((self.root / "rsync-local/config.yaml").is_file())
#
#     def test_removed_app_cleanup_leaves_unmanaged_folders(self):
#         catalog.materialize_apps([self.entry])
#         (self.root / "notes").mkdir()
#         catalog.materialize_apps([])
#         self.assertFalse((self.root / "rsync-local").exists())
#         self.assertTrue((self.root / "notes").is_dir())
#
#
#
class RootSubmoduleTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.root_patch = patch.object(catalog, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        self.source = self.root / "Rsync-Local"
        app = self.source / "rsync-local"
        app.mkdir(parents=True)
        (app / "config.yaml").write_text(
            "name: Rsync Local\nversion: '1.74.1'\nslug: rsync-local\n"
            "description: USB backups\narch: [amd64]\n"
        )
        (self.source / "README.md").write_text("Back up Home Assistant files.\n")
        self.repo = {
            "name": "Home-Assistant-Rsync-Local-Addon",
            "default_branch": "main", "description": "USB backups",
        }
        self.modules = {"Rsync-Local": {
            "key": "submodule.rsync",
            "url": "https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon.git",
        }}

    def test_nested_app_discovery_ignores_source_workflows(self):
        (self.source / ".github").mkdir()
        (self.source / ".github/config.yaml").write_text("invalid: [")
        self.assertEqual(catalog.app_metadata(self.root)[0]["version"], "1.74.1")
        self.assertEqual(catalog.app_metadata(self.source)[0]["path"], "rsync-local")

    def test_sync_keeps_root_submodule_and_pins_default_branch(self):
        with patch.object(catalog, "git", return_value="a" * 40) as git:
            entry = catalog.sync_repository(self.repo, self.modules, 500)
        self.assertEqual(entry["path"], "Rsync-Local")
        self.assertEqual(entry["commit"], "a" * 40)
        self.assertFalse((self.root / ".sources").exists())
        git.assert_any_call("fetch", "--depth=1", "origin", "refs/heads/main", cwd=self.source)
        git.assert_any_call("checkout", "--detach", "a" * 40, cwd=self.source)
        self.assertFalse(any(call.args[:2] == ("submodule", "add") for call in git.call_args_list))

    def test_sync_refuses_unmanaged_directory(self):
        with self.assertRaisesRegex(ValueError, "unmanaged"):
            catalog.sync_repository(self.repo, {}, 500)

    def test_managed_paths_reject_unrelated_modules(self):
        unrelated = {"notes": {
            "key": "submodule.notes", "url": "https://github.com/another/project.git",
        }}
        self.assertEqual(set(catalog.managed_submodules(self.modules | unrelated)), {"Rsync-Local"})


if __name__ == "__main__":
    unittest.main()
