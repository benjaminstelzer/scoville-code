---
format_version: 1
id: ADR-0001
status: superseded
created: 2026-08-31
accepted: 2026-08-31
scope: skills/maintainability
superseded_by: ADR-0002
---

# Add maintainable file and module structure as a code standard

## Decision

Scoville Code adds language-independent maintainability rules to the existing
Change reference. Hand-written source files should generally contain no more
than 1,000 physical lines. Stricter project rules take precedence, and coherent
exceptions require justification. The rules also cover domain-based file and
directory boundaries, dependency direction, generator and runtime boundaries,
state and resource ownership, and duplication without speculative abstraction.

## Problem

The current Skill protects scope, ownership, boundary semantics, and evidence,
but it defines no concrete file-size ceiling and offers too little actionable
guidance for file, directory, and module structure. Large catch-all files,
unstructured subsystem sprawl, or purely metric-driven splits can therefore
pass the existing general rules.

## Drivers

- The user selected a 1,000-line ceiling with an exception when no meaningful
  split is possible.
- Adapters, plugins, and data-import functions should have discoverable domain
  areas. Language-level import statements are a separate concern.
- Fluid Base demonstrates useful responsibility boundaries, but also contains
  large generated and hand-written files. Its specific PHP and trait structure
  is not a universal template.
- Professional primary sources support cohesion, small verifiable changes,
  traceable dependencies, and reproducible checks. They do not establish a
  universal file-size limit.
- Fable's Plan review and independent recommendation call for the same
  calibration and warn against duplicate rules and a long textbook checklist.

## Considered alternatives

- Add no concrete limit. This leaves the explicitly named failure mode
  unresolved.
- Require every file over 1,000 lines to be split. This damages generated,
  externally maintained, or coherently indivisible content and expands narrow
  fixes.
- Introduce a new general architecture reference or fixed layer structure.
  This increases loading and maintenance costs and overrides project
  conventions.
- Recommend only a tool rule. Tool defaults differ and have no authority
  without project configuration.

## Consequences

New or substantially changed hand-written files are split earlier at domain
boundaries. Exceeding the limit requires a concrete justification but does not
trigger automatic legacy refactoring. Project rules, target versions, and
runtime contracts remain authoritative. The Change reference becomes larger,
so the addition stays limited to decision-relevant rules and cases. Historical
benchmarks do not prove the changed package.

## Confirmation

The reference names the ceiling, precedence, exceptions, and prohibited metric
tricks. Five evaluation definitions cover the named boundary cases. Package
validation, JSON validation, link checking, diff inspection, and byte
comparison of the local copies confirm only structure and synchronization. A
behavioral test must be run and reported separately as such.

## Revisit when

Real projects repeatedly show that the limit prevents useful changes,
exceptions become arbitrary, the additional reference reduces decision
quality, or a project-native measure demonstrably solves the task better.
