#!/usr/bin/env python3
"""Discover seb5594's public apps, pin their submodules, and render the catalog."""

from __future__ import annotations

import html
import json
import os
from pathlib import Path
import re
# Disabled after restoring root submodules: import shutil
import subprocess
import sys
# Disabled after restoring root submodules: from tempfile import TemporaryDirectory
import time
import urllib.error
import urllib.request

import yaml

ROOT = Path(__file__).resolve().parents[2]
OWNER = "seb5594"
EXCLUDED_REPOSITORIES: set[str] = set()
EXCERPT_MAX_CHARS = 500
NAME_PATTERN = re.compile(r"^Home-Assistant-(?P<project>[A-Za-z0-9][A-Za-z0-9._-]*)-(?:App|Addon)$")
ARCHITECTURES = {"aarch64", "amd64", "armhf", "armv7", "i386"}
CONFIG_NAMES = {"config.yaml", "config.yml", "config.json"}


def git(*args: str, cwd: Path = ROOT) -> str:
    """Run Git without a shell; never suppress errors."""
    return subprocess.run(
        ["git", *args], cwd=cwd, check=True, text=True, stdout=subprocess.PIPE,
        timeout=180, env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
    ).stdout.strip()


def fetch_json(url: str):
    """Retry transient API errors and authenticate when a token is available."""
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "seb5594-home-assistant-apps-sync",
    }
    if token := os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(
                urllib.request.Request(url, headers=headers), timeout=30
            ) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code not in {429, 500, 502, 503, 504} or attempt == 3:
                raise RuntimeError(f"GitHub API returned HTTP {error.code}: {url}") from error
        except (urllib.error.URLError, TimeoutError):
            if attempt == 3:
                raise
        time.sleep(2 ** attempt)


def discover_repositories(excluded: set[str]) -> list[dict]:
    """List every page rather than relying on GitHub search indexing."""
    repositories = []
    page = 1
    while True:
        batch = fetch_json(
            f"https://api.github.com/users/{OWNER}/repos"
            f"?type=owner&sort=full_name&per_page=100&page={page}"
        )
        if not isinstance(batch, list):
            raise ValueError("Expected a repository list from GitHub.")
        repositories.extend(
            repo for repo in batch
            if repo["owner"]["login"].casefold() == OWNER.casefold()
            and NAME_PATTERN.fullmatch(repo["name"])
            and not repo.get("private")
            and not repo.get("archived")
            and not repo.get("disabled")
            and repo["name"] not in excluded
        )
        if len(batch) < 100:
            break
        page += 1
    return sorted(repositories, key=lambda repo: repo["name"].casefold())


def readme_excerpt(folder: Path, fallback: str, limit: int) -> str:
    """Extract the first prose paragraph, skipping headings, badges and code."""
    readme = next((p for p in sorted(folder.iterdir())
                   if p.is_file() and p.name.casefold() == "readme.md"), None)
    paragraph = []
    in_code = False
    in_comment = False
    if readme:
        for line in readme.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if "<!--" in line:
                in_comment = True
            if in_comment:
                if "-->" in line:
                    in_comment = False
                continue
            if line.startswith(("```", "~~~")):
                in_code = not in_code
                if paragraph:
                    break
                continue
            if in_code:
                continue
            if not line or line.startswith(("#", "[", "!", "<", "|", "---", "* ", "- ", ">")):
                if paragraph:
                    break
                continue
            paragraph.append(line)
    text = " ".join(paragraph) or fallback or "See the source repository for details."
    # Plain text excerpts avoid broken relative links and unresolved badge references.
    text = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]*>", "", text)
    text = re.sub(r"\s+", " ", html.unescape(text)).strip()
    if len(text) > limit:
        text = text[:limit - 1].rsplit(" ", 1)[0] + "…"
    return html.escape(text, quote=False)


def app_metadata(folder: Path) -> list[dict]:
    """Check catalog fields; Supervisor still validates its complete app schema."""
    apps = []
    for config in sorted(folder.rglob("config.*")):
        parts = config.relative_to(folder).parts
        if (config.name not in CONFIG_NAMES or any(p.startswith(".") or p == "rootfs" for p in parts)):
            continue
        if config.is_symlink():
            raise ValueError(f"App configurations must not be symlinks: {config}")
        data = yaml.safe_load(config.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or "slug" not in data:
            continue
        for key in ("name", "version", "slug", "description"):
            if not isinstance(data.get(key), str) or not data[key].strip():
                raise ValueError(f"Missing or invalid {key!r} in {config}")
        if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", data["slug"]):
            raise ValueError(f"Invalid app slug in {config}")
        if not isinstance(data.get("arch"), list) or not data["arch"] or not set(data["arch"]) <= ARCHITECTURES:
            raise ValueError(f"Invalid architectures in {config}")
        app_path = config.parent.relative_to(folder).as_posix()
        apps.append({
            "name": data["name"], "slug": data["slug"], "version": data["version"],
            "description": data["description"], "arch": data["arch"], "path": app_path,
        })
    if not apps:
        raise ValueError(f"No Home Assistant app configuration found in {folder.name}.")
    return apps


def current_submodules() -> dict[str, dict[str, str]]:
    """Read paths and URLs from .gitmodules without assuming submodule names."""
    if not (ROOT / ".gitmodules").exists():
        return {}
    result = {}
    for line in git("config", "--file", ".gitmodules", "--list").splitlines():
        key, value = line.split("=", 1)
        if key.startswith("submodule.") and key.endswith(".path"):
            prefix = key.removesuffix(".path")
            result[value] = {"key": prefix, "url": git("config", "--file", ".gitmodules", f"{prefix}.url")}
    return result


def project_path(name: str) -> str:
    """Strip the repository naming prefix and suffix without changing project case."""
    if not (match := NAME_PATTERN.fullmatch(name)):
        raise ValueError(f"Invalid source repository name: {name}")
    return match["project"]


def managed_submodules(modules: dict) -> dict[str, dict[str, str]]:
    """Identify our generated folders using .gitmodules instead of a lock file."""
    managed = {}
    prefix = f"https://github.com/{OWNER}/"
    for path, module in modules.items():
        url = module["url"]
        if not url.startswith(prefix) or not url.endswith(".git"):
            continue
        name = url[len(prefix):-4]
        # Replaced: if NAME_PATTERN.fullmatch(name) and path in {name, project_path(name)}:
        if NAME_PATTERN.fullmatch(name) and path in {name, project_path(name), f".sources/{project_path(name)}"}:
            managed[path] = {**module, "repository_name": name}
    return managed


def sync_repository(repo: dict, modules: dict, limit: int) -> dict:
    """Pin exactly the latest commit of the actual default branch."""
    name = repo["name"]
    # Replaced: path = project_path(name)
    project = project_path(name)
    # Replaced: path = f".sources/{project}"
    path = project
    folder = ROOT / path
    url = f"https://github.com/{OWNER}/{name}.git"
    branch = repo["default_branch"]
    existing = [old_path for old_path, module in managed_submodules(modules).items()
                if module["url"] == url]
    if len(existing) > 1:
        raise ValueError(f"Multiple managed submodules reference {name}.")
    if existing and existing[0] != path:
        old_path = existing[0]
        if folder.exists() or path in modules:
            raise ValueError(f"Refusing to overwrite an existing directory: {path}")
        # Initialize before moving so migration also works with checkout submodules: false.
        git("submodule", "update", "--init", "--", old_path)
        # Disabled after restoring root submodules: (ROOT / ".sources").mkdir(exist_ok=True)
        git("mv", "--", old_path, path)
        modules = current_submodules()
    if path not in modules:
        if folder.exists():
            raise ValueError(f"Refusing to overwrite an unmanaged directory: {path}")
        # Disabled after restoring root submodules: (ROOT / ".sources").mkdir(exist_ok=True)
        git("submodule", "add", "--", url, path)
    else:
        if modules[path]["url"] != url:
            raise ValueError(f"Unexpected submodule URL for {name}; fix .gitmodules first.")
        git("submodule", "sync", "--", path)
        git("submodule", "update", "--init", "--", path)
    git("fetch", "--depth=1", "origin", f"refs/heads/{branch}", cwd=folder)
    sha = git("rev-parse", "FETCH_HEAD", cwd=folder)
    git("checkout", "--detach", sha, cwd=folder)
    # Initialize source submodules at their pinned commits, never their remote heads.
    git("submodule", "update", "--init", "--recursive", cwd=folder)
    apps = app_metadata(folder)
    return {
        # Replaced: "repository": f"{OWNER}/{name}", "path": path, "branch": branch, "commit": sha,
        "repository": f"{OWNER}/{name}", "path": project, "branch": branch, "commit": sha,
        "url": f"https://github.com/{OWNER}/{name}",
        "excerpt": readme_excerpt(folder, repo.get("description") or apps[0]["description"], limit),
        "apps": apps,
    }


# Disabled: direct copies are replaced by the original root submodules.
# def materialize_apps(entries: list[dict]) -> None:
#     """Expose complete build folders directly, hiding pinned source checkouts."""
#     wanted = {app["slug"] for entry in entries for app in entry["apps"]}
#     existing = {
#         folder.name for folder in ROOT.iterdir()
#         if folder.is_dir() and not folder.is_symlink() and not folder.name.startswith(".")
#         and (folder / ".catalog-source.json").is_file()
#     }
#     for slug in wanted:
#         if (ROOT / slug).exists() and slug not in existing:
#             raise ValueError(f"Refusing to overwrite an unmanaged app folder: {slug}")
#
#     # Stage every complete app before replacing any previously generated copy.
#     with TemporaryDirectory(prefix=".catalog-stage-", dir=ROOT) as temporary:
#         stage = Path(temporary)
#         for entry in entries:
#             source = ROOT / ".sources" / entry["path"]
#             for app in entry["apps"]:
#                 target = stage / app["slug"]
#                 shutil.copytree(source / app["path"], target, symlinks=True,
#                                 ignore=shutil.ignore_patterns(".git"))
#                 for license_name in ("LICENSE", "LICENCE", "LICENSE.md", "LICENCE.md", "COPYING"):
#                     if (source / license_name).is_file() and not (target / license_name).exists():
#                         shutil.copy2(source / license_name, target / license_name)
#                 (target / ".catalog-source.json").write_text(json.dumps({
#                     "repository": entry["repository"], "commit": entry["commit"],
#                     "path": app["path"],
#                 }, indent=2) + "\n", encoding="utf-8")
#         for slug in existing:
#             shutil.rmtree(ROOT / slug)
#         for slug in sorted(wanted):
#             shutil.move(str(stage / slug), ROOT / slug)
#
#
#
def render_catalog(entries: list[dict]) -> str:
    sections = []
    for entry in entries:
        sections.extend([
            f"### [{entry['path']}]({entry['url']})", "",
            f"> {entry['excerpt']}", "",
            "| App | Version | Architectures |", "| --- | --- | --- |",
        ])
        for app in entry["apps"]:
            name = app["name"].replace("|", "\\|")
            version = app["version"].replace("|", "\\|")
            sections.append(f"| {name} | `{version}` | {', '.join(app['arch'])} |")
        sections.extend([
            "", f"[Source & documentation]({entry['url']}) · "
            f"[Pinned commit `{entry['commit'][:7]}`]({entry['url']}/commit/{entry['commit']})", "",
        ])
    return "\n".join(sections).strip() or "No matching apps are currently available."


def main() -> None:
    excluded = EXCLUDED_REPOSITORIES
    limit = EXCERPT_MAX_CHARS
    template = (ROOT / ".templates/README.md").read_text(encoding="utf-8")
    if template.count("{{APP_CATALOG}}") != 1:
        raise ValueError("README template must contain exactly one {{APP_CATALOG}} placeholder.")
    metadata = json.loads((ROOT / ".templates/repository.json").read_text(encoding="utf-8"))
    if not isinstance(metadata, dict) or set(metadata) - {"name", "url", "maintainer"}:
        raise ValueError("Repository template must contain only name, url and maintainer.")
    if not isinstance(metadata.get("name"), str) or not metadata["name"].strip():
        raise ValueError("Repository template must contain a nonempty name.")
    if any(not isinstance(value, str) or not value.strip() for value in metadata.values()):
        raise ValueError("Repository metadata values must be nonempty strings.")
    repository_yaml = yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True)
    repositories = discover_repositories(set(excluded))
    modules = current_submodules()
    if managed_submodules(modules) and not repositories:
        raise ValueError("Refusing to remove the whole catalog; check the API and exclusions.")
    paths = [project_path(repo["name"]).casefold() for repo in repositories]
    if len(paths) != len(set(paths)):
        raise ValueError("Multiple source repositories resolve to the same app folder.")
    entries = [sync_repository(repo, modules, limit) for repo in repositories]
    slugs = [app["slug"] for entry in entries for app in entry["apps"]]
    if len(slugs) != len(set(slugs)):
        raise ValueError("Duplicate app slugs would collide in Home Assistant.")
    # Replaced: wanted = {entry["path"] for entry in entries}
    # Replaced: wanted = {f".sources/{entry['path']}" for entry in entries}
    wanted = {entry["path"] for entry in entries}
    # Disabled after restoring root submodules: materialize_apps(entries)
    # Remove only managed submodules after all current sources validate.
    for path in managed_submodules(current_submodules()):
        if path not in wanted:
            git("rm", "--force", "--", path)
    # Remove the legacy catalog state; Git already pins every submodule commit.
    (ROOT / "apps.lock.json").unlink(missing_ok=True)
    (ROOT / "README.md").write_text(template.replace("{{APP_CATALOG}}", render_catalog(entries)), encoding="utf-8")
    (ROOT / "repository.yaml").write_text(repository_yaml, encoding="utf-8")
    # Replaced: print(f"Synchronized {len(entries)} repositories and {len(slugs)} apps.")
    # Replaced: print(f"Synchronized {len(entries)} sources and {len(slugs)} directly installable app folders.")
    print(f"Synchronized {len(entries)} repositories and {len(slugs)} apps.")
    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(summary, "a", encoding="utf-8") as stream:
            stream.write(f"## App catalog\n\n{render_catalog(entries)}\n")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, RuntimeError, OSError, subprocess.SubprocessError, yaml.YAMLError) as error:
        print(f"Synchronization failed: {error}", file=sys.stderr)
        sys.exit(1)
