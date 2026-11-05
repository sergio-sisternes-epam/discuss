# Discuss

Discuss turns a human–AI conversation into a durable, agent-maintained Atlas graph that records the reasoning and helps navigate related ideas.

## Why / what this is not

The graph is a high-fidelity record and navigation aid; new ideas come from the conversation. Discuss is not an implementation workflow and does not store process memory in the skill package. For live discussion, it uses the active project's or session's Atlas, whose target must be confirmed before writing.

## Modules

| Module | What you get |
| --- | --- |
| Getting started | First-use orientation and a useful first journey. |
| Help | Explain Discuss modules without executing them. |
| From conversation | Turn a live or past conversation into graph fabric. |
| Sprout | Park a surviving pending idea as a protostar linked to its origin. |
| Terminate | Close a wrong frame with an exit reason and a living thesis. |
| Lint | Check graph discipline against the KVA contract. |
| Consolidate | Create a partial dated view of the pieces. |
| Constellation | Join what stands into one official picture. |
| Checkpoint | Index every node at a point in time. |

## Install

```bash
apm marketplace add sergio-sisternes-epam/atlas-marketplace --name atlas
apm install discuss@atlas
```

## Use

Start a live discussion with a clear subject and objective:

```text
I need to discuss with you the following idea: <clear subject>. Objective: <one line>.
```

For orientation without starting a live discussion, ask: `What can Discuss do?`

## Prerequisites

The package depends on Atlas. Live discussion requires an active project or session Atlas target; Discuss asks the operator to confirm the target before writing. Help and getting-started are explain-only and do not mount or write to an Atlas.

## Related

- [Atlas marketplace](https://github.com/sergio-sisternes-epam/atlas-marketplace) — package catalog.
- [`atlas`](https://github.com/sergio-sisternes-epam/atlas) — knowledge substrate used for live discussion.
- [`autogenesis`](https://github.com/sergio-sisternes-epam/autogenesis) — skill design process with a separate discussion authority boundary.
- [`think`](https://github.com/sergio-sisternes-epam/think) — companion thinking primitives.
- [`SKILL.md`](SKILL.md) — runtime contract, target-confirmation rules, and module paths.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Report vulnerabilities through a private GitHub security advisory rather than a public issue.

## License

Copyright 2026 Sergio Sisternes. Licensed under [Apache-2.0](LICENSE).
