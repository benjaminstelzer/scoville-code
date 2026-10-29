# Shell command rules

Run complete commands in the current tool shell. If another shell is necessary,
use its known suitable launcher. Preserve generated commands and argument quoting.
In PowerShell, invoke a quoted executable path with `&`.

Give `rg` existing file or directory paths and select files with `-g`, for example:
`rg -n -g "*.php" -- "search text" "<existing-directory>"`.
The command-capture helper passes arguments unchanged and expands no wildcards.
Use native shell commands for simple inventories; use a literal-safe file or
script for composed text or complex logic instead of nested inline code.

Before Python commands or runtime-helper operations, read
[python-discovery.md](python-discovery.md). File reading does not require Python.

## Encoding and command status

PowerShell `Out-String` formats objects; POSIX command substitution removes
trailing newlines. Use complete raw capture when byte preservation matters.
Before piping text into Python from PowerShell, set
`$OutputEncoding = [System.Text.UTF8Encoding]::new($false)` and launch Python
with `-X utf8`.

For nested JSON, set `ConvertTo-Json -Depth` to cover the complete structure;
PowerShell's default depth of 2 can replace nested values with strings.

Evaluate each command's own exit status; a later success must not hide an earlier
failure. Run checks separately or stop the group on failure. In PowerShell,
inspect `$LASTEXITCODE` immediately after a native command;
`$ErrorActionPreference` alone does not make native failures terminating.
Running commands remain incomplete; retain their handle through final status.

Before potentially large output, limited transfer, complete-file delivery or
a nonrepeatable effect, read [output-delivery.md](output-delivery.md). Choose
capture before execution; never repeat effects to recover output. Missing or
unread required output, capture failure or decoding failure stops dependent
work even after exit 0. Preserve failures' stdout, stderr and original exit
status. These rules grant no command, source-capture or write permission.
