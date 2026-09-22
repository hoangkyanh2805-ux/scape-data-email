# Runbook - Hermes Desktop + Telegram Gateway

Use this when cloning the self-improving agent OS into a project that uses Telegram instead of WhatsApp as the operator channel. Hermes Desktop may contain many profiles, remote VPS targets, and old repo connections; select the intended profile before treating any gateway status or Telegram token as relevant.

## Required Local Runtime

- Hermes CLI installed and callable.
- Python runtime available in PATH.
- Project agent contracts installed under `.ai/agents/`.
- Telegram bot token stored only in local Hermes config or secret storage.
- Telegram allowed users/home channel restricted to approved ids.

## Scope Boundary

This bundle owns project files and operating rules only. It does not own the user's global Hermes Desktop state, other Hermes profiles, VPS connections, or Telegram bot tokens from older repos.

Before gateway work, map:

- profile name;
- repo/project path;
- remote VPS target, if any;
- Telegram bot username, without token;
- allowed chat/user ids;
- intended gateway status.

## Commands

```powershell
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' desktop --build-only
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' desktop --skip-build
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' profile list
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' gateway restart
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' gateway status
& 'C:\Users\Admin\AppData\Local\hermes\bin\hermes.exe' logs gateway -n 50
```

## Telegram Delta

Telegram needs a BotFather token and allowed chat/user ids for the selected profile. It does not need WhatsApp pairing, QR login, phone state, or Cloud API app setup.

Do not send live Telegram messages without explicit approval. A valid gateway startup only proves the selected profile's bot can connect; it does not approve outreach, alerts, or automated replies.

## Validation

Pass when:

- Desktop package builds without error.
- Desktop launcher can be invoked.
- the intended Hermes profile is mapped to the intended repo/VPS;
- `gateway status` keeps the intended profile gateway running after 30 seconds.
- Gateway logs show Telegram connected and no token rejection.

Fail when:

- Telegram rejects the token for the selected profile.
- The observed gateway belongs to an old repo or different VPS.
- Allowed users are broad or unset.
- The gateway starts and exits repeatedly.
- A test message would be sent without a human-approved approval packet.
