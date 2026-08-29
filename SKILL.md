---
name: discuss
description: Use this skill to run a durable discussion about a clear subject as an agent-maintained Atlas graph. Trigger on discuss, discussion graph, one idea at a time, grow the graph, KVA this branch, persist this discussion, fail-fast this thesis, terminate this branch, wrong comparison, KVA terminate, walk back, consolidate view, picture of the pieces, gaps and contradictions. Complements Autogenesis Discussion mode (authority fence). Not for implement. Persist, prune, and test forming ideas.
metadata:
  version: "0.3.5"
  status: mvp
  work_id: 2026-08-29-discuss-human-narration
---

# Discuss

Run a discussion as a durable, agent-maintained Atlas graph. The graph is a high-fidelity record and navigation aid. New ideas come from the human–AI conversation. The graph persists that work, amortises discarded-session cost, and accelerates human connections.

Process memory is **not** authored in this skill package. Canonical store: `github.com/sergio-sisternes-epam/discuss-atlas`. That store’s git root **is** the OKF root (`SCHEMA.json` at the store root, not nested `atlas/SCHEMA.json`). It is checked in here as the `references/atlas` git submodule (see `.gitmodules`). Compile and query at `references/atlas`.

```text
atlas mount github.com/sergio-sisternes-epam/discuss-atlas --ref main --target references/atlas
```

**Default Atlas root:** `references/atlas`
**Authority fence:** Autogenesis Discussion mode still applies when called from Autogenesis — zero implement authority, no product writes outside this Atlas, no discussion-to-implement short-circuit.

## Enter

Emit before discuss work:

```text
skill: discuss
skill_path: <this skill root>
mode: discussion
subject: <clear subject>
intent: <one line>
atlas_root: <path, default references/atlas>
objective: <original objective>
discussion_root: <atlas-relative path of the starting node>
current_branch: <atlas-relative path of the node we are on>
```

- `discussion_root` is the origin. It does not move.
- `current_branch` moves as the graph expands.
- `objective` stays on the card. KVA always evaluates against it.
- If subject or objective is missing, ask. If root is missing, create a hub page and set both root and current_branch to it.

Then load Atlas via the multi-harness substrate contract (query before write; remember to persist). Do not invent a parallel store.

## Path registry (load before execute)

| path_id | When | Module |
|---------|------|--------|
| **from-conversation** | Turn a live or past conversation into graph fabric | `references/paths/from-conversation.md` |
| **sprout** | Park a surviving pending as a protostar linked to its origin | `references/paths/sprout.md` |
| **terminate** | KVA-terminate a wrong frame; write exit-reason; link living thesis | `references/paths/terminate.md` |
| **lint** | Check fabric discipline. L1 hubs; L2–L6 KVA contract | `references/paths/lint.md` |
| **consolidate** | Partial dated view; stance edges. Informal: walk-back | `references/paths/consolidate.md` |

Default live loop is this SKILL body. Ingest / retrofit / fabric a conversation → read from-conversation first. Park refine / todo / later → read sprout first. User kills a frame → read **terminate** first. from-conversation parks through sprout. After a sprout, terminate, or fabric pass, or on request → read lint first. Consolidate / walk back / picture the pieces / gaps and contradictions → read **consolidate** first.

## Human narration (required)

Load `references/human-turn.md` with the live loop. The human usually cannot see the Atlas. Chat is the shared picture.

- Write in **plain British English**, in **reasonably elaborated sentences** (not telegraphic packets, not essays).
- Assume the user knows discuss terms unless they ask. Jargon is allowed; unexplained jumps in the *graph* are not.
- Every live turn must make visible: where we are after the last pin, what the live distinction is, what was set aside when that affects the picture, then the ask.
- Activation cards and file paths must not replace that prose.

## Process

1. **Query first.** Atlas query on `atlas_root`. Read hub, `thesis/current-reality.md`, and `current_branch`. Report growing (`kva: forming`) vs alive nodes in short form.
2. **One conversation orbit.** Talk on `current_branch`. Do not silently jump nodes. Narrate that orbit per **Human narration**.
3. **Batch, then optional 1-by-1.** Present several questions or counters together. Offer to take them 1-by-1.
   - Batch stay listed on the current node.
   - If the user engages 1-by-1, persist only that item as a new page with edges, then set `current_branch` to it.
4. **Agent maintains the graph.** You write pages, edges, and compile. Do not ask the human to file.
5. **Multiverse.** Branches may co-exist. Mark current reality vs alternative branches in the page body. Contradictions are branches, not defects.
6. **KVA evaluate.** Knowledge Variance Authority. Against the original objective, set `kva` on the branch when its state changes, and on `current_branch` at end of turn — not on every typo persist.
   - Values: `forming` | `alive` | `deprecated` | `superseded` | `terminated`.
   - **forming** — not yet fit for use (typical protostar).
   - **alive** — fit for use; may grow forming children off an origin.
   - **deprecated** — was alive; no successor; do not use.
   - **superseded** — was alive; replaced; do not use.
   - **terminated** — never fit, failed, or out of scope; do not use.
   - Do not delete exit stubs. Do not flip `deprecated` | `superseded` | `terminated` to `forming` on the same page. Reactivation is a new forming page with `derived_from` the stub.
   - Exit ramps require a final node: `type: document`, `kva_role: exit-reason`, `kva: alive`. Subject points at it with `kva_deprecate` | `kva_supersede` | `kva_terminate`. Never embed a reason string field on the subject. **Load path terminate** before executing a terminate ramp (do not improvise the artefacts).
   - Value test: a branch has value iff it moves the locked objective toward a usable distinction (stay alive, grow forming children, or record an exit with a final node). Idle decoration is terminate.
   - Name origin: Marvel Loki TVA (Time Variance Authority). Operational name is KVA. Inception note: `autogenesis/decisions/kva-inception.md`.
7. **Optional consult.** Other Atlases or another view only when lost or when a different point of view would help. Not default. Bound the consult.
8. **Fail fast / prove.** Ideation is not enough. When a claim is stable enough, run a cheap probe (think-challenge, a concrete counter-example, compile/smoke, or a user-named test). Record the result.
   - Failure is information — keep as alive, reshape, or take an exit ramp.
   - No failure yet means direction may be right, not that the thesis is proven.
9. **Lineage.** If the discussion produces a conclusion or action, persist a node that records or is derived_from the originating branches. That is not implement authority.
10. **Sprout pendings.** Anything still pending at the end of the turn (refine, question, counter, probe, tension, action) becomes a `protostar` via path sprout (`kva: forming`). Required origin edge to the conversation node that birthed it. Batch-only bullets are not enough once the item survives the turn.
11. **Compile green.** Every persist ends with atlas compile on `atlas_root` exit 0.

## Graph conventions

Types in use: work, decision, experience, document, protostar.

A **protostar** is a forming idea on the Atlas sky (`kva: forming`, `status: open`, `growth: true`, `star_kind` set). Find with atlas search on `kva: forming` or `growth: true` (the two must match). Every protostar `relates_to` its originating conversation node. Not implement authority. A protostar may later be an exit stub; then `growth` is not true.

Authoritative edges live in frontmatter `relates_to` as path plus kind:

- follows — next step in the same thread
- related — connected, no stronger claim
- derived_from — grown out of
- records — this page records that event
- contradicts — cannot both be current reality
- counters — challenge or opposing idea
- backed_by — research or source that supports
- refuted_by — research or source that cuts against
- kva_deprecate — subject is deprecated; target is the final-reason node
- kva_supersede — subject is superseded; target is the final-reason node
- kva_terminate — subject is terminated; target is the final-reason node
- confirms — this consolidate view takes the idea as standing
- refutes — this view rejects the idea; the page remains
- expands — this view grows or re-scopes the idea
- restates — same claim, tighter wording on the view
- indexes — navigation only; default for protostar gaps
- defers — known, out of this snapshot
- absorbs — folded into another idea named on the view
- feeds — this view is input to a later consolidate view

A page with `consolidation: true` is a partial dated snapshot (`consolidate-YYYY-MM-DD-slug.md`). It is not an L1 hub. KVA on an idea is not changed by a view stance.

Research nodes that ground a counter must carry the external source, then link with backed_by or refuted_by.

`kva` values: forming, alive, deprecated, superseded, terminated.

`status` is page-process only: in-discussion, probed, settled, open. It must not repeat KVA values.

## Non-goals

- Implement product files or Autogenesis implement path.
- Mandatory placement ritual or mandatory cross-Atlas crawl.
- Treating the graph as a thesis engine that replaces conversation.
- Auto-pruning without a recorded KVA decision.
- Wiring discuss into Autogenesis automatically (separate wire path).
- A sixth `kva` value named expand. Alive nodes grow; forming children carry the unfinished work.

## Progressive disclosure

Load via Atlas query or direct read. Do not paste into this file.

- Settled thesis: `references/atlas/thesis/current-reality.md`
- Forming ideas: atlas search `kva: forming` (no concept hub)
- Human chat register: `references/human-turn.md`
- Human chat register: `references/human-turn.md`
- Founding conversation: `references/atlas/founding/hub.md`
- KVA inception: `references/atlas/autogenesis/decisions/kva-inception.md`
- Work hub: `references/atlas/autogenesis/work/2026-08-26-kva-protostar-tighten.md`
