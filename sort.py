#!/data/data/com.termux/files/usr/bin/env python3
# SPDX-License-Identifier: 0BSD
"""Sort the download list."""


def main() -> None:
    path = "list.csv"
    with open(path, mode="r", encoding="utf-8", newline="\n") as file:
        lines = sorted(file.readlines())
    with open(path, mode="w", encoding="utf-8", newline="\n") as file:
        file.writelines(lines)


if __name__ == "__main__":
    main()
