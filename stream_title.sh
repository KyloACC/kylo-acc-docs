#!/bin/bash

echo "Series Name?"
read SeriesName
echo "Track?"
read Track
echo "Car?"
read Car
echo "Season?"
read Season
echo "Week?"
read Week

n=$(py "C:\Users\lucaz\Documents\Assetto Corsa Competizione\Setups\starts.py")

echo "LFM - $SeriesName - Race $n - Season $Season Week $Week - $Track in $Car"
read