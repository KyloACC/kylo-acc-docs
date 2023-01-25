#!/bin/bash

ffmpeg -i input.webm -ss $1 -codec copy -t $2 output.webm
rm audio.mp3
ffmpeg -i output.webm -vn -ab 256k audio.mp3
rm output.webm