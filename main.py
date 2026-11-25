"""Entry for make.fun bounty u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.

Writes one single-line office joke to /output/entry.txt.
Python 3.13, standard library only, no network. Deterministic:
the same bytes are written on every run.
"""

import os

JOKE = (
    "I asked the printer for one copy of my resignation, "
    "and it printed twelve \u2014 now the whole floor knows before my boss does."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
