# Code review quality

Complete rules already supplied or read from this build satisfy references to
code-review.md. Retain them; do not reread unchanged copies.

Every code review must assess these aspects within its assigned scope before
approving code or reporting no findings:

1. Simplicity: Check unnecessary behavior, state, layers, ownership or data flow
   and simpler solutions that preserve the required behavior and guarantees.
2. Loops and recursion: Check whether a claimed input can reach the code. If
   actual bounds exclude it, reject that failure attribution. Always trace
   loops, recursion and collection scans for reachable inputs; identify what
   grows and repeats. Nested loops or recursion alone prove
   no defect. Disjoint traversals or one bounded visit per item can be linear;
   a small fixed bound or work required by the result can justify the algorithm.
   Report avoidable quadratic, exponential or comparable work when its concrete
   consequence warrants a correction and an equivalent lookup, pass or reuse
   removes it without disproportionate complexity. If only a complexity claim
   is unsupported, correct that claim.
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
missing necessary sources as an evidence gap. Optional alternatives do not
block. An unnecessary mechanism that adds state, work or maintenance without a
required purpose is a concrete defect. Use existing findings and evidence
fields; output no checklist and add no review phase.
