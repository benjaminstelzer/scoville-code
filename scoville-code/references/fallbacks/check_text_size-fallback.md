<!-- helper-fallback: scripts/check_text_size.py -->
# Text-size check without Python

This is the manual route for a host without suitable Python 3.11+. A missing
script or a helper error is a defect to report, not a reason to use it. The
[output-delivery rules](../output-delivery.md) say when a capture, size check
or publication is due; the [machine-data rules](../machine-data.md) still apply
to what is shown.

## Capture a command

1. For a command with an effect or a result that cannot be repeated, arrange
   saving before the first execution. Rerunning it to add saving repeats the
   effect.
2. Capture complete stdout, stderr and the original exit status with a host
   facility before anything is displayed. Stdin receives EOF. Grouped streams
   do not show their time order.
3. Keep the original bytes and status before decoding and check that both
   streams are valid UTF-8. On invalid UTF-8, hold text-dependent work, use
   only an encoding the producer establishes and do not rerun the producer.
4. Where a deadline is needed, use the host's bounded wait and process-family
   termination. Output from a timed-out command is incomplete. Report a
   process whose termination is unconfirmed with its identity; do not restart
   it.

Content that was withheld stays unread even after status 0. A read-only
reviewer does not save source captures. If no complete capture is possible,
report that and leave dependent work open.

## Check size

Run a numeric check only for a declared or explicitly overridden output
limit. Use the smallest applicable one as given; do not guess or raise it.
Prepare the complete planned output as UTF-8, including labels and combined
results, and count its bytes with a file-size tool. At or below
`floor(limit_in_tokens * 4 / 5)` bytes the check passes; this is a
conservative proxy, not a token count. Above it, shorten wording and remove
irrelevant material while keeping every required fact and safeguard. Cutting
text off is never the fix.

## Publish complete text

Publish when necessary text still cannot fit or the role's delivery contract
permits or asks for a file. Without a limit, skip the size check and make no fit claim.

1. Resolve the existing workspace and `.scoville/temp` before creating
   anything; the resolved directory must stay inside the workspace. Create its
   missing `.gitignore` containing `*` without replacing or following an
   existing file.
2. Compute SHA-256 over the complete unchanged UTF-8 bytes and use
   `<hash>.txt` in that directory.
3. Reject a symlink or non-file at that name. Reuse an existing regular file
   only when its bytes are identical.
4. Otherwise write and close a separate temporary file in that directory, then
   publish it atomically without overwriting an existing target.
5. After successful publication, remove only the temporary file you created.

If the byte count, hash, path check or atomic publication is unavailable or
fails, report its diagnostic and keep any complete temporary file as the
recovery copy, naming its path. Writing directly to the final name is not a
substitute, because a partial file there would look complete.

Return the size-check result, or the absolute path of the published file with
the statement that it holds the complete unchanged text.
