#!/bin/bash

files=("kylo" "jimmy" "kargulu")

for file in "${files[@]}"
do
        echo "$file"
        python3 aor_t1.py "$file"
        python3 average.py "$file" > "output2_$file.txt"
done

python3 aor_all.py "$1" $2
