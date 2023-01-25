#!/bin/bash

ffmpeg -i input.mp4 -ss $1 -codec copy -t $2 output.mp4
rm audio.mp3
ffmpeg -i output.mp4 -vn -ab 256k audio.mp3
rm output.mp4