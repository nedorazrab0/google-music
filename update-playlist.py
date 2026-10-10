#!/data/data/com.termux/files/usr/bin/env python3
# SPDX-License-Identifier: 0BSD
"""Update the playlist file."""

from pathlib import Path
from json import dumps


def main():
    files = tuple(file.name for file in Path.cwd().glob("*.m4a"))
    content = dumps(files, indent=4) + "\n"
    Path("playlist.json").write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
