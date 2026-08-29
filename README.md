# discuss

Private APM package: `sergio-sisternes-epam/discuss`

Grok-native layout: `SKILL.md` and `apm.yml` at the repository root.

```text
apm install sergio-sisternes-epam/discuss
```

Process memory is **not** authored in this skill package. Canonical store:

https://github.com/sergio-sisternes-epam/discuss-atlas

That store’s git root **is** the OKF root (`SCHEMA.json` at the store root, not nested `atlas/SCHEMA.json`). Check it out as the `references/atlas` git submodule (see `.gitmodules`). After clone:

```text
git submodule update --init --recursive
```

Or mount:

```text
atlas mount github.com/sergio-sisternes-epam/discuss-atlas --ref main --target references/atlas
```

Mount path = compile/query root: `references/atlas` (not `references/atlas/atlas`)

See `SKILL.md`.

## License

Apache-2.0. See `LICENSE`.
