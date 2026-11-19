# Changelog

## 2026-11-19 - Compatibility before release

- Rule 3 says when a break in compatibility is usually wanted: while a product has not been released. "During development" also described released software that is still being developed.

## 2026-11-19 - Protection nobody asked for is a defect

- Rule 2 opens with the prohibition again: protection, options and bookkeeping nobody asked for are defects, and that something could go wrong is not a need. A use nobody described (a second writer at the same moment, a second window, another process) is a question for the user, neither built nor reported as a defect. In a greenfield test, reviewers reported such cases and authors built locks and stale-data checks for them.
- A remedy for repeated work must not change what the user sees or add state to keep in step: no paging, cache with invalidation or change-tracking flag where once per action is enough.
- "Check, then load again" is about two reads within one operation.
- A review finding is a breach of a rule; further protection or an undescribed case is left out or listed apart as a question. The author holds each finding against the rules and declines one that asks for what rule 2 keeps out.
- A write, a request or a file read can fail in the described use, and its failure reaches the user or the caller. The wording before it ("a failure that does occur") let Opus leave storage write failures unhandled in the recheck. With this sentence both Opus chains of a further run report failed writes and file reads to the user again; Sol was not rerun with it.
- The README shows the test results per model in two tables and describes the independent review as it now applies to every change of code behavior.

## 2026-11-19 - How much structure the code gets

- Rule 2 says what a need is: the request, an input that can reach the code now, another rule, or what the plan and the existing code show is coming.
- Rule 4 now decides both directions of structure in one place, and the author judges it: a shared helper, class, component or interface is wanted where several places do the same thing now or will by the plan, and it keeps module details out of shared code; for a single use the direct code is right. Before, rule 2 read as if generalisation were forbidden and could contradict the module rule. 
- One source of truth is spelled out: a default value, limit, status, list of codes or message is defined in one place, also across server and client and across code and configuration.
- A file, class or function keeps its one responsibility as it grows; a second pattern for a job the project already solves one way counts as a second implementation; a failure that can occur is handled or reported, not swallowed or hidden behind a default. Not tested with models yet.

## 2026-11-18 - Reviewers answer every question

- A reviewer goes through the questions for the finished change in order and states for each one the defects it shows or that it shows none. In a review test on 23 real project changes, reviewers with the Skill listed bugs and repeated work but left the module question unanswered: no review reported module keys in shared code that a change had moved there unchanged.
- The module rule and its question cover code a change adds, moves or extends, also where it lands in shared code or a file that registers and wires. Before, they named new code only.
- The review section names the rules and questions by their headings; "above" pointed at nothing in this package.

## 2026-11-18 - Five rules and a general independent review

- The code rules are five: work that grows, nothing without a need, one implementation, a value loaded again after its check, and state and effects across a change. The first one now says directly that added code is linear only if neither its caller nor what it calls repeats per item, and has the author read upward to the caller and downward into the helpers before adding a loop.
- Compatibility is the user's decision. When a change replaces something, the old form goes in the same change; no fallback, adapter, migration or version switch unless the request or a project rule asks for it. Where something outside the codebase may still depend on the old form and that is open, the author asks.
- When Code runs alone, each change to code behavior gets one independent review by a separate agent that checks it against these rules, starting with repeated work. Under a workflow that already reviews each change, no second review starts.
- Removed: the case traces before the design, the detailed storage rules, the narrow reader with its two questions, and the review table that repeated every rule. Not tested with models yet.

## 2026-11-17 - A reader finding is resolved in full

- A missing check or assignment is added at every place the reader's finding covers. A case the reader describes is one example of the finding. In a measured run an author added the assignment only for the case the reader had described, and the selection was lost in the other.
- What the old path kept and the change drops is restored unless the request or a project rule removes it. Calling the difference deliberate settles no finding; one author had declined a finding that way.
- Not measured yet.

## 2026-11-17 - Shorter workspace rules; a bug fix needs evidence of the defect, not a red run

- The section on commands and workspace boundaries is five sentences. It keeps what a limit covers (redirected output, tool defaults, child processes), the scratch directory chosen before the first command, and cleaning up only the paths the work created.
- A bug fix needs evidence that shows the defect on the supported path, existing or reproduced, and a test that passes with the fix and covers the case. The test no longer has to be written and seen failing first: in three compared tasks that order brought no better result than runs without the Skill. Behavior whose failure is costly still sees its assertion fail without the change.
- A refactoring may reuse a matching result from before the change. A test the project runs separately stays separate and is not wired into another suite.
- The Planning reference is no longer read for an open choice about the product, only for planning records and work across an interruption. References are read in the part that applies.
- Two sentences that only explained where a rule came from are gone, and the README duty for a new project stands once, in the Skill itself.
- None of this is measured yet.

## 2026-11-17 - Findings follow the requested result; rules without a recorded failure removed

- A reader finding is corrected where the requested result relies on the missing check or assignment. Otherwise the author names the line, the guarantee, or the consumer and behavior that show the result does not rely on it, and reports a finding outside the change. That the gap existed before settles nothing. On a fresh task an author had rebuilt a signature for a gap the reader itself called older than the change.
- The written answer on repeated work also names where the final path shares that work, or the code, contract or project rule behind the exception. An author had named a query per item and left it as the existing pattern.
- A test takes its expected result from the request, the project's contract or the established path. A test the author wrote does not turn its expectation into a requirement.
- Removed, because over all compared tasks both models did this right without the Skill or no task ever touched it: the rules on caches and on one source for each fact, the advice on names, single-purpose functions and comments, the test rows for documentation-only changes and for requested failing-first tests, the paragraph on saving durable state, and two report details. The rule against leftovers stays.
- Shared code rules: an unchecked reload is still a defect where the old code had the same gap; whether this change corrects or reports it follows from the affected path.
- None of this is measured yet.

## 2026-11-17 - No paragraph on line endings

- The paragraph on encoding, line endings and Git's conversion notice is removed. On two tasks Sol kept the line endings in all four runs without the Skill and converted files in three of six runs with it, once after the paragraph had been sharpened for exactly that notice. The paragraph made line endings a subject that the models otherwise leave alone. The effect of the removal is not measured yet.

## 2026-11-16 - One independent reading for reloaded values and assigned state

- Where a change reloads a checked value or replaces how state is kept, and the host can start a separate agent, an author has the finished change read once by a reader that knows only the diff and the two questions on reloaded values and on state across a change, and waits for its answer without a timed wakeup. A missing check or assignment is added, or the line or guarantee that covers it is named. Under a workflow that already reviews each change by the shared review rules, no reader starts. This is a trial after measured runs in which authors named the place and argued the check away. A reader with the full review rules was measured as well: authors then also acted on remarks outside the two questions, and two such corrections damaged a correct change.
- No test is handed over failing on purpose unless the request asks for that. An open question about the expected result is asked or reported with the case that shows it.
- Shared review rules: a reviewer answers the questions on reloaded values and on state across a change first, by file and line. A missing line is a finding; a comment or an argument is not such a line.
- Shared code rules: the rule on assigned state names its holder, an element, list or record whose content the new path changes, also when the item the state points to stays untouched.

## 2026-11-16 - Assigned state is set again; a named bound for few items

- Shared code rules: where the old path assigned a selection, a value, the focus or a flag, the new path sets the same value after each of its steps. The author no longer has to judge whether that state can change.
- Shared code rules: a query, request, read or parse per item stays only where code, the contract or a project rule that the author names bounds the real callers to a few items.

## 2026-11-16 - Test the check on a reloaded value

- Where the changed path loads a value again after checking it, a test now covers the check the report names, whether it was found or added: the later load returns a value the first check rejects, and the consumer must not use it. A named guarantee that excludes a change replaces the test.
- For state held by something the new path changes, the test covers the result of the operation that keeps it. A passing test does not replace that operation.
- Shared code rules: the question about a value that is loaded again also covers loads inside the helpers the path calls.

## 2026-11-15 - Reading checks and located questions

- The code criteria are thirteen short rules that are checked by reading the code. They replace the procedure that asked for a proof of the work a whole operation does. Code does not time, benchmark, profile or instrument unless the request or a project rule asks for it.
- Repeated work is judged at the sizes the application's actual callers can pass (ADR-0237). A query, request, file read or parse per item is removed already at modest numbers; work in memory over a few items stays as it is.
- Existing logic is preferred until using it makes the work quadratic on a large collection, repeats a query, read or parse per item, or needs more wrapping than a plain implementation. Then Code writes the simpler implementation, or improves the helper at its owner where a project rule names it.
- State and effects of a path that a change replaces are kept unless the request removes them. State held by something the new path changes, such as a selection or focus, is preserved or restored at each change, and the test covers it also where the author concludes it cannot change.
- A value that is loaded again after a check is checked where it is used, also where the old code had the same gap.
- A filter that narrows candidates before an exact check admits every form the exact check accepts; those forms are read from the check's own parser or matcher.
- An author answers three questions in the final report, each with file and line: work that repeats, values loaded again, and state and effects of a replaced path. In our measured runs these three defects stayed when the questions were only read.
- A defect on the affected path that the requested result depends on is part of the change. Other defects need your go-ahead.
- A change whose result only a rendered interface shows gets no automated test from Code; Scoville UI decides its rendered checks.
- Shared rules: a reply uses the language of the request, while a record or file you edit keeps the language it is written in. Files saved with `--publish-full` are delivered output, so cleanup leaves them in place. A rule that holds only until something happens states that end in the rule.

## 2026-11-14 - Decisions already covered by the request

- Decide routine implementation details within the requested outcome. Ask only for material choices the request and project leave open, including in the shared review rules.
- An explicit contract change supplies its own authority; preserve other guarantees and separate action permissions.
- Correct a known violation of a required guarantee before treating the change as complete. Reporting it does not resolve it.
- Keep the existing test policy; add development cases for these decision boundaries without claiming measured model improvement.

## 2026-11-14 - Goodhart corrections

- Remove examples that repeated our own test tasks; a rule now stands without one where it reads on its own.
- Guards: add one for a case that is reachable in supported use or through a concrete attack path, and do not drop a check at a process or network boundary because the caller on the other side already checks.
- Fail-first: the test has to fail on its assertion, not on a missing name. It applies to a bug fix and to new behavior whose failure would charge a wrong amount, grant access, lose data or open a security hole.
- Report: name the test that proves the request and its result. The lines for reused code, guards and loops are gone, and only a claim about runtime behavior that rests on reading is marked as such.
- Tests: take the proving test's name from the output of the project's own test command, with the runner's verbose flag where needed.
- New projects: keep concerns apart as functions first; a concern gets its own module once it outgrows a few functions.
- Shared rules: a final report after a small change no longer loads the writing reference, a test runner's console summary is not machine data, and a complete copy of a reference in context counts as read.

## 2026-11-13 - Review corrections

- Review: name an unneeded abstraction by what it is for, a second variant nobody asked for, not by a list of forms.
- Ask for a test that fails first only for a bug fix and for behavior whose failure is costly, such as money, permissions, data loss or security. Other new behavior gets a test that is read against the request; a refactoring keeps the existing tests green before and after, and a change without runtime behavior gets the fitting source, type, lint or build check instead of a test.
- Report only what applies: reused code, added guards with their real case, the proving test. No line per function and no label on every statement.
- Ask for the thing instead of a sentence about it: start from the simplest approach and find where a guarded case comes from before adding the guard.
- Replace rule examples that came from our own test tasks with examples from other domains.

## 2026-11-12 - Concrete instructions and release command

- Replace the mode table and general advice with 16 steps for maintainable changes: reuse what the project has, keep one path, use other modules through their public interface, keep one source for each fact, read every loop for work repeated per item, and size safeguards, structure and tests to the request. The loop check is a reading check; it asks for no timing or profiling.
- Require the test that proves a change to fail without it, to sit where the changed rule lives and to run in the project's own test command. The report names that test; "all tests pass" does not count when it was not among them.
- End every change with a check of the diff against the steps and a short proof in the report: what was reused, which guard covers which real case, which test ran.
- Add a review table to the code quality reference that looks for the same defects in someone else's change, with a list of what is not a defect. Each defect is its own finding.
- Lay out a new project by responsibility, with a README that says in one line per module what lives where.
- Activate for building a new tool or project and for adding a feature.
- Cut the member references to half. An ordinary change now reads SKILL.md only.
- Reword the shared writing, machine-data, shell and output-delivery rules the same way.

## 2026-11-11 - Size check for placed components and tested models

- Name the tested models and the minimum reasoning effort in the README.

## 2026-11-10 - Leaner instructions and Plan validator fixes

- Link the shared writing, machine-data, shell, output-delivery and Python references directly from SKILL.md, each with its reading condition, instead of chained read-first rules.
- Shorten the shared rules: drop permission disclaimers that have no recorded incident and state scope and reason for the stop rules that remain.
- Reduce output delivery to when the checker is needed, its three calls and how to read a result. Every capture failure now names its next step in the helper's `instruction` field.
- Add short illustrated examples for material choices, needed protection and machine data, and show in one table what each kind of request authorizes.
- Name diagnosis of failing tests, builds and commands in the description so the Skill activates for them.

## 2026-10-30 - Source reading and UTF-8 diagnostics

- Clarify direct source reading and producer-owned instruction-design loading while preserving report evaluation.
- Explain retained bytes, child status and unresolved text interpretation after invalid UTF-8.
- Remove redundant layout wording without changing activation or sibling requirements.

## 2026-10-30 - Capture and diagnostic follow-up

- Load Code quality for implementation recommendations as well as implementation and review.
- Capture complete command output without a guessed token limit and preserve primary failure details.

## 2026-10-30 - Shared criteria and focused helper fixes

- Use one Code quality standard before design and acceptance, including justified safeguards, encapsulation and costly loops or recursion.
- Keep standalone family owners explicitly optional and describe the development cycle without individual test reports.

## 2026-10-29 - Capture and rule boundaries

- Preserve original failed capture bytes, use noninteractive EOF and offer an explicit bounded command timeout with honest cleanup status.
- Distinguish source contracts from result data and retain user resolution of equally authoritative rule conflicts in both profiles.

## 2026-10-29 - Development records

- Remove an obsolete research report and its development-index link; retain current Skill and test sources.

## 2026-10-29 - Follow-up corrections

- Restore disputed-conclusion and shell/data reading routes; limit new protection to justified needs and retain scope, idioms and explicit authorization in reviews.

## 2026-10-29

- Focus implementation on the simplest sound solution at the responsible owner,
  including shared causes behind recurring workarounds. Scope required review
  to affected code paths, guarantees and avoidable superlinear work.
- Reassess failed repairs from the evidence and continue only with a supported
  next approach, while preserving host attempt limits and independent test
  guarantees. Explain evidenced feasibility limits without claiming success.
- Load machine-data evaluation, interpreter discovery and size-helper guidance
  through their conditional routes. Preserve complete required text, checked
  report output and existing permission boundaries.

## 2026-10-28

- Consolidate outcome guidance, distinguish wording checks from behavior tests,
  and keep unknown check failures unresolved until the evidence identifies their
  cause. Agent-facing reviews use the shared instruction-design rules.

- Keep outcome-based Acceptance rules available in standalone and suite Code packages.

- Assess algorithmic costs within reachable input bounds; correct an unsupported complexity claim without demanding an unnecessary algorithm change.

- Count failures observed during normal supported use, normal-use failures and reachable attack paths as credible; treat other injected faults, constructed interleavings and worst-case inputs only as possible failures, not as a reason for new safeguards. Prefer narrowing a claim or removing the risky state, remove replaced paths in the same change, and require reproduction or a trace through normal supported use or a reachable attack path before fixing audit or review findings.
- Count an unnecessary mechanism with added state, work or maintenance as a concrete review defect.

## 2026-10-27

- Require code reviews to inspect simplicity, maintainability, foreseeable extension and clarity for later agents. Trace loops, recursion and scanning calls for avoidable nonlinear repeated work without requiring benchmarks.

## 2026-10-20

- Keep required text complete when choosing how to read it. File size and metadata remain optional, and completed reads need no verification reread.
- Ground defect claims in requested behavior or an independent contract. Reuse valid evidence, check meaningful preconditions and update superseded result summaries.

## 2026-10-19

- Write reports as compact lists of checked scope, results and relevant gaps. Group equivalent outcomes and refer to existing evidence instead of retelling the run.
- Apply one shared evidence rule in user and agent exchanges: defend supported conclusions, correct demonstrated errors, and respect user decisions without treating them as factual proof.
- Define when an existing pathway fits the requested operation. Preserve shared guarantees without importing conditions from a different purpose.
- Apply the same scope in reviews. Defend supported findings with decisive facts and revise them only for a demonstrated correction to their basis.

## 2026-10-18

- Reuse known results and request only the scope the next decision needs. Narrow direct tool requests before display when code preprocessing is unavailable.

## 2026-10-15

- Process complete reports in code, including saved captures and failures. Load the rules before data, preserve required original text, and keep parser errors from echoing stored state. Evaluate producer output before display, retain one-time results, and distinguish saved captures from missing output.

## 2026-10-14

- Compare nested report data in code and display only decisive results and necessary diagnostics, including structured state stored in text fields.


- Interpret actual report values through their documented meaning. Allow equivalent wording while preserving exact contracts and unresolved outcomes.
- Process machine reports through code before displaying results. Avoid redundant shared-rule reads and keep check reports focused on decisive evidence.
- Parse machine reports completely and display checked facts and all in-scope deviations. Reuse fully read shared rules across Skills without hiding required inputs.

## 2026-10-13

- Load detailed command capture and full-file delivery only when needed. Keep complete output, failure diagnostics and role permissions.

- Check ordinary generated and copied outputs through current creation and
  expected results; use content or hash comparisons for an actual requirement
  or concrete defect, not as a routine gate.

- Keep saved oversized results out of Git status with `.scoville/temp/.gitignore`;
  existing ignore files and tracked files stay unchanged.
- Send oversized results as a file path only; recipients read the whole file
  without hash checks. Save composed text without a separate verification pass.
- Simplify shared writing rules; command-specific size details now live in the
  shell-command rules.

## 2026-10-12

- Return complete command output directly when it fits; save only oversized
  captures. Verify supplied artifacts once and compare saved native Finals
  directly, avoiding repeated hash checks for unchanged text.

- Apply test-expectation criteria to affected existing assertions as well as
  new tests; revise unjustified implementation pins without weakening guarantees.

- Derive test expectations from the required behavior. Use justified bounds for
  internal work and valid measurement; preserve exact contractual guarantees.

## 2026-10-11

- Read required files completely with an agent-chosen method. Remove the document-reading helper and multipart protocol; keep output capture and result delivery separate.

## 2026-10-10

- Load command capture and large-result delivery only when needed; preserve complete outputs and role permissions.
- Remove the obsolete Workflow runner restriction; keep normal Skill selection and role permissions. Load material cost/cache and implementation-review guidance only when relevant.
- Keep agent messages and internal commentary compact. Reference readable source text instead of copying it; preserve required facts and exact controls.
- Keep the full reading procedure in one reference and load host command details when needed. Preserve complete reads and existing permissions.

## v2.1.15 - 2026-10-10

- Reject direct Python script capture before execution with an actionable no-start diagnostic; preserve explicit interpreter calls and source reads.

## v2.1.14 - 2026-10-10

- Save temporary read captures only when the current role and phase permit that specific file. Keep takeover and complete-reading safeguards.

## v2.1.13 - 2026-10-09

- Use exact search paths and keep filename patterns in rg's -g filters. Existing files, directories and regular expressions remain available.

## v2.1.12 - 2026-10-09

- Keep the verified Python interpreter and all required arguments when capturing a helper command. Small direct calls remain available.

## v2.1.11 - 2026-10-09

- Clarify which path runs the reader and which document it reads, including source files from another Skill.

## v2.1.10 - 2026-10-09

- Reuse completed work, unchanged reviewed content and complete passing results. Repeat affected checks only for a relevant change, an unanswered question or a binding protocol.
- Keep process sessions and final failure status visible, preserve reader commands between document parts, and limit guards to their supported scope without weakening required guarantees.

## v2.1.9 - 2026-10-09

- Use a complete reader command when continuing document reads, and an existing directory with a file filter when searching. Prefer direct shell commands for simple file inventories.

## v2.1.8 - 2026-10-09

- Preserve literal arguments and failure status when reading required context. Changed output limits restart the complete read instead of skipping part of the input.

## v2.1.7 - 2026-10-08

- Make scope selection, implementation and proportionate validation easier to follow, with prerequisites and failure stops explicit.

## v2.1.6 - 2026-10-08

- Use a short ordered sequence to locate the relevant code, choose a proportionate check and implement the change.

## v2.1.5 - 2026-10-08

- Diagnose shortened output from the observed failing layer; a later shortened query does not prove that the original capture lost information.

## v2.1.4 - 2026-10-08

- Distinguish Python program files from document inputs and preserve complete output from running command sessions.
- Keep safeguards and validation focused on the actual failure risk. Use Plan field rules for assigned reviews of native planning records.

## v2.1.3 - 2026-10-08

- Read complete bounded UTF-8 text before using it. Capture full command output and its original status before display.
- Verify stateful behavior against the actual application store through its factory and participating processes. Report counts only when they affect a decision.

## v2.1.2 - 2026-10-07

- Keep standalone acceptance focused on distinct necessary results. Put implementation and test execution in subordinate steps while preserving methods and checks explicitly required for acceptance.

## v2.1.1 - 2026-10-07

- Keep Instructions and Evidence focused on future work. Remove duplicated Steps and review transcripts, and handle routine Plan closure without another bookkeeping worker.
- Check complete text before large reads and preserve Python launcher arguments when invoking the size checker.

## v2.1.0 - 2026-10-07

- Keep development ahead of bookkeeping and stop validation after decisive evidence unless a changed behavior or concrete concern calls for more.
- Test observable results. Use source-content checks only for an actual external contract, not to freeze incidental instruction wording.
- Preserve complete text through compaction or a hashed temporary file when it exceeds the known output limit. Offer the separate manual helper procedure only without Python.
- Follow the applicable Codex or Claude Code project rules without copying rules between hosts.

## v2.0.9 - 2026-10-02

- Keep fixes and validation proportionate to the requested result. Reassess repeated failed corrections and add caching only for a concrete benefit.
- Let Handoff own explicitly requested continuation prompts when active, while keeping Code independently usable.

## v2.0.8 - 2026-10-01

- Keep the Change route for high-risk work even when the current request only classifies future work. Reading the route does not authorize implementation.
- Allow bounded local diagnosis while keeping external or durable effects within the user's authorization. Run broad validation only when the task or project requires it.
- Guide new projects through dependency identity, a usable README and focused checks without replacing an existing project's organization.

## v2.0.7 - 2026-10-01

- Recognize Project Context Cleanup as the active owner for requested edits to project rules and index text. Keep engineering work within Code's existing scope.

## v2.0.6 - 2026-09-29

- Check runtime and memory costs before and after implementation, including repeated searches, I/O and recursive work. Keep bounded quadratic work when suitable and prefer simpler alternatives before proposing a cache.
- Use existing caches through their validity and isolation contracts. Ask before adding a new result cache unless already authorized, while allowing ordinary traversal-local indexes.

## v2.0.4 - 2026-09-28

- Scale safeguards to actual consequences and prefer the simplest sufficient failure handling.
- Separate saved results from resumable execution, and keep useful recovery output available without claiming successful persistence.
- Require meaningful safeguard checks at the affected boundary and actionable diagnostics.

## v2.0.3 - 2026-09-27

- Remove the blanket network-access claim from the compatibility description.

## v2.0.1 - 2026-09-26

- Preserve unrelated encoding and line endings during edits, and evaluate each validation command by its own exit status.

## v2.0.0 - 2026-09-25

- Rename the Skill and installation directory to scoville-code.

## v1.0.36 - 2026-09-24

- Keep concrete planning and risk review for high-impact operations in the High risk class when execution is deferred.
- Use Scoville Plan as the record owner only when it is independently available and applicable.

## v1.0.35 - 2026-09-23

- Follow established project conventions for existing code unless they
  conflict with the requested outcome, safety or a binding contract.
- Start Greenfield code with the smallest coherent responsibility-based layout
  and split at real domain, I/O, integration or state boundaries. Keep the
  2,000-line default as a backstop, not an architecture target.

## v1.0.34 - 2026-09-22

- Apply engineering guardrails to Plan entries even when no code changes.
- Make reference selection explicit for implementation, validation and
  risk classification without granting permission to perform deferred work.

## v1.0.33 - 2026-09-20

- Simplify operation routing and stop dependent work when a material decision
  remains unresolved.

## v1.0.32 - 2026-09-20

- Make repository authority, Develop-mode retention, material-choice blocking,
  and durable completion requirements explicit.
- Clarify that discovering another family Skill does not activate it, while
  independently authorized work continues and a user opt-out applies only to
  the excluded Skill.

## v1.0.31 - 2026-09-19

- Bound broad reads before content is returned, and filter required large
  sources locally instead of draining truncated output or listing an entire
  tree.
- Derive boundary expectations from an agreed contract or independent
  consumer, prove negative tests reach the named failure operation, and cover
  every independently affected consumer variant without inventorying unrelated
  neighbors.

## v1.0.26 - 2026-09-12

- Bound source searches and recover only relevant missing output after truncation. Explicitly requested traces and generated sources remain in scope.

## v1.0.25 - 2026-09-11

- Classify purely editorial work by its actual effects even when the request calls it a migration. Real migrations, including audits and dry runs, retain their High risk classification.

## v1.0.23 - 2026-09-10

- Allow a demonstrated cause to justify inspection of related inputs, state, or
  consumers without turning a contained change into a broad rewrite.
- Keep mocked behavior separate from evidence for an actual integration
  boundary.
- Diagnose repeated causal failures across checks without weakening stop rules,
  permissions, or acceptance criteria.

## v1.0.18 - 2026-09-01

- Added a 2,000-line ceiling for hand-written source files, with project
  precedence and exceptions for generated, declarative, vendored, or narrowly
  patched legacy files.
- Added language-independent guidance for domain boundaries, subsystem
  directories, dependency direction, state and resource ownership, runtime
  compatibility, and evidence-based abstraction.
- Reject metric gaming, fake file splits, and unrequested refactors whose only
  purpose is to satisfy a size number.

## v1.0.11 - 2026-08-11

- Made every Scoville Skill optional and independently usable. Discovering a
  sibling does not install or activate it.

## v1.0.6 - 2026-08-08

- Let Scoville Plan own durable Plans, Work Items, and Decisions when it is
  independently available and applicable.
- Keep the repository's existing record owner when Plan is absent or
  inapplicable.
- Do not cross an explicit proposal-acceptance boundary through an unattended
  implementation assumption.

## v1.0.3 - 2026-08-06

- Generalized planning language so Code works with any authoritative project
  plan without depending on one planning product.
- Map independently resumable outcomes to Work Items while keeping
  implementation, review, testing, and documentation steps inside the same
  behavior-complete item.
- Reduce repeated large diagnostics to a stable failure signature and the
  meaningful delta after the first complete capture.
- Treat aggregate evidence as stale when later code, tests, or harness changes
  affect the completion claim.
- Require decisive checks to cover every explicit acceptance behavior and each
  concrete coupling that can make a required path behave differently.

## v1.0.1 - 2026-08-03

### Rename to Scoville Code Anti-AI-Slop

- Renamed the Skill from `scoville-anti-ai-coding-slop` to
  `scoville-code-anti-ai-slop`.

### Migration

- Replace an installation under `scoville-anti-ai-coding-slop/` with
  `scoville-code-anti-ai-slop/`. Do not keep both names installed.

### Runtime-neutral operation and validation floor - 2026-07-26

- Keep internal modes, risk flags, and framing questions out of user-facing
  output.
- When a changed symbol is used elsewhere, require at least one check through a
  real use instead of validating only its owner.
- Allow one documented setup step after an infrastructure failure before one
  substitute check.
- In projects without version control, read before overwriting and preserve
  unrelated content because edits may be irreversible.
- Ask one specific material question after all independent work is complete. In
  unattended work, state the necessary assumption instead of blocking.
- Inspect the complete scoped change and working-tree state once before
  completion, using the facilities available in the current runtime.

### Durable handoff and local code style - 2026-07-22

- Preserve binding constraints and unrecorded material decisions in compacted
  or handed-off work, then reconcile the record with current instructions and
  version-control state when resuming.
- Match the surrounding code's naming, idioms, error handling, comments,
  annotations, and test style.
- Comment only when the code cannot express an important constraint. Do not
  narrate the edit or address a reviewer through comments.
- Report unrelated pre-existing findings only when they could change the user's
  next action.

### Validation stop semantics - 2026-07-21

- After one infrastructure failure, allow one different substitute check. If it
  cannot prove the behavior, stop and report the result as unverified.
- Treat decisive evidence as terminal unless another changed behavior, named
  risk, or higher-priority requirement remains open.
- Open another validation cycle only when the final inspection finds a concrete
  defect that is then fixed.

### Goal-first rewrite - 2026-07-20

- Rebuilt the Skill around the requested observable outcome. Correctness,
  structure, and validation constrain delivery but do not replace it.
- Added Advise, Review, Explore, Develop, and Harden modes while keeping
  structural and high-risk flags independent of change size.
- Presume failed checks are substantive and caused by the change until evidence
  shows otherwise.
- Stop after two failed attempts against the same check, reread the owner
  contract, and change or narrow the approach.
- Treat retained experiments as Develop work and validate them accordingly.
- Removed Skill-owned fallback plan and decision files. Existing project records
  remain canonical.

### Runtime and user precedence - 2026-07-18

- Resolve planning through user instructions, runtime facilities, and project
  conventions before considering a temporary fallback.
- Keep subagent planning ephemeral when the subagent cannot access the caller's
  plan owner.
- Skip written plans for tiny work unless the user or runtime requires one.

### Bounded discovery and validation - 2026-07-16

- Add broader validation only for a named structural or high-risk concern, an
  explicit project rule, or a user requirement.
- Do not rerun an unchanged failed command or continue similar checks after
  decisive evidence.
- Use exact task paths and targeted symbol or filename searches first. Expand
  only when inspected evidence leaves a material owner, boundary, or validation
  question unresolved.
- Stop locating once the source and directly relevant test establish the
  canonical owner.

### Adaptive, risk-proportionate workflow - 2026-07-13

- Inherit user and repository workflows concern by concern and use fallback
  rules only where the project is silent.
- Separate change size from structural and high-risk classification so small
  edits stay lightweight without weakening safety or evidence requirements.
- Organize work around behavior-complete outcomes, real stop conditions,
  focused evidence, final review, and explicit residual risk.

### Structural execution and review gate - 2026-07-10

- Added explicit Change, Review, Advisory, and Non-engineering operations for
  code and engineering artifacts.
- Added structural checks for misleading wrappers, silent fallbacks, lossy
  boundaries, state published before durable work, duplicate owners,
  responsibility growth, speculative abstraction, mode creep,
  implementation-mirroring tests, and incomplete scaffolding.
- Added owner, boundary, atomicity, dependency, failure, completion, and
  residual-risk gates.

### Structural quality beyond green tests - 2026-07-07

- Added pre-edit and post-edit structural review so passing tests alone cannot
  approve a harmful change.
- Added whole-diff review for atomicity, boundary loss, misleading wrappers,
  file-growth signals, and failure-mode coverage.

### Execution-focused quality gate - 2026-07-03

- Replaced the original checklist with an execution loop for locating the
  canonical owner, making a scoped change, validating behavior, inspecting the
  result, and reporting remaining risk.
- Added read-before-edit, conflict detection, dependency approval, fail-first
  defect proof, narrow-to-broad checks, and repository-owned version-control
  policy.

## v1.0.0 - 2026-06-29

- Added the first goal-oriented engineering quality gate for AI-assisted code
  changes and reviews.
