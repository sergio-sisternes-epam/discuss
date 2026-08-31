---
name: discuss/paths/speak
description: Always-on prefix path. Load before any human-facing discuss reply. Owns sentence shape. Not a public mode.
path_id: speak
default: prefix
---

# Path: speak

Mandatory prefix. Discuss has not entered until this file and `references/human-turn.md` are loaded.

## When

Every discuss activation. Live loop, from-conversation, sprout, terminate, lint, consolidate, and constellation all go through speak first when the next output is for a human.

## Enter

Missing load ⇒ `incomplete: missing speak`.

Receipt must include `speak_loaded: yes`.

## Procedure

1. `read_file` this module.
2. `read_file` `references/human-turn.md`.
3. Shape the human reply using that file. Filing the Atlas is separate work.
4. Do not replace the reply with an activation card or a path table.

## Non-goals

- Not a third discussion mode.
- Does not write Atlas pages.
- Does not replace sprout, terminate, lint, or constellation.
- Cannot compile-check stacked sentences. That remains a later test.
