# Python interpreter

The project's own commands, such as its tests, use the interpreter the
project sets up. For bundled helpers and other Python you run:

1. Reuse a Python 3.11+ interpreter already verified in this session.
2. Otherwise try `py -3` on Windows or `python3` elsewhere, then `python`.
   Check the version before the first helper call. Choose locally, without
   asking the user.

Use that executable wherever an example says `python` or `<verified-python>`,
including after `--run --`. Report a missing runtime only after finding no
suitable installed interpreter; the Runtime helpers rule then applies.
