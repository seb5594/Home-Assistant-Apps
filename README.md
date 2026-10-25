# Home Assistant Apps by seb5594

[![Home Assistant](https://img.shields.io/static/v1?label=Home%20Assistant&message=Add%20app%20repository&color=18BCF2&logo=homeassistant&logoColor=white&style=flat)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fseb5594%2FHome-Assistant-Apps)<br>
[![catalog sync](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Apps/update.yml?branch=main&label=catalog%20sync&style=flat)](https://github.com/seb5594/Home-Assistant-Apps/actions/workflows/update.yml) ![apps](https://img.shields.io/static/v1?label=apps&message=4&color=1877A5&style=flat)<br>
[![synced](https://img.shields.io/github/last-commit/seb5594/Home-Assistant-Apps?label=synced&style=flat)](https://github.com/seb5594/Home-Assistant-Apps/commits/main)

Practical Home Assistant apps for backups and configuration history. Add this catalog once, then choose the apps that fit your setup. Their versions, supported architectures, available mounts, and build status are shown below.

## Install

Use the blue button above, or open **Settings → Apps → App store → ⋮ → Repositories** in Home Assistant and add `https://github.com/seb5594/Home-Assistant-Apps`. Older versions may call these *Add-ons* and *Add-on store*. A Supervisor-based installation, such as Home Assistant OS, is required.

## Available apps

<!-- Generated from the source repositories by the hass-workflows catalog action. -->
### [git-exporter](https://github.com/seb5594/Home-Assistant-git-exporter-Addon) (1.19.0)

> Git Exporter is a Home Assistant app that copies your configuration into a Git repository you choose: `/config`, Lovelace dashboards, ESPHome and Node-RED files, and the options of your other apps. Every change becomes a commit, so you get a readable history and can restore any earlier state. It runs once per start, for example from an automation, blanks `secrets.yaml` values in the export and can scan for secrets and IP addresses before it commits.

[Changelog](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/blob/main/git-exporter/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=1.19.0&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/releases/tag/v1.19.0) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=20&color=1877A5&style=flat)<br>
![arch](https://img.shields.io/static/v1?label=arch&message=amd64%20%C2%B7%20aarch64%20%C2%B7%20armv7%20%C2%B7%20armhf%20%C2%B7%20i386&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=stable&color=2F855A&style=flat) ![mounts (read-write)](https://img.shields.io/static/v1?label=mounts%20%28read-write%29&message=app%20configs%20%C2%B7%20config&color=B45309&style=flat) ![image size](https://img.shields.io/static/v1?label=image%20size&message=amd64%2090.6%20%C2%B7%20aarch64%20102.7%20%C2%B7%20armv7%2073.8%20%C2%B7%20armhf%2082.8%20%C2%B7%20i386%2085.8%20MiB&color=157F71&style=flat)<br>
[![stars](https://img.shields.io/github/stars/seb5594/Home-Assistant-git-exporter-Addon?label=stars&style=flat)](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/stargazers) [![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-git-exporter-Addon?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=2%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-git-exporter-Addon/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-git-exporter-Addon) · [Pinned commit `e843942`](https://github.com/seb5594/Home-Assistant-git-exporter-Addon/commit/e843942b50bf69b0cd347feb6dacb603113c4161)

### [Gitea-MCP-Server](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App) (1.0.0-dev7)

> Brings the official Gitea MCP server to Home Assistant. MCP, the Model Context Protocol, is how AI assistants use tools. With this app, Assist, Claude and ChatGPT can search your repositories, read files, and look at or write issues and pull requests in your own Gitea.

[Changelog](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App/blob/main/gitea_mcp_server/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=1.0.0-dev7&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App/releases/tag/v1.0.0-dev7) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=28&color=1877A5&style=flat)<br>
![arch](https://img.shields.io/static/v1?label=arch&message=amd64%20%C2%B7%20aarch64&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat) ![mounts (read-only)](https://img.shields.io/static/v1?label=mounts%20%28read-only%29&message=ssl&color=157F71&style=flat) ![image size](https://img.shields.io/static/v1?label=image%20size&message=amd64%2058.3%20%C2%B7%20aarch64%2066.6%20MiB&color=157F71&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Gitea-MCP-Server-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=23%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Gitea-MCP-Server-App/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App) · [Pinned commit `efde338`](https://github.com/seb5594/Home-Assistant-Gitea-MCP-Server-App/commit/efde3385b67004407657c5017a71b8ca7ddd9d4b)

### [Playstation-VR-Camera-Loader](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App) (1.0.0-beta.4)

> A Home Assistant app that turns the PlayStation 4 / PlayStation VR camera into a far-field microphone for Assist: four capsules, speech focus against TV and music, one clean 16 kHz input for any voice satellite. The camera picture comes along as a bonus.

[Changelog](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/blob/main/sony_playstation_vr_camera_loader/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=1.0.0-beta.4&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/releases/tag/v1.0.0-beta.4) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=4&color=1877A5&style=flat)<br>
![arch](https://img.shields.io/static/v1?label=arch&message=amd64%20%C2%B7%20aarch64&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=experimental&color=2F855A&style=flat) ![ingress](https://img.shields.io/static/v1?label=ingress&message=enabled&color=7C3AED&style=flat) ![mounts (read-write)](https://img.shields.io/static/v1?label=mounts%20%28read-write%29&message=addon_config&color=B45309&style=flat) ![local disks](https://img.shields.io/static/v1?label=local%20disks&message=attached&color=1877A5&style=flat) ![image size](https://img.shields.io/static/v1?label=image%20size&message=amd64%20217.0%20%C2%B7%20aarch64%20204.1%20MiB&color=157F71&style=flat)<br>
[![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=5%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App) · [Pinned commit `5064e67`](https://github.com/seb5594/Home-Assistant-Playstation-VR-Camera-Loader-App/commit/5064e670381b775b7978b0bc8b4b2c85d34df54f)

### [Rsync-Local](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon) (1.75.0)

> Rsync Local is a Home Assistant app that backs up the source folders you configure, such as `/config`, `/share` or `/media`, to a USB drive attached to your Home Assistant host. It copies with rsync, runs once per start and exits, so a Home Assistant automation can schedule it. The folders are mounted read-only; files you delete at the source are removed from the drive on the next run unless you change the rsync options.

[Changelog](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/blob/main/rsync-local/CHANGELOG.md)<br>
[![version](https://img.shields.io/static/v1?label=version&message=1.75.0&color=1877A5&style=flat)](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/releases/tag/v1.75.0) ![image pulls](https://img.shields.io/static/v1?label=image%20pulls&message=20&color=1877A5&style=flat)<br>
![arch](https://img.shields.io/static/v1?label=arch&message=amd64%20%C2%B7%20aarch64%20%C2%B7%20armv7%20%C2%B7%20armhf%20%C2%B7%20i386&color=157F71&style=flat) ![stage](https://img.shields.io/static/v1?label=stage&message=stable&color=2F855A&style=flat) ![mounts (read-only)](https://img.shields.io/static/v1?label=mounts%20%28read-only%29&message=app%20configs%20%C2%B7%20backup%20%C2%B7%20config%20%C2%B7%20local%20apps%20%C2%B7%20media%20%C2%B7%20share%20%C2%B7%20ssl&color=157F71&style=flat) ![local disks](https://img.shields.io/static/v1?label=local%20disks&message=attached&color=1877A5&style=flat) ![privileged](https://img.shields.io/static/v1?label=privileged&message=SYS_ADMIN&color=B45309&style=flat) ![apparmor](https://img.shields.io/static/v1?label=apparmor&message=disabled&color=B45309&style=flat) ![image size](https://img.shields.io/static/v1?label=image%20size&message=amd64%2047.6%20%C2%B7%20aarch64%2056.8%20%C2%B7%20armv7%2037.1%20%C2%B7%20armhf%2042.5%20%C2%B7%20i386%2043.6%20MiB&color=157F71&style=flat)<br>
[![stars](https://img.shields.io/github/stars/seb5594/Home-Assistant-Rsync-Local-Addon?label=stars&style=flat)](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/stargazers) [![issues](https://img.shields.io/github/issues/seb5594/Home-Assistant-Rsync-Local-Addon?label=issues&style=flat)](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/issues) ![runtime tests](https://img.shields.io/static/v1?label=runtime%20tests&message=12%20passed&color=2F855A&style=flat) [![checks](https://img.shields.io/github/actions/workflow/status/seb5594/Home-Assistant-Rsync-Local-Addon/ci.yml?branch=main&label=checks&style=flat)](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/actions/workflows/ci.yml)

[Source & documentation](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon) · [Pinned commit `bcea13c`](https://github.com/seb5594/Home-Assistant-Rsync-Local-Addon/commit/bcea13cdade86122b8702ca104583d9c73e15090)

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
