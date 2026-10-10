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

