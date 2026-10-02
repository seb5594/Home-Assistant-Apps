# Home Assistant Apps by seb5594

[![Add repository to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fseb5594%2FHome-Assistant-Apps)
[![Catalog](https://github.com/seb5594/Home-Assistant-Apps/actions/workflows/update.yml/badge.svg)](https://github.com/seb5594/Home-Assistant-Apps/actions/workflows/update.yml)
[![Buy Me a Coffee](https://img.shields.io/badge/Support-Buy%20Me%20a%20Coffee-FFDD00?logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/seb5594)
[![PayPal](https://img.shields.io/badge/Support-PayPal-0070BA?logo=paypal&logoColor=white)](https://www.paypal.com/donate/?hosted_button_id=QMQPNRENXDN26)

Practical Home Assistant apps for backups and configuration history. Add this catalog once, then choose the apps that fit your setup. Their versions, supported architectures, available mounts, and build status are shown below.

## Install

Use the blue button above, or open **Settings → Apps → App store → ⋮ → Repositories** in Home Assistant and add `https://github.com/seb5594/Home-Assistant-Apps`. Older versions may call these *Add-ons* and *Add-on store*. A Supervisor-based installation, such as Home Assistant OS, is required.

## Available apps

<!-- Generated from the source repositories. Edit .templates/README.md for static content. -->
### [git-exporter](https://github.com/seb5594/Home-Assistant-git-exporter-Addon)

> Keep a readable history of your Home Assistant configuration in a Git repository you control. Exporters for Lovelace, ESPHome, Node-RED, app settings, and app configurations are optional; choose the files worth tracking.

**Home Assistant Git Exporter** · [Version 1.18.1](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/releases) · [Changelog](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/blob/main/git-exporter/CHANGELOG.md)

[![Build](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-git-exporter-Addon/ci.yml?branch=main&label=build)](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/actions/workflows/ci.yml) [![Release downloads](https://img.shields.io/github/downloads/seb5594/Home-Assistant-git-exporter-Addon/total?label=release%20downloads)](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/releases) [![Stars](https://img.shields.io/github/stars/seb5594/Home-Assistant-git-exporter-Addon?label=stars)](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/stargazers)

![armhf](https://img.shields.io/badge/armhf-supported-157F71) ![armv7](https://img.shields.io/badge/armv7-supported-157F71) ![aarch64](https://img.shields.io/badge/aarch64-supported-157F71) ![amd64](https://img.shields.io/badge/amd64-supported-157F71) ![i386](https://img.shields.io/badge/i386-supported-157F71)
![mount](https://img.shields.io/badge/mount-config-1877A5) ![mount](https://img.shields.io/badge/mount-app%20configs-1877A5)

[Source & documentation](https://github.com/seb5594/Home-Assistant-git-exporter-Addon) · [Pinned commit `39d7c67`](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/commit/39d7c67d62540f6651de6f732b49ba852297872e)

### [Rsync-Local](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon)

> Keep a second copy of the Home Assistant files that matter most on a USB stick, hard drive, or SSD plugged directly into your server. **`/config`** contains your automations, dashboards, scripts, and secrets; share, media, and app configuration folders can join the same scheduled backup.

**Rsync Local** · [Version 1.74.3](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/releases) · [Changelog](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/blob/main/rsync-local/CHANGELOG.md)

[![Build](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Rsync-Local-Addon/ci.yml?branch=main&label=build)](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/actions/workflows/ci.yml) [![Release downloads](https://img.shields.io/github/downloads/seb5594/Home-Assistant-Rsync-Local-Addon/total?label=release%20downloads)](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/releases) [![Stars](https://img.shields.io/github/stars/seb5594/Home-Assistant-Rsync-Local-Addon?label=stars)](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/stargazers)

![armhf](https://img.shields.io/badge/armhf-supported-157F71) ![armv7](https://img.shields.io/badge/armv7-supported-157F71) ![aarch64](https://img.shields.io/badge/aarch64-supported-157F71) ![amd64](https://img.shields.io/badge/amd64-supported-157F71) ![i386](https://img.shields.io/badge/i386-supported-157F71)
![mount](https://img.shields.io/badge/mount-config-1877A5) ![mount](https://img.shields.io/badge/mount-share-1877A5) ![mount](https://img.shields.io/badge/mount-media-1877A5) ![mount](https://img.shields.io/badge/mount-backup-1877A5) ![mount](https://img.shields.io/badge/mount-ssl-1877A5) ![mount](https://img.shields.io/badge/mount-local%20apps-1877A5) ![mount](https://img.shields.io/badge/mount-app%20configs-1877A5) ![mount](https://img.shields.io/badge/mount-local%20disks-1877A5)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon) · [Pinned commit `5831551`](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/commit/5831551dfbba413ae070f65687fe46a724f8d847)

The download badges count GitHub release assets, not installations, GHCR pulls, or local builds. GitHub does not expose country or continent totals for those downloads. See each app's documentation for the actual backup or export behavior.

The catalog follows each source repository's current default branch and pins that commit as a Git submodule. [How catalog updates work](.github/DEVELOPMENT.md).
