# Shell commands

Facts that commonly break commands in agent shells. Apply those that match the
shell in use.

- **Shell and quoting:** Run commands in the current tool shell; when another
  shell is necessary, use its known launcher. Keep generated commands and their
  argument quoting intact. In PowerShell, call a quoted executable path with `&`.
- **Search:** Give `rg` existing file or directory paths and select files with
  `-g`, for example `rg -n -g "*.php" -- "search text" "<existing-directory>"`.
- **Composed text and complex logic:** Write them to a file with a literal-safe
  UTF-8 write or patch, then run or pass that file. Shells rewrite backslashes,
  quotes and `$` inside nested inline code, so interpolated content arrives
  changed. Finish the write before the commands that depend on it; a failed
  write holds them.
- **Exact bytes:** PowerShell `Out-String` formats objects and POSIX command
  substitution strips trailing newlines; capture raw output when bytes matter.
- **PowerShell to Python:** Before piping text into Python, set
  `$OutputEncoding = [System.Text.UTF8Encoding]::new($false)` and start Python
  with `-X utf8`.
- **Nested JSON:** Set `ConvertTo-Json -Depth` to cover the whole structure;
  the default depth of 2 replaces deeper values with strings.
- **Exit status:** Judge each command by its own exit status, because a later
  success on the same line hides an earlier failure. Run checks separately or
  chain them so nothing runs after a failed one. In PowerShell read
  `$LASTEXITCODE` directly after a native command; `$ErrorActionPreference`
  alone does not make native failures terminating. Keep a failed command's
  stdout, stderr and original status.
- **Running commands:** A command that is still running has no result yet;
  keep its handle until the final status arrives.
