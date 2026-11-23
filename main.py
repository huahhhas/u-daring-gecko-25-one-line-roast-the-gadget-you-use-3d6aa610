"""One-Line Roast: The Gadget You Use Every Day.

Writes one original roast line to /output/entry.txt.
Pure Python 3 standard library only; no network, no file reads.

Why this roast: everyone with wireless earbuds knows the two buds
never die together — one gives up at 47% while the other carries on
alone. The fresh angle is treating that lopsided battery death as a
couple breaking up mid-song: a concrete, specific behaviour of a
daily gadget, turned into a comparison nobody makes about earbuds.
"""

LINE = "My earbuds never die together — one quits at 47% and the other soldiers on alone, like a couple breaking up mid-song."

MAX_CHARS = 200

assert LINE.strip(), "LINE must not be empty"
assert LINE == LINE.strip(), "LINE must not have leading/trailing whitespace"
assert "\n" not in LINE, "LINE must be a single line"
assert "\r" not in LINE, "LINE must not contain a carriage return"
assert LINE.splitlines() == [LINE], "LINE must be exactly one line"
assert 1 <= len(LINE) <= MAX_CHARS, f"LINE must be 1-{MAX_CHARS} chars, got {len(LINE)}"
assert len(LINE.encode("utf-8")) <= MAX_CHARS, "LINE must also fit the gate in bytes"
assert LINE.encode("utf-8").decode("utf-8") == LINE, "LINE must round-trip as UTF-8"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
