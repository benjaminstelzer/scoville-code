# Machine data

Machine data is output written for programs: test, build and coverage reports
in a structured format such as JUnit XML or JSON, log files, JSON or YAML
state, and structured strings embedded in them. This holds whether it arrives as a tool result, a saved file or failure output. Evaluate it in code and show
the checked result. Raw records fill the context with values nobody reads and
bury the few that decide something. A test runner's console summary, such as
its pass and fail counts with the failure messages, is written for people:
read it directly.

Classify by purpose and content, not by filename or size. Illustration:

| Item | Treat as |
| --- | --- |
| A `package.json` or YAML configuration the change depends on | Source: read it directly. |
| Source excerpts, search matches, a source diff, targeted `git status` | Source: read it directly. |
| A compiler error or stack trace for the failure being fixed | Prose diagnostic: read it in full. |
| A JUnit XML, a JSON lint or coverage report, a tool's saved state, a log file | Machine data: parse, check and report the checked result. |
| A JSON object inside a log line or message string | Machine data, even in a short result. |

A report stays machine data when someone renames or edits the file.

When you can run commands:

1. Parse all data the next decision needs. Before you write a filter or
   assertion, take field names, types and actual values from the data and the producer's schema or documented format. A guessed literal silently matches
   nothing: `status == "failed"` finds no row when the tool writes `FAILED`.
   For an unfamiliar schema, first print field names, types and collection
   sizes, not records or values. Parse a string as embedded data only where
   its established format requires it.
2. Run the required checks over all of it, not a sample. A sample cannot
   show absence, and a successful parse is not a result. Narrowing to what the
   decision needs is not sampling. A parse error, missing required field,
   wrong type, unsupported format or unknown or contradictory meaning leaves
   the check unresolved. Treat and report it as unresolved, never as a pass or
   a permission. Different
   wording with the same established meaning is a defect only where exact values are
   binding.
3. Print what was checked, the processed count and, where the producer
   states one, the expected count, and every
   deviation with its identity, expected and actual value and complete
   diagnostic text. Print identical diagnostics once with their count and
   scope; keep distinct ones apart. Do not print subtrees or state strings
   instead. Show a control value only where the check or its explanation needs
   its established meaning; stored payloads are not control values. Compare
   structured values, including state before and after, in code; do not print
   both. On a parser failure report the location and reason, not the input.

Prose inside the data still counts as prose: read messages, diagnostics and
schema descriptions in full where their wording matters.

When a native tool shows its data before any code can process it, use the
tool's own filters to fetch only what you need. Without command permission,
ask a caller that has it or report the missing capability.

When the producing command has an effect or cannot be repeated, save its
original output before evaluating it, so that a bug in the evaluation never
forces a rerun; [output delivery](output-delivery.md) has the capture call.
Fitting the display limit does not turn machine data into prose.
