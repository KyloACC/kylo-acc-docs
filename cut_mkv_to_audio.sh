#!/bin/bash

ffmpeg -i input.mkv -ss $1 -codec copy -t $2 output.mkv
rm audio.mp3
ffmpeg -i output.mkv -vn -ab 256k audio.mp3
rm output.mkv