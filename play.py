#!/data/data/com.termux/files/usr/bin/env python3
# SPDX-License-Identifier: 0BSD
"""Termux music player."""

from subprocess import check_output, run
from random import choice
from pathlib import Path
from time import sleep

PLAYER_CMD = "termux-media-player"
STOP_CMD = [PLAYER_CMD, "stop"]

def is_ready() -> bool:
    output = check_output([PLAYER_CMD, "info"], text=True)
    return output == "No track currently!\n"


def main() -> None:
    path = Path.home() / "google-music-main" / "audio"
    songs = tuple(path.glob("*.m4a"))
    while True:
        if is_ready():
            run([PLAYER_CMD, "play", choice(songs)], check=True)
            sleep(60)
        sleep(5)


if __name__ == "__main__":
    try:
        main()
    finally:
        run(STOP_CMD)
