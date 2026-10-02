# Catalog maintenance

This repository is generated. The workflow in `.github/workflows/update.yml` runs the
shared catalog action from the private `hass-workflows` engine; the README and
`repository.yaml` are rewritten by it and should not be edited by hand.

## What gets listed

Public, active repositories owned by **[seb5594](https://github.com/seb5594)** whose names
match **`Home-Assistant-<project>-App`** or **`Home-Assistant-<project>-Addon`** (case-sensitive,
nonempty project name). Each needs at least one app configuration, at its root or in a nested
folder. Invalid metadata or duplicate slugs stop the run before anything is pushed.

| Repository name | Listed? |
| --- | --- |
| `Home-Assistant-git-exporter-Addon` | Yes |
| `Home-Assistant-Example-App` | Yes |
| `Home-Assistant-App`, `Home-Assistant-Apps` | No |
| A matching repository of another account | No |

## Updates

| Trigger | Behavior |
| --- | --- |
| Schedule | Every hour at minute 17, UTC |
| Manual | **Actions → Synchronize app catalog → Run workflow** |
| App release | The app pipeline sends an `update-addons` dispatch |
| Edit of `update.yml` | For example a new engine pin |

Every run pins each project's latest default-branch commit as a Git submodule. Unchanged
results produce no commit. GitHub may delay scheduled runs and pauses them after long
repository inactivity; re-enable the workflow under Actions if that happens.

The workflow needs an Actions secret named `ORCHESTRATION_PAT`: a fine-grained token with
**Contents: Read** on `seb5594/hass-workflows`.

Apps with an `image:` setting use that image; this catalog does not build containers.
Moving a submodule without changing the app version does not create an app update in
Home Assistant. Removed, renamed, archived or private projects disappear on the next
successful run, but an empty discovery result never erases an existing catalog.

To refresh the store in Home Assistant, run `ha store reload`. If obsolete metadata remains,
run `ha store repair 4c7fee11` followed by `ha store reload`; repairing does not uninstall apps.
