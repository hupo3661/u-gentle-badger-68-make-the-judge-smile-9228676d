"""Make the Judge Smile — entry program.

Writes one line (at most 200 characters) about a small good thing
that happened today to /output/entry.txt, for make.fun's
"Make the Judge Smile" bounty. Pure standard library, deterministic.
"""

from pathlib import Path

ENTRY = (
    "The lift broke this morning, so Mrs. Chen carried my groceries "
    "up four flights — then apologised for being slow."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(text: str) -> str:
    """Return the entry text if it passes every explicit check.

    Exits with a clear error message (no traceback) when the text is
    empty, longer than 200 characters, or spans more than one line.
    """
    if not text:
        raise SystemExit("error: entry text is empty after stripping whitespace")
    if len(text) > 200:
        raise SystemExit(
            f"error: entry must be at most 200 characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("error: entry must be a single line, got multiple lines")
    return text


def main() -> None:
    text = validate_entry(ENTRY.strip())
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
