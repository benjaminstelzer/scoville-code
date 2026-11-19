# Change Workflow

SKILL.md covers an ordinary change. Read the section for your situation.

## Changing something other code consumes

For a changed symbol, format or public behavior, locate the directly affected
callers, registrations and test doubles, including independently deployed
readers or writers of shared data. Exercise the affected contract directions
with those consumers: preserve meaning and data, or reject unsupported use
before damage. A producer's own round trip does not check an older consumer.
One real consumer is enough when inspection finds a single contract variant;
unrelated callers and neighbouring modules need no inventory.

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
against the package's official documentation.

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
