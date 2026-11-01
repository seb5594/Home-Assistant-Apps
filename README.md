# Home Assistant Apps by seb5594

[![Home Assistant](https://img.shields.io/static/v1?label=Home%20Assistant&message=Add%20app%20repository&color=18BCF2&logo=homeassistant&logoColor=white&style=flat)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fseb5594%2FHome-Assistant-Apps)<br>
[![catalog sync](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Apps/update.yml?branch=main&label=catalog%20sync&style=flat)](https://github.com/seb5594/Home-Assistant-Apps/actions/workflows/update.yml) ![apps](https://img.shields.io/static/v1?label=apps&message=10&color=1877A5&style=flat)<br>
[![synced](https://img.shields.io/github/last-commit/seb5594/Home-Assistant-Apps?label=synced&style=flat)](https://github.com/seb5594/Home-Assistant-Apps/commits/main)

Practical Home Assistant apps for backups and configuration history. Add this catalog once, then choose the apps that fit your setup. Their versions, supported architectures, available mounts, and build status are shown below.

## Install

Use the blue button above, or open **Settings → Apps → App store → ⋮ → Repositories** in Home Assistant and add `https://github.com/seb5594/Home-Assistant-Apps`. Older versions may call these *Add-ons* and *Add-on store*. A Supervisor-based installation, such as Home Assistant OS, is required.

## Available apps

<!-- Generated from the source repositories by the hass-workflows catalog action. -->
### [Assist-AI-Router](https://github.com/seb5594/Home-Assistant-Assist-AI-Router-App) (1.0.5)

> Assist AI Router bündelt verschiedene KI-Anbieter und lokale Modelle hinter einem authentifizierten, OpenAI-kompatiblen Endpunkt für Home Assistant Assist. Die App nutzt das enthaltene **LiteLLM SDK** für Modellanfragen und ergänzt eine eigene Routinglogik, Verbrauchserfassung und Ingress-Oberfläche. Anbieter, Modelle, Schlüssel, Prioritäten und Limits verwaltest du im Browser. Speichern übernimmt Änderungen in die App-Konfiguration und wendet sie sofort an.

[Changelog](https://github.com/seb5594/Home-Assistant-Assist-AI-Router-App/blob/dev/assist_ai_router/CHANGELOG.md)<br>
![home assistant](https://img.shields.io/static/v1?label=home%20assistant&message=%E2%89%A5%202026.8.0&color=1877A5&style=flat) [![version](https://img.shields.io/static/v1?label=version&message=1.0.5&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Assist-AI-Router-App/releases) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=28&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%201235.7%20%C2%B7%20aarch64%201242.6%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=stable&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Assist-AI-Router-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Assist-AI-Router-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=4%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Assist-AI-Router-App/ci.yml?branch=dev&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Assist-AI-Router-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Assist-AI-Router-App) · [Pinned commit `3efc780`](https://github.com/seb5594/Home-Assistant-Assist-AI-Router-App/commit/3efc780876e67d31d6a80e2c0527fbb89ffedae6)

### [Git-Exporter](https://github.com/seb5594/Home-Assistant-Git-Exporter-Addon) (2.0.0-beta.2)

> Exports your Home Assistant configuration to one or more git repositories (GitHub, GitLab, Gitea, Bitbucket or your own server) and keeps them up to date. A web interface shows what would change before anything is pushed, which files the exclude rules keep out, and lets you adjust those rules with a click.

[Changelog](https://github.com/seb5594/Home-Assistant-Git-Exporter-Addon/blob/main/git-exporter/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=Beta%202&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Git-Exporter-Addon/releases/tag/v2.0.0-beta.2) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=40&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%20137.1%20%C2%B7%20aarch64%20149.1%20%C2%B7%20armv7%20110.5%20%C2%B7%20armhf%20119.3%20%C2%B7%20i386%20122.6%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat) ![mounts (read-only)](https://img.shields.io/static/v1?label=mounts%20%28read-only%29&message=app%20configs%20%C2%B7%20config%20%C2%B7%20local%20apps&color=157F71&style=flat)<br>
[![stars](https://img.shields.io/github/stars/seb5594/Home-Assistant-Git-Exporter-Addon?label=stars&style=flat)](https://github.com/seb5594/Home-Assistant-Git-Exporter-Addon/stargazers) [![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Git-Exporter-Addon?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Git-Exporter-Addon/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=49%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Git-Exporter-Addon/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Git-Exporter-Addon/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Git-Exporter-Addon) · [Pinned commit `4cf7f6a`](https://github.com/seb5594/Home-Assistant-Git-Exporter-Addon/commit/a25b38980cdf491d560cb3b6710deb3088b3dd7a)

### [Gitea-MCP-Server](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App) (1.0.0-alpha.11)

> Lets Assist, Claude, ChatGPT and other AI agents work with your own Gitea: search repositories, read files, and look at or write issues and pull requests.

[Changelog](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App/blob/dev/gitea_mcp_server/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=Alpha%2011&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App/releases/tag/v1.0.0-alpha.11) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=60&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%2058.4%20%C2%B7%20aarch64%2066.6%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Gitea-MCP-Server-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=24%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Gitea-MCP-Server-App/ci.yml?branch=dev&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App) · [Pinned commit `b9fed01`](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App/commit/b9fed01aacdaaf94d40f7765f3edf05cb26bbf42)

### [Gitea-Mirror](https://github.com/seb5594/Home-Assistant-Gitea-Mirror-App) (1.0.0-alpha.2)

> Mirrors repositories from GitHub, GitLab or another Gitea to your own Gitea and keeps them up to date, with the original web interface inside Home Assistant.

[Changelog](https://github.com/seb5594/Home-Assistant-Gitea-Mirror-App/blob/dev/gitea_mirror/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=Alpha%202&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-Mirror-App/releases/tag/v1.0.0-alpha.2) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=12&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%20545.1%20%C2%B7%20aarch64%20543.9%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Gitea-Mirror-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-Mirror-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=24%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Gitea-Mirror-App/ci.yml?branch=dev&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-Mirror-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Gitea-Mirror-App) · [Pinned commit `9b90d6b`](https://github.com/seb5594/Home-Assistant-Gitea-Mirror-App/commit/9b90d6b34e28d56ec683670d15c33f695ddcaa8c)

### [Gitea-Runner](https://github.com/seb5594/Home-Assistant-Gitea-Runner-App) (1.0.0-alpha.11)

> Runs the Actions workflows of your own Gitea on Home Assistant, inside an isolated app.

[Changelog](https://github.com/seb5594/Home-Assistant-Gitea-Runner-App/blob/dev/gitea_runner/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=Alpha%2011&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-Runner-App/releases/tag/v1.0.0-alpha.11) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=28&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%20136.4%20%C2%B7%20aarch64%20145.5%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Gitea-Runner-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-Runner-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=13%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Gitea-Runner-App/ci.yml?branch=dev&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-Runner-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Gitea-Runner-App) · [Pinned commit `030bc4c`](https://github.com/seb5594/Home-Assistant-Gitea-Runner-App/commit/030bc4c9ee03c2e2f982f02809f297043223955a)

### [Playstation-VR-Camera-Loader](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App) (1.0.0-beta.6)

> A far-field microphone for Assist, made from a PlayStation 4 / PlayStation VR camera.

[Changelog](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/blob/main/sony_playstation_vr_camera_loader/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=Beta%206&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/releases) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=8&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%20217.0%20%C2%B7%20aarch64%20204.1%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat) ![mounts (read-write)](https://img.shields.io/static/v1?label=mounts%20%28read-write%29&message=addon_config&color=B45309&style=flat) ![local disks](https://img.shields.io/static/v1?label=local%20disks&message=attached&color=1877A5&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=5%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App) · [Pinned commit `b4ce53e`](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/commit/18fc25ed6273b82047b2ed86b1f13c5e9e5cd9f3)

### [Rsync-Local](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon) (1.75.0)

> Rsync Local is a Home Assistant app that backs up the source folders you configure, such as `/config`, `/share` or `/media`, to a USB drive attached to your Home Assistant host. It copies with rsync, runs once per start and exits, so a Home Assistant automation can schedule it. The folders are mounted read-only; files you delete at the source are removed from the drive on the next run unless you change the rsync options.

[Changelog](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/blob/main/rsync-local/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=1.75.0&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/releases/tag/v1.75.0) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=36&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%2047.6%20%C2%B7%20aarch64%2056.8%20%C2%B7%20armv7%2037.1%20%C2%B7%20armhf%2042.5%20%C2%B7%20i386%2043.6%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=stable&color=2F855A&style=flat) ![mounts (read-only)](https://img.shields.io/static/v1?label=mounts%20%28read-only%29&message=app%20configs%20%C2%B7%20backup%20%C2%B7%20config%20%C2%B7%20local%20apps%20%C2%B7%20media%20%C2%B7%20share%20%C2%B7%20ssl&color=157F71&style=flat) ![local disks](https://img.shields.io/static/v1?label=local%20disks&message=attached&color=1877A5&style=flat) ![privileged](https://img.shields.io/static/v1?label=privileged&message=SYS_ADMIN&color=B45309&style=flat) ![apparmor](https://img.shields.io/static/v1?label=apparmor&message=disabled&color=B45309&style=flat)<br>
[![stars](https://img.shields.io/github/stars/seb5594/Home-Assistant-Rsync-Local-Addon?label=stars&style=flat)](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/stargazers) [![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Rsync-Local-Addon?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=12%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Rsync-Local-Addon/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon) · [Pinned commit `eb32907`](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/commit/e1e379094af2c945bba1d03a7ff346f1d0c31d93)

### [Tuya-Breaker](https://github.com/seb5594/Home-Assistant-Tuya-Breaker-App) (1.2.0-beta.4)

> Tuya Breaker combines UnTuyaOS3, Lightleak and Tuya-Cloudcutter in one experimental Home Assistant Ingress workspace. Choose a tool, review its requirements and use the shared WiFi App Helper to isolate one dedicated adapter. Includes the community hardware explorer, private firmware library and bounded Lightleak flash readout. The Lightleak controller is experimental and awaits physical-device validation.

[Changelog](https://github.com/seb5594/Home-Assistant-Tuya-Breaker-App/blob/dev/tuya_breaker/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=Beta%204&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Tuya-Breaker-App/releases) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=8&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%20200.2%20%C2%B7%20aarch64%20219.4%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat) ![mounts (read-write)](https://img.shields.io/static/v1?label=mounts%20%28read-write%29&message=share&color=B45309&style=flat) ![privileged](https://img.shields.io/static/v1?label=privileged&message=NET_ADMIN%2C%20NET_RAW&color=B45309&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Tuya-Breaker-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Tuya-Breaker-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=9%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Tuya-Breaker-App/ci.yml?branch=dev&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Tuya-Breaker-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Tuya-Breaker-App) · [Pinned commit `af08179`](https://github.com/seb5594/Home-Assistant-Tuya-Breaker-App/commit/af0817997ee5b4cae586d63ae3d7669b9e7bdcfb)

### [UnTuyaOS3](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App) (1.0.2)

> UnTuyaOS3 provides the original interactive UnTuyaOS3 firmware menus in Home Assistant Ingress, with a live terminal and continuously visible diagnostics. It requires the WiFi App Helper and an unused, AP-capable Wi-Fi adapter.

[Changelog](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App/blob/dev/untuyaos3/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=1.0.2&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App/releases/tag/v1.0.2) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=61&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%20153.6%20%C2%B7%20aarch64%20168.0%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=stable&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat) ![mounts (read-write)](https://img.shields.io/static/v1?label=mounts%20%28read-write%29&message=share&color=B45309&style=flat) ![privileged](https://img.shields.io/static/v1?label=privileged&message=NET_ADMIN%2C%20NET_RAW&color=B45309&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-UnTuyaOS3-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=6%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-UnTuyaOS3-App/ci.yml?branch=dev&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App) · [Pinned commit `d5ced2a`](https://github.com/seb5594/Home-Assistant-UnTuyaOS3-App/commit/d5ced2abe435100eb5911dd1a1300ec4c503ca4e)

### [WiFi-Helper](https://github.com/seb5594/Home-Assistant-WiFi-Helper-App) (1.0.2)

> Reusable local service for Home Assistant apps: lends one unused, AP-capable WLAN PHY to a client's isolated network namespace and restores it afterwards. It has no Web UI, HTTP listener, Docker API or host PID access.

[Changelog](https://github.com/seb5594/Home-Assistant-WiFi-Helper-App/blob/dev/wifi_helper/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=1.0.2&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-WiFi-Helper-App/releases/tag/v1.0.2) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=12&color=1877A5&style=flat)<br>
![arch & size](https://img.shields.io/static/v1?label=arch%20%26%20size&message=amd64%20130.1%20%C2%B7%20aarch64%20145.4%20MiB&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=stable&color=2F855A&style=flat) ![mounts (read-write)](https://img.shields.io/static/v1?label=mounts%20%28read-write%29&message=share&color=B45309&style=flat) ![privileged](https://img.shields.io/static/v1?label=privileged&message=NET_ADMIN&color=B45309&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-WiFi-Helper-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-WiFi-Helper-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=2%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-WiFi-Helper-App/ci.yml?branch=dev&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-WiFi-Helper-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-WiFi-Helper-App) · [Pinned commit `1361041`](https://github.com/seb5594/Home-Assistant-WiFi-Helper-App/commit/13610411fc9c8e5e7d417c2537dc5df1793acc23)

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
