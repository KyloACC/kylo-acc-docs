#!/bin/bash

INPUT=$3
TYPE="${INPUT##*.}"
OUTPUT="output.$TYPE"

ffmpeg -i "$INPUT" -ss $1 -codec copy -t $2 "$OUTPUT"
rm audio.mp3
ffmpeg -i "$OUTPUT" -vn -ab 256k audio.mp3
rm "$OUTPUT"