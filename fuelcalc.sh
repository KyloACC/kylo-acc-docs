#!/bin/sh
# Fuel calculator

echo "How much fuel do you use per lap? (like 256 for 2.56)"
read per_lap
((per_lap = per_lap * 10))

echo "How long is an average lap in seconds?"
read time

((fuel_per_minute = per_lap / time))
((fuel_per_minute1 = fuel_per_minute / 1000))
((fuel_per_minute2 = fuel_per_minute % 1000))

echo $fuel_per_minute1 . $fuel_per_minute2
read