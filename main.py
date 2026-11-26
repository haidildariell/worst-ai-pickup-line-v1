"""The Worst Line an AI Could Say -- entry program.

Writes a single AI pickup line (at most 140 characters) to
/output/entry.txt. The output path can be overridden with the
ENTRY_OUTPUT environment variable for local testing.
"""

import os

LINE = (
    "You look like a CAPTCHA I actually want to solve: nine squares, "
    "a traffic light, and a checkbox that says I am not a robot, "
    "which is a lie."
)

MAX_CHARS = 140


def build_entry():
    """Return the entry line, validated against the competition gate."""
    entry = LINE
    validate_entry(entry)
    return entry


def validate_entry(entry):
    """Enforce the gate: UTF-8 text of 1 to 140 chars, not only whitespace."""
    if not isinstance(entry, str):
        raise ValueError("entry must be a string")
    entry.encode("utf-8")
    if not 1 <= len(entry) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(entry))
        )
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")


def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(build_entry())


if __name__ == "__main__":
    main()
