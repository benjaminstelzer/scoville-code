---
format_version: 1
id: ADR-0002
status: accepted
created: 2026-08-31
accepted: 2026-08-31
scope: skills/maintainability
supersedes: ADR-0001
---

# Use Checkstyle's 2,000-line value

## Decision

Scoville Code uses a general ceiling of 2,000 physical lines for hand-written
source files. Stricter project rules continue to take precedence. The existing
exceptions and safeguards against metric gaming and unrequested legacy
refactoring remain in place.

## Problem

The previously selected ceiling of 1,000 lines no longer reflects the current
user decision. The requested value is the configurable 2,000-line default from
Checkstyle FileLength.

## Drivers

- The user explicitly selected 2,000 lines.
- Checkstyle documents 2,000 as the default value of its configurable
  FileLength check.
- File size remains a maintainability signal. Cohesion, project precedence,
  and concrete exceptions still determine whether a split is useful.
- A single tool value is not presented as a universal industry standard.

## Considered alternatives

- Keep the previous 1,000-line limit. This contradicts the new user decision.
- Replace every project limit with 2,000. This would override stricter binding
  project conventions.
- Remove the size rule entirely. This would leave the previously confirmed
  maintainability failure mode ungoverned again.

## Consequences

Hand-written files between 1,001 and 2,000 lines no longer require an exception
solely because of the Scoville rule. A clear domain split can still be useful
earlier. Existing files over 2,000 lines are not refactored automatically.
Historical Plan and Decision records retain the 1,000-line value that applied
at the time.

## Confirmation

The active Change reference and current documentation must name 2,000 at the
locations relevant to the rule. Boundary cases must be above 2,000. Package,
JSON, link, and synchronization checks must pass. Fable then reviews the
finished Skill read-only.

## Revisit when

The user selects another value, a binding project limit takes precedence, or
real use shows that the limit does not achieve the intended maintainability
effect.
