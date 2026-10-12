<!-- helper-fallback: scripts/check_text_size.py -->
# Text-size check without Python

Use this route only when no suitable Python 3.11+ is available. A missing script or helper error
does not enable it.

For a permitted command, capture complete stdout, stderr and its original status
with an available host facility before display. Validate UTF-8 and measure the
whole rendered output, including labels. Grouped streams do not prove their
chronological order. Withheld content remains unread even after status 0. For
effects or nonreproducible required results, prepare permitted complete saving
before the first execution; never rerun merely to add saving. A reviewer does not
save source captures. If no safe capture is available, stop the dependent work.

For a supplied expected SHA-256, compare it with a host tool's hash of the
original bytes; a mismatch or failure stops dependent work. Hash verification
does not replace reading the complete file.

For composed output or permitted result delivery, prepare the complete planned output as UTF-8 without displaying
it. Include every label and combined result. Retain the smallest applicable
declared or explicitly overridden tool-output limit. Do not guess or increase it.
The shared writing rules determine whether a limit applies and preserve
read-only roles. Without an applicable declared limit, no numeric check is due.

When a limit applies, count the file's bytes with an available file-size tool. Use at most
`floor(limit_in_tokens * 4 / 5)` UTF-8 bytes as the same conservative target.
This is not an exact token count or proof of a token overflow. At or below the
target, the size check passes. Above it, compact wording and remove only irrelevant
material while preserving every required fact and safeguard. Never truncate.

If the complete necessary text still cannot fit, or the active role's transfer
contract independently permits file delivery, use the publication procedure
below. Without a content limit, omit the size check and make no fit claim.
1. Resolve the existing workspace and `.scoville/temp` before creating anything.
   The resolved directory must stay inside that workspace.
2. Compute SHA-256 over the complete unchanged UTF-8 bytes; use `<hash>.txt` there.
3. Reject a symlink or non-file at that name. Reuse an existing regular file
   only if its bytes are identical.
4. Otherwise write and close a separate temporary file in that directory.
   Publish it atomically without overwriting an existing target.
5. Remove only the temporary file you created.

If the required byte count, SHA-256, path check or publication operation is
unavailable or fails, stop with its diagnostic.

Return only the size result or the absolute published path and SHA-256. Say that
the file contains the complete unchanged text. Explicitly instruct the recipient
to verify the hash over original bytes and read the entire file as UTF-8
through complete outputs that fit any applicable limits before dependent work.
Existing role, read-stage and transfer gates still apply.
