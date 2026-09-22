# Runbook - Hermes Desktop + Telegram Gateway

## Purpose
Set up Hermes Desktop and the selected Hermes Telegram gateway for this project, using the same agent OS boundaries as the self-improving runtime while swapping the message channel from WhatsApp to Telegram.

## Scope Boundary

Hermes Desktop is a global runtime with many profiles, projects, and remote VPS connections. This repository is not the owner of every Hermes profile, VPS, or Telegram gateway shown in Desktop.

Use this runbook only to map the selected Hermes profile to this project. A Telegram token found in another Hermes profile or another repo is evidence about that profile only; it is not automatically a blocker or dependency for this repo.

| Layer | Owned by this repo? | Notes |
| --- | --- | --- |
| Project SOP, agent contracts, bundles | Yes | Files under this repo: `docs/`, `.ai/`, `.codex/skills/`, `bundles/`. |
| Hermes Desktop app | No | Shared local UI/runtime across profiles and repos. |
| Hermes profile | No, unless explicitly bound | Pick the profile intentionally before starting a gateway. |
| VPS/remote connection | No, unless selected | Remote profiles may point to old repos or other projects. |
| Telegram bot token | No | Secret belongs to the selected Hermes profile; never store it in this repo. |

## Observed Global Hermes State

- Hermes CLI is installed at `C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe`.
- Hermes version checked by `hermes doctor`: `0.21.3`.
- Python runtime is available in PATH and local skill validation passes.
- Desktop package was built successfully at `C:\Users\Admin\AppData\Local\hermes\hermes-agent\apps\desktop\release\win-unpacked\Hermes.exe`.
- A Telegram gateway configuration exists in the currently selected Hermes profile, including allowed user/home channel values.
- In the checked profile, Telegram rejected the configured bot token. Treat that as a profile-specific finding, not as proof that this repo owns or needs that token.

Never commit or paste the bot token into repo files, chat logs, runbooks, screenshots, or final reports.

## Channel Difference From WhatsApp

Telegram gateway setup is simpler than WhatsApp because it uses a BotFather bot token and an allowed user or chat id. It does not need WhatsApp pairing, QR scanning, a phone session, or WhatsApp Cloud API app credentials.

The safety boundary is the same:

- read and draft locally without approval;
- do not send outbound Telegram messages without explicit human approval;
- keep `TELEGRAM_ALLOWED_USERS` narrow;
- redact token values in logs and reports;
- stop if the gateway cannot authenticate or the bot is contacted by an unapproved user.

## Desktop Setup

Build the packaged Desktop app:

```powershell
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' desktop --build-only
```

Launch through the Hermes Desktop launcher:

```powershell
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' desktop --skip-build
```

If the packaged app exits immediately, inspect logs:

```powershell
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' logs gui -n 80
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' logs desktop -n 80
```

## Profile Selection Before Telegram Gateway Setup

Before touching Telegram, choose the intended Hermes profile and bind it to the intended project/repo. Do not reuse a gateway from an old repo just because it appears in Desktop.

```powershell
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' profile list
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' gateway list
```

For each profile, record:

- profile name;
- local project path or remote VPS target;
- repo/project it is meant to operate on;
- Telegram bot username, without token;
- allowed user/chat ids;
- gateway status.

Only continue when the selected profile, repo path, and Telegram bot all match the project you intend to run.

## Telegram Gateway Setup

1. Create or reset the Telegram bot token with `@BotFather`, only if the selected profile belongs to this project.
2. Update the local Hermes secret for that selected profile only, not any repo file:

```powershell
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' config set telegram.bot_token '<NEW_BOTFATHER_TOKEN>'
```

3. Confirm the allowed user/home channel are set to the intended Telegram user or chat id:

```powershell
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' config get telegram.allowed_users
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' config get telegram.home_channel
```

4. Restart the selected profile gateway:

```powershell
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' gateway restart
```

5. Verify status:

```powershell
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' gateway status
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' gateway list
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' logs gateway -n 50
```

Expected result after a valid token in the selected profile: that profile's gateway remains running and gateway logs show Telegram connected without token rejection.

## Troubleshooting

If `gateway restart` briefly reports a PID but `gateway status` later says no process is detected, check `hermes logs gateway -n 50`. A token rejection means Hermes started correctly but Telegram refused the bot credential for the selected profile.

If the Desktop package exists but no GUI process remains, launch with `desktop --skip-build` and inspect `gui` or `desktop` logs. Do not delete local AppData state unless the user explicitly approves a reset.

If `gateway status` warns about `gateway.multiplex_profiles`, leave it alone unless the run needs one gateway to serve all profiles. Migrating profiles changes runtime topology and should be treated as a separate maintenance task.

## Approval Gate

Before sending any Telegram test message or enabling automatic replies, produce this approval packet:

```text
Channel: Telegram
Hermes profile:
Repo/project path:
VPS/remote target, if any:
Bot: <bot username, no token>
Allowed users/chats: <ids only>
Message to send:
Reason for test:
Rollback command:
```

The human must approve the exact selected profile and test message before `hermes send` or any live Telegram outbound action is used.
