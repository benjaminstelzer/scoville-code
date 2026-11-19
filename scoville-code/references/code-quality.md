## Reviewing a change

A reviewer checks the change against the rules in "What the code has to be"
and answers every one of the "Questions for the finished change": the same
ones its author had to follow. Read the whole change with its callers and the
helpers it calls, also where the change did not touch them. Go through the
questions in their order and write down for each one the defects it shows or
that it shows none; a question you leave out is a rule nobody checked. Start
with question 1, because the author of a loop usually sees it as linear.
Judge from the code; run no benchmark for this.

A finding names the file and line, the rule it breaks and, where one exists,
the function or structure to use instead. Report each defect on its own. A
defect is a breach of one of the rules. An optional improvement, a further
protection or a case nobody described is not one: leave it out, or list it
apart as a question. A read-only reviewer changes nothing.
