# Machine-data evaluation

Apply this rule before reading or displaying machine reports, logs or structured
state from any producer: direct native results, saved captures and files,
failures, and structured data embedded in strings. It grants no command or
write permission. Instructions, assignments, native finals, binding records and
needed source text remain required prose and must be read completely.

Classify by purpose and content, not filename or size: a needed `package.json`
or YAML configuration is source; a report in that format is result data.
Targeted Git status and plain-text diagnostics may be read directly. Evaluate
embedded objects and report records before display, even in a short result.
Renaming or editing a report does not turn its stored payloads into source.

When commands are permitted:

1. Parse the complete relevant scope in code. Establish fields and types from
   the records and producer contract. For schema discovery, display field names,
   types and collection sizes, not records or values. Establish actual values
   from the data and their meaning from the schema, producer or binding contract
   before writing filters or assertions; do not guess literals. Display a control
   value only when its established meaning is needed for the check or explanation.
   Stored payloads are not control values.
2. Extract and read required prose fully, including diagnostics, messages and
   schema descriptions whose wording matters. Objects, arrays and serialized
   state remain data even inside strings; inspect and compare them in code.
   Parse strings as embedded data only when their established format requires
   it. Catch parser failures before display and report location and reason
   without echoing input or state.
3. Run the required semantic checks over the entire checked scope. Parsing is
   not a result. Unknown or contradictory meanings remain unresolved and prove
   neither success nor permission. Different wording with the same established
   meaning is no defect unless exact values are binding. Parse errors, missing
   required fields, wrong types and unsupported formats prevent a pass.
4. Before executing display code, check its output expressions and emitted
   values against these rules. Compare structured values, including before/after
   state, in code. Emit checked collection/field names, decisive control values,
   results and all relevant deviations, not selected report subtrees or state
   strings. For each deviation, include its identity or property, decisive
   expected/actual values and complete necessary diagnostic text as applicable.
   Group identical diagnostics by count and affected scope; preserve distinct
   conditions. Collection checks report processed and expected counts instead
   of every passing entry. Correct overbroad output expressions before execution
   without printing this self-check.

Do not substitute sampling for a complete check. The relevant scope is what the
next decision requires; narrowing to it is not sampling. Retain the complete
result in evaluating code before emitting checked output. If a native tool
cannot be evaluated in code before display, use its supported filters to obtain
the required scope without raw dumps. Broaden only for a concrete uncertainty.
Without command permission, obtain evaluation from a permitted caller or report
the missing capability; read required prose fully.

Capture and size checks govern transport, not eligibility for display. For
potentially large output, limited transfers or nonrepeatable effects, use
[output-delivery.md](output-delivery.md). Preserve the original result before
evaluation so evaluator failure never requires repeating an effect.
