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


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
