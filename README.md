# discuss

Private APM package: `sergio-sisternes-epam/discuss`

Grok-native layout: `SKILL.md` and `apm.yml` at the repository root.

```text
apm install sergio-sisternes-epam/discuss
```

Process memory is **not** authored here. Canonical store:

https://github.com/sergio-sisternes-epam/discuss-atlas

Git root there **is** the OKF root (`SCHEMA.json`). Mount it at `references/atlas` (git submodule, checked in via `.gitmodules`):

```text
atlas mount github.com/sergio-sisternes-epam/discuss-atlas --ref main --target references/atlas
```

Mount path = compile/query root: `references/atlas`

See `SKILL.md`.

## License

Apache-2.0. See `LICENSE`.
