#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line (at most 180 characters) for an
ordinary office object, presented as an ancient artifact, to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

# The placard: a stapler, catalogued like a relic of a lost civilisation.
# Catalogue number, date, material, donor, and the ritual purpose the
# object supposedly served — binding papyrus to appease a feared god.
LINE = (
    "Cat. No. 0417, c. 2019 CE. Stapler, forged steel, gift of the "
    "Facilities Department. Ritual binding device; scribes clamped "
    "papyrus to appease the dread god of deadlines."
)

MAX_LENGTH = 180


def main() -> int:
    line = LINE.strip()

    # Validation: one non-empty line, within the 180-character budget.
    if not line:
        print("error: placard line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: placard line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_LENGTH:
        print(
            f"error: placard line is {len(line)} chars, over the "
            f"{MAX_LENGTH} limit",
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")

    print(f"wrote {len(line)}-character placard to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
