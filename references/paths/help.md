---
name: discuss/paths/help
description: Explain Discuss modules without executing them. List the installed registry, or explain one named module from bundled references. Do not consult the skill store.
path_id: help
---

# Path: help

Explain Discuss. Do not execute Discuss. Load this module for discovery or
for a named-module explanation. Reading another module to explain it is not
permission to run that module.

## When

In Discuss context only:

- no target: “help”, “what can Discuss do?”, “list modules”
- named module or topic: “explain terminate”, “what does sprout need?”
- unknown name: “help frobnicate”

Do not require a clarifying question just to list the registry.

Unqualified “help” outside Discuss context must not activate this skill or
hijack an unrelated task. “Terminate this branch” is path **terminate**, not
help. “Help me centre this CSS” is not Discuss.

## Enter

Load path **speak** first. Then emit this card as a fenced `text` block.
`path` stays `help` even when the topic is another module. `intent` is the
learning goal.

No-target example:

```text
skill: discuss
skill_path: <this skill root>
mode: discussion
subject: discuss
path: help
path_module: references/paths/help.md
intent: List every installed Discuss module
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

Named-module example (still path help):

```text
skill: discuss
skill_path: <this skill root>
mode: discussion
subject: discuss
path: help
path_module: references/paths/help.md
intent: Understand how terminate works without terminating a branch
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

Do not emit `path: terminate` (or sprout, or from-conversation) for an
explanation. Do not create `discussion_root`. If speak is missing ⇒
`incomplete: missing speak`.

Field contract:

- `intent` names the user’s learning goal, near the top.
- `atlas_id` / `atlas_root` name the write target. Help has none.
  The card says `atlas_target: none`. Never name the skill store
  `github.com/sergio-sisternes-epam/discuss-atlas`. Never fabricate a mount path.
- `atlas_status` stays `baseline-only`. Keep `atlas_root: none`.
  Do not add `atlas_reason` for the skill store.
- `atlas_used` stays empty. Help does not retrieve from an Atlas.
- `help_status`: `complete` or `limited` on the final card. No `pending` on
  the card that accompanies the answer.
- If bundled references suffice and no retrieval occurred, the baseline-only
  card is enough. Do not duplicate identical cards.
- Card, citations, and prose must agree.

## Installed registry (bundled)

This table is the no-target answer. It matches the path registry in
`SKILL.md` for this package version. One line each. Do not load every
module file just to list.

| Module | Purpose |
|--------|---------|
| **getting-started** | First-use: purpose, prerequisites, shortest useful first journey |
| **help** | Explain modules without running them |
| **speak** | Always-on prefix; human narration before any human-facing reply |
| **from-conversation** | Turn a live or past conversation into graph fabric |
| **sprout** | Park a surviving pending as a protostar linked to its origin |
| **terminate** | KVA-terminate a wrong frame; write exit-reason; link living thesis |
| **lint** | Check fabric discipline. L1 hubs; L2–L6 KVA contract |
| **consolidate** | Partial dated view; stance edges. Informal: walk-back |
| **constellation** | Join cadence. Official picture of what stands. Synonym: checkpoint |

Aliases for lookup only: walk-back, walk back, picture of the pieces, gaps and contradictions → **consolidate**; checkpoint, join what stands → **constellation**.

After the list, say the user can ask for any one module by name. Do not
ask which to list.

## Named module or topic

1. Map the utterance to one `path_id` in the registry (or an alias above).
2. If it does not match, say it is unknown and list the valid module names
   from the registry table. Do not invent flags, CLI verbs, or extra modules.
3. Load **only** that module file (`references/paths/<path_id>.md`), plus
   files it explicitly names as required contract (for example
   `references/human-turn.md` when the topic is **speak**, and
   `references/paths/consolidate.md` when the topic is **constellation**).
   Do not load every module.
4. Explain from that source:
   - intent (what it is for)
   - inputs (Enter card fields)
   - prerequisites
   - examples
   - outputs
   - side effects
   - boundaries / non-goals
   KVA values and live-loop rules in `SKILL.md` override stale wording in a
   module file. The current enum is `forming | alive | deprecated |
   superseded | terminated`. Do not present `keep`, `expand`, or any other
   extra `kva` symbol as current capability.
5. Stop if that file answers the actual question. Set
   `atlas_status: baseline-only`, `atlas_used: []`, `help_status: complete`.

Topic overlap or fluent general knowledge is not enough. Mechanics do not
always explain design rationale. A partial answer is a gap.

## Explain, do not execute

Help never:

- mutates the discussion graph (no pages, edges, KVA writes, sprouts, exits)
- mounts, inits, installs, authenticates, or repairs Atlas
- runs from-conversation, sprout, terminate, lint, consolidate, or constellation
- compiles, remembers, commits, or pushes
- creates a hub because `discussion_root` is missing

Reading `references/paths/terminate.md` to explain terminate is not a
terminate ramp. Same for sprout and from-conversation.

## Bundled baseline first

Ship and use versioned references in this package. Help must work with no
Atlas mounted. If the loaded references answer the question, stop. Do not
enrich from the skill store.

## No skill-store enrichment

Do not `atlas mount`. Do not auto-mount. Do not `atlas resolve`. Do not `atlas search`. Help must work with no Atlas mounted. The skill store is
not a help source. A partial bundled answer stays `help_status: limited`
and `atlas_target: none`. Do not add `atlas_reason` for a store that must
not be queried. Never mount, authenticate, install, repair, or publish
just to answer help.

## Non-goals

- A second catalog skill named help
- Visualise / Cartograph (out of scope for this package)
- Hijacking unqualified help outside Discuss
- Replacing speak, or running the live discuss loop
- Schema overlays or curated `help/` articles in this change
