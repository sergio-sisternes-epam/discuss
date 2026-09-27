---
name: discuss/paths/getting-started
description: First-use orientation for Discuss. Purpose, prerequisites, and the shortest useful first journey. Explain; do not execute.
path_id: getting-started
---

# Path: getting-started

First-use for Discuss. Load when the user is new to Discuss, asks how it works,
or wants a useful first step. This path explains. It does not start a discussion
graph, mount a store, or run another module.

## When

- “I am new to Discuss”
- “How does Discuss work?”
- “What does Discuss do?”
- “How do I start a durable discussion graph?”
- First-use intent clearly about Discuss

Do not steal an unrelated “getting started” task. If the user is not asking
about Discuss, leave this path unloaded.

## Enter

Load path **speak** first. Then emit this card as a fenced `text` block.
Keep `intent` as the user’s learning goal, not an operation to run.

```text
skill: discuss
skill_path: <this skill root>
mode: discussion
subject: discuss
path: getting-started
path_module: references/paths/getting-started.md
intent: Learn what Discuss does and take a first useful step
atlas_id: none
ref: none
strategy: none
atlas_root: none
atlas_target: none
atlas_status: baseline-only
atlas_used: []
help_status: complete
speak_loaded: yes
```

Do not create `discussion_root`. Do not ask for a discussion subject or
objective just to orient. If speak is missing ⇒ `incomplete: missing speak`.

Field contract (same as path **help**):

- `intent` is the learning goal.
- `atlas_id`, `ref`, `strategy`, and `atlas_root` are `none`.
  The card says `atlas_target: none`.
- `atlas_status` stays `baseline-only`. Do not add `atlas_reason`.
  Getting-started does not resolve or consult an Atlas.
- `atlas_used` stays empty. This path does not retrieve from an Atlas.
- `help_status`: `complete` or `limited`.
- Final cards contain no `pending` placeholders.

If this file answers the question, stop. Keep `atlas_status: baseline-only`
and `atlas_used: []`. Do not duplicate an identical card.

## Bundled baseline (this package, this version)

Answers here are for the installed Discuss package. They do not need
`discuss-atlas` to be mounted.

### Purpose

Discuss runs a discussion as a durable, agent-maintained Atlas graph. The
graph is a high-fidelity record and navigation aid. New ideas come from the
human–AI conversation. The graph persists that work, amortises
discarded-session cost, and accelerates human connections.

This package is not for implementation. Autogenesis Discussion mode still
applies when called from Autogenesis: zero implement authority, no product
writes outside the confirmed project Atlas, no discussion-to-implement
short-circuit.

### Prerequisites

1. APM CLI (see `CONTRIBUTING.md` for the version this checkout expects).
2. Marketplace install, not a git-tag install in consumer docs:

   ```bash
   apm marketplace add sergio-sisternes-epam/atlas-marketplace --name atlas
   apm install discuss@atlas
   ```

3. Atlas is the knowledge substrate. Discuss depends on it; do not invent a
   parallel store.
4. Persistence uses the default Atlas of the active project or session.
   That may be branch `atlas` on the project repo, or a dedicated repo
   already registered in the project mesh. Installing Discuss does not
   mount a store. `github.com/sergio-sisternes-epam/discuss-atlas` is the
   own Atlas of the discuss repository only. It is not the write target
   for any other project.
5. A git repository is required before Atlas will persist. Getting-started
   does not create one.

### Shortest useful first journey

1. **Name the work.** A clear subject and a one-line objective. Discuss will
   ask for these when you actually start a discussion, not during this
   orientation.
2. **Project Atlas, when you will persist.** Discuss names the target on
   the activation card. The first live turn asks you to confirm the project
   Atlas. It does not mount the skill store. This path must not run mount
   or resolve as live setup on the user's behalf.

3. **Start discussing.** Ask to discuss the subject with that objective. Discuss
   loads **speak** and `human-turn.md` first, then emits its live card, and
   talks in plain British English. The card names a confirmed known target
   before anything is written. Chat is the shared picture; the Atlas is
   usually invisible.
4. **Let the agent file.** Query first, stay on one conversation orbit, batch
   questions, persist engaged items, sprout leftovers as protostars, compile
   green. You do not file nodes by hand.
5. **Then use module help.** For what each module does, load path **help**.
   No-target help lists the installed registry. Named help explains one
   module without running it.

### Human narration

Every live turn must make visible: where we are after the last pin, what the
live distinction is, what was set aside when that still matters, then the ask.
Activation cards do not replace that prose. Path **speak** owns the register.

## No skill-store enrichment

If this file does not answer the actual question, load path **help**. Do
not `atlas mount`. Do not `atlas resolve`. Do not consult
`github.com/sergio-sisternes-epam/discuss-atlas`. Keep `atlas_target: none`.

Refresh the card **before** the explanation only if the learning goal
changed. Do not replace `atlas_target: none` with a store id.

## Next modules

Point the user at path **help** for the installed registry, then at a named
module if they already know which one they need. Typical next reads:

- **speak** — how Discuss talks
- **from-conversation** — turn talk into fabric
- **sprout** — park a surviving pending
- **terminate** — close a wrong frame

## Non-goals

- Starting a discussion or creating a hub
- Mounting, resolving, or repairing `discuss-atlas`
- Running sprout, terminate, lint, consolidate, or constellation
- Teaching Atlas CLI as if it were Discuss
- Hijacking a getting-started request that is not about Discuss
