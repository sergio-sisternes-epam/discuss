# discuss

Private APM package: `sergio-sisternes-epam/discuss`

Grok-native layout: `SKILL.md` and `apm.yml` at the repository root.

```text
apm install sergio-sisternes-epam/discuss
```

Process memory is **not** committed in this repo. Canonical store:

https://github.com/sergio-sisternes-epam/discuss-atlas

Git root there **is** the OKF root (`SCHEMA.json`). Mount after that flatten is on `main` (avoids `atlas/atlas` nesting):

```text
atlas mount github.com/sergio-sisternes-epam/discuss-atlas --ref main --target references/atlas
```

Mount path = compile/query root: `references/atlas` (gitignored).

See `SKILL.md`.
