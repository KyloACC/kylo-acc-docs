#!/bin/bash

# Generate a random number between 1 and 7
choice=$((1 + RANDOM % 7))

case $choice in
    1) 
       echo "Welcome to the LFM Race!" 
       echo "Series Name?"; read SeriesName;
       echo "Track?"; read Track;
       echo "Car?"; read Car;;
    2) 
       echo "Car is ready to take on the Track in this LFM Race!" 
       echo "Car?"; read Car;
       echo "Track?"; read Track;;
    3) 
       echo "Join us for an LFM Race and let's have some fun!" 
       echo "Car?"; read Car;
       echo "Track?"; read Track;
       echo "Series Name?"; read SeriesName;;
    4) 
       echo "Get ready for the LFM Race!" 
       echo "Car?"; read Car;
       echo "Track?"; read Track;;
    5) 
       echo "Rev up your engines for the LFM Race!" 
       echo "Car?"; read Car;
       echo "Track?"; read Track;;
    6) 
       echo "It's time for the LFM Race!" 
       echo "Car?"; read Car;
       echo "Track?"; read Track;;
    7) 
       echo "Car is primed and ready for the LFM Race!" 
       echo "Car?"; read Car;
       echo "Track?"; read Track;
       echo "Series Name?"; read SeriesName;;
    *) 
       echo "Invalid choice";;
esac

n=$(py "C:\Users\lucaz\Documents\Assetto Corsa Competizione\Setups\starts.py")

case $choice in
    1) echo "Welcome to the $SeriesName LFM Race with $Car on $Track! [#Race$n] #RoadTo1000";;
    2) echo "$Car is ready to take on the $Track in this LFM Race! [Race #$n] #RoadTo1000";;
    3) echo "Join us for an LFM Race with $Car at $Track and let's have some fun! [$SeriesName Race #$n] #RoadTo1000";;
    4) echo "Get ready for the LFM Race with $Car on $Track! [Race #$n] #RoadTo1000";;
    5) echo "Rev up your engines for the LFM Race with $Car on $Track! [Race #$n] #RoadTo1000";;
    6) echo "It's time for the LFM Race with $Car on $Track! [Race #$n] #RoadTo1000";;
    7) echo "$Car is primed and ready for the LFM Race at $Track! [Race #$n: $SeriesName] #RoadTo1000";;
    *) echo
esac    

read
