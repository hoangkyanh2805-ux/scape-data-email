# Hermes Desktop Correct Project Routing

## Problem

Hermes Desktop can show many profiles, sessions, gateways, and remote VPS connections at once. If Desktop is connected through an old SSH gateway, the chat may read the remote machine, old repo, or old profile even when the local CLI profile is correct.

For this repo, the correct local identity is:

- Hermes profile: `scapedata`
- Hermes project: `scape-data`
- Primary folder: `G:\Other computers\My Computer\Project\scape-data`
- Gateway mode for local work: `Local gateway`
- Do not use the old SSH gateway `103.72.97.183` for this repo unless that VPS has a separate `scapedata` checkout and profile.

## Desktop Checklist

Before asking Hermes Desktop to read this project:

1. Open the profile switcher at the lower left.
2. Select `scapedata`, not `default`, `root`, `orchestrator`, `forex-*`, or a remote/VPS profile.
3. Go to Settings -> Gateways.
4. Select `Local gateway` for local repo work.
5. Do not leave `Connect via SSH` selected unless the target VPS is explicitly prepared for this repo.
6. In Workspace or Projects, select `scape-data`.
7. Start a new session after switching profile/gateway. Old sessions may retain old context.
8. Ask a sanity-check prompt before real work:

```text
Bạn đang ở profile nào, project nào, cwd nào? Chỉ trả lời profile/project/cwd, không phân tích.
```

Expected answer must include:

```text
profile: scapedata
project: scape-data
cwd: G:\Other computers\My Computer\Project\scape-data
```

## If Remote VPS Is Required

A remote VPS is valid only when it has its own checkout and profile for this repo.

Required remote setup:

- repo checkout exists on VPS;
- Hermes profile on VPS is named `scapedata` or clearly mapped to this repo;
- remote project points to the repo checkout;
- Telegram token is dedicated to that remote profile, if Telegram is needed;
- AGENTS.md exists in the remote repo checkout.

If those are not true, do not use the SSH gateway for this repo.

## Common Failure Pattern

Wrong routing usually looks like this:

- Desktop shows `root` or a remote host in the bottom bar;
- Settings -> Gateways has `Connect via SSH` selected;
- sessions mention unrelated projects such as Azzam, NCI, forex, old CRM, or old Telegram gateway;
- right panel shows a remote dashboard error from the SSH target.

Fix by switching to `scapedata` + `Local gateway` + new session.
