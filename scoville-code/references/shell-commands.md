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
Large supplied inputs and file results must be read completely before dependent
work. A path, metadata or partial output is not the result.

Preserve complete UTF-8 output, including a failure's stdout and stderr, and
each command's exit status. A capture or
decoding failure, output_complete=false or unread required content stops dependent
work even after exit 0. Running commands are not complete; retain their handle,
chunks and final status. Role and host permissions still apply: these rules
permit no new command, source capture or file write.
