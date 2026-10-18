# Catalog maintenance

This repository is generated. `.github/workflows/update.yml` runs the shared catalog action from
the private `hass-workflows` engine; the README, `repository.yaml` and the submodules are rewritten by it and should not be edited by hand.

## What gets listed

Public, active repositories owned by **[seb5594](https://github.com/seb5594)** named
`Home-Assistant-<project>-App` or `Home-Assistant-<project>-Addon` with at least one app configuration, at the root or in a nested folder.
Private, archived and disabled repositories are skipped entirely, so they are neither listed nor
pinned; a repository that turns private is removed on the next run.

## Updates

| Trigger | Behavior |
| --- | --- |
| Schedule | Every hour at minute 17, UTC |
| Manual | **Actions → Synchronize app catalog → Run workflow** |
| app release | The app pipeline sends an `update-addons` dispatch |
| Edit of `update.yml` | For example a new engine pin |

Each run pins the latest default-branch commit of every listed app as a Git submodule, because the Supervisor installs from the repository tree.
Unchanged results produce no commit. The workflow needs the Actions secret `ORCHESTRATION_PAT`
with **Contents: Read** on `seb5594/hass-workflows`.
