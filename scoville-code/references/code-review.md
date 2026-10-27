# Code review quality

Complete rules already supplied or read from this build satisfy references to
code-review.md. Retain them; do not reread unchanged copies.

Every code review must assess these aspects within its assigned scope before
approving code or reporting no findings:

1. Simplicity: Check unnecessary behavior, state, layers, ownership or data flow
   and simpler solutions that preserve the required behavior and guarantees.
2. Loops and recursion: Trace them through relevant callees, including built-in
   or library calls that scan a collection. Identify what grows with input and
   what is processed repeatedly. Report avoidable quadratic, exponential or
   comparable repeated work when an equivalent lookup, pass or reuse removes it
   without disproportionate complexity. Nested loops or recursion alone prove
   no defect. Disjoint traversals or one visit per item can be linear when each
   visit does bounded work. A small fixed bound or work required by the result
   can justify the algorithm.
3. Maintainability and extensibility: Check clear responsibilities and whether
   foreseeable changes fit the structure without unnecessary coupling or
   duplicated policy. Do not demand abstractions for hypothetical needs.
4. Clarity for later agents: Owners, contracts, data flow and dependencies must
   be understandable from code and project records without chat history.

Use code inspection for the algorithmic check, not benchmarks or extra test
runs. This is not a general performance, memory, I/O or cache-tuning request.
Fewer lines alone prove no improvement. Preserve distinct responsibilities,
required guarantees and diagnostics; require no routine comments.

Do not approve with an unassessed aspect or unresolved material finding. Report
missing necessary sources as an evidence gap. Optional alternatives without a
concrete defect do not block. Use existing findings and evidence fields; output
no checklist and add no review phase.
