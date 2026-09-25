# Conventions for a wholly new project

Use this reference only for the initial organization of a wholly new project.
First read applicable project instructions and inspect the named project root
for an existing layout. An empty new folder inside an existing project, a new
module, a refactor or missing individual rules is not complete greenfield.
Preserve the established organization in those cases.

## Choose the applicable convention

Project requirements come first. Apply explicit user instructions under the
host's authority rules, then the project's prescribed organization and naming.
Use the chosen language or framework's official conventions for remaining
choices. Use the general fallback below only where that ecosystem leaves the
choice open. There is no single industry-standard tree or casing for all stacks.

If the already applicable global or project `AGENTS.md` explicitly directs you
to a user conventions file, read that exact file. Resolve a relative path from
the directory containing that `AGENTS.md`. Do not search for personal files or
treat an incidental path mention as an instruction. The file can customize
organization and naming, but cannot change task permissions, technical loading
requirements or the complete-greenfield boundary. Project-specific instructions
take precedence over generic personal defaults unless the user explicitly
directs otherwise. Missing or unreadable required conventions remain an open
input: report the exact path and stop only organization choices that depend on
it. Do not silently substitute the bundled defaults.

## Follow the ecosystem

Keep required entry points, manifests, configuration names and casing where
the actual toolchain expects them. Use the project's selected stack, not a
framework chosen just to obtain a folder template. Consult the official guide
for that stack when its conventions are needed. If it cannot be reached, use
available authoritative local guidance and state any material uncertainty.

| Ecosystem | Convention and primary source |
| --- | --- |
| Python | Lowercase module names, underscores where useful, such as `invoice_parser.py`. Package names are short and lowercase. See [PEP 8](https://peps.python.org/pep-0008/#package-and-module-names). |
| Angular | Hyphenated files such as `user-profile.ts`, matching `user-profile.spec.ts` tests, related files colocated and directories organized by feature. See the [style guide](https://angular.dev/style-guide). |
| Next.js | Preserve reserved route files such as `page.tsx`, `layout.tsx` and `route.ts`. Follow the chosen router's structure and its supported `src/` option. Next.js permits several organizational approaches. See [project structure](https://nextjs.org/docs/app/getting-started/project-structure). |
| WordPress PHP | For code following WordPress conventions, use descriptive lowercase hyphenated filenames and the class-file convention, for example `class-wp-error.php`. Test-class filenames have their documented exception. See [PHP naming](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/php/#naming-conventions). |
| PHP with PSR-4 | Namespace directories and class filenames must match their declared case, for example `Billing/InvoiceParser.php`. Do not apply WordPress's class-file naming to a PSR-4-loaded class. See [PSR-4](https://www.php-fig.org/psr/psr-4/). |

These are conditional examples, not a stack inventory to apply to every project.
For other stacks, use their corresponding official conventions.

## Minimal general fallback

When no project or ecosystem requirement determines the layout, use:

```text
project/
  src/          product source
  tests/        tests not colocated with their source
  docs/         maintained project documentation
  scripts/      project build and development tools
  README.md
  .gitignore
```

Create a directory only with its first needed content. Place native manifests
and configuration at their required locations. Planning records belong to the
existing planning mechanism and are not created by this fallback alone.

Group source by meaningful feature or domain and keep related files together.
Use technical subdivisions when they clarify an actual responsibility or
boundary. Name files for their contents and tests for the behavior or source
they cover. Follow the selected test framework's naming and discovery rules.

For freely chosen general directories and documents, use descriptive English
`kebab-case` names. Language/module/class files retain their ecosystem's casing
and separators. Preserve conventional names such as `README.md`. Avoid spaces,
platform-reserved names and paths distinguished only by case. Do not use
`new`, `final`, numbered fragments or backup suffixes instead of clear ownership
and version control.

Let build tools use their conventional outputs, such as `dist/`, `build/` or
`target/`, and keep those outputs, local secrets, caches and temporary evidence
out of the maintained source inventory and version control by default. Follow
explicit distribution requirements when generated files must be retained.
Do not create a `development/` wrapper or `releases/` directory as a universal
requirement. Record only non-obvious chosen conventions in the project's
existing instructions or development documentation so later work can reuse them.
