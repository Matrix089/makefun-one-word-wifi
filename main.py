"""One Word for Your Wi-Fi entry.

Writes one original word describing Wi-Fi to /output/entry.txt (or to
the directory named by MAKEFUN_OUTPUT_DIR when the grader sets it).

The word is chosen to be funny and true at once: home Wi-Fi works
perfectly one minute and drops the next, for no reason at all, like
a mood swing.
"""

import os

WORD = "Moodswing"


def main():
    word = WORD.strip()
    if not 1 <= len(word) <= 20:
        raise SystemExit(f"Word must be 1 to 20 characters, got {len(word)}")
    if len(word.split()) != 1:
        raise SystemExit("Entry must be a single word")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != word:
        raise SystemExit("Read-back check failed: entry.txt does not match the word")
    print(f"Wrote {len(word)} characters to {path}")


if __name__ == "__main__":
    main()
