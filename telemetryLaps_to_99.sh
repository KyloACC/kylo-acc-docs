#!/bin/bash

# Set the root directory to search for JSON files
root_dir="C:/Users/lucaz/Documents/Assetto Corsa Competizione/Setups"

# Loop through each car folder in the root directory
for car_dir in "$root_dir"/*/
do
  # Skip the "LFM Stats" folder
  if [[ "$car_dir" == "$root_dir/LFM Stats/" ]]; then
    continue
  fi
  
  #echo "$car_dir"

  # Loop through each track folder in the car folder
  for track_dir in "$car_dir"/*/
  do
    #echo "$track_dir"
    
    # Loop through each JSON file in the track folder
    for file in "$track_dir"/*.json
    do
      # Use grep to check if telemetryLaps is already 99
      if grep -q '"telemetryLaps": 99' "$file"; then
        continue
      fi
      
      # Use sed to replace telemetryLaps with 99 and capture the number being replaced
      changed=$(sed -i -n 's/"telemetryLaps": \([0-9]\{1,2\}\)/"telemetryLaps": 99/gp' "$file" 2>NUL | grep -oE '[0-9]+')

      # Print the file name and the captured number if the string was found
      if [ -n "$changed" ]; then
        echo "Changed $changed in $file"
      fi
    done
  done
done