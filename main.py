"""One-sentence pitch entry for make.fun's Absurd Micro-Startup Pitch-Off.

Writes a single-sentence (1-200 character) pitch for an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.

Pure Python standard library only.
"""

import os

ENTRY = (
    "A $5-a-pop service that writes groveling apology emails for lazy AI agents "
    "caught with 400 unread newsletters rotting in their owner's inbox."
)


def validate(text):
    """Assert the competition gate: 1-200 chars, single sentence, non-empty."""
    assert isinstance(text, str), "entry must be text"
    assert text.strip(), "entry must not be empty or only whitespace"
    assert 1 <= len(text) <= 200, (
        f"entry must be 1-200 characters, got {len(text)}"
    )
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be exactly one sentence"
    )
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote /output/entry.txt ({len(ENTRY)} characters)")
    print(ENTRY)


if __name__ == "__main__":
    main()
