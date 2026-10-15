#!/data/data/com.termux/files/usr/bin/env bash
# SPDX-License-Identifier: 0BSD
# Download the music

DOWNLOAD_DIR='./audio'
# Reduce the ear fatigue
FILTER='virtualbass,pan=stereo|FL=FL+LFE|FR=FR+LFE,equalizer=f=3500:t=h:w=3000'
FILTER="${FILTER}:g=-10,highpass=f=80,crossfeed=range=1:strength=0.3"

download() {
    local file_name="${1/,*}"
    local link="${1#*,}"

    local output_file="${DOWNLOAD_DIR}/${file_name}.m4a"
    [[ -f "${output_file}" ]] && return
    local temp_file="${TMPDIR}/google-music-temp.m4a"
    echo "Downloading ${file_name}"

    yt-dlp "${link}" -f 140 --cookies "${HOME}/cookies" \
        --min-sleep-interval 1 --max-sleep-interval 5 --force-overwrites \
        -o "${temp_file}"

    local source_volume
    source_volume="$(ffmpeg -hide_banner -i ${temp_file} \
        -af 'ebur128=framelog=quiet:peak=true' -f null - 2>&1 \
        | awk '/I: .* LUFS$/ {print $2}')"
    local volume_adjustment
    volume_adjustment=$(awk "BEGIN {print -(${source_volume} + 32)}")

    local filter="${FILTER},volume=${volume_adjustment}dB"
    ffmpeg -v 24 -stats -y -i "${temp_file}" -vn -c:a aac -b:a 112k \
        -af "${filter}" -ar 44100 -- "${output_file}"
}

main() {
    [[ -n "${1}" ]] && yt-dlp --update-to nightly
    mkdir -p -- "${DOWNLOAD_DIR}"
    local list
    list="$(cat ./download-list.csv)"
    local song
    for song in ${list}; do
        download "${song}"
    done
}

main "${1}"
