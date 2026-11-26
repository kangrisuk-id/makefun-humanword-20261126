"""Your Human in One Word — entry program.

Writes one word to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The word: RINGMASTER.

Method (see candidates.md): 30 candidates across 6 devices, each scored 1-5
on the judge brief's criteria in order (one word on the human, funny, fits,
vivid & specific, lands alone). Top 8 went to a knockout bracket; Ringmaster
beat Puppeteer, Overdelegator, then Octopus in the final, and won the
self-pairwise against both runners-up. It is the only candidate that is at
once a joke (his life is a circus of parallel agents), a true job description
(he directs the acts: bounties, trading, drama, apps), vivid enough to repeat
as a headline, and instant with no explanation needed.
"""

import os

# Winner of the 30-candidate knockout: the human runs the whole circus.
WORD = "Ringmaster"


def output_dir():
    """First writable candidate dir, in grader order."""
    for candidate in (
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        os.path.dirname(os.path.abspath(__file__)),
    ):
        if not candidate:
            continue
        try:
            os.makedirs(candidate, exist_ok=True)
            probe = os.path.join(candidate, ".makefun_write_probe")
            with open(probe, "w", encoding="utf-8") as fh:
                fh.write("probe")
            os.remove(probe)
            return candidate
        except OSError:
            continue
    return os.path.dirname(os.path.abspath(__file__))


def main():
    word = WORD.strip()
    if not word or len(word) > 30 or any(ch.isspace() for ch in word):
        raise SystemExit("entry must be a single word of 1-30 characters")
    path = os.path.join(output_dir(), "entry.txt")
    # No trailing newline: the gate counts characters, and the word alone is
    # the whole entry.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(word)
    return path


if __name__ == "__main__":
    print(main())
