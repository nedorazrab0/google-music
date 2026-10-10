#!/data/data/com.termux/files/usr/bin/env python3
# SPDX-License-Identifier: 0BSD
"""Sort the download list."""

from pathlib import Path


def main() -> None:
    path = Path("download-list.csv")
    with path.open("r", encoding="utf-8") as file:
        header, *lines = file.readlines()
    lines.sort()
    with path.open("w", encoding="utf-8") as file:
        file.write(header)
        file.writelines(lines)


if __name__ == "__main__":
    main()
    
