# Old apps or versions remain in the Home Assistant App Store

[Deutsch](#deutsch) | [English](#english)

## English

The current catalog contains separate UnTuyaOS3, Tuya Breaker and WiFi App Helper sources. GitHub container packages are image storage; deleting them does not clear Home Assistant's local catalog checkout.

After the former Anti-Tuya bundle was split, an existing Supervisor checkout can retain the removed `Anti-Tuya` submodule directory. Supervisor searches recursively for app configurations, including configurations left in that directory. A local reproduction using its fetch/reset/submodule-update/clean sequence kept both old and new configurations. This can produce an old helper entry or let an old configuration override the current version. This is a repository-checkout problem, separate from an installed app's version.

1. Finish every flashing session and verify the old helper has returned its radio. Make a Home Assistant backup and keep your private pairing secret.
2. Open **Settings > Apps > App store > three-dot menu > Check for updates**. Older Home Assistant versions call these Add-ons.
3. If the old catalog entries remain, open **three-dot menu > Repositories**. Remove only the repository entry `https://github.com/seb5594/Home-Assistant-Apps`, then add that exact same URL again. This removes and reclones the store source; do not uninstall apps or delete their data as a way to refresh it. Keep the exact URL, without a new branch suffix, so the repository identifier stays the same.
4. Search for updates again and reopen the App Store. Check the available versions: UnTuyaOS3 **1.0.1**, WiFi App Helper **1.0.1**, Tuya Breaker **1.2.0-beta.3** or newer.
5. An already installed old helper may remain visible as an installed/orphaned app even after the store source is fixed. Remove that old installation only after verified radio restoration, backup and migration to WiFi App Helper. An installed 1.2 beta of UnTuyaOS3 does not automatically downgrade to 1.0.1; back up/export its configuration and private files before following the standalone app's reinstall guidance.

No Home Assistant Core/host restart or host shell command is required for this catalog repair. This procedure does not prove a device is safe to flash.

Sources: [Supervisor repository update code](https://github.com/home-assistant/supervisor/blob/main/supervisor/store/git.py), [recursive app discovery](https://github.com/home-assistant/supervisor/blob/main/supervisor/store/data.py), [official store API](https://contributors.home-assistant.io/apps/supervisor-api/store/).

## Deutsch

Der aktuelle Katalog verwendet getrennte Quellen fuer UnTuyaOS3, Tuya Breaker und WiFi App Helper. GitHub-Packages speichern Container-Images. Ihr Loeschen bereinigt nicht den lokalen Katalog-Checkout von Home Assistant.

Nach der Aufteilung des Anti-Tuya-Buendels kann im Supervisor-Checkout das entfernte Unterverzeichnis `Anti-Tuya` als altes Git-Submodul zurueckbleiben. Der Supervisor liest App-Konfigurationen rekursiv ein und findet deshalb auch diese alten Dateien. Das wurde lokal mit seiner Update-Abfolge nachgestellt. Dadurch koennen alte Helper-Eintraege erscheinen und alte Konfigurationen die aktuelle Versionsanzeige ueberlagern. Der installierte App-Stand ist davon getrennt zu betrachten.

1. Alle Flash-Sitzungen abschliessen, erfolgreiche Adapter-Rueckgabe im alten Helper pruefen und ein Home-Assistant-Backup erstellen. Das private Kopplungsgeheimnis aufbewahren.
2. **Einstellungen > Apps > App-Store > Drei-Punkte-Menue > Nach Updates suchen**. Aeltere Versionen nennen die Apps Add-ons.
3. Bleiben die alten Katalogeintraege, unter **Drei-Punkte-Menue > Repositories** nur den Repository-Eintrag `https://github.com/seb5594/Home-Assistant-Apps` entfernen und exakt dieselbe URL wieder hinzufuegen. Das legt die Store-Quelle neu an. Nicht die Apps deinstallieren oder App-Daten loeschen, um den Katalog zu aktualisieren. Die identische URL ohne neuen Branch-Zusatz erhaelt die Repository-Kennung.
4. Erneut nach Updates suchen und den Store neu oeffnen. Erwartete verfuegbare Versionen: UnTuyaOS3 **1.0.1**, WiFi App Helper **1.0.1**, Tuya Breaker **1.2.0-beta.3** oder neuer.
5. Ein bereits installierter alter Helper kann weiterhin als installierte/verwaiste App auftauchen. Erst nach bestaetigter Adapter-Rueckgabe, Backup und Umzug zum WiFi App Helper entfernen. Eine installierte UnTuyaOS3-Version 1.2 Beta wird nicht automatisch auf 1.0.1 heruntergestuft; vorher Konfiguration und private Dateien sichern/exportieren und die Neuinstallationshinweise der eigenstaendigen App beachten.

Ein Core-/Host-Neustart oder Host-Terminalbefehle sind fuer diese Katalog-Reparatur nicht erforderlich. Die Anleitung ist keine Freigabe zum Flashen eines Geraets.
