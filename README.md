# discuss

Private APM package: `sergio-sisternes-epam/discuss`

Grok-native layout: `SKILL.md` and `apm.yml` at the repository root.

```text
apm install sergio-sisternes-epam/discuss
```

Process memory is **not** in this repo. Do not add `references/atlas/` here. Canonical store:

https://github.com/sergio-sisternes-epam/discuss-atlas

OKF root inside that repo is `atlas/` (`atlas/SCHEMA.json`), not git root.

```text
atlas mount github.com/sergio-sisternes-epam/discuss-atlas --ref main
```

Compile/query root: `.atlas/github.com/sergio-sisternes-epam/discuss-atlas/atlas`

See `SKILL.md`.
