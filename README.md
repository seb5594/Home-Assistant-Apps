# Home Assistant Apps by seb5594

[![Home Assistant](https://img.shields.io/static/v1?label=Home%20Assistant&message=Add%20app%20repository&color=18BCF2&logo=homeassistant&logoColor=white&style=flat)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fseb5594%2FHome-Assistant-Apps)<br>
[![catalog sync](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Apps/update.yml?branch=main&label=catalog%20sync&style=flat)](https://github.com/seb5594/Home-Assistant-Apps/actions/workflows/update.yml) ![apps](https://img.shields.io/static/v1?label=apps&message=9&color=1877A5&style=flat)<br>
[![synced](https://img.shields.io/github/last-commit/seb5594/Home-Assistant-Apps?label=synced&style=flat)](https://github.com/seb5594/Home-Assistant-Apps/commits/main)

Practical Home Assistant apps for backups and configuration history. Add this catalog once, then choose the apps that fit your setup. Their versions, supported architectures, available mounts, and build status are shown below.

## Install

Use the blue button above, or open **Settings → Apps → App store → ⋮ → Repositories** in Home Assistant and add `https://github.com/seb5594/Home-Assistant-Apps`. Older versions may call these *Add-ons* and *Add-on store*. A Supervisor-based installation, such as Home Assistant OS, is required.

## Available apps

<!-- Generated from the source repositories by the hass-workflows catalog action. -->
### [Assist-AI-Router](https://github.com/seb5594/Home-Assistant-Assist-AI-Router-App) (2026-10-27)

> Die experimentelle Home-Assistant-App bündelt LiteLLM-kompatible Anbieter hinter einem lokalen Endpunkt. Profile, Schlüssel, Modelle, Prioritäten und Limits verwaltest du in der Ingress-Weboberfläche. Die native **LiteLLM-Integration** verbindet den Router mit Assist.

[Changelog](https://github.com/seb5594/Home-Assistant-Assist-AI-Router-App/blob/main/assist_ai_router/CHANGELOG.md)<br>
![home assistant](https://img.shields.io/static/v1?label=home%20assistant&message=%E2%89%A5%202026.8.0&color=1877A5&style=flat) [![version](https://img.shields.io/static/v1?label=version&message=v2026-10-27&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Assist-AI-Router-App/releases/tag/v2026-10-27) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=4&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%201235.6%20%C2%B7%20aarch64%201242.6%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Assist-AI-Router-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Assist-AI-Router-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=3%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Assist-AI-Router-App/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Assist-AI-Router-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Assist-AI-Router-App) · [Pinned commit `b7aa75e`](https://github.com/seb5594/Home-Assistant-Assist-AI-Router-App/commit/b7aa75e5a7c389a5b9f4a26249e60e1cf53051b0)

### [git-exporter](https://github.com/seb5594/Home-Assistant-git-exporter-Addon) (2.0.0-beta.1)

> Exports your Home Assistant configuration to one or more git repositories (GitHub, GitLab, Gitea, Bitbucket or your own server) and keeps them up to date. A web interface shows what would change before anything is pushed, which files the exclude rules keep out, and lets you adjust those rules with a click.

[Changelog](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/blob/main/git-exporter/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=Beta%201&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/releases/tag/v2.0.0-beta.1) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=30&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%2089.1%20%C2%B7%20aarch64%20101.1%20%C2%B7%20armv7%2073.0%20%C2%B7%20armhf%2081.7%20%C2%B7%20i386%2084.7%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat) ![mounts (read-only)](https://img.shields.io/static/v1?label=mounts%20%28read-only%29&message=app%20configs%20%C2%B7%20config%20%C2%B7%20local%20apps&color=157F71&style=flat)<br>
[![stars](https://img.shields.io/github/stars/seb5594/Home-Assistant-git-exporter-Addon?label=stars&style=flat)](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/stargazers) [![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-git-exporter-Addon?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=49%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-git-exporter-Addon/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-git-exporter-Addon) · [Pinned commit `bdc1226`](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/commit/bdc122617b962251e459c7aef84fa02b6cce7f35)

### [Gitea-MCP-Server](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App) (1.0.0-alpha.10)

> Brings the official Gitea MCP server to Home Assistant. MCP, the Model Context Protocol, is how AI assistants use tools. With this app, Assist, claude.ai, ChatGPT, Claude Code and other agents can search your repositories, read files, and look at or write issues and pull requests in your own Gitea. You decide which of them you connect.

[Changelog](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App/blob/main/gitea_mcp_server/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=Alpha%2010&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App/releases/tag/v1.0.0-alpha.10) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=56&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%2059.3%20%C2%B7%20aarch64%2067.7%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Gitea-MCP-Server-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=24%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Gitea-MCP-Server-App/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App) · [Pinned commit `ea5c954`](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App/commit/ea5c95470b5a3834a11f1c921da025f5b1962880)

### [Gitea-Mirror](https://github.com/seb5594/Home-Assistant-Gitea-Mirror-App) (1.0.0-alpha.1)

> Brings Gitea Mirror to Home Assistant. It mirrors repositories from GitHub, GitLab or another Gitea to your own Gitea and keeps them up to date. The original web interface is the page of the app, so there is nothing to open on your network.

[Changelog](https://github.com/seb5594/Home-Assistant-Gitea-Mirror-App/blob/main/gitea_mirror/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=Alpha%201&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-Mirror-App/releases/tag/v1.0.0-alpha.1) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=4&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%20536.1%20%C2%B7%20aarch64%20534.9%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Gitea-Mirror-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-Mirror-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=24%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Gitea-Mirror-App/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-Mirror-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Gitea-Mirror-App) · [Pinned commit `307ce52`](https://github.com/seb5594/Home-Assistant-Gitea-Mirror-App/commit/307ce5201c0bd51426717222b5f76e14ff9ac5b4)

### [Gitea-Runner](https://github.com/seb5594/Home-Assistant-Gitea-Runner-App) (1.0.0-alpha.10)

> Brings the Gitea Runner to Home Assistant. Gitea Actions workflows need a runner to execute them; with this app your own Gitea builds, tests and deploys on your own hardware, without a cloud service.

[Changelog](https://github.com/seb5594/Home-Assistant-Gitea-Runner-App/blob/main/gitea_runner/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=Alpha%2010&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-Runner-App/releases/tag/v1.0.0-alpha.10) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=24&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%20137.2%20%C2%B7%20aarch64%20146.5%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Gitea-Runner-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-Runner-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=13%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Gitea-Runner-App/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-Runner-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Gitea-Runner-App) · [Pinned commit `0b02ba8`](https://github.com/seb5594/Home-Assistant-Gitea-Runner-App/commit/0b02ba8120dbed350c1677ba27cd8c60237e3c25)

### [Playstation-VR-Camera-Loader](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App) (1.0.0-beta.5)

> A Home Assistant app that turns the PlayStation 4 / PlayStation VR camera into a far-field microphone for Assist: four capsules, speech focus against TV and music, one clean 16 kHz input for any voice satellite. The camera picture comes along as a bonus.

[Changelog](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/blob/main/sony_playstation_vr_camera_loader/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=Beta%205&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/releases/tag/v1.0.0-beta.5) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=8&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%20217.0%20%C2%B7%20aarch64%20204.1%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat) ![mounts (read-write)](https://img.shields.io/static/v1?label=mounts%20%28read-write%29&message=addon_config&color=B45309&style=flat) ![local disks](https://img.shields.io/static/v1?label=local%20disks&message=attached&color=1877A5&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=5%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App) · [Pinned commit `8778b9c`](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/commit/8778b9c2e2ac2a01cae9cf92967a934ae99de0d0)

### [Rsync-Local](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon) (1.75.0)

> Rsync Local is a Home Assistant app that backs up the source folders you configure, such as `/config`, `/share` or `/media`, to a USB drive attached to your Home Assistant host. It copies with rsync, runs once per start and exits, so a Home Assistant automation can schedule it. The folders are mounted read-only; files you delete at the source are removed from the drive on the next run unless you change the rsync options.

[Changelog](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/blob/main/rsync-local/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=1.75.0&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/releases/tag/v1.75.0) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=36&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%2047.6%20%C2%B7%20aarch64%2056.8%20%C2%B7%20armv7%2037.1%20%C2%B7%20armhf%2042.5%20%C2%B7%20i386%2043.6%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=stable&color=2F855A&style=flat) ![mounts (read-only)](https://img.shields.io/static/v1?label=mounts%20%28read-only%29&message=app%20configs%20%C2%B7%20backup%20%C2%B7%20config%20%C2%B7%20local%20apps%20%C2%B7%20media%20%C2%B7%20share%20%C2%B7%20ssl&color=157F71&style=flat) ![local disks](https://img.shields.io/static/v1?label=local%20disks&message=attached&color=1877A5&style=flat) ![privileged](https://img.shields.io/static/v1?label=privileged&message=SYS_ADMIN&color=B45309&style=flat) ![apparmor](https://img.shields.io/static/v1?label=apparmor&message=disabled&color=B45309&style=flat)<br>
[![stars](https://img.shields.io/github/stars/seb5594/Home-Assistant-Rsync-Local-Addon?label=stars&style=flat)](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/stargazers) [![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Rsync-Local-Addon?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=12%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Rsync-Local-Addon/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon) · [Pinned commit `1397e7e`](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/commit/1397e7e09cf01a0a2d45d38877894fd26c4bb75d)

### [UnTuyaOS3](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App) (untuyaos3 1.0.0-beta.2, untuyaos3_wifi 1.0.0-beta.2)

> An interactive Home Assistant app for UnTuyaOS3, with an Ingress console, verbose live logs, firmware uploads and a dedicated Wi-Fi radio.

**UnTuyaOS3** · [Changelog](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App/blob/main/untuyaos3/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=Beta%202&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App/releases/tag/v1.0.0-beta.2) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=45&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%20151.2%20%C2%B7%20aarch64%20165.6%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat) ![mounts (read-write)](https://img.shields.io/static/v1?label=mounts%20%28read-write%29&message=share&color=B45309&style=flat) ![privileged](https://img.shields.io/static/v1?label=privileged&message=NET_ADMIN%2C%20NET_RAW&color=B45309&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-UnTuyaOS3-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=4%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-UnTuyaOS3-App/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App/actions/workflows/ci.yml)

**UnTuyaOS3 Wi-Fi Helper** · [Changelog](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App/blob/main/untuyaos3_wifi/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=Beta%202&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App/releases/tag/v1.0.0-beta.2) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=45&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%20151.2%20%C2%B7%20aarch64%20165.6%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![mounts (read-write)](https://img.shields.io/static/v1?label=mounts%20%28read-write%29&message=share&color=B45309&style=flat) ![privileged](https://img.shields.io/static/v1?label=privileged&message=NET_ADMIN&color=B45309&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-UnTuyaOS3-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=4%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-UnTuyaOS3-App/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App) · [Pinned commit `cbc7597`](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App/commit/cbc75971f30646cfd0d6439a2b4104a9e337e3f2)

Image pull counts come from the public GHCR package pages and image sizes from the build pipeline; GitHub does not report installations or countries. See each app's documentation for the actual backup or export behavior.

The catalog follows each source repository's current default branch and pins that commit as a Git submodule. [How catalog updates work](.github/DEVELOPMENT.md).

## Support

Questions or problems? Open an issue on GitHub, but in the repository of the app concerned: every
app lives in its own repository, linked in its entry above. Issues opened here cannot be handled.

## Say thanks

All my projects are built in my spare time, just for the fun of it. Still, they take a lot of time and care, and many of the smart home gadgets I buy end up here because I want to make them cloud-free and smart-home ready. Every bit of support means a lot to me.

If my work helped you or turned out to be useful, show your appreciation with a hot drink for my next sleepless night.

[![PayPal](https://img.shields.io/static/v1?label=Support&message=PayPal&color=0070BA&logo=paypal&logoColor=white&style=for-the-badge)](https://paypal.me/seb5594) [![Buy Me a Coffee](https://img.shields.io/static/v1?label=Support&message=Buy%20Me%20a%20Coffee&color=FFDD00&logo=buy-me-a-coffee&logoColor=black&style=for-the-badge)](https://buymeacoffee.com/seb5594)

## License

Every project listed here is licensed on its own. The `LICENSE` file in each repository states which terms apply.
