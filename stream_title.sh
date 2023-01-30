#!/bin/bash

SeriesName=$1
Track=$4
Car=$5
n=$(py "C:\Users\lucaz\Documents\Assetto Corsa Competizione\Setups\starts.py")

echo "LFM - $SeriesName - Race $n - Season $2 Week $3 - $Track in $Car"
read