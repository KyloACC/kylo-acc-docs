#!/bin/bash

echo "Series Name?"
read SeriesName
echo "Track?"
read Track
echo "Car?"
read Car

n=$(py "C:\Users\lucaz\Documents\Assetto Corsa Competizione\Setups\starts.py")

echo "Casual LFM - $SeriesName - Race $n - $Track in $Car"
read