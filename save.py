#!/data/data/com.termux/files/usr/bin/env python3
# SPDX-License-Identifier: 0BSD
"""Archive the music."""

from shutil import make_archive
from pathlib import Path


def main() -> None:
    make_archive(
        str(Path.home() / "storage" / "downloads" / "google-music"),
        "zip",
        "..",
        base_dir=Path.cwd().name
    )


if __name__ == "__main__":
    main()
