# Version checks

How to ground a change in the version actually installed.

## Find the installed version

- Python: `pyproject.toml`, `requirements*.txt`, `uv.lock`, `poetry.lock`.
- Node: `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`.
- Go: `go.mod` / `go.sum`. Rust: `Cargo.toml` / `Cargo.lock`.
- Prefer the lockfile over the manifest: the manifest may declare a range,
  the lockfile records what is really installed.

## Check the docs for that version

- Use a docs tool (Context7) pinned to the library name and version when
  available; otherwise read the official docs site or the tag in the library's
  repository matching the installed version.
- Confirm: function/class signatures, required arguments, configuration keys,
  return types, and any deprecation or replacement notes.
- If only docs for a newer major version exist, do not extrapolate backwards.
  State the version gap and ask before upgrading.

## Record what you verified

Keep a short note during the task: `library@version — signature/key — source`.
It becomes the "APIs verified" part of the final report and lets the user
re-check your work quickly.
