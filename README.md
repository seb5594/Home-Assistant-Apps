# Home-Assistant-Apps

**One repository for seb5594's Home Assistant apps and add-ons.**

Install this repository once to browse the available apps in Home Assistant.
Matching source projects are discovered automatically and added as Git submodules
in folders named after the project, such as `Rsync-Local/` and `git-exporter/`.
This page previews the introduction from each source README.

[![Add repository to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fseb5594%2FHome-Assistant-Apps)
[![Synchronize app catalog](https://github.com/seb5594/Home-Assistant-Apps/actions/workflows/update.yml/badge.svg)](https://github.com/seb5594/Home-Assistant-Apps/actions/workflows/update.yml)

## Install in Home Assistant

Click the button above, or open **Settings → Apps → App store → ⋮ → Repositories**
and add:

```text
https://github.com/seb5594/Home-Assistant-Apps
```

On older Home Assistant versions, the menus are named **Add-ons** and **Add-on store**.
These apps require Supervisor, such as the installation provided by Home Assistant OS.

## Available apps

<!-- Generated from the source repositories. Edit .templates/README.md for static content. -->
### [git-exporter](https://github.com/seb5594/Home-Assistant-git-exporter-Addon)

> Export your entire Home Assistant configuration to a Git repository of your choice. This addon allows you to safely version your setup and optionally share it in public repositories.

| App | Version | Architectures |
| --- | --- | --- |
| Home Assistant Git Exporter (dev) | `0.8.1dev` | armhf, armv7, aarch64, amd64, i386 |

[Source & documentation](https://github.com/seb5594/Home-Assistant-git-exporter-Addon) · [Pinned commit `57daa71`](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/commit/57daa7100e31d550899f5ae87a6356956fed73c3)

### [Rsync-Local](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon)

> Back up **`/config`**, including your automations, dashboards, scripts, and `secrets.yaml`, to a USB stick, USB hard drive, or USB SSD attached directly to your Home Assistant server. Keep the important resources from `/share`, `/media`, and your app configuration folders alongside them.

| App | Version | Architectures |
| --- | --- | --- |
| Rsync Local | `1.74.2` | armhf, armv7, aarch64, amd64, i386 |

[Source & documentation](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon) · [Pinned commit `d0124a1`](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/commit/d0124a1296e18b2d700100b696bc434df9e39d57)

## Discovery rules

Only public, active repositories owned by **[seb5594](https://github.com/seb5594)**
are included. Names must match **`Home-Assistant-<project>-App`** or
**`Home-Assistant-<project>-Addon`**, with a nonempty project name.
Matching is case-sensitive; forks owned by seb5594 are eligible.

| Repository name | Eligible? |
| --- | --- |
| `Home-Assistant-git-exporter-Addon` | Yes |
| `Home-Assistant-Rsync-Local-Addon` | Yes |
| `Home-Assistant-Example-App` | Yes |
| `Home-Assistant-App` / `Home-Assistant-Addon` | No: missing project name |
| `Home-Assistant-Apps` / `Home-Assistant-Addons` | No: plural suffix |
| A matching repository owned by another account | No |

Each project must contain at least one Home Assistant app configuration, at its
root or inside a nested folder. Invalid catalog metadata and duplicate app slugs
stop synchronization before changes are pushed.

## Automatic updates

| Trigger | Behavior |
| --- | --- |
| Scheduled | Every hour at minute 17, UTC |
| Manual | **Actions → Synchronize app catalog → Run workflow** on `main` |
| Source push | Optional notification workflow dispatches `update-addons` |
| Maintenance | Changes to the helper or templates on `main` refresh the catalog |

Every successful check follows each project's latest default-branch commit.
README excerpts, versions and architecture lists are generated from that pinned
source. Unchanged results produce no commit. GitHub may delay scheduled runs.

## Publish and initialize

1. Upload the package contents directly into the root of
   **`seb5594/Home-Assistant-Apps`** on **`main`**, including the `.github` folder.
   The package contains only `.github/` and `.templates/`; keep both folders at the repository root.
2. Enable GitHub Actions. The initial push starts synchronization; alternatively,
   select **Actions → Synchronize app catalog → Run workflow**.
3. Wait for a successful run before adding the repository to Home Assistant.

The action creates the app subfolders as real Git submodules, `.gitmodules`,
`repository.yaml` and this README. Git stores the pinned source commits, so no
separate lock file is required. No project files or Git
metadata need to be uploaded manually. The job requests `contents: write`
for the built-in `GITHUB_TOKEN`; no PAT is required for ordinary synchronization.
Repository or organization rules must allow that token to push to `main`.

## Optional immediate source notifications

Copy [.templates/notify-main.yml](.templates/notify-main.yml) to
`.github/workflows/notify-main.yml` in every source project. Configure an Actions
secret named **`PAT_TOKEN`** in each source repository using a fine-grained PAT
with access only to **`seb5594/Home-Assistant-Apps`** and permission
**Contents: Read and write**.

Pushes to the source's default branch, or a manual notification run, then refresh
the complete catalog. A missing secret emits a warning; hourly synchronization
still works. The source's `GITHUB_TOKEN` cannot dispatch to another repository.
Pushes made by a source's own `GITHUB_TOKEN` generally do not trigger another push
workflow; the scheduled fallback still discovers those commits.

## Simple maintenance

- Create a source repository with a matching name to add a new app automatically.
- Set `EXCLUDED_REPOSITORIES` and `EXCERPT_MAX_CHARS` in
  [.github/scripts/update_repo.py](.github/scripts/update_repo.py) to exclude repositories or change excerpt length.
- Edit [.templates/README.md](.templates/README.md) to change the catalog's static text.
- Edit [.templates/repository.json](.templates/repository.json) to change repository metadata;
  the action converts it into the root `repository.yaml` used by Home Assistant.
- Develop apps in their source projects and update their configured versions for
  Home Assistant to offer app updates.

Source files, licenses and build settings are preserved. Apps with an `image:`
setting use that image; this catalog does not build or publish containers.
Publish the image for a new version before exposing it on the default branch.
Moving a submodule without changing the app version does not create an app update.
Existing installations from other repository URLs are not migrated automatically.

Previously managed projects that are excluded, renamed, deleted, archived or made
private are removed on the next successful synchronization. An empty discovery
result cannot automatically erase an existing complete catalog.

If a scheduled workflow stops after prolonged public-repository inactivity,
re-enable it under Actions. If a push is denied, check Actions permissions and
branch rules. If an app update is missing, refresh the Home Assistant store and
check the source's configured version and published image.

For this repository, refresh the Home Assistant store with `ha store reload`.
If obsolete metadata remains, run `ha store repair 4c7fee11` followed by
`ha store reload`. Repository repair does not uninstall existing apps.
