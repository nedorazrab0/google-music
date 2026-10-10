#!/data/data/com.termux/files/usr/bin/env python3
# SPDX-License-Identifier: 0BSD
"""Termux music player."""

from subprocess import check_output, run
from random import choice
from pathlib import Path
from time import sleep
from json import loads

PLAYER_CMD = "termux-media-player"


def is_ready() -> bool:
    output = check_output([PLAYER_CMD, "info"], text=True)
    return output == "No track currently!\n"


def main() -> None:
    path = Path.home() / "google-music"
    playlist = path / "playlist.json"
    songs = loads(playlist.read_text())
    while True:
        if is_ready():
            song = path / "audio" / choice(songs)
            run([PLAYER_CMD, "play", song], check=True)
            sleep(60)
        sleep(5)


if __name__ == "__main__":
    try:
        main()
    finally:
        run([PLAYER_CMD, "stop"])
