# discuss

Run a discussion as a durable, agent-maintained Atlas graph. Fill the gaps in your thinking with this companion skill that explores the graph for you, finds where they are, and proposes solutions.

## Why / what this is not

The graph is a high-fidelity record and navigation aid. New ideas come from
the human–AI conversation. The Atlas persists that work, amortises
discarded-session cost, and accelerates human connections.

This package is not for implementation. It does not replace conversation with a
thesis engine, and it does not author process memory automatically.

## Install

`--name atlas` is required so the package resolves as `discuss@atlas`.

```bash
apm marketplace add sergio-sisternes-epam/atlas-marketplace --name atlas
apm install discuss@atlas
```

## Use

```text
I need to discuss with you the following idea: <clear subject>. Objective: <one line>.
```

See `SKILL.md` for the runtime contract.

## Modules

| Module | What it does |
| --- | --- |
| Getting started | First-use orientation: purpose, prerequisites, and a useful first journey. |
| Help | Explain Discuss modules without running them. |
| From conversation | Turn a live or past conversation into graph fabric. |
| Sprout | Park a surviving pending as a protostar linked to its origin. |
| Terminate | Close a wrong frame with an exit reason and a living thesis. |
| Lint | Check fabric discipline against the KVA contract. |
| Consolidate | Write a partial dated view of the pieces (walk-back). |
| Constellation | Join what stands into one official picture (checkpoint). |

## Related

- [atlas](https://github.com/sergio-sisternes-epam/atlas) — knowledge substrate this skill depends on.
- [autogenesis](https://github.com/sergio-sisternes-epam/autogenesis) — design process; durable discussion lives here.

A live discussion is stored in the default Atlas of the active project or
session. That may be branch `atlas` on the project repo, or a dedicated
repo the project already registered. Discuss asks you to confirm that
target and names it on the activation card before writing.

[discuss-atlas](https://github.com/sergio-sisternes-epam/discuss-atlas)
is the own Atlas of this repository. It is private. It is not a GitHub
dependency of the installed skill. Agents outside this repository must not mount it, write to it, or open a pull request against it.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

Do not file public issues for vulnerabilities; report them through a private
GitHub security advisory.

## License

Copyright 2026 Sergio Sisternes.

Apache-2.0. See `LICENSE`.
