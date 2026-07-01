---
name: playbook-common
description: Shared skill-resolution rules and dependency catalog for TeckTinkerere agent-skill-routers playbooks. Load when a playbook references a missing child skill or when installing playbook dependencies.
---

# Playbook common

Read-only reference skill. Do not replace situational playbooks.

## Files

- [resolution.md](references/resolution.md) — where skills live, how to load them
- [skill-catalog.md](references/skill-catalog.md) — install commands for every child skill

When any playbook says "install missing skills", use the catalog.
