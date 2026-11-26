# fresh-code

A [Hermes Agent](https://github.com/NousResearch/hermes-agent) skill that
makes Hermes write **complete, up-to-date code**: it checks the installed
dependency versions and their current documentation before coding, writes
every required file without placeholders, and runs the project's own checks
before reporting success.

## Install

Direct from this repository (Hermes resolves `owner/repo/path`):

```bash
hermes skills install siavashmirtaheri/hermes-fresh-code/fresh-code
```

Or add the repo as a tap and browse it as a source:

```bash
hermes skills tap add siavashmirtaheri/hermes-fresh-code
hermes skills search fresh-code --source github
```

Then invoke it with `/fresh-code <your coding task>` or stack it with other
skills, e.g. `/fresh-code /test-driven-development implement the auth flow`.

## What is inside

```text
fresh-code/
├── SKILL.md                              # main instructions
├── references/
│   ├── version-checks.md                 # grounding in installed versions
│   └── completeness-checklist.md         # "done" criteria
└── templates/
    └── implementation-report.md          # final report shape
```

## Why a skill, not a plugin

This skill changes *how the agent authors code*; it does not need a runtime
hook. Hermes skills are loaded on demand, so its instructions only consume
context when the user invokes `/fresh-code` or the agent selects it.

## Tests

Structural checks (stdlib only):

```bash
python -m unittest discover -s tests -v
```

## Author

Siavash Mirtaheri (BlackVash) — 2026. MIT license.
Backed by [Metadigi](https://metadigi.ir) — https://metadigi.ir
