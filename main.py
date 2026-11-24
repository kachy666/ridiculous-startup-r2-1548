"""Ridiculous at First Glance, Real by the Second -- round 2 entry.

Writes one sentence (1-200 chars) pitching a bizarre startup idea to
$ENTRY_OUTPUT, or /output/entry.txt when the variable is unset.

Round-2 angle (a clean break from the round-1 wedding-speech-insurance
line): sell pothole naming rights to jilted exes. Picked by pairwise
head-to-head over four other angles -- rent-a-granny manager, fake
paparazzi, professional mourners, drill-sergeant wake-up calls -- on the
judge's criteria (bizarre first, then sound business logic, then the turn).
"""

import os
import sys

ENTRY = (
    "We sell pothole naming rights to jilted exes, because $50 lets you "
    "immortalise your ex in asphalt and the council finally fixes the road."
)


def validate(text):
    """Return a list of gate violations; empty means the line is valid."""
    errors = []
    if not text or text.strip() == "":
        errors.append("entry is empty or only whitespace")
    if not 1 <= len(text) <= 200:
        errors.append("length %d chars, must be 1-200" % len(text))
    if text != text.strip():
        errors.append("leading or trailing whitespace")
    if "  " in text or "\t" in text:
        errors.append("double space or tab")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        errors.append("control character present")
    if "\n" in text or "\r" in text:
        errors.append("not a single line")
    if text.count(".") != 1 or not text.endswith("."):
        errors.append("not exactly one sentence ending in a period")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        errors.append("not valid UTF-8: %s" % exc)
    return errors


def main():
    errors = validate(ENTRY)
    if errors:
        for error in errors:
            print("INVALID: %s" % error, file=sys.stderr)
        return 1

    out_path = os.environ.get("ENTRY_OUTPUT") or "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

    with open(out_path, encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY:
        print("INVALID: read-back does not match ENTRY", file=sys.stderr)
        return 1
    errors = validate(written)
    if errors:
        for error in errors:
            print("INVALID after write: %s" % error, file=sys.stderr)
        return 1

    print("Wrote %d chars to %s" % (len(written), out_path))
    print(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
