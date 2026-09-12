# discuss

Public APM package: `discuss@atlas`

Grok-native layout: `SKILL.md` and `apm.yml` at the repository root.

```bash
apm marketplace add sergio-sisternes-epam/atlas-marketplace --name atlas
apm install discuss@atlas
```

Direct git tag install:

```bash
apm install sergio-sisternes-epam/discuss#v0.3.10 --target agent-skills
```

Supported validation targets are `agent-skills`, `copilot`, and `claude`.
Public github.com installs do not need a consumer PAT.

## Discussion store

Process memory is **not** authored in this skill package. Its canonical store is:

https://github.com/sergio-sisternes-epam/discuss-atlas

That store is All Rights Reserved knowledge, not a secret private GitHub
dependency.

The store's git root is the OKF root (`SCHEMA.json` is at the store root).
In a source checkout, initialise the pinned mount:

```bash
git submodule update --init --recursive
```

APM does not materialise git submodules. In a consumer repository, use the
Atlas skill to mount the store without a custom target, then resolve
the root:

```bash
atlas mount github.com/sergio-sisternes-epam/discuss-atlas --ref main
atlas resolve github.com/sergio-sisternes-epam/discuss-atlas
```

The default mount is
`.atlas/github.com/sergio-sisternes-epam/discuss-atlas`. Always use the path
returned by `atlas resolve` as the compile/query root.

See `SKILL.md`.

## Contributing

See `CONTRIBUTING.md` for validation, release, and failed-tag
procedures.

## License

Copyright 2026 Sergio Sisternes.

Apache-2.0. See `LICENSE`.
