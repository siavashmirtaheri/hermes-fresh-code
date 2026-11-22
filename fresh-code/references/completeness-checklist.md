# Completeness checklist

Run this before saying a code change is done.

- [ ] Implementation exists for every branch of the requested behaviour.
- [ ] Registration / wiring / exports updated where the project requires it.
- [ ] Configuration defaults and examples updated if a new setting was added.
- [ ] Tests cover the happy path and at least one failure/edge path.
- [ ] Error messages are explicit and do not leak secrets or internal paths.
- [ ] No `TODO`, `FIXME`, `pass`-only bodies, `NotImplementedError`, or
      commented-out placeholder code remains.
- [ ] No unrelated files were reformatted or rewritten.
- [ ] Tests, type checker and linter were run; failures were fixed or reported.
- [ ] Final report lists changed files, verification commands and outcomes.
