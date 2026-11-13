# Change Workflow

SKILL.md covers an ordinary change. Read the section for your situation. A
review of the result uses [Code quality](code-quality.md).

## Changing something other code consumes

For a changed symbol, format or public behavior, locate the directly affected
callers, registrations and test doubles. Exercise each contract variant the
change affects independently, for example both registered consumers of a
renamed field and the stale test double. One real consumer is enough when
inspection finds a single variant. Unrelated callers and neighbouring modules
need no inventory.

## Reusing a path built for another operation

An existing path fits when it produces the requested result and keeps every
guarantee that holds whichever path is taken: authorization, protection of
other data, required persistence. A step the old path performs only for its
own operation does not become required through reuse; if it blocks the
request, separate it. Example: removing a feature's records needs the
permission check and the protection of foreign records, not the checks that
only served displaying that feature.

## Adding a package

Before installing a new direct package, verify its exact name and source
against the official project documentation.

## Helpers, scripts and prompts for agents

Keep required inputs few and give an invocation the agent can run as written.
Successful output must work in its next consumer without repair. An error
names the bad argument or condition, the expected format or allowed values
and the next action.

## Searching a large tree

Start from the paths the request names; otherwise select candidate paths
before searching contents. Leave browser profiles, generated artifacts and
raw traces out of ordinary searches unless they are named or implicated, and
filter a large source for the needed field instead of printing it. Stop
exploring when the responsible source, the affected behavior and the deciding
check are known.
