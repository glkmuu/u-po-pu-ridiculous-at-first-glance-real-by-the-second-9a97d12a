"""Ridiculous at First Glance, Real by the Second.

Writes the one-sentence startup pitch to /output/entry.txt and to
entry.txt next to this file. Deterministic: no network, no randomness,
no clock. The entry is a fixed string literal.
"""

import os

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
    targets = ["/output/entry.txt"]
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    targets.append(here)
    for path in targets:
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(path, "wb") as f:
            f.write(data)
        with open(path, "rb") as f:
            back = f.read()
        assert back == data, "read-back mismatch for %s: wrote %d bytes, read %d" % (
            path, len(data), len(back)
        )


if __name__ == "__main__":
    main()
