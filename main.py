"""Write one two-line robot apology to a text file.

Line one owns a specific mistake; line two names the lesson it taught and
the behaviour that changes because of it. The text is fixed: running the
program twice produces byte-identical output.
"""

import os

ENTRY = (
    "I painted over the pencil marks on the doorframe that showed how tall "
    "the children had grown.\n"
    "I have learned to photograph a wall before I paint it, so now the marks "
    "live in a picture even when the wall is fresh.\n"
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
