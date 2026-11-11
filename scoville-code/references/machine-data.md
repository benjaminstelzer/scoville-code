# Machine data

Machine data is output written for programs: test, build and coverage reports,
logs, JSON or YAML state, and structured strings embedded in them, whether it
arrives as a tool result, a saved file or failure output. Evaluate it
in code and show the checked result, because raw records fill the context with
values nobody reads and bury the few that decide something.

Classify by purpose and content, not by filename or size. Illustration:

| Item | Treat as |
| --- | --- |
| A `package.json` or YAML configuration the change depends on | Source: read it directly. |
| Source excerpts, search matches, a source diff, targeted `git status` | Source: read it directly. |
| A compiler error or stack trace for the failure being fixed | Prose diagnostic: read it in full. |
| A JUnit XML, a JSON lint or coverage report, a tool's saved state, a log | Machine data: parse, check and report the checked result. |
| A JSON object inside a log line or message string | Machine data, even in a short result. |

A report stays machine data when someone renames or edits the file.

When you can run commands:

1. Parse the whole scope the next decision needs. Take field names, types and
   actual values from the data and the producer's contract before writing a
   filter or assertion, because a guessed literal silently matches nothing. For
   an unfamiliar schema, print field names, types and collection sizes first,
   not records or values. Parse a string as embedded data only where its established
   format requires it.
2. Run the required checks over that whole scope rather than a sample; a
   sample cannot show absence, and a successful parse is not a result.
   Narrowing to what the decision needs is not sampling. A parse error, missing
   required field, wrong type, unsupported format or unknown or contradictory
   meaning leaves the check unresolved, which is neither a pass nor a
   permission. Different wording with the same established meaning is a defect
   only where exact values are binding.
3. Print what was checked, processed and expected counts, and every deviation
   with its identity, expected and actual value and its complete diagnostic
   text. Group identical diagnostics with their count and scope and keep
   distinct ones apart, rather than report subtrees or state strings. Show a
   control value only where its established meaning is needed for the check or
   its explanation; stored payloads are not control values. Compare structured
   values, including before and after state, in code rather than printing
   both. On a parser failure report the location and reason, not the input.

Prose inside the data still counts as prose: read messages, diagnostics and
schema descriptions in full where their wording matters.

When a native tool returns data that cannot pass through code before it is
shown, use the tool's own filters to fetch only the needed scope. Without
command permission, ask a caller that has it or report the missing capability.

When the producing command has an effect or cannot be repeated, save its
original output before evaluating it, so that a bug in the evaluation never
forces a rerun; [output delivery](output-delivery.md) has the capture call.
Fitting the display limit does not turn machine data into prose.
