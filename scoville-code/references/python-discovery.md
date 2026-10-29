# Python interpreter

For Python commands and bundled helpers, reuse an already verified Python 3.11+
interpreter. Otherwise check `py -3` on Windows or `python3` elsewhere, then
`python` if needed. Choose locally without asking the user and verify the
version before the first helper operation.

Use that executable wherever examples say `python` or `<verified-python>`,
including commands after `--run --`. Report a missing runtime only after finding
no suitable installed interpreter. Apply the operation owner's helper policy
for the resulting stop or permitted no-Python route; a helper failure does not
enable that route.
