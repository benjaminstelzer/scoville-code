# Conventions for a wholly new project

These conventions organize a wholly new project. Read the applicable
instructions and inspect the root for an existing layout first: new modules,
empty subfolders, refactors and individual missing rules follow the
organization their project already has.

## Choose the applicable convention

Apply user and project requirements first, then the chosen ecosystem's official
conventions, then the general fallback for remaining choices.

If an already applicable global or project `AGENTS.md` or
`CLAUDE.md` explicitly
directs you to user conventions, read that exact file; resolve relative paths
from the directing file's directory. Read only that named file; an incidental
mention of conventions is not such a direction. User conventions shape
organization and naming only. Project-specific rules override personal
defaults unless the user directs otherwise. If required conventions are
unreadable, report their exact path and leave the choices that depend on them
open, because the bundled defaults are what the user chose to replace.

## Follow the ecosystem

Preserve required entry points, manifests, configuration names and casing.
Use the selected stack's official guide when conventions are needed; if
unavailable, use authoritative local guidance and state material uncertainty.
Choose target runtime and dependencies from the request and stack requirements,
not merely the installed runtime. Respect lockfiles or pinning; prefer native
or existing checks and provide one usable check. Keep or create a README with
actual prerequisites, setup, usage, startup and check commands when needed.

## Minimal general fallback

When no project or ecosystem requirement determines layout, use:

```text
project/
  src/          product source
  tests/        tests not colocated with their source
  docs/         maintained project documentation
  scripts/      project build and development tools
  README.md
  .gitignore
```

Create directories with their first needed content. Keep manifests at required
locations and planning records with their existing owner.

Group related source by feature or domain, preserving real responsibility
boundaries and test discovery conventions. Use descriptive English `kebab-case`
for freely chosen general directories/documents; retain ecosystem casing and
conventional names such as `README.md`. Avoid spaces, reserved names, case-only
distinctions and names such as `new`, `final` or numbered backup fragments.

Use conventional build outputs and exclude generated output, secrets, caches
and temporary evidence from source/version control unless distribution requires
them. Create no universal `development/` or `releases/` wrapper. Record only
non-obvious conventions needed by later work in existing project documentation.
