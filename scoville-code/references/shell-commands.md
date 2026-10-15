# Shell command rules

Run complete commands in the current tool shell. If another shell is necessary,
use its known suitable launcher. Preserve generated commands and argument quoting.
In PowerShell, invoke a quoted executable path with `&`.

Give `rg` existing file or directory paths and select files with `-g`, for example:
`rg -n -g "*.php" -- "search text" "<existing-directory>"`.
The command-capture helper passes arguments unchanged and expands no wildcards.

Use native shell commands for simple inventories. For composed text or more
complex logic, use a literal-safe file or script rather than nested inline code.

PowerShell `Out-String` formats objects; POSIX command substitution removes
trailing newlines. Use complete raw-output capture when byte preservation matters.
Before piping text into Python from PowerShell, set
`$OutputEncoding = [System.Text.UTF8Encoding]::new($false)` and start Python
with `-X utf8` so source text and stdin agree.

## Read output details when needed

Before potentially large command output, limited result transfer, complete-file
delivery or any nonrepeatable effect, read [output-delivery.md](output-delivery.md).
Choose capture before the effect; never repeat effects to recover output.
Supplied inputs and file results follow the shared reading rule: process
machine data in code and read required prose completely. A path, metadata or
partial output alone proves neither.

Preserve complete UTF-8 output, including a failure's stdout and stderr, and
each command's exit status. A capture or decoding failure, or unread required
content, stops dependent work even after exit 0. For JSON `"status": "complete_file"`, open
the path in `full_file` and process its contents under the shared reading rule;
`"output_complete": false` describes the inline result. Without that complete-file route, missing output remains a
blocker. Running commands are not complete; retain their handle,
chunks and final status. Role and host permissions still apply: these rules
permit no new command, source capture or file write.
