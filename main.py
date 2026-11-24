"""Ridiculous at First Glance, Real by the Second.

Writes the one-sentence startup pitch to /output/entry.txt and to
entry.txt next to this file. Deterministic: no network, no randomness,
no clock. The entry is a fixed string literal.
"""

import os
import sys

# ENTRY is one sentence, 141 characters, no trailing newline.
ENTRY = (
    "We sell sealed jars of air from your hometown to homesick expats, "
    "because nostalgia is a market and a $30 breath of home beats a "
    "$900 flight."
)


def main():
    # Gate checks: one sentence, 1-200 characters, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, "entry length out of range"
    assert ENTRY == ENTRY.strip(), "entry has leading/trailing whitespace"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "not one sentence"
    assert "\n" not in ENTRY, "entry must be a single line"
    data = ENTRY.encode("utf-8")

    # Strict write: /output/entry.txt is the graded artifact. Any failure
    # here (including a read-back mismatch) must fail the program.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    with open("/output/entry.txt", "rb") as f:
        back = f.read()
    assert back == data, "read-back mismatch for /output/entry.txt: wrote %d bytes, read %d" % (
        len(data), len(back)
    )

    # Best-effort local copy: the grader mounts the repo directory
    # read-only, so writing entry.txt next to this script raises
    # PermissionError there. That must not fail the run — /output/entry.txt
    # above is already verified, so a failed local copy only warns.
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    try:
        with open(here, "wb") as f:
            f.write(data)
        with open(here, "rb") as f:
            back = f.read()
        assert back == data, "read-back mismatch for %s: wrote %d bytes, read %d" % (
            here, len(data), len(back)
        )
    except OSError as exc:
        print("warning: could not write local copy %s: %s" % (here, exc), file=sys.stderr)


if __name__ == "__main__":
    main()
