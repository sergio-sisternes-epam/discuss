---
name: discuss/paths/checkpoint
description: "Use this path when the human wants a checkpoint, a point in time, or a summary of every node in the current discussion, including when they ask where the whole graph is right now or to capture all of it before a new branch. Write one dated index of all nodes and do not judge them. Do not use this path for what stands, what is set aside, a selective picture, a walk-back, or parking a leftover."
path_id: checkpoint
---

# Path: checkpoint

## When

The human asks for a checkpoint, a point in time, or a summary of every node
in the current discussion. Do not use this path for what stands, a picture of
the pieces, a walk-back, or parking this for later.

This is not a consolidate view, not a synonym of constellation, and not an
approval gate. Do not load consolidate. Do not use the headings standing,
set aside, or still open.

## Enter

Discuss card plus:

```text
path: checkpoint
path_module: references/paths/checkpoint.md
view_page: <discussion-folder>/checkpoint-YYYY-MM-DD-<slug>.md
node_count: <number of indexed nodes>
```

Speak is already loaded. Reply in prose first; the file path does not replace
the reply.

## Procedure

1. Deterministically enumerate every node in the current discussion: the
   discussion folder of `discussion_root`, including forming, alive,
   deprecated, superseded, and terminated nodes. Use a store listing or Atlas
   search of that discussion. Do not rely on memory, drop exited nodes, or
   filter to important nodes.
2. Write a new `checkpoint-YYYY-MM-DD-<slug>.md` page in the discussion
   folder. Use `type: document`, `kva: alive`, and `checkpoint: true`. Do not
   set `consolidation: true`. Set `created` to the date and `as_of` to a
   timestamp; together they define the point in time.
3. Group the body by `kva`. Write one line per node only: path, type, `kva`,
   title. Do not paste page bodies.
4. Add `relates_to` edges to every indexed node with `kind: indexes`. Also
   add `derived_from` to the discussion hub and `implements` to the work hub
   when one exists.
5. Do not change `kva`, status, or stance on indexed nodes. Do not move
   `discussion_root`. Set `current_branch` to the new page.
6. Run `atlas compile` and require exit 0. Report `node_count`.

## Non-goals

- A new page type beyond `document`
- Body copies, judgement, or implement authority
- Constellation headings or selective indexing
- Treating this as a human-approval gate
