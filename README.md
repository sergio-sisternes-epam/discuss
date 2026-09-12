# discuss

Private APM package: `sergio-sisternes-epam/discuss`

Grok-native layout: `SKILL.md` and `apm.yml` at the repository root.

```bash
apm install sergio-sisternes-epam/discuss#v0.3.10 --target agent-skills
```

Supported validation targets are `agent-skills`, `copilot`, and `claude`.
Private installs need a GitHub credential with Contents: read access to
`discuss`, `atlas`, and `okf`; in CI, expose it as
`GITHUB_APM_PAT_SERGIO_SISTERNES_EPAM`.

Pull-request workflows never receive this credential. Private dependency and
store validation runs locally on the reviewed head and remotely only from
trusted `main` or an exact-main release tag. Fork changes must first be
reproduced on a trusted branch.

## Discussion store

Process memory is **not** authored in this skill package. Its canonical store is:

https://github.com/sergio-sisternes-epam/discuss-atlas

The store's git root is the OKF root (`SCHEMA.json` is at the store root).
In a source checkout, initialise the pinned mount:

```bash
git submodule update --init --recursive
```

APM does not materialise git submodules. In a consumer repository, use the
Atlas skill to mount the private store without a custom target, then resolve
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

See `CONTRIBUTING.md` for validation, release, private-token, and failed-tag
procedures.

## License

Copyright 2026 Sergio Sisternes.

Apache-2.0. See `LICENSE`.
