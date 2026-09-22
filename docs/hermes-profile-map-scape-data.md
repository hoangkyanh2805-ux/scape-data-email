# Hermes Profile Map - scape-data

## Active Project Profile

- Hermes profile: `scapedata`
- Hermes project: `scape-data`
- Project id: `p_8a6b3b15`
- Primary folder: `G:\Other computers\My Computer\Project\scape-data`
- Alias: `scapedata` -> `hermes -p scapedata`
- Gateway status: stopped by default
- Telegram channel: not cloned from old profiles; configure a dedicated bot token only if this project needs Telegram

## Why This Profile Exists

Hermes Desktop is global and already contains older profiles such as `default`, `orchestrator`, and several `forex-*` profiles. Those profiles may point to other repos, VPS targets, or Telegram credentials.

This repo should use `scapedata` only. Do not infer project ownership from another profile's gateway, token, VPS, logs, or bot status.

## Daily Commands

```powershell
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' profile use scapedata
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' -p scapedata project list
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' -p scapedata gateway status
```

Use the alias when the shell PATH includes `C:\Users\Admin\.local\bin`:

```powershell
scapedata project list
scapedata chat
scapedata gateway status
```

## Telegram Rule

If Telegram is needed for this project, create or choose a bot dedicated to `scapedata`. Configure it only inside the `scapedata` Hermes profile. Do not copy Telegram tokens from `default`, `forex-*`, or a remote VPS profile.

Approval is required before sending any Telegram test message or enabling automatic replies.

## 2026-09-21 Cleanup Note

Issue: profile `scapedata` was created from `default`, which copied old profile identity into `SOUL.md`, `config.yaml` `agent.environment_hint`, `memories/`, and active skill folder `skills/webkhoahoc`. Hermes Desktop therefore still answered as the old course project even after profile/project selection looked correct.

Fix applied:

- backed up old profile files under `C:\Users\Admin\AppData\Local\hermes\profiles\scapedata\_scape-data-cleanup-backup-*`;
- replaced `SOUL.md` with scape-data identity;
- replaced `memories/MEMORY.md` and `memories/USER.md` with scape-data boundary notes;
- changed `config.yaml` environment hint to scape-data;
- moved active `skills/webkhoahoc` into the backup folder;
- removed Telegram variables from the profile `.env`;
- restarted Hermes serve as `-p scapedata serve --isolated --skip-build`;
- sanity test passed with profile `scapedata`, project `scape-data`, cwd `G:\Other computers\My Computer\Project\scape-data`.

Desktop rule after cleanup: close old sessions and start a new session. Old sessions can retain old prompt/context in their conversation history.
