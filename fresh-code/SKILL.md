---
name: fresh-code
description: Writes complete, current code by checking docs first.
version: 1.0.0
metadata:
  hermes:
    tags: [coding, code-generation, documentation, verification]
    category: development
---

# Fresh Code

## When to Use

Use when the user asks to write, rewrite, or extend code — especially in a
project with third-party dependencies whose APIs change between releases.
The goal is code that is complete, runnable and aligned with the versions
actually installed, rather than code recalled from stale training examples.

Load this skill together with a test-driven or review skill when the task is
large; stack up to five leading `/skill` tokens in one message.

## Procedure

1. **Establish the ground truth of the project.** Read the manifest and
   lockfile (`pyproject.toml`, `package.json`, `go.mod`, `Cargo.toml`,
   `uv.lock`, `pnpm-lock.yaml`, and so on) to learn the exact language/runtime
   and dependency versions. Read the surrounding source and the project's
   `AGENTS.md` / `README.md` for local conventions before writing anything.

2. **Verify the APIs you are about to use.** For each library that matters,
   consult current authoritative documentation for the *installed version* —
   official docs, the library's own repository, or a docs tool such as
   Context7 when available. Confirm function signatures, configuration keys,
   and deprecations. Do not rely on memory for version-sensitive details.

3. **Check for breaking changes.** Compare the installed version against the
   examples you found online. If docs describe a newer major version, follow
   the docs for the version in the lockfile, or tell the user an upgrade is
   required before using the newer API. Never silently mix versions.

4. **Write the complete change.** Produce every file needed for the feature to
   work end to end: implementation, wiring/registration, configuration
   defaults, and tests. No `TODO`, `pass`, `raise NotImplementedError`,
   placeholder comments or "left as an exercise" gaps. Include input
   validation and explicit error handling at trust boundaries. Keep the
   change scoped to what was asked; do not refactor unrelated code.

5. **Verify before reporting success.** Run the project's own checks — its
   test command, type checker and linter — using the terminal tool. If a
   check fails, fix the cause and rerun until green. If a check cannot run in
   this environment, say exactly which one and why instead of claiming it
   passed.

6. **Report concisely.** List the files changed, the versions/APIs you
   verified, the commands you ran and their outcome, and any remaining risk
   or follow-up the user should decide on.

## Pitfalls

- Inventing an API or parameter name because it "looks familiar" — verify it
  in the docs for the exact installed version first.
- Copying examples from a newer major release into an older project; read the
  lockfile and honour the installed version.
- Adding a dependency without checking whether it already exists in the lock
  file or whether it conflicts with the project's pinned constraints.
- Leaving placeholders, stubs or commented-out sections and calling the task
  done; the definition of done is that the code runs and checks pass.
- Ignoring a failing test or a lint error because it "seems unrelated" —
  report it rather than silently skipping verification.
- Fetching or executing untrusted install scripts just to get a library
  working; ask the user before anything with side effects outside the repo.
- Treating this skill as a substitute for the project's own test suite — it
  guides authoring, it does not replace verification.

## Verification

The change is complete only when:

- every file the feature needs exists and contains no placeholder markers;
- every external API used was checked against documentation for the installed
  version (or the version gap was explicitly reported to the user);
- the project's test, type-check and lint commands were run and passed, or
  their inability to run was stated plainly;
- the final report names the changed files, the verification commands and the
  result of each.
