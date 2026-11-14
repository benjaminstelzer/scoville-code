# Conventions for a wholly new project

These conventions organize a wholly new project. Read the applicable
instructions and inspect the root for an existing layout first: new modules,
empty subfolders, refactors and individual missing rules follow the
organization their project already has.

Apply user and project requirements first, then the chosen ecosystem's
official conventions for entry points, manifests, configuration names and
casing, then the fallback below.

If an already applicable global or project `AGENTS.md` or
`CLAUDE.md` explicitly
directs you to user conventions, read that exact file; resolve relative paths
from the directing file's directory. An incidental mention of conventions is
no such direction. User conventions shape organization and naming only;
project-specific rules override them unless the user directs otherwise. If the
named file is unreadable, report its exact path and leave the choices that
depend on it open, because the bundled defaults are what the user chose to
replace.

## Minimal general fallback

```text
project/
  src/          product source
  tests/        tests not colocated with their source
  docs/         maintained project documentation
  scripts/      project build and development tools
  README.md
  .gitignore
```

Create a directory with its first needed content. Name freely chosen
directories and documents in descriptive English `kebab-case`; keep ecosystem
casing and conventional names such as `README.md`. Avoid spaces, case-only
distinctions and names such as `new`, `final` or numbered backups. Create no
`development/` or `releases/` wrapper.

## Structure a person and an agent can extend

Size the structure to the project. Keep the concerns below apart in any
project; a small tool keeps them as functions in one file, and a concern gets
its own module once it outgrows a few functions.

- Keep the entry point thin. It reads arguments or the request, calls a
  function and prints or returns the result.
- Put rules and calculations in functions that take data and return data.
  Their module imports without side effects: no reading of input, argument
  parsing or output at import time, so a test or another agent can call them
  directly.
- Keep file, network and database access at the edge and pass its results to
  the rules.
- Read configuration in one place and pass the values in.
- Write tests for the rules in the ecosystem's conventional place, and a
  README that says how to run the program and the tests and, where there is
  more than one module, what each module holds in one line.
