#!/bin/bash

rm file1.mp3
rm file2.mp3
rm file3.mp3

ffmpeg -i audio.mp3 -af "afftdn=nf=-25" file1.mp3
ffmpeg -i file1.mp3 -af "afftdn=nf=-25" file2.mp3
ffmpeg -i file2.mp3 -af "highpass=f=200, lowpass=f=3000" file3.mp3