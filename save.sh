#!/data/data/com.termux/files/usr/bin/env bash
# SPDX-License-Identifier: 0BSD
# Archive the music
set -e

main() {
    zip -FS -9r ../google-music.zip -- ../google-music-main
}

main
