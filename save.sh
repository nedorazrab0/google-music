#!/data/data/com.termux/files/usr/bin/env bash
# SPDX-License-Identifier: 0BSD
# Archive the music
set -e

main() {
    local archive='../google-music.zip'
    [[ -f "${archive}" ]] && rm -f "${archive}"
    zip -9r "${archive}" -- .
}

main
