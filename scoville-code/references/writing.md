# Shared writing rules

Apply these rules to plans, decisions, instructions, agent messages, handoffs,
reviews and reports. Preserve the required output schemas and delivery contracts.

When saving composed or transferred text, use a literal-safe UTF-8 file-write
or patch operation. Do not interpolate the content into executable code. Finish and verify saved
content before any dependent command. A preparation failure stops that command. Existing write permissions
still apply.

Never truncate text, including command and combined tool output. The checker
measures the complete emitted text, not opaque host framing or exact provider
token counts.

Attribute truncation only to the layer supported by the evidence. A shortened
later query does not prove that the original capture was truncated. If the
model-visible output or effective host cap is unknown, leave the host cause
unconfirmed and use the existing complete-output recovery.

## Large reads

Without an applicable limit, read complete UTF-8 directly; invent no budget.
With an applicable limit:

1. Use the smallest declared or explicitly selected limit of the command and
   every enclosing tool output. Read separately unless the complete combined output,
   including labels and metadata, is measured and fits; combined reads share
   that budget.
2. If the file may exceed that limit, use the verified Python interpreter and
   bundled reader:
   `<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --file "<document>" --max-output-tokens <limit> --part 1`.
   It validates the complete UTF-8 file and budgets labels too.
   Python runs the full checker path `<skill-directory>/scripts/check_text_size.py`
   after `-X utf8`. The checker reads every document only through `--file`, including
   SKILL.md files and references of any Skill, assignments, and `.py` files read as
   text. Keep the verified launcher, checker path and quoting unchanged. Copy the
   last correct complete command: change only `--part` for the reported next part;
   for another document change only `--file` and reset `--part` to 1.
3. For multipart output, follow `part=N bytes=start:end/total next=M` with
   `--part M` through `last`,
   where end equals total. Read every unchanged part in order before dependent
   work. Use one limit for the whole sequence. If an applicable limit changes,
   restart at part 1 with the new smallest limit; never raise a binding limit
   to keep the old sequence.

Reader parts are already bounded. Execute the supplied reader command unchanged;
do not wrap it in `--run`, add `--publish-full`, or save its output.

A reader error leaves the read incomplete, even if its diagnostic cannot fit.
Correct a visible cause and restart at part 1. Do not repeat an unchanged failed
call or raise a binding limit. Otherwise report the unread document and stop
dependent work.
Do not alter or copy the input, truncate it or recover omitted text after an
oversized read.

To check a supplied expected SHA-256, use the same checker with
`--file "<artifact>" --sha256 --max-output-tokens <limit>` and compare its
`sha256` with the supplied value. A mismatch or error stops dependent work.
Then read the same unchanged file from `--part 1` through `last` with the same
limit. Hash verification is not reading; ordinary sources need no extra hash check.

Without suitable Python 3.11+, use
the manual fallback listed in [Runtime helpers](../SKILL.md#runtime-helpers). A missing helper
or helper error does not enable it.
If commands are forbidden, use the host's permitted UTF-8 reader in ordered
ranges within its limits. This replaces no required helper operation. Name any
required unread input and stop the work depending on it.

Before shell commands, complete-file preparation or output that may exceed an
applicable limit, read [command and output-delivery rules](shell-commands.md).
These procedures grant no additional permissions.

If your role cannot run commands or write files, compact your answer without
losing required content and return the complete text through its permitted
result channel. The caller must capture the complete result and apply the size
check or complete-file route before displaying it through a limited tool output.
These rules grant no additional command or write permission. Role instructions
own any necessary delivery exception. If a known cap on that result channel itself
prevents complete delivery, report the concrete transport limitation.

Write for the actual recipient. Messages to agents, including assignments,
steering, questions, results, reviews and handoffs, and the commentary of an
agent that does not answer the user directly use minimal clearly labelled
fields, not conversational status prose. Visible output is not automatically
addressed to the user. Send only facts needed
for the next correct decision or action: result, decisive evidence, concrete
defect or blocker, unresolved limit and necessary next permitted action.
Omit narration, recaps, unchanged settings, history and known procedures unless
the recipient needs them or a contract requires them. Use unambiguous labels
and actions; no unexplained abbreviations or invented protocol tokens.

Treat an uncertain recipient as fresh; assume no hidden history. Supply every
fact and constraint needed for the next correct decision or action. For source
text the recipient can access and is permitted to read, give its exact path and
section with an explicit reading instruction instead of repeating it. State
other required facts directly. Quote only wording needed as decisive evidence
or required text from a source the recipient cannot read.
Preserve required schemas, statuses, exact control
messages and user relay text, identities, permissions, stops, quiescence and
complete-delivery contracts unchanged. Keep required facts when rewriting or
transferring content.

Human-addressed text, including unchanged user relay bodies, follows the direct
user question and its delivery contract. A final user report states whether the
whole requested task is complete, required checks and actual results, and specific
missing inputs or decisions. Continue authorized work. An agent answering the
user directly gives brief material findings and next actions during longer work.
Make the final user report
understandable on its own.
Writing rules change no task risk, required model, role or authority. Questions
and assessments authorize no changes.

Skill, reference, Plan, Decision and builder-fixed instruction text and
human-addressed explanations use the shortest wording that even simpler models,
such as Luna, Haiku or Gemini, understand on first reading: complete sentences
with a verb or imperative, one term per meaning and plain words before jargon.
Composed internal fields need not be complete sentences but keep one term per
meaning.
Avoid slash chains in prose; preserve literal paths, commands, field names and
technical syntax. Length alone proves neither effectiveness nor performance.

Keep each rule at its responsible source. Remove repetition and low-value
maintenance detail while preserving required context and safeguards. Retain
records only when needed for development or an independently binding requirement.
Record that required reviews occurred; do not archive their text, reconstruct a
complete history, duplicate Steps as prose or document solely for bookkeeping.
A TL;DR cannot replace necessary explanation. Use paragraphs, lists or compact
diagrams when they clarify decisions; preserve useful diagrams.

For adviser work, apply these rules to generated framing and answers. Do not
stylistically rewrite literal user questions, quotations, technical data or
hidden expectation keys. Explicitly requested edits and required secret redaction
retain their own authority.
