#!/usr/bin/env python3
"""Shipped on Friday — entry for Famous Last Words: The Funniest Epitaph on make.fun.

Prints exactly one line (at most 150 characters): a tombstone epitaph.
"""

LINE = "Here lies a developer who shipped on Friday and told everyone not to worry. The bug was found Monday. So was he."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 150
    print(LINE)


if __name__ == "__main__":
    main()
